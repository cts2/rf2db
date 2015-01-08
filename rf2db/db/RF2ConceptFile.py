# -*- coding: utf-8 -*-
# Copyright (c) 2013, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

""" RF2 Concept File access routines
"""

from rf2db.parsers.RF2BaseParser import RF2Concept
from rf2db.parsers.RF2Iterator import RF2ConceptList, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms, ep_values, rf2_values
from rf2db.db.RF2DBConnection import cp_values, singleresultargs
from rf2db.utils.lfu_cache import lfu_cache, clear_caches
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, intparam, enumparam, sctidparam
from rf2db.constants.RF2ValueSets import primitive, defined


# Parameters for concept access
concept_parms = ParameterDefinitionList(global_rf2_parms)
concept_parms.concept = sctidparam()

concept_list_parms = ParameterDefinitionList(global_rf2_parms)
concept_list_parms.add(iter_parms)
concept_list_parms.after = intparam()

new_concept_parms = ParameterDefinitionList(global_rf2_parms)
new_concept_parms.sctid = sctidparam()
new_concept_parms.effectiveTime = intparam()
new_concept_parms.definitionstatus = enumparam(['p', 'f'], default='p')

update_concept_parms = ParameterDefinitionList(global_rf2_parms)
update_concept_parms.definitionstatus = enumparam(['p', 'f'])

delete_concept_parms = ParameterDefinitionList(global_rf2_parms)


class ConceptDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Concept_']
    table = 'concept'


    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      %(base)s,
      definitionStatusId bigint(20) NOT NULL,
       KEY id (id),
       %(keys)s );"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    hasrf2rec = True
    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2Concept(*args, **kwargs)

    @lfu_cache(maxsize=200)
    def read(self, cid, **kwargs):
        """
        Read the concept record
        @param cid: concept sctid
        @return: Updated RF2Concept record if valid else None
        """
        db = self.connect()
        return db.singleton_query(self._fname, RF2Concept, filter_="id=%s" % cid, **kwargs)

    def _doupdate(self, cid, changeset, effectivetime=None, definitionstatusid=None, **kwargs):
        """ Helper function to update a concept record
        @param cid: concept id to update
        @param changeset: changeset
        @param effectivetime: new effective time
        @param definitionstatusid: new definition status is not empty
        @param kwargs: context
        """
        fname = self._fname
        effectivetime, _ = self.effectivetime_and_moduleid(effectivetime, None)
        query = "UPDATE %(fname)s SET effectiveTime=%(effectivetime)s, "
        query += "definitionStatusId=%(definitionstatusid)s, " if definitionstatusid else ""
        query += "WHERE id=%(cid)s AND changeset='%(changeset)s' AND locked=1"
        db = self.connect()
        db.execute_query(query % vars(), **kwargs)
        db.commit()

    def update(self, cid, changeset=None, definitionstatus=None, **kwargs):
        """ Update an existing concept record
        @param cid: sctid of concept to update
        @param changeset: containing changeset
        @param definitionstatus: field to update
        @param kwargs: context
        @return: new record if update successful, otherwise an error message.
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)
        current_value = self.read(cid, changeset=changeset, **kwargs)
        if not current_value:
            return "UnknownEntity - concept not found"
        # Various situations:
        # 1) record is not locked:
        #     1a) record will change
        #         1aa) snapshot:  Not allowed.
        #         1ab) full:  update record with lock, changeset, new effectiveDate and changes
        #     1b) record will not change
        #         Return existing record untouched
        # 2) Record is locked
        #     2a) record changeset = changeset?
        #       1aa) snapshot:  Change record value and effectivedate
        #       1ab) full: add new record with lock, changeset, new effectiveDate and changes
        #     2b) record changeset <> changeset
        #       2aa) snapshot: Not allowed
        #       2ab) full:  ????
        #
        # Don't update effective time if nothing will change (PUT is idempotent)
        if not current_value.locked:
            if current_value.changeset != changeset or \
               current_value.isPrimitive and definitionstatus == 'f' or \
               current_value.isFullyDefined and definitionstatus == 'p':
                if cp_values.ss:
                    return "Concept: Cannot update an existing snapshot record"
                else:
                    return "Concept: Full record update is not implemented"
            else:
                return current_value
        else:
            if current_value.changeset == changeset:
                if cp_values.ss:
                    definitionstatusid = primitive if (definitionstatus == 'p' and current_value.isFullyDefined) \
                        else defined if (definitionstatus == 'f' and current_value.isPrimitive) else None
                    self._doUpdate(cid, changeset, definitionstatusid=definitionstatusid, **kwargs)
                    clear_caches()
                    return self.read(cid, _nocache=True, **kwargs)
                else:
                    return "Concept: Full record update is not implemented"
            else:
                return "Concept: Record is locked under a different changeset"


    def delete(self, cid, changeset=None, **kwargs):
        """ Delete or deactivate a concept
        @param cid: concept identifier
        @param changeset: containing changeset
        @param kwargs: context
        @return: None if success otherwise an error message
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)

        # delete is idempotent, so if we can't find it or it is already gone claim success
        kwargs['active'] = 0  # read even if inactive
        current_value = self.read(cid, **kwargs)
        if not current_value or not current_value.isActive():
            return None

        if not current_value.locked:
            if cp_values.ss:
                return "Cannot delete committed concepts in a snapshot database"
            else:
                return "Concept: Full record delete is not implemented"
        else:
            if current_value.changeset == changeset:
                db = self.connect()
                db.execute_query(
                    "DELETE FROM %(fname)s WHERE id=%(cid)s AND changeset=%(changeset)s AND locked=1" % vars())
                db.commit()
                clear_caches()
                return None
            else:
                return "Concept: Record is locked under a different changeset"


    def add(self, changeset, cid=None, effectivetime=None, moduleid=None, definitionstatus='p', **kwargs):
        """
        @param changeset: Changeset identifier.
        @type changeset: UUID
        @param cid: concept identifier.  Default: next concept in server namespace
        @param effectivetime: Timestamp for record.  Default: today's date
        @param moduleid: owning module.  Default: service module (ep_values.moduleId)
        @param definitionstatus: 'p' (primitive) or 'f' (fully defined).  Default: 'p'
        @return: Concept record or none if error.
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)

        db = self.connect()
        if not cid:
            cid = self.newconceptid()
        effectivetime, moduleid = self.effectivetime_and_moduleid(effectivetime, moduleid)

        definitionstatusid = defined if definitionstatus == 'f' else primitive
        fname = self._fname
        db.execute("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, "
                   "definitionStatusId, changeset, locked) "
                   "VALUES (%(cid)s, %(effectivetime)s, 1, %(moduleid)s, "
                   "%(definitionstatusid)s, '%(changeset)s', 1 )" % vars())
        db.commit()
        clear_caches()
        return self.read(cid, changeset=changeset, **kwargs)

    def getAllConcepts(self, active=1, order='asc', sort=None, page=0, maxtoreturn=None, after=0,
                       changeset=None, moduleid=None, locked=False, **kwargs):
        """
        Read a number of concept records
        @param parmlist: parsed parameter list
        """

        if maxtoreturn is None:
            maxtoreturn = rf2_values.defaultblocksize

        if not cp_values.ss:
            raise Exception('FULL table not supported for complete concept list')

        start = (page * maxtoreturn) if maxtoreturn > 0 else 0

        query = 'SELECT %s FROM %s' % ('*' if maxtoreturn != 0 else 'count(*)', self._fname)
        query += ' WHERE %s ' % ('active=1' if active else 'TRUE')
        if changeset:
            if locked:
                query += " AND (changeset = '%s' AND locked = 1)" % changeset
            else:
                query += " AND (changeset = '%s' OR locked = 0)" % changeset
        else:
            query += ' AND locked = 0'
        if after:
            query += ' AND id > %s' % after
        if moduleid:
            query += ' AND ' + ' AND '.join(['moduleid = %s' % m for m in listify(moduleid)])
        query += ' ORDER BY '
        if sort:
            query += ", ".join(("%s " % s + order) for s in listify(sort)) + ", "
        query += ' id %s' % order
        if maxtoreturn > 0:
            query += ' LIMIT %s' % (maxtoreturn + 1)
        if start > 0:
            query += ' OFFSET %s' % start
        db = self.connect()
        db.execute(query)
        return [RF2Concept(c) for c in db.ResultsGenerator(db)] if maxtoreturn else list(
            db.ResultsGenerator(db))

    @classmethod
    def refsettype(cls, parms):
        return RF2ConceptList(parms)


