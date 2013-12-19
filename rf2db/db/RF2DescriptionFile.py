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

from rf2db.parsers               import RF2Iterator

from rf2db.db.RF2FileCommon      import RF2FileWrapper
from rf2db.parsers.RF2BaseParser import RF2Description
from rf2db.utils.lfuCache        import lfu_cache


    
class DescriptionDB(RF2FileWrapper):
     
    directory = 'Terminology'
    prefixes  = ['sct2_Description_', 'sct2_TextDefinition_']
    table = 'description'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id bigint(20) NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      conceptId bigint(20) NOT NULL,
      languageCode varchar(10) COLLATE utf8_bin NOT NULL,
      typeId bigint(20) NOT NULL,
      term text(16384) CHARACTER SET utf8 NOT NULL,
      caseSignificanceId bigint(20) NOT NULL,
      KEY concept (conceptId) USING BTREE,
       %(primkey)s ); """
    
    def __init__(self, *args, **kwargs): 
        RF2FileWrapper.__init__(self, *args, **kwargs)
        self._descTextDB = None
    
    @lfu_cache(maxsize=100)
    def getConceptDescription(self, conceptId, active=True, ss=True):
        db = self.connect()
        return [RF2Description(d) for d in db.query(self._tname(ss), "conceptId = %s" % conceptId, active=active, ss=ss)]
        
    def getConceptForDescription(self, descId, active=True, ss=True):
        rlist = self.getDescriptionById(descId, active, ss)
        return str(rlist.conceptId) if rlist else None
    
    @lfu_cache(maxsize=20)
    def getDescriptionById(self, descId, active=False, ss=True):
        db = self.connect()
        rlist = [RF2Description(d) for d in db.query(self._tname(ss), "id = %s" % descId, active=active, ss=ss)]
        return rlist[0] if len(rlist) else None

    @lfu_cache(maxsize=20)
    def getConceptDescriptionList(self, conceptId, active=True, ss=True, **kwargs):
        thelist = RF2Iterator.RF2DescriptionList(**kwargs)
        for d in self.getConceptDescription(conceptId, active, ss):
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(d)
        return thelist.finish(False)

