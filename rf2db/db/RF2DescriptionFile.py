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

""" RF2 Description File Access Routines
"""

from rf2db.parsers.RF2BaseParser import RF2Description
from rf2db.parsers.RF2Iterator import RF2DescriptionList, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms, rf2_values
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.parameterparser.ParmParser import ParameterDefinitionList

# Parameters for description access
description_parms = global_rf2_parms
description_list_parms = ParameterDefinitionList(global_rf2_parms)
description_list_parms.add(iter_parms)

    
class DescriptionDB(RF2FileWrapper):
     
    directory = 'Terminology'
    prefixes  = ['sct2_Description_', 'sct2_TextDefinition_']
    table = 'description'

    idGenerator = None
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      conceptId bigint(20) NOT NULL,
      languageCode varchar(10) COLLATE utf8_bin NOT NULL,
      typeId bigint(20) NOT NULL,
      term text(16384) CHARACTER SET utf8 NOT NULL,
      caseSignificanceId bigint(20) NOT NULL,
      KEY concept (conceptId) USING BTREE,
       %(keys)s ); """
    
    def __init__(self, *args, **kwargs): 
        RF2FileWrapper.__init__(self, *args, **kwargs)
        self._descTextDB = None
    
    @lfu_cache(maxsize=100)
    def getConceptDescription(self, conceptId, maxtoreturn=None, **kwargs):
        db = self.connect()
        rval = db.query(self._fname, filter_="conceptId = %s" % conceptId, maxtoreturn=maxtoreturn, **kwargs)
        return [RF2Description(d) for d in rval] if maxtoreturn != 0 else list(rval)

    def getConceptIdForDescription(self, descId, **kwargs):
        rlist = self.getDescriptionById(descId, **kwargs)
        return str(rlist.conceptId) if rlist else None


    @lfu_cache(maxsize=20)
    def getDescriptionById(self, descId, **kwargs):
        db = self.connect()
        rlist = [RF2Description(d) for d in db.query_p(self._fname, filter_="id = %s" % descId, **kwargs)]
        return rlist[0] if len(rlist) else None


    @staticmethod
    def asDescriptionList(dlist, maxtoreturn=None, **kwargs):
        if maxtoreturn is None:
            maxtoreturn=rf2_values.defaultblocksize
        thelist = RF2DescriptionList(maxtoreturn=maxtoreturn, **kwargs)
        if maxtoreturn == 0:
            return thelist.finish(True, total=list(dlist)[0])
        for d in dlist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(d)
        return thelist.finish(False)

