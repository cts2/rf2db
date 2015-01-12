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

""" RF2 Simple Reference Set file access
"""
import uuid

from rf2db.db.RF2ConceptFile import new_concept_parms, ConceptDB
from rf2db.db.RF2TransitiveClosure import TransitiveClosureDB
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper, global_refset_parms
from rf2db.parsers.RF2RefsetParser import RF2SimpleReferenceSetEntry
from rf2db.parsers.RF2Iterator import RF2SimpleReferenceSet, iter_parms
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam, enumparam, booleanparam
from rf2db.constants.RF2ValueSets import simpleReferenceSetRoot
from rf2db.utils.listutils import listify
from rf2db.utils.lfu_cache import clear_caches

simplerefset_list_parms = ParameterDefinitionList(global_refset_parms)
simplerefset_list_parms.add(iter_parms)
simplerefset_list_parms.component = sctidparam()
simplerefset_list_parms.refset = sctidparam()

new_simplerefset_parms = ParameterDefinitionList(new_concept_parms)

update_simplerefset_parms = ParameterDefinitionList(global_refset_parms)
update_simplerefset_parms.operation = enumparam(('add', 'remove', 'replace'), default='add')
update_simplerefset_parms.refset = sctidparam(required=True)
update_simplerefset_parms.component = sctidparam(splittable=True)
update_simplerefset_parms.children = booleanparam(default=False)
update_simplerefset_parms.leafonly = booleanparam(default=False)


class SimpleReferencesetDB(RF2RefsetWrapper):
   
    directory = 'Refset/Content'
    prefixes = ['der2_Refset_Simple']
    table = 'simplerefset'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      %(base)s,
      UNIQUE KEY racu (refsetId, referencedComponentId),
       %(keys)s ); """

    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def get_simple_refset(self, refset=None, component=None, sort=None, maxtoreturn=None, **kwargs):
        filtr = 'refsetId=%s' % refset if refset else 'True'
        filtr += (' AND referencedComponentId = %s ' % component) if component else ' '
        db = self.connect()
        # TODO: Sort
        db.execute(db.build_query(self._fname,
                                  filter_=filtr,
                                  sort=sort,
                                  **kwargs))
        return [RF2SimpleReferenceSetEntry(e) for e in db.ResultsGenerator(db)] if maxtoreturn \
            else list(db.ResultsGenerator(db))

    @classmethod
    def refsettype(cls, parms):
        return RF2SimpleReferenceSet(parms)

    def new(self, changeset=None, parent=None, **kwargs):
        if not parent:
            parent = simpleReferenceSetRoot
        db = self.connect()
        return db.add(changeset, parent=parent, **kwargs)

    @staticmethod
    def _resolvecomponents(cdb, tcdb, changeset, component, children, leafonly, **kwargs):
        components = listify(component)
        for c in components:
            if not cdb.validconcept(c, changeset, **kwargs):
                return "Invalid member concept: %s" % c
        if not children:
            return components
        return set(tcdb.children(c) for c in components)

    class _rowgenerator():
        def __init__(self, effectivetime, moduleid, refsetid, changeset):
            self._et, self._mi, self._ri, self._cs = effectivetime, moduleid, refsetid, changeset

        def row(self, component):
            return "('%s', %s, %s, %s, %s, %s, '%s', %s)" % \
                   (uuid.uuid4(), self._et, 1, self._mi, self._ri, component, self._cs, 1)

    def _removeall(self, refset, changeset):
            sql = "DELETE FROM %s WHERE refsetId=%s AND changeset='%s' AND locked=1 " % (self._fname, refset, changeset)
            db = self.connect()
            db.execute_query(sql)
            db.commit()

    def _doadd(self, effectivetime, moduleid, refset, changeset, components):
            effectivetime, moduleid = self.effectivetime_and_moduleid(effectivetime, moduleid)
            rg = self._rowgenerator(effectivetime, moduleid, refset, changeset)
            if components:
                sql = "INSERT IGNORE INTO %s (id, effectiveTime, active, moduleId, refsetId, referencedComponentId, " \
                    "changeset, locked) VALUES " + ','.join(list(rg.row(c) for c in components))
                db = self.connect()
                db.execute_query(sql % self._fname)
                db.commit()

    def update(self, operation="add", changeset=None, refset=None, effectivetime=None, moduleid=None, component=None,
               children=False, leafonly=False, **kwargs):

        # Make sure the change set is open and editable
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)

        # Make sure that the refset is a valid refset and is editable
        cdb = ConceptDB()
        if not cdb.validconcept(refset, changeset, **kwargs):
            return "Unrecognized refset concept "
        tcdb = TransitiveClosureDB()
        if simpleReferenceSetRoot not in tcdb.parents(refset, changeset=changeset, moduleid=moduleid, **kwargs):
            return "%s is not a simple reference set" % refset

        # Resolve the components of the reference set
        components = self._resolvecomponents(cdb, tcdb, changeset, component, children, leafonly, **kwargs)
        if not isinstance(components, list):
            return components

        if operation == 'add':
            self._doadd(effectivetime, moduleid, refset, changeset, components)
            clear_caches()
            return None

        if operation == 'remove':
            if components:
                sql = "DELETE FROM %s WHERE refsetId=%s AND changeset='%s' AND locked=1 AND " \
                      "referencedComponentId in (%s)" % (self._fname, refset, changeset, ','.join(str(c) for c in components))
                db = self.connect()
                db.execute_query(sql)
                db.commit()
            else:
                self._removeall(refset, changeset)
            clear_caches()
            return None

        if operation == 'replace':
            self._removeall(refset, changeset)
            self._doadd(effectivetime, moduleid, refset, changeset, components)
            clear_caches()
            return None

        return None, (500, "Unknown operation: " % operation)

    def delete(self, changeset=None, refset=None, **kwargs):
        # Make sure the change set is open and editable
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)

        # Make sure that the refset is a valid refset and is editable
        cdb = ConceptDB()
        if not cdb.validconcept(refset, changeset, **kwargs):
            return "Unrecognized refset concept "
        self._removeall(refset, changeset)
        clear_caches()
        return None
