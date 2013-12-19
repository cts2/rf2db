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
from rf2db.parsers.RF2Iterator import RF2ConceptList
from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.utils.ParmParser import boolparam, intparam

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

    @lfu_cache(maxsize=100)
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

    def getAllConcepts(self, **kwargs):
        """
        @param active: return only active entities C{True} or all C{False}.  Default: C{True}
        @type active: boolean

        @param page: return starting at M{maxtoreturn*page}. Default: 0
        @type page: int

        @oaran after: sctid to start after
        @type after: str

        @param maxtoreturn: number of entries to return.  Default: 100
        @type maxtoreturn: int

        @param moduleid: constrain to entries in this module.
        @type moduleid: sctid
        """
        active = boolparam(kwargs.pop('active', None), True)
        page = intparam(kwargs.get('page', 0), 0)
        order = kwargs.pop('order', 'asc')
        after = kwargs.pop('after', None)
        if order.lower() not in ('asc', 'desc'):
            order = 'asc'

        maxtoreturn = intparam(kwargs.get('maxtoreturn'), 100)
        start = page * maxtoreturn
        moduleid = kwargs.get('moduleid')
        ss = boolparam(kwargs.get('ss'), True)

        if not ss:
            raise Exception('FULL table not supported for complete concept list')
        db = self.connect()
        db.execute("SELECT * FROM %s WHERE %s" % (self._tname(ss), 'ACTIVE=1' if active else 'TRUE') +
                           (' AND id > %s' % after if after else "") +
                           (' ORDER BY id %s ' % order) +
                           (" LIMIT %s, %s" % (start, maxtoreturn + 1) if maxtoreturn else ""))

        thelist = RF2ConceptList(**kwargs)
        src = db.ResultsGenerator(db)
        for d in src:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(RF2Concept(d))
        return thelist.finish(False)
