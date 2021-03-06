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
from rf2db.parsers.RF2RefsetParser import RF2SimpleMapReferenceSetEntry
from rf2db.parsers.RF2Iterator import RF2SimpleMapReferenceSet, iter_parms
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam, strparam

simplemap_list_parms = ParameterDefinitionList(global_rf2_parms)
simplemap_list_parms.add(iter_parms)
simplemap_list_parms.component = sctidparam()
simplemap_list_parms.target = strparam()
simplemap_list_parms.refset = sctidparam()


class SimpleMapDB(RF2RefsetWrapper):
      
    directory   = 'Refset/Map'
    prefixes    = ['der2_sRefset_SimpleMap']
    table       = 'simplemap'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      mapTarget varchar(255) COLLATE utf8_bin NOT NULL,
      key targ (mapTarget(16)),
      %(keys)s );"""

    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def get_simple_map(self, refset=None, component=None, target=None, sort=None, maxtoreturn=None, **kwargs):
        filtr = 'refsetId=%s' % refset if refset else 'True'
        filtr += (' AND referencedComponentId = %s ' % component) if component else ' '
        filtr += (" AND mapTarget = '%s' " % target) if target else ' '
        db = self.connect()
        if not sort:
            sort=['refsetId', 'referencedComponentId']
        db.execute(db.build_query(self._fname,
                                  filter_=filtr,
                                  sort=sort,
                                  maxtoreturn=maxtoreturn,
                                  **kwargs))
        return [RF2SimpleMapReferenceSetEntry(e) for e in db.ResultsGenerator(db)] if maxtoreturn \
            else list(db.ResultsGenerator(db))

    @classmethod
    def refsettype(cls, parms):
        return RF2SimpleMapReferenceSet(parms)



