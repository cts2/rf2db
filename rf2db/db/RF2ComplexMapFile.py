# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
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

""" RF2 SimpleMap reference processing routines
"""

from rf2db.db.RF2FileCommon import global_rf2_parms, rf2_values
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.db.RF2SimpleMapFile import SimpleMapDB
from rf2db.parsers.RF2Iterator import iter_parms, RF2ComplexMapReferenceSet
from rf2db.parsers.RF2RefsetParser import RF2ComplexMapReferenceSetEntry
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam, strparam
from warnings import filterwarnings


class ComplexMapDB(RF2RefsetWrapper):
      
    directory   = 'RefSet/Map'
    prefixes    = ['der2_iisssccRefset_ExtendedMapSnapshot', 'der2_iissscRefset_ComplexMapSnapshot']
    table       = 'complexmap'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      %(base)s,
      mapGroup int(4) NOT NULL,
      mapPriority int(4) NOT NULL,
      mapRule text(8192) CHARACTER SET utf8,
      mapAdvice text(8192) CHARACTER SET utf8,
      mapTarget text(256),
      correlationId bigint(20),
      mapCategoryId bigint(20),
      KEY target(refsetId, mapTarget(16)),
      key targ (mapTarget(16)),
      %(keys)s );"""

    _complexmap_list_parms = ParameterDefinitionList(global_rf2_parms)
    _complexmap_list_parms.add(iter_parms)
    _complexmap_list_parms.component = sctidparam()
    _complexmap_list_parms.target = strparam()
    _complexmap_list_parms.refset = sctidparam()

    
    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file):
        smdb = SimpleMapDB()
        if not smdb.hascontent():
            print("Error: Simple map table must be loaded before complex map table")
            return

        # Load the native data
        filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(ComplexMapDB, self).loadTable(rf2file)

        # Copy the simple map file data across
        db = self.connect()
        print "Importing simple map table"
        db.execute("""INSERT INTO %s (id, effectiveTime, active, moduleId, refsetId,
                                                 referencedComponentId, mapGroup, mapPriority, mapTarget)
                      SELECT id, effectiveTime, active, moduleId, refsetId,
                                                 referencedComponentId, 1, 1, mapTarget from %s;""" %
                   (self._fname, smdb._fname))
        db.commit()

    def get_complex_map(self, component=None, target=None, sort=None, **kwargs):
        filtr = 'refsetId=%s' % kwargs.get('refset', 'True')
        filtr += (' AND referencedComponentId = %s ' % component) if component else ' '
        filtr += (" AND mapTarget = '%s' " % target) if target else ' '
        db = self.connect()
        if not sort:
            sort=['refsetId', 'referencedComponentId', 'mapGroup', 'mapPriority']
        return [RF2ComplexMapReferenceSetEntry(e) for e in db.query(self._fname,
                                                                      sort=sort,
                                                                      filter_=filtr,
                                                                      **kwargs)]

    @classmethod
    def complexmap_list_parms(cls):
        return cls._complexmap_list_parms

    @staticmethod
    def as_reference_set(mlist, maxtoreturn=None, **kwargs):
        if maxtoreturn is None:
            maxtoreturn=rf2_values.defaultblocksize
        thelist=RF2ComplexMapReferenceSet(maxtoreturn=maxtoreturn, **kwargs)
        if maxtoreturn == 0:
            return thelist.finish(True, total=list(mlist)[0])
        for m in mlist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(m)
        return thelist.finish(False)




