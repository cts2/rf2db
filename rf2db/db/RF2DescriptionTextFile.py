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

from rf2db.parsers import RF2Iterator

from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.exceptions import RF2Exceptions
from rf2db.parsers.RF2BaseParser import RF2Description
from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.utils.listutils import listify
from rf2db.utils.ParmParser import boolparam, intparam
from rf2db.db.ParameterSets import iter_parms


class match_parms(iter_parms):
    matchalgorithms = ['contains','startswith', 'endswith', 'exact', 'wordstart', 'phrase']

    def __init__(self, **kwargs):
        iter_parms.__init__(self, **kwargs)
        self.matchvalue=self._p.str('matchvalue')
        self.matchalgorithm=self._p.enum('matchalgorithm', self.matchalgorithms)

class DescriptionTextDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Description_']
    table = 'description_text'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id bigint(20) NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      conceptId bigint(20) NOT NULL,
      languageCode varchar(10) COLLATE utf8_bin NOT NULL,
      typeId bigint(20) NOT NULL,
      term text(8192) CHARACTER SET utf8 NOT NULL,
      caseSignificanceId bigint(20) NOT NULL,
      conceptActive tinyint(1) DEFAULT NULL,
      KEY concept (conceptId),
      FULLTEXT(term),
       %(primkey)s 
    ) ENGINE=MyISAM;"""

    _loadStmt1 = """INSERT INTO %(table)s SELECT d.*, 0 FROM %(desctable)s d, 
         (SELECT id, MAX(effectiveTime) AS effectiveTime FROM %(desctable)s GROUP BY id) as d_keys
        WHERE d.id = d_keys.id AND d.effectiveTime = d_keys.effectiveTime AND d.active = 1;"""

    _loadStmt2 = """UPDATE %(table)s, %(conctable)s as c,
        (SELECT id, MAX(effectiveTime) AS effectiveTime FROM %(conctable)s GROUP BY id) as c_keys
        SET conceptActive = c.active
        WHERE c.id = c_keys.id AND c.effectiveTime = c_keys.effectiveTime
        AND conceptid = c.id;"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file, ss, cfg):
        cdb = ConceptDB()
        ddb = DescriptionDB()
        if cdb.hascontent(ss) and ddb.hascontent(ss):
            db = self.connect()
            db.execute(
                self._loadStmt1 % {'table': self._tname(ss), 'desctable': ddb._tname(ss), 'conctable': cdb._tname(ss)})
            db.commit()
            db.execute(
                self._loadStmt2 % {'table': self._tname(ss), 'desctable': ddb._tname(ss), 'conctable': cdb._tname(ss)})
            db.commit()
        else:
            print("Concept and Description tables must be loaded first")


    def loadFile(self, fname, ss):
        print(self.table, "must be loaded from", ConceptDB.table, "and", DescriptionDB.table, "tables")

    def getDescriptions(self, **kwargs):
        """ 
        Return all descriptions that match the matchvalues(s) using the supplied match algorithm.
        
        @param active: return only active entities C{True} or all C{False}.  Default: C{True}
        @type active: boolean

        @param page: return starting at M{maxtoreturn*page}. Default: 0
        @type page: int

        @param maxtoreturn: number of entries to return.  Default: 100
        @type maxtoreturn: int

        @param matchvalue: match text.
        @type matchvalue: str or list(str)

        @param moduleid: constrain to entries in this module.
        @type moduleid: sctid

        @param order: sort order - asc or desc

        @param matchalgorithm: match algorithm to use. One of
        - "contains" - match any phrase that contains matchvalue
        - "startswith"
        - "exactmatch"
        - "endswith"
        @type matchalgorithm: localname
        
        Note: description_ss is the combination of the description and definition snapshots joined
        to active (conceptActive) on the conceptfile
        """
        active = boolparam(kwargs.pop('active',None), True)
        page = intparam(kwargs.get('page', 0), 0)
        matchvalues = listify(kwargs.pop('matchvalue', []))
        matchalgorithms = listify(kwargs.pop('matchalgorithm', None),'contains')
        order = kwargs.pop('order', 'asc')
        if order.lower() not in ('asc', 'desc'):
            order = 'asc'

        maxtoreturn = intparam(kwargs.get('maxtoreturn'), 100)
        start = page * maxtoreturn
        moduleid = kwargs.get('moduleid')
        ss = boolparam(kwargs.get('ss'), True)

        # If we have more algorithms than values, repeat the last value out to match the algorithms
        diff = len(matchalgorithms) - len(matchvalues)
        if diff > 0:
            matchvalues += matchvalues[-1:] * diff
        elif diff < 0:
            matchalgorithms += matchalgorithms[-1:] * -diff

        query = "SELECT * FROM %s WHERE 1" % self._tname(ss)

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
                    query += " AND (term LIKE ('%% %s %%') OR term LIKE('%s %%') OR term LIKE('%% %s') OR term = '%s')" % (v,v,v,v)
                elif a == 'wordstart':
                    query += " AND (term LIKE ('%s%%') OR term LIKE ('%% %s%%'))" % (v,v)
                elif a == 'phrase':
                    query += " AND term LIKE('%s%%')" % v
                else:
                    raise RF2Exceptions.UnknownMatchAlgorithm(
                        a + ' : valid values are contains, startswith, endswith, exactmatch, word, wordstart and phrase')
        if active:
            query += " AND active = 1 AND conceptActive = 1"
        query += " ORDER BY length(term) %s, term %s" % (order, order)

        if maxtoreturn:
            query += " LIMIT %s, %s" % (start, maxtoreturn + 1)
        db = self.connect()
        db.execute(query)

        thelist = RF2Iterator.RF2DescriptionList(**kwargs)
        src = db.ResultsGenerator(db)
        for d in src:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(RF2Description(d))
        return thelist.finish(False)


