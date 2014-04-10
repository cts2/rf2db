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

""" Function to build the SNOMED CT Transitive Closure File
"""


from rf2db.db.RF2DBConnection import RF2DBConnection
from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.constants.RF2ValueSets import is_a
from rf2db.db.RF2RelationshipFile import RelationshipDB

chunksize = 100000

class Paths(object):
    def __init__(self, src, graph):
        self._src  = src
        self._destmap = {}
        self._graph = graph
        self.dfs(src)

    def dfs(self, src, depth=1):
        for dst in self._graph.get(src,[]):
            self.addchild(dst, depth, dst not in self._graph)
            self.dfs(dst, depth+1)

    def addchild(self, dest, depth, isleaf):
        self._destmap.setdefault(dest, [depth, isleaf])
        if depth < self._destmap[dest][0]:
            self._destmap[dest][0] = depth
        if isleaf != self._destmap[dest][1]:
            assert False, "Serious logic error in leaf detection"

    def entries(self):
        for (k,v) in self._destmap.items():
            yield self._src, k, v[0], v[1]
        raise StopIteration()

def transitive_closure(g):
    """ Convert a set of source/destination tuples into a dictionary
        whose key is the source concept
        and the data is a set of destinations """
    gdict = {}
    for dest, src in g: gdict.setdefault(src, set()).add(dest)

    closure = set()
    for src in gdict.iterkeys():
        paths = Paths(src, gdict)
        closure |= set(p for p in paths.entries())
    return closure

class TransitiveClosureDB(RF2FileWrapper):
    table = 'transitive'
    fltr = ' active = 1 '

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
            `sourceId` bigint(20) NOT NULL,
            `destinationId` bigint(20) NOT NULL,
            `depth` int NOT NULL,
            `isLeaf` tinyint NOT NULL,
            `isRoot` tinyint NOT NULL DEFAULT 0);"""


    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file, ss, cfg):
        print("Reading active relationships from relationship snapshot table")
        db = RF2DBConnection()
        rdb = RelationshipDB()
        if not rdb.hascontent(True):
            print("Error: Transitive table load requires Snapshot releationship table")
            return

        db.execute("""SELECT sourceId, destinationId FROM %s WHERE %s AND typeId = %s""" %
                   (rdb._tname(True), self.fltr, is_a))

        print("Computing transitive closure")
        tbl = {'tname':self._tname(ss)}
        tc = list(transitive_closure(db))
        print("Dropping indices")
        TransitiveClosureDB._dropIndexes(tbl)
        print("Writing records to table")
        for s in range(0, len(tc), chunksize):
            TransitiveClosureDB._writeblock(tc[s:s+chunksize], db, tbl)

        print("Indexing table")
        TransitiveClosureDB._createIndexes(tbl)

        print("Computing root entries")
        db.execute("""UPDATE %s t1 LEFT JOIN %s t2 ON t1.sourceid=t2.destinationid
                      SET t1.isRoot=1
                      WHERE t1.depth=1 AND t2.destinationid IS null""" % (self._tname(True), self._tname(True)))
        db.commit()


    @staticmethod
    def _writeblock(tc, db, tbl):
        insertList = ["(%s,%s,%s,%s)" % e for e in tc]
        db.execute("INSERT INTO %(tname)s (sourceId, destinationId, depth, isLeaf) VALUES " % tbl + ','.join(insertList) )
        db.commit()

    @staticmethod
    def _dropIndexes(tbl):
        db = RF2DBConnection()
        # Strange as it may seem, mysql doesn't have a drop index if exists command
        try:
            db.execute("""DROP INDEX %(tname)s_idx1 on %(tname)s""" % tbl)
        except Exception:
            pass
        try:
            db.execute("""DROP INDEX %(tname)s_idx2 on %(tname)s""" % tbl)
        except Exception:
            pass
        try:
            db.execute("""DROP INDEX %(tname)s_idx3 on %(tname)s""" % tbl)
            db.commit()
        except Exception as e:
            pass


    @staticmethod
    def _createIndexes(tbl):
        db = RF2DBConnection()

        db.execute("""CREATE UNIQUE INDEX %(tname)s_idx1 ON %(tname)s(sourceId, destinationId)""" % tbl)
        db.execute("""CREATE INDEX %(tname)s_idx2 ON %(tname)s(sourceId)""" % tbl)
        db.execute("""CREATE INDEX %(tname)s_idx3 ON %(tname)s(destinationId)""" % tbl)
        db.commit()


    def are_related(self, parent, child):
        if parent == child:
            return True
        db = self.connect()
        tname = self._tname(True)
        return bool(list(db.executeAndReturn(
            "SELECT count(*) FROM %(tname)s WHERE sourceId = %(parent)s AND destinationId=%(child)s" % locals()))[0][0])

    def doquery(self, query, start, maxtoreturn):
        start, maxtoreturn = int(start), int(maxtoreturn)
        db = self.connect()
        if maxtoreturn:
            query += " LIMIT %d, %d " % (start * maxtoreturn, maxtoreturn + 1)
        db.execute(query)
        rval = set([e if len(e) > 1 else e[0] for e in db])
        return rval


    def hasChildren(self, sctid, **kwargs):
        return bool(self.children(sctid, maxtoreturn=1, **kwargs))

    def children(self, sctid, start=0, maxtoreturn=0, **kwargs):
        return self.doquery("SELECT destinationId FROM %s WHERE sourceId = %s AND depth=1 ORDER BY destinationId" %
                            (self._tname(True), sctid), start, maxtoreturn)

    def parents(self, sctid, **kwargs):
        return self.doquery("SELECT sourceId FROM %s WHERE destinationId = %s AND depth=1 ORDER BY sourceId" %
                            (self._tname(True), sctid), start=0, maxtoreturn=0)





            
        


