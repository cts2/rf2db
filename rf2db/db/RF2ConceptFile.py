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
from rf2db.parsers.RF2Iterator import RF2ConceptList, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, intparam


# Parameters for concept access
concept_parms = global_rf2_parms
concept_list_parms = ParameterDefinitionList(global_rf2_parms)
concept_list_parms.add(iter_parms)
concept_list_parms.after = intparam()


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
    def getConcept(self, cid, parmlist):
        """
        Read the concept record
        @param cid: concept sctid
        """
        db = self.connect()
        rlist = [RF2Concept(c) for c in db.query_p(self._tname(parmlist.ss), parmlist, filter="id=%s" % cid)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def getAllConcepts_p(self, active=1, order='asc', page=0, maxtoreturn=100, after=0):
        return self.getAllConcepts(concept_list_parms.parse(
            **{'active': active, 'order': order, 'page': page, 'maxtoreturn': maxtoreturn, 'after': after}))

    def getAllConcepts(self, parmlist):
        """
        Read a number of concept records
        @param parmlist: parsed parameter list
        """

        if not parmlist.ss:
            raise Exception('FULL table not supported for complete concept list')
        db = self.connect()
        query = 'SELECT %s FROM %s' % ('*' if parmlist.maxtoreturn else 'count(*)', self._tname(parmlist.ss))
        query += ' WHERE %s ' % ('active=1' if parmlist.active else 'TRUE')
        if parmlist.after:
            query += ' AND id > %s' % parmlist.after
        if parmlist.moduleid:
            query += ' AND ' + ' AND '.join(['moduleid = %s' % m for m in listify(parmlist.moduleid)])
        if parmlist.order:
            query += ' ORDER BY id %s' % parmlist.order
        if parmlist.maxtoreturn:
            query += ' LIMIT %s, %s' % (parmlist.start, parmlist.maxtoreturn + 1)
        db.execute(query)
        return [RF2Concept(c) for c in db.ResultsGenerator(db)] if parmlist.maxtoreturn else list(
            db.ResultsGenerator(db))

    @staticmethod
    def asConceptList_p(clist, active=1, order='asc', page=0, maxtoreturn=100, after=0):
        return ConceptDB.asConceptList(clist, concept_list_parms.parse(
            **{'active': active, 'order': order, 'page': page, 'maxtoreturn': maxtoreturn, 'after': after}))

    @staticmethod
    def asConceptList(clist, parmlist):
        thelist = RF2ConceptList(parmlist)
        if not parmlist.maxtoreturn:
            return thelist.finish(True, total=list(clist)[0])
        for c in clist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(c)
        return thelist.finish(False)

