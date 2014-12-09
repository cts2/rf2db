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

""" The SNOMED CT Transitive Closure file.  This file carries the transitive closure of
the SNOMED CT is_a relationship, which allows one to determine all children of a given parent or
all parents for a given child.  The one based depth provides the number of hops to the given
parent or child.  In the case of multiple paths, the shortest number of hops is the one provided.
"""

from mysql.connector import ProgrammingError
from mysql.connector.errorcode import ER_CANT_DROP_FIELD_OR_KEY

from rf2db.db.RF2DBConnection import RF2DBConnection, cp_values
from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.constants.RF2ValueSets import is_a
from rf2db.db.RF2RelationshipFile import RelationshipDB


chunksize = 100000      # Chunk size for batch database writes on load


class Paths(object):
    """ The set of children of a given  parent according to the supplied graph
    """
    def __init__(self, parent, graph):
        self._parent = parent
        self._destmap = {}      # map from child to (depth, isLeaf) tuple
        self._graph = graph     # graph being traversed
        self.dfs(parent)

    def dfs(self, src, depth=1):
        """ Depth first search.  Add children to the graph using a recursive depth first traversal.
        @param src: parent concept
        @param depth: search depth
        """
        for child in self._graph.get(src, []):
            self.addchild(child, depth, child not in self._graph)
            self.dfs(child, depth+1)

    def addchild(self, child, depth, isleaf):
        """ Add a child to the graph
        @param child: child to add to the graph
        @param depth: number of hops to the child (1 based)
        @param isleaf: child has no descendants
        """
        self._destmap.setdefault(child, [depth, isleaf])
        if depth < self._destmap[child][0]:
            self._destmap[child][0] = depth
        if isleaf != self._destmap[child][1]:
            assert False, "Serious logic error in transitive closure leaf detection"

    def entries(self):
        """ Iterate over the entries in the map
        @return: parent, child, depth, isLeaf tuple
        """
        for (k, v) in self._destmap.items():
            yield self._parent, k, v[0], v[1]
        raise StopIteration()


def transitive_closure(g):
    """ Convert a set of source/destination tuples into a dictionary
        whose key is the source concept
        and the data is a set of destinations """
    gdict = {}
    for dest, src in g:
        gdict.setdefault(src, set()).add(dest)

    closure = set()
    for src in gdict.iterkeys():
        paths = Paths(src, gdict)
        closure |= set(p for p in paths.entries())
    return closure


class TransitiveClosureDB(RF2FileWrapper):
    table = 'transitive'
    fltr = ' active = 1 '


    # The transitive table reflects the contents of the relationship table.
    # parent: destinationId of an active SNOMED CT is_a (or other transtive) relationship
    # child: the sourceId of an active SNOMED CT is_a relationship
    # depth: one based number of hops from parent to child (minimum if multiple paths)
    # isLeaf: true means child is not a parent
    # isRoot: true means that parent is not a child
    # locked: true means that parent is locked in a changeset and should not be visible
    #         if the parent isn't visible.
    createSTMT = ("CREATE TABLE IF NOT EXISTS %(table)s ("
                  "parent bigint(20) NOT NULL, "
                  "child bigint(20) NOT NULL, "
                  "depth int NOT NULL, "
                  "isLeaf tinyint NOT NULL, "
                  "isRoot tinyint NOT NULL DEFAULT 0, "
                  "locked tinyint(1) NOT NULL DEFAULT 0 "
                  ");")

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file):
        print("Reading active relationships from relationship snapshot table")
        db = RF2DBConnection()
        rdb = RelationshipDB()
        fname = self._fname
        if not cp_values.ss:
            print("Error: Transitive closure not implemented for FULL tables")
            return
        if not rdb.hascontent():
            print("Error: Transitive table load requires Snapshot releationship table")
            return

        db.execute("SELECT sourceId, destinationId FROM %s WHERE %s AND typeId = %s" %
                   (rdb._fname, self.fltr, is_a))

        print("Computing transitive closure")
        tc = list(transitive_closure(db))
        print("Dropping indices")
        TransitiveClosureDB._dropindices(self._fname)
        print("Writing records to table")
        for s in range(0, len(tc), chunksize):
            TransitiveClosureDB._writeblock(tc[s:s+chunksize], db, fname)
        print("Creating indices")
        TransitiveClosureDB._createindices(fname)
        print("Computing root entries")
        db.execute_query("UPDATE %(fname)s t1 LEFT JOIN %(fname)s t2 ON t1.parent=t2.child "
                         "SET t1.isRoot=1 WHERE t1.depth=1 AND t2.child IS null" % vars())
        db.commit()


    @staticmethod
    def _writeblock(tc, db, fname):
        insertlist = ["(%s,%s,%s,%s)" % e for e in tc]
        db.execute("INSERT INTO %(fname)s (parent, child, depth, isLeaf) VALUES " % vars() + ','.join(insertlist))
        db.commit()

    @staticmethod
    def _dropindices(fname):
        db = RF2DBConnection()
        commit_needed = False
        # Strange as it may seem, mysql doesn't have a drop index if exists command
        try:
            db.execute_query("DROP INDEX %(fname)s_idx1 on %(fname)s" % vars())
            commit_needed = True
        except ProgrammingError as e:
            if e.errno != ER_CANT_DROP_FIELD_OR_KEY:
                raise e
        try:
            db.execute_query("DROP INDEX %(fname)s_idx2 on %(fname)s" % vars())
            commit_needed = True
        except ProgrammingError as e:
            if e.errno != ER_CANT_DROP_FIELD_OR_KEY:
                raise e
        try:
            db.execute_query("DROP INDEX %(fname)s_idx3 on %(fname)s" % vars())
            commit_needed = True
        except ProgrammingError as e:
            if e.errno != ER_CANT_DROP_FIELD_OR_KEY:
                raise e
        if commit_needed:
            db.commit()


    @staticmethod
    def _createindices(fname):
        db = RF2DBConnection()
        db.execute("CREATE UNIQUE INDEX %(fname)s_idx1 ON %(fname)s(parent, child)" % vars())
        db.execute("CREATE INDEX %(fname)s_idx2 ON %(fname)s(parent, locked)" % vars())
        db.execute("CREATE INDEX %(fname)s_idx3 ON %(fname)s(child, locked)" % vars())
        db.commit()

    addstatement = "INSERT INTO %(fname)s (parent, child, depth, isLeaf, isRoot, locked) " +\
                   "VALUES (%(parent)s, %(child)s, %(depth)d, %(isleaf)d, %(isroot)d,  %(locked)d) "

    def addrow(self, db, parent, child, depth, isleaf, isroot, changeset):
        fname = self._fname
        locked = 1
        isleaf = 1 if isleaf else 0
        isroot = 1 if isroot else 0
        db.execute_query(self.addstatement % vars())
        if not isroot:
            for p in self.parents(parent):
                self.addrow(db, p, child, depth+1, 0, self.hasParents(p, changeset), changeset)

    def add(self, sourceid, typeid, destinationid, changeset):
        if typeid != is_a:
            return
        parent = destinationid
        child = sourceid
        isleaf = self.hasChildren(child, changeset=changeset)
        isroot = not self.hasParents(parent, changeset=changeset)
        locked = 1
        db = self.connect()
        self.addrow(db, parent, child, 1, self.hasChildren(child, changeset=changeset),
                    self.hasParents(parent, changeset=changeset), changeset)
        db.commit()

    def unlock(self, db, sourceid):
        fname = self._fname
        db.execute_query("UPDATE %(fname)s SET locked=0 WHERE child=%(sourceid)s" % vars())

    def remove(self, db, sourceid):
        fname = self._fname
        db.execute_query("DELETE FROM %(fname)s WHERE child=%(sourceid)s AND locked=1" % vars())


    def are_related(self, parent, child, changeset=None):
        if parent == child:
            return True
        db = self.connect()
        tname = self._fname
        filtr = " AND locked = 0" if not changeset else ""
        return bool(list(db.executeAndReturn(
            "SELECT count(*) FROM %(tname)s WHERE parent = %(parent)s AND child=%(child)s %(filtr)s" % locals()))[0][0])


    def doquery(self, rtnchild, sctid, start=0, maxtoreturn=0, changeset=None, **_):
        db = self.connect()
        fname = self._fname
        r, s = ("child", "parent") if rtnchild else ("parent", "child")
        query = "SELECT %(r)s FROM %(fname)s WHERE %(s)s = %(sctid)s AND depth=1" % vars()
        if not changeset:
            query += " AND locked = 0"
        query += " ORDER BY %s" % r
        if maxtoreturn > 0:
            query += " LIMIT %d" % (maxtoreturn+1)
        if start:
            query += " OFFSET %d" % start
        db.execute(query)
        rval = set([e if len(e) > 1 else e[0] for e in db])
        return rval


    def hasChildren(self, sctid, **kwargs):
        return bool(self.children(sctid, **self.singleResultArgs(**kwargs)))


    def children(self, sctid, **kwargs):
        return self.doquery(True, sctid, **kwargs)


    def hasParents(self, sctid, **kwargs):
        return bool(self.parents(sctid, **self.singleResultArgs(**kwargs)))


    def parents(self, sctid, **kwargs):
        return self.doquery(False, sctid, **kwargs)





            
        


