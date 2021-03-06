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

from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.parsers.RF2Iterator import iter_parms
from rf2db.parsers.RF2BaseParser import RF2Description
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms, rf2_values
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, strparam, enumparam
from rf2db.exceptions import RF2Exceptions

""" Parameters for text matching. """
description_match_parms = ParameterDefinitionList(global_rf2_parms)
description_match_parms.add(iter_parms)
description_match_parms.matchvalue = strparam(splittable=True)
description_match_parms.matchalgorithm = enumparam(['contains', 'startswith', 'endswith', 'exactmatch', 'wordstart',
                                                    'wordend', 'phrase'], default='wordstart')


class DescriptionTextDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Description_']
    table = 'description_text'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      conceptId bigint(20) NOT NULL,
      languageCode varchar(10) COLLATE utf8_bin NOT NULL,
      typeId bigint(20) NOT NULL,
      term text(8192) CHARACTER SET utf8 NOT NULL,
      caseSignificanceId bigint(20) NOT NULL,
      conceptActive tinyint(1) DEFAULT NULL,
      KEY concept (conceptId),
      FULLTEXT(term),
       %(keys)s
    ) ENGINE=MyISAM;"""

    _loadStmt1 = """INSERT IGNORE INTO %(table)s SELECT d.*, 0 FROM %(desctable)s d,
         (SELECT id, MAX(effectiveTime) AS effectiveTime FROM %(desctable)s GROUP BY id) as d_keys
        WHERE d.id = d_keys.id AND d.effectiveTime = d_keys.effectiveTime AND d.active = 1;"""

    _loadStmt2 = """UPDATE %(table)s, %(conctable)s as c,
        (SELECT id, MAX(effectiveTime) AS effectiveTime FROM %(conctable)s GROUP BY id) as c_keys
        SET conceptActive = c.active
        WHERE c.id = c_keys.id AND c.effectiveTime = c_keys.effectiveTime
        AND conceptid = c.id;"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    hasrf2rec = True
    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2Description(*args, **kwargs)

    @staticmethod
    def _d(**kwargs):
        return vars()['kwargs']

    def loadTable(self, rf2file):
        cdb = ConceptDB()
        ddb = DescriptionDB()
        if cdb.hascontent() and ddb.hascontent():
            db = self.connect()
            db.execute(
                self._loadStmt1 % self._d(table=self._fname, desctable=ddb._fname, conctable=cdb._fname))
            db.commit()
            db.execute(
                self._loadStmt2 % self._d(table=self._fname, desctable=ddb._fname, conctable=cdb._fname))
            db.commit()
        else:
            print("Concept and Description tables must be loaded first")


    def loadFile(self):
        print((self.table, "must be loaded from", ConceptDB.fname(), "and", DescriptionDB.fname(), "tables"))


    @lfu_cache(100)
    def getDescriptions(self,
                        matchvalue='',
                        matchalgorithm='wordstart',
                        maxtoreturn=None,
                        active=True,
                        moduleid=None,
                        order='asc',
                        start=0,
                        sort=None,
                        **kwargs):
        """
        Return all descriptions that match the matchvalues(s) using the supplied match algorithm.

        Note: description_ss is the combination of the description and definition snapshots joined
        to active (conceptActive) on the conceptfile
        @param matchvalues: set of values to match
        @param matchalgorithm: algorithm or set of algorithms to match
        @param maxtoreturn: max to return
        @param kwargs: context
        @return: matching descriptions (or count if maxtoreturn == 0)
        """

        # If we have more algorithms than values, repeat the last value out to match the algorithms
        if maxtoreturn is None:
            maxtoreturn=rf2_values.defaultblocksize
        matchalgorithms = listify(matchalgorithm)
        matchvalues = listify(matchvalue)
        diff = len(matchalgorithms) - len(matchvalues)
        if diff > 0:
            matchvalues += matchvalues[-1:] * diff
        elif diff < 0:
            matchalgorithms += matchalgorithms[-1:] * -diff

        query = "SELECT %s FROM %s WHERE 1" % ('*' if maxtoreturn != 0 else 'count(*)', self._fname)
        # TODO: Make sure that injections have been filtered before we get here
        for (v, a) in zip(matchvalues, matchalgorithms):
            if v:
                if a == 'contains':
                    query += " AND term LIKE('%%%s%%')" % v
                elif a == 'startswith':
                    query += " AND term LIKE ('%s%%')" % v
                elif a == 'endswith':
                    query += " AND term LIKE ('%%%s')" % v
                elif a == 'exactmatch':
                    query += " AND term = '%s'" % v
                elif a == 'word':
                    query += " AND (term LIKE ('%% %s %%') OR term LIKE('%s %%') OR term LIKE('%% %s') OR term = '%s')" % (
                    v, v, v, v)
                elif a == 'wordstart':
                    query += " AND (term LIKE ('%s%%') OR term LIKE ('%% %s%%'))" % (v, v)
                elif a == 'wordend':
                    query += " AND (term LIKE ('%%%s') OR term LIKE ('%%%s %%'))" % (v, v)
                elif a == 'phrase':
                    query += " AND term LIKE('%s%%')" % v
                else:
                    raise RF2Exceptions.UnknownMatchAlgorithm(
                        a + ' : valid values are contains, startswith, endswith, exactmatch, word, wordstart and phrase')
        if active:
            query += " AND active = 1 AND conceptActive = 1"
        if moduleid:
            query += ' AND ' + ' AND '.join(['moduleid = %s' % m for m in listify(moduleid)])
        query += " ORDER BY "
        if sort:
            query += ', '.join( ("%s " % s) + order for s in listify(sort)) + ', '
        query += " length(term) %s, term %s" % (order, order)

        if maxtoreturn > 0:
            query += " LIMIT %s, %s" % (start, maxtoreturn + 1)
        db = self.connect()
        db.execute(query)
        return [RF2Description(d) for d in db.ResultsGenerator(db)] if maxtoreturn != 0 else list(
            db.ResultsGenerator(db))

    def add(self, **kwargs):
        locals = kwargs.copy()
        locals['fname'] = self._fname
        db = self.connect()
        db.execute_query("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, "
                         "conceptId, languageCode, typeId, term, caseSignificanceId, conceptActive, changeset, locked) "
                         "VALUES (%(descid)s, %(effectivetime)s, 1, %(moduleid)s, "
                         "%(concept)s, '%(language)s', %(typeid)s, '%(term)s', %(csig)s, 1, '%(changeset)s', 1 )" % locals)
        db.commit()
