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

""" RF2 Relationships file access
"""

from rf2db.parsers.RF2BaseParser import RF2Relationship
from rf2db.parsers.RF2Iterator import iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB, rel_id
from rf2db.db.RF1CanonicalCore import CanonicalCoreDB
from rf2db.parsers.RF2Iterator import RF2RelationshipList
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.sctid_generator import *
from rf2db.constants.RF2ValueSets import additionalRelationship, some, inferredRelationship

# Parameters for relationship file query
rel_parms = ParameterDefinitionList(global_rf2_parms)

# Stated relationships are included in queries
rel_parms.stated = booleanparam(default=True)

# Inferred relationships are included in queries
rel_parms.inferred = booleanparam(default=True)

# additional relationships are included in queries
rel_parms.additional = booleanparam(default=True)

# C{True} means canonical relationships only, C{False} means any
rel_parms.canonical = booleanparam(default=False)

""" Parameters for relationship list query """
rellist_parms = ParameterDefinitionList(rel_parms)
rellist_parms.add(iter_parms)


def build_filtr(filtr, parmlist):
    assert parmlist.inferred or parmlist.addl, "Shouldn't be building a filter if you are returning nothing"
    if parmlist.canonical: filtr += ' AND isCanonical=1 '
    if parmlist.inferred and parmlist.additional:
        return filtr
    return (
    filtr + ' AND characteristicTypeId=%s' % (additionalRelationship if parmlist.additional else inferredRelationship))


class RelationshipDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Relationship_']
    table = 'relationship'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id bigint(20) NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      sourceId bigint(20) NOT NULL,
      destinationId bigint(20) NOT NULL,
      relationshipGroup int(11) NOT NULL,
      typeId bigint(20) NOT NULL,
      characteristicTypeId bigint(20) NOT NULL,
      modifierId bigint(20) NOT NULL,
      isCanonical tinyint(1) NOT NULL DEFAULT 0,
      KEY source (sourceId) USING HASH,
      KEY target (destinationId) USING HASH,
      KEY predicate (typeId),
      %(primkey)s );"""

    def __init__(self, *args, **kwargs):
        self._srdb = StatedRelationshipDB()
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @lfu_cache(maxsize=100)
    def _existsRecs(self, filtr, parmlist):
        if parmlist.stated and self._srdb._existsRecs(filtr, parmlist):
            return True
        db = self.connect()
        return bool([r for r in db.query(self._tname(parmlist.ss), build_filtr(filtr, parmlist),
                                         active=parmlist.active, ss=parmlist.ss)])

    def loadTable(self, rf2file, ss, cfg):
        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(RelationshipDB,self).loadTable(rf2file, ss, cfg)
        # Temporary fix.  There is an error in the 20140131 distro where a significant number of the
        # relations have two entries on the same date, one for active and one for inactive.  We have
        # remove all of the inactive duplicates.
        # Also note that we may be able skip Step 1: below -- it may be that canonical doesn't actually
        # reactivate anything except the errors
        print "Removing relationship duplicates...",
        q = """ DELETE r1.* FROM %(tname)s r1, %(tname)s r2
            WHERE r1.effectiveTime=r2.effectiveTime AND r1.moduleid=r2.moduleid AND
                  r1.sourceId=r2.sourceId AND r1.destinationId=r2.destinationId AND
                  r1.relationshipGroup=r2.relationshipgroup AND r1.typeId=r2.typeId AND
                  r1.characteristicTypeId=r2.characteristicTypeId AND r1.modifierId = r2.modifierId AND
                  r1.active=0 AND r2.active=1""" % {'tname':self._tname(ss)}
        db = self.connect()
        db.execute(q)
        db.commit()
        print "done"


    class _BlockWriter(object):
        addrow = "(%(id)s, %(effectiveTime)s, %(active)s, %(moduleId)s, %(sourceId)s, \
                             %(destinationId)s, %(relationshipGroup)s, %(typeId)s, %(characteristicTypeId)s, \
                             %(modifierId)s, %(isCanonical)s)"
        blocksize = 1000
        insert_stmt = "INSERT INTO %s VALUES "

        def __init__(self, tname, release):
            self.idGenerator = sctid_generator(MAYO_Namespace, sctid_generator.RELATIONSHIP, 0)
            self.moduleId = self.idGenerator.next()
            self.effectiveTime = release
            self._stmt = self.insert_stmt % tname
            self.active = 1
            self.characteristicTypeId = additionalRelationship
            self.modifierId = some
            self.isCanonical = 1
            self.rowstoadd = []
            self.rdb = RelationshipDB()

        def addrec(self, (sourceId, typeId, destinationId, relationshipGroup)):
            id = self.idGenerator.next()
            self.rowstoadd += [self.addrow % dict(self.__dict__, **vars())]
            if len(self.rowstoadd) >= self.blocksize:
                self.flush()

        def flush(self):
            if len(self.rowstoadd):
                db = self.rdb.connect()
                db.execute(self._stmt + ','.join(self.rowstoadd))
                db.commit()
            self.rowstoadd = []

    def updateFromCanonical(self, canon_fname, ss, cfg):
        ccdb = CanonicalCoreDB()
        if not ccdb.hascontent(ss):
            print("Canonical DB is empty -- relationship tables not updated")
            return

        db = self.connect()

        # Step 1: Add the canonical tag to everything that exists.  Note that the canonical table can re-activate an
        #         inactive entry, so we need to select it out...
        db.execute("""UPDATE %s s, %s c SET isCanonical=1
            WHERE conceptid1 = sourceId AND conceptid2 = destinationId AND relationshiptype = typeId
            AND s.relationshipgroup=c.relationshipgroup AND active=1""" % (
            self._tname(ss), ccdb._tname(ss)))
        db.commit()

        # Step 2: Add additional relationship entries for new assertions in the canonical table
        bw = self._BlockWriter(self._tname(ss), cfg.release)
        query = """SELECT conceptid1, relationshiptype, conceptid2, c.relationshipgroup FROM %s c
             LEFT JOIN %s r ON (conceptid1=sourceid AND conceptid2=destinationid AND
             relationshiptype=typeid AND c.relationshipgroup=r.relationshipgroup) WHERE sourceid IS NULL OR active=0""" % (
            canon_fname, self._tname(ss))
        for e in db.executeAndReturn(query):
            bw.addrec(e)
        bw.flush()

    def existsSourceRecs(self, sourceId, parmlist):
        return self._existsRecs('sourceId = %s ' % sourceId, parmlist)

    def existsPredicateRecs(self, predicateId, parmlist):
        return self._existsRecs('typeId = %s ' % predicateId, parmlist)

    def existsTargetRecs(self, targetId, parmlist):
        return self._existsRecs('destinationId = %s ' % targetId, parmlist)


    @lfu_cache(maxsize=100)
    def _getRecs(self, filtr, parmlist, key):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        Note that we have 4 controlling parameters:
            - stated -- if true, we return stated relationships
            - inferred -- if true we return inferred relationships
            - additional -- if true we return additional relationships (are in the relationships_ss file)
            - canonical -- if true we return I{only} canonical relationships meeting the above criteria

        """
        if not parmlist.maxtoreturn:    # we're getting counts
            infcount = int(list(self.connect().query_p(self._tname(parmlist.ss),
                                           parmlist,
                                           filter=build_filtr(filtr, parmlist)))[0]) \
                if parmlist.inferred else 0
            statedcount = self._srdb._getRecs(filtr, parmlist) if parmlist.stated else 0
            # TODO: the count is not accurate unless we subtract out both inferred and stated...
            return [infcount + statedcount]


        rval = {k:v for k,v in map(lambda r:(rel_id(r), r),
                                   map(lambda r: RF2Relationship(r),
                                       self.connect().query_p(self._tname(parmlist.ss),
                                                              parmlist,
                                                              filter=build_filtr(filtr, parmlist))))} \
            if parmlist.inferred else {}
        if parmlist.stated:
            for r in self._srdb._getRecs(filtr, parmlist):
                rval[rel_id(r)] = r

        return sorted(rval.values(), key=key)


    def getSourceRecs(self, sourceId, parmlist):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs('sourceId = %s ' % sourceId, parmlist, lambda r: (r.relationshipGroup, r.destinationId))


    def getPredicateRecs(self, predicateId, parmlist):
        return self._getRecs('typeId = %s ' % predicateId, parmlist,
                             lambda r: (r.sourceId, r.relationshipGroup, r.destinationId))


    def getTargetRecs(self, targetId, parmlist):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs('destinationId = %s ' % targetId, parmlist, lambda r: (r.relationshipGroup, r.sourceId))


    def getSourcesForTarget(self, targetId, parmlist):
        """ Return a list of sourceId's connected with the given targetId."""

        sources = self._srdb.getSourcesForTarget(targetId, parmlist) if parmlist.stated else set()
        if parmlist.inferred:
            db = self.connect()
            return sources.union(map(lambda r: RF2Relationship(r).sourceId,
                db.query(self._tname(parmlist.ss),
                         build_filtr("destinationId = '%s' " % targetId, parmlist),
                         active=parmlist.active, ss=parmlist.ss)))

    @lfu_cache(maxsize=100)
    def getRelationship(self, relId, parmlist):
        """ Return the relationship record identified by relId"""
        rel = self._srdb.getRelationship(relId, parmlist)
        if rel:
            return rel
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._tname(parmlist.ss),
                                                      "id = '%s'" % relId,
                                                      active=parmlist.active,
                                                      maxtoreturn=1,
                                                      ss=parmlist.ss)]
        return rlist[0] if len(rlist) else None

    def asRelationshipList(self, rels, parmlist):
        """ Format rels as a Relationship List """
        thelist = RF2RelationshipList(parmlist)
        if not parmlist.maxtoreturn:
            return thelist.finish(True, total=list(rels)[0])
        for d in rels:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(d)
        return thelist.finish(False)



