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

from rf2db.parsers.RF2BaseParser import RF2Concept
from rf2db.db.RF2FileCommon import RF2FileWrapper

from rf2db.utils.lfuCache import lfu_cache


class ConceptDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Concept_']
    table = 'concept'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id bigint(20) NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      definitionStatusId bigint(20) NOT NULL,
       KEY id (id),
       %(primkey)s );"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @lfu_cache(maxsize=20)
    def getConcept(self, cid, active=True, ss=True):
        """
        Read the concept record
        @param cid: concept SCTID
        @param active: True - only return active concepts
        @param ss: True - use snapshot tables.  False, use full tables
        @return: RF2Concept record or None if not found
        """
        db = self.connect()
        rlist = [RF2Concept(c) for c in db.query(self._tname(ss), "id=%s" % cid, active=active, ss=ss)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def getAllConcepts(self, active=True, ss=True, limit=None, after=None):
        """
        Retrieve all (or all active) concepts
        @param active: active concepts only or all
        @param ss: snapshot table or full table
        @param limit: maximum number to return (default: all)
        @param after: sctid to start after (default: start at beginning of the file
        @return: generator for entries in the concept file
        """
        db = self.connect()
        if not ss:
            raise Exception('FULL table not supported for complete concept list')
        return db.executeAndReturn("SELECT * FROM %s WHERE %s" % (self._tname(ss), 'ACTIVE=1' if active else 'TRUE') +
                                   (' AND id > %s' % after if after else "") +
                                   ' ORDER BY id ASC ' +
                                   (" LIMIT %s" % limit if limit else ""))


