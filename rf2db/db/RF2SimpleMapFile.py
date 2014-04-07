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


from rf2db.db.RF2FileCommon import global_rf2_parms
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.parsers.RF2RefsetParser import RF2SimpleMapReferenceSetEntry
from rf2db.parsers.RF2Iterator import RF2SimpleMapReferenceSet, iter_parms
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam, strparam


class SimpleMapDB(RF2RefsetWrapper):
      
    directory   = 'Refset/Map'
    prefixes    = ['der2_sRefset_SimpleMap']
    table       = 'simplemap'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id varchar(36) COLLATE utf8_bin NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      refsetId bigint(20) NOT NULL,
      referencedComponentId bigint(20) NOT NULL,
      mapTarget varchar(255) COLLATE utf8_bin NOT NULL,
      %(primkey)s );"""

    _simplemap_list_parms = ParameterDefinitionList(global_rf2_parms)
    _simplemap_list_parms.add(iter_parms)
    _simplemap_list_parms.component = sctidparam()
    _simplemap_list_parms.target = strparam()
    _simplemap_list_parms.refset = sctidparam()

    
    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def get_simple_map(self, parmlist):
        filtr = 'refsetId=%s' % parmlist.refset if parmlist.refset else 'True'
        filtr += (' AND referencedComponentId = %s ' % parmlist.component) if parmlist.component else ' '
        filtr += (" AND mapTarget = '%s' " % parmlist.target) if parmlist.target else ' '
        db = self.connect()
        if not parmlist.sort:
            parmlist.sort=['refsetId', 'referencedComponentId']
        return [RF2SimpleMapReferenceSetEntry(e) for e in db.query_p(self._tname(parmlist.ss),
                                                                     parmlist,
                                                                     filter=filtr)]

    @classmethod
    def simplemap_list_parms(cls):
        return cls._simplemap_list_parms


    @staticmethod
    def as_reference_set(mlist, parmlist):
        thelist=RF2SimpleMapReferenceSet(parmlist)
        if not parmlist.maxtoreturn:
            return thelist.finish(True, total=list(mlist)[0])
        for m in mlist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(m)
        return thelist.finish(False)




