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

""" RF2 SimpleMap reference processing routines
"""


from rf2db.db.RF2FileCommon import RF2FileWrapper
   
class SimpleMapFileDB(RF2FileWrapper):
      
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
    
    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)
        
    def getMapEntries(self, refsetId, start=0, maxtoreturn=100, ss=True):
        """ Return maxtoreturn entries from the map file refset identified by refsetId """
        start       = int(start)
        maxtoreturn = int(maxtoreturn)
        db = self.connect()
        return db.query(self._tname(ss), "refsetId=%s" % refsetId, active=True, ss=ss,
                             start=start*maxtoreturn, maxtoreturn=maxtoreturn, sort='mapTarget')
        

