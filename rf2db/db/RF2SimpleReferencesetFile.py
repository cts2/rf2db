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


from rf2db.db.RF2FileCommon import global_rf2_parms, rf2_values
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.parsers.RF2RefsetParser import RF2SimpleReferenceSetEntry
from rf2db.parsers.RF2Iterator import RF2SimpleReferenceSet, iter_parms
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam


class SimpleReferencesetDB(RF2RefsetWrapper):
   
    directory   = 'Refset/Content'
    prefixes    = ['der2_Refset_Simple']
    table       = 'simplerefset'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      %(base)s,
       %(keys)s ); """


    _simplerefset_list_parms = ParameterDefinitionList(global_rf2_parms)
    _simplerefset_list_parms.add(iter_parms)
    _simplerefset_list_parms.component = sctidparam()
    _simplerefset_list_parms.refset = sctidparam()
    
    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def get_simple_refset(self,  refset=None, component=None, sort=None, **kwargs):
        filtr = 'refsetId=%s' % refset if refset else 'True'
        filtr += (' AND referencedComponentId = %s ' % component) if component else ' '
        db = self.connect()
        # TODO: Sort
        return [RF2SimpleReferenceSetEntry(e) for e in db.query(self._fname,
                                                                filter_=filtr,
                                                                sort=sort,
                                                                **kwargs)]

    @classmethod
    def simplerefset_list_parms(cls):
        return cls._simplerefset_list_parms


    @staticmethod
    def as_reference_set(mlist, maxtoreturn=None, **kwargs):
        if maxtoreturn is None:
            maxtoreturn=rf2_values.defaultblocksize
        thelist=RF2SimpleReferenceSet(maxtoreturn=maxtoreturn, **kwargs)
        if maxtoreturn == 0:
            return thelist.finish(True, total=list(mlist)[0])
        for m in mlist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(m)
        return thelist.finish(False)

