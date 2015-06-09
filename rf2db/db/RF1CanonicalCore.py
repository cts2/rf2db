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
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
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
import os

from rf2db.db.RF2FileCommon import RF2FileWrapper

class CanonicalCoreDB(RF2FileWrapper):
    directory = os.path.join('OtherResources', 'Canonical Table')
    prefixes = ['res1_Canonical_Core_']
    table = 'canonical_core'
    isRF1File = True

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      conceptid1 bigint(20) NOT NULL,
      relationshiptype bigint(20) NOT NULL,
      conceptid2 bigint(20) NOT NULL,
      relationshipgroup int(11) NOT NULL,
      KEY conceptid1 (conceptid1) USING HASH);"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file):
        from rf2db.db.RF2RelationshipFile import RelationshipDB
        from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB
        rdb = RelationshipDB()
        srdb = StatedRelationshipDB()
        if not rdb.hascontent() or not srdb.hascontent():
            print(("Relationship databases must be loaded before loading %s" % self._fname))
            return

        super(CanonicalCoreDB, self).loadTable(rf2file)

        print("Updating Stated Relationship File")
        srdb.updateFromCanonical(self._fname)

        print("Updating Relationship File")
        rdb.updateFromCanonical(self._fname)