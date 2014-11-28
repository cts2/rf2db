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

""" Function to build the SNOMED CT Transitive Children file -- a helper table that
    returns the number of children given a source concept and depth
"""

from rf2db.db.RF2DBConnection import RF2DBConnection
from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.db.RF2TransitiveClosure import TransitiveClosureDB


class TransitiveChildrenDB(RF2FileWrapper):
    table = 'transitive_children'
    closuredb = TransitiveClosureDB

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
            `sourceId` bigint(20) NOT NULL,
            `depth` int NOT NULL,
            `count` int NOT NULL DEFAULT 0,
             PRIMARY KEY (sourceId, depth));"""

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file):
        db = RF2DBConnection()
        print("Populating transitive children table")
        tcdb = self.closuredb()
        if not tcdb.hascontent():
            print("Error: Transitive children load requires transitive closure table")
            return
        tname = self._fname
        tcdbname = TransitiveClosureDB.fname()
        db.execute("""INSERT INTO %(tname)s
                      SELECT DISTINCT sourceid, depth, 0 FROM %(tcdbname)s""" % locals())
        db.commit()

        print("Computing number of children")
        db.execute("""UPDATE %(tname)s t,
                       (SELECT c.sourceid, c.depth, count(t.sourceid) AS dc
                           FROM %(tcdbname)s t, %(tname)s c
                           WHERE t.sourceid=c.sourceid AND t.depth<=c.depth
                           GROUP BY c.sourceid, c.depth) tc
                        SET t.count = tc.dc
                        WHERE t.sourceid=tc.sourceid AND t.depth=tc.depth""" % locals())
        db.commit()


    def numDescendants(self, sctid, maxDepth=0, ss=True, **_):
        # The following assumes that count can't increase as depth increases
        query = "SELECT max(count) FROM %s WHERE sourceId = %s " % (self._fname, sctid)
        if maxDepth:
            query += " AND depth <= %s " % maxDepth
        db = RF2DBConnection()
        db.execute(query)
        return db.next()






            
        


