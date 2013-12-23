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
from rf2db.db.ParameterSets import iter_parms, base_parms

from rf2db.utils.lfuCache import lfu_cache

class all_conc_parms(iter_parms):
    def __init__(self, **kwargs):
        iter_parms.__init__(self, **kwargs)
        self.after = self._p.str('after')

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
    def getConcept(self, cid, **kwargs):
        """
        Read the concept record
        @param cid: concept SCTID
        """
        p = base_parms(**kwargs)
        db = self.connect()
        rlist = [RF2Concept(c) for c in db.query(self._tname(p.ss), "id=%s" % cid, active=p.active, ss=p.ss, moduleids=p.moduleids)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def getAllConcepts(self, **kwargs):
        """
        Read a number of concept records
        @param after: SCTID to start after
        """
        p = all_conc_parms(**kwargs)

        if not p.ss:
            raise Exception('FULL table not supported for complete concept list')
        db = self.connect()
        db.execute("SELECT * FROM %s WHERE %s" % (self._tname(p.ss), 'active=1' if p.active else 'TRUE') +
                   (' AND id > %s' % p.after if p.after else "") +
                   ((' AND moduleid IN (' + ', '.join([str(m) for m in p.moduleids])) if p.moduleids else '') +
                   (' ORDER BY id %s ' % p.order) +
                   (' LIMIT %s, %s' % (p.start, p.maxtoreturn + 1) if p.maxtoreturn else ""))

        return db.ResultsGenerator(db)

    @staticmethod
    def asConceptList(clist, **kwargs):
        thelist = RF2ConceptList(**kwargs)
        for c in clist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(RF2Concept(c))
        return thelist.finish(False)

