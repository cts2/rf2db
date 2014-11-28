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

""" Synthetic Preferred Name and FSN file for RF2
"""

from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.db.RF2LanguageFile import LanguageDB
from rf2db.db.RF2DBConnection import RF2DBConnection, cp_values
from rf2db.constants import RF2ValueSets
from rf2db.utils.lfu_cache import lfu_cache

BATCH_SIZE = 1000

class PNandFSNDB(RF2FileWrapper):
    directory = ''        # Loaded strictly from other tables
    prefixes = []
    table = 'RF2PNandFSN'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id   BIGINT(20) NOT NULL,
      lang BIGINT(20) NOT NULL,
      fsn  VARCHAR(1024) CHARACTER SET utf8 NOT NULL,
      pn   VARCHAR(1024) CHARACTER SET utf8 NOT NULL,
      PRIMARY KEY(id,lang))"""

    selSTMT = """SELECT d.conceptid, l.refsetId, d.typeId, d.term FROM %(descfn)s AS d, %(langfn)s AS l
       WHERE l.referencedComponentId = d.id AND
             l.active = 1 and d.active = 1 AND
             l.acceptabilityId = %(pref)s AND
             d.typeId IN (%(fsn)s, %(syn)s)
       ORDER BY d.conceptid, l.refsetId ASC"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)


    class _inserter(object):
        def __init__(self, db, filename, batchsize):
            self._db = db
            self._filename = filename
            self._batchsize = batchsize
            self._insertList = []

        def append(self, rec):
            self._insertList.append(rec)
            if len(self._insertList) >= self._batchsize:
                self.flush()

        def flush(self):
            if len(self._insertList):
                self._db.execute(
                    "INSERT INTO %s (id, lang, fsn, pn) VALUES " % self._filename + ','.join(self._insertList))
                self._db.commit(disconnect=False)
            self._insertList = []


    @staticmethod
    def _d(**kwargs):
        return vars()['kwargs']

    def loadTable(self, _):
        """
        @param _: unused
        """
        if not cp_values.ss:
            print "Index only works on snapshot files at the moment"
            return

        descdb = DescriptionDB()
        langdb = LanguageDB()

        if not (descdb.hascontent() and langdb.hascontent()):
            print "Description and Language tables must be loaded before loading %s" % self._fname
            return

        db = self.connect()

        args = self._d(descfn = descdb._fname,
                       langfn = langdb._fname,
                       pref = RF2ValueSets.preferred,
                       fsn = RF2ValueSets.fsn,
                       synv = RF2ValueSets.synonym)

        loader = self._inserter(RF2DBConnection(), self._fname, BATCH_SIZE)
        key = [0, 0]
        fsn = ""
        pn = ""
        print "Executing query..."
        for e in db.executeAndReturn(self.selSTMT % args):
            if key != e[0:2]:
                if key[0]:
                    loader.append("(%s, %s, '%s', '%s')" % (key[0], key[1], fsn, pn))
                else:
                    print "done"
                key = e[0:2]
                fsn = ""
                pn = ""
            if e[2] == RF2ValueSets.fsn:
                fsn = e[3].replace("'", r"\'")
            else:
                pn = e[3].replace("'", r"\'")
        loader.flush()

    @lfu_cache(maxsize=200)
    def getfsn(self, cid, language=RF2ValueSets.us_english, **_):
        rlist = [e[0] for e in self.connect().executeAndReturn(
            "SELECT fsn FROM %s WHERE id = %s AND lang = %s" % (self._fname, cid, language))]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    @lfu_cache(maxsize=200)
    def getpn(self, cid, language=RF2ValueSets.us_english, **_):
        rlist = [e[0] for e in self.connect().executeAndReturn(
            "SELECT pn FROM %s WHERE id = %s AND lang = %s" % (self._fname, cid, language))]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    @lfu_cache(maxsize=200)
    def getpnfsn(self, cid, language=RF2ValueSets.us_english, **_):
        rlist = [(e[0], e[1]) for e in self.connect().executeAndReturn(
            "SELECT pn, fsn FROM %s WHERE id = %s AND lang = %s" % (self._fname, cid, language))]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None




