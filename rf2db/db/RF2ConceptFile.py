# -*- coding: utf-8 -*-
# Copyright (c) 2013, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
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
from time import gmtime, strftime
from cherrypy import HTTPError

from rf2db.parsers.RF2BaseParser import RF2Concept
from rf2db.parsers.RF2Iterator import RF2ConceptList, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms, extensionParms
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.listutils import listify
from rf2db.utils.sctid_generator import sctid_generator
from rf2db.db.RF2Namespaces import IDGenerator
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, intparam, enumparam, sctidparam
from rf2db.constants.RF2ValueSets import primitive, defined


# Parameters for concept access
concept_parms = global_rf2_parms
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

    idGenerator = None


    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      %(base)s,
      definitionStatusId bigint(20) NOT NULL,
       KEY id (id),
       %(keys)s );"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def _idGenerator(self):
        """ Return an id generator instance.  This isn't invoked until needed as it can entail some expense
        :return: ID generator for the default namespace
        """
        if not self.idGenerator:
            self.idGenerator = IDGenerator(extensionParms.namespace)
        return self.idGenerator


    @lfu_cache(maxsize=100)
    def getConcept(self, cid, parmlist):
        """
        Read the concept record
        @param cid: concept sctid
        """
        db = self.connect()
        rlist = [RF2Concept(c) for c in db.query_p(self._tname(parmlist.ss), parmlist, filter="id=%s" % cid)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None


    def updateConcept(self, cid, parmlist):
        """
        The only thing that can be changed on an existing concept is the definition status.  All other parms are fixed
        :param changeset: Change set identifier for the udpate
        :param sctid: Concept identifier to be changed
        :param definitionstatus: New definition status
        :return: Updated concept
        """
        msg = self.validChangeSet(parmlist)
        if msg:
            return msg

        current_value = self.getConcept(cid, parmlist)
        if not current_value:
            return HTTPError(status=400, message="UnknownEntity - concept not found")
        # Various situations:
        # 1) record is not locked:
        #     1a) record will change
        #         1aa) snapshot:  Not allowed.
        #         1ab) full:  update record with lock, changeset, new effectiveDate and changes
        #     1b) record will not change
        #         ???
        # 2) Record is locked
        #     2a) record changeset = changeset?
        #       1aa) snapshot:  Change record value and effectivedate
        #       1ab) full: add new record with lock, changeset, new effectiveDate and changes
        #     2b) record changeset <> changeset
        #       2aa) snapshot: Not allowed
        #       2ab) full:  ????
        #
        # Don't update effective time if nothing will change (PUT is idempotent)
        if parmlist.ss and not current_value.locked:
            return HTTPError(status=400, message="Unable to update a snapshot")

        if current_value.changeset != parmlist.changeset or \
                not current_value.locked or \
                (current_value.isPrimitive and parmlist.definitionstatus=='f') or \
                (current_value.isFullyDefined and parmlist.definitionstatus=='p'):
            parmlist.definitionStatusId = primitive if parmlist.definitionstatus == 'p' else defined
            db = self.connect()
            parmlist.fname = self._tname(parmlist.ss)
            if not parmlist.effectivetime:
                parmlist.effectivetime = strftime("%Y%m%d", gmtime())

            parmlist.cid = cid
            parmlist.cvet = current_value.effectiveTime

            db.execute("UPDATE %(fname)s SET "
                       "effectiveTime=%(effectivetime)s, "
                       "definitionStatusId=%(definitionstatusid)s, "
                       "changeset='%(changeset)s', locked=1 "
                       "WHERE id=%(cid)s AND effectiveTime=%(cvet)s" % parmlist.__dict__)

            db.commit()
        return self.getConcept(cid, parmlist, _nocache=True)


    def deleteConcept(self, cid, parmlist):
        msg = self.validChangeSet(parmlist)
        if msg:
            return msg

        parmlist.active=0       # Include already deleted concepts
        current_value = self.getConcept(cid, parmlist)
        if not current_value:
            return HTTPError(status=400, message="UnknownEntity - concept not found")
        # If the concept is locked under our change set, we can just remove it.  If it isn't locked, we can only do
        # the Full thingie for the time being
        # Locked is only readable under our change set...
        if parmlist.ss and not current_value.locked:
            return HTTPError(status=400, message="Unable to delete from a snapshot")
        if current_value.isActive():
            db = self.connect()
            fname = self._tname(parmlist.ss)
            effectivetime = strftime("%Y%m%d", gmtime())
            cvet = current_value.effectiveTime
            db.execute("UPDATE %(fname)s SET "
                       "effectiveTime=%(effectivetime)s, "
                       "active=0 "
                       "WHERE id=%(cid)s AND effectiveTime=%(cvet)s" % vars())
            db.commit()
        return self.getConcept(cid, parmlist, _nocache=True)



    def newConcept(self, parmlist):
        """
        Parameterized newConcept.
        :param changeset: Change Set Identifier associated with the change
        :type changeset: UUID
        :param sctid: SCTID of new concept.  If absent, sctid is generated using rf2 namespace parameter
        :param effectivetime: Effective time of insertion.  If absent, today as 'yyyymmdd'
        :param moduleid: module id of new concept. Default: rf2 moduleid parameter
        :param definitionstatus: 'p' or 'd' (primitive or defined). Default: 'p'
        :return: RF2Concept representation of new entry
        """
        msg = self.validChangeSet(parmlist)
        if msg:
            raise msg

        db = self.connect()
        parmlist.fname = self._tname(parmlist.ss)
        if not parmlist.sctid:
            parmlist.sctid = self._idGenerator().next(sctid_generator.CONCEPT)
        if not parmlist.effectivetime:
            parmlist.effectivetime = strftime("%Y%m%d", gmtime())
        if not parmlist.moduleid:
            parmlist.moduleid = extensionParms.moduleid

        parmlist.definitionStatusId = primitive if parmlist.definitionstatus == 'p' else defined
        db.execute("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, definitionStatusId, changeset, locked) "
        "VALUES (%(sctid)s, %(effectivetime)s, 1, %(moduleid)s, %(definitionstatusid)s, '%(changeset)s', 1 )" % parmlist.__dict__)
        db.commit()
        return self.getConcept(parmlist.sctid, parmlist)


    def getAllConcepts_p(self, active=1, order='asc', page=0, maxtoreturn=100, after=0):
        return self.getAllConcepts(concept_list_parms.parse(
            **{'active': active, 'order': order, 'page': page, 'maxtoreturn': maxtoreturn, 'after': after}))


    def getAllConcepts(self, parmlist):
        """
        Read a number of concept records
        @param parmlist: parsed parameter list
        """

        if not parmlist.ss:
            raise Exception('FULL table not supported for complete concept list')
        db = self.connect()
        query = 'SELECT %s FROM %s' % ('*' if parmlist.maxtoreturn else 'count(*)', self._tname(parmlist.ss))
        query += ' WHERE %s ' % ('active=1' if parmlist.active else 'TRUE')
        if parmlist.changeset:
            query += " AND (changeset = '%s' OR locked = 0)" % parmlist.changeset
        else:
            query += ' AND locked = 0'
        if parmlist.after:
            query += ' AND id > %s' % parmlist.after
        if parmlist.moduleid:
            query += ' AND ' + ' AND '.join(['moduleid = %s' % m for m in listify(parmlist.moduleid)])
        if parmlist.order:
            query += ' ORDER BY id %s' % parmlist.order
        if parmlist.maxtoreturn:
            query += ' LIMIT %s, %s' % (parmlist.start, parmlist.maxtoreturn + 1)
        db.execute(query)
        return [RF2Concept(c) for c in db.ResultsGenerator(db)] if parmlist.maxtoreturn else list(
            db.ResultsGenerator(db))

    @staticmethod
    def asConceptList_p(clist, active=1, order='asc', page=0, maxtoreturn=100, after=0):
        return ConceptDB.asConceptList(clist, concept_list_parms.parse(
            **{'active': active, 'order': order, 'page': page, 'maxtoreturn': maxtoreturn, 'after': after}))

    @staticmethod
    def asConceptList(clist, parmlist):
        thelist = RF2ConceptList(parmlist)
        if not parmlist.maxtoreturn:
            return thelist.finish(True, total=list(clist)[0])
        for c in clist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(c)
        return thelist.finish(False)

