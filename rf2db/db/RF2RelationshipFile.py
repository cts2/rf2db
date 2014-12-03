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
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms, rf2_values
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB, rel_id
from rf2db.db.RF1CanonicalCore import CanonicalCoreDB
from rf2db.parsers.RF2Iterator import RF2RelationshipList
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam, sctidparam
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.sctid_generator import *
from rf2db.constants.RF2ValueSets import additionalRelationship, some, inferredRelationship

# Parameters for relationship file query
rel_parms = ParameterDefinitionList(global_rf2_parms)
rel_parms.rel = sctidparam()

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

# Relationships for source concept
rel_source_parms=ParameterDefinitionList(rellist_parms)
rel_source_parms.source=sctidparam()

# Relationships for predicate concept
rel_predicate_parms=ParameterDefinitionList(rellist_parms)
rel_predicate_parms.predicate=sctidparam()

# Relationships for predicate concept
rel_target_parms=ParameterDefinitionList(rellist_parms)
rel_target_parms.target=sctidparam()


def build_filtr(filtr, inferred=False, addl=False, canonical=False, additional=False, **kwargs):
    assert inferred or addl, "Shouldn't be building a filter if you are returning nothing"
    if canonical:
        filtr += ' AND isCanonical=1 '
    if inferred and additional:
        return filtr
    return (
    filtr + ' AND characteristicTypeId=%s' % (additionalRelationship if additional else inferredRelationship))


class RelationshipDB(RF2FileWrapper):
    directory = 'Terminology'
    prefixes = ['sct2_Relationship_']
    table = 'relationship'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
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
      %(keys)s );"""

    def __init__(self, *args, **kwargs):
        self._srdb = StatedRelationshipDB()
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @lfu_cache(maxsize=100)
    def recsexist(self, filtr, stated=False, **kwargs):
        if stated and self._srdb.recsexist(filtr, **kwargs):
            return True
        db = self.connect()
        return bool([r for r in db.query(self._fname, build_filtr(filtr, **kwargs))])

    def loadTable(self, rf2file):
        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(RelationshipDB,self).loadTable(rf2file)
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
                  r1.active=0 AND r2.active=1""" % {'tname':self._fname}
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

    def updateFromCanonical(self, canon_fname):
        ccdb = CanonicalCoreDB()
        if not ccdb.hascontent():
            print("Canonical DB is empty -- relationship tables not updated")
            return

        db = self.connect()

        # Step 1: Add the canonical tag to everything that exists.  Note that the canonical table can re-activate an
        #         inactive entry, so we need to select it out...
        db.execute("""UPDATE %s s, %s c SET isCanonical=1
            WHERE conceptid1 = sourceId AND conceptid2 = destinationId AND relationshiptype = typeId
            AND s.relationshipgroup=c.relationshipgroup AND active=1""" % (
            self._fname, ccdb._fname))
        db.commit()

        # Step 2: Add additional relationship entries for new assertions in the canonical table
        bw = self._BlockWriter(self._fname, rf2_values.release)
        query = """SELECT conceptid1, relationshiptype, conceptid2, c.relationshipgroup FROM %s c
             LEFT JOIN %s r ON (conceptid1=sourceid AND conceptid2=destinationid AND
             relationshiptype=typeid AND c.relationshipgroup=r.relationshipgroup) WHERE sourceid IS NULL OR active=0""" % (
            canon_fname, self._fname)
        for e in db.executeAndReturn(query):
            bw.addrec(e)
        bw.flush()

    def existsSourceRecs(self, sourceId, **kwargs):
        return self.recsexist('sourceId = %s ' % sourceId, **kwargs)

    def existsPredicateRecs(self, predicateId, **kwargs):
        return self.recsexist('typeId = %s ' % predicateId, **kwargs)

    def existsTargetRecs(self, targetId, **kwargs):
        return self.recsexist('destinationId = %s ' % targetId, **kwargs)


    @lfu_cache(maxsize=100)
    def _getRecs(self, filtr, key, maxtoreturn=None, inferred=True, stated=True, **kwargs):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        Note that we have 4 controlling parameters:
            - stated -- if true, we return stated relationships
            - inferred -- if true we return inferred relationships
            - additional -- if true we return additional relationships (are in the relationships_ss file)
            - canonical -- if true we return I{only} canonical relationships meeting the above criteria

        """
        if maxtoreturn == 0:    # we're getting counts
            infcount = int(list(self.connect().query(self._fname,
                                                     filter_=build_filtr(filtr,
                                                                         inferred=inferred,
                                                                         stated=stated,
                                                                         **kwargs),
                                                     inferred=inferred,
                                                     stated=stated,
                                                     maxtoreturn=maxtoreturn,
                                                     **kwargs))[0]) \
                if inferred else 0
            statedcount = self._srdb._getRecs(filtr,
                                              maxtoreturn=maxtoreturn,
                                              stated=stated,
                                              inferred=inferred,
                                              **kwargs) if stated else 0
            # TODO: the count is not accurate unless we subtract out both inferred and stated...
            return [infcount + statedcount]


        rval = {k:v for k,v in map(lambda r:(rel_id(r), r),
                                   map(lambda r: RF2Relationship(r),
                                       self.connect().query(self._fname,
                                                              filter_=build_filtr(filtr,
                                                                                  inferred=inferred,
                                                                                  stated=stated,
                                                                                  **kwargs),
                                                              maxtoreturn=maxtoreturn,
                                                              stated=stated,
                                                              inferred=inferred,
                                                              **kwargs)))} \
            if inferred else {}
        if stated:
            for r in self._srdb._getRecs(filtr, **kwargs):
                rval[rel_id(r)] = r

        return sorted(rval.values(), key=key)


    def getSourceRecs(self, sourceId, **kwargs):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs('sourceId = %s ' % sourceId, lambda r: (r.relationshipGroup, r.destinationId), **kwargs)


    def getPredicateRecs(self, predicateId, **kwargs):
        return self._getRecs('typeId = %s ' % predicateId,
                             lambda r: (r.sourceId, r.relationshipGroup, r.destinationId),
                             **kwargs)


    def getTargetRecs(self, targetId, **kwargs):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs('destinationId = %s ' % targetId, lambda r: (r.relationshipGroup, r.sourceId), **kwargs)


    def getSourcesForTarget(self, targetId, stated=True, inferred=True, **kwargs):
        """ Return a list of sourceId's connected with the given targetId."""

        sources = self._srdb.getSourcesForTarget(targetId, stated=stated, inferred=inferred, **kwargs) if stated else set()
        if inferred:
            db = self.connect()
            return sources.union(map(lambda r: RF2Relationship(r).sourceId,
                db.query(self._fname,
                         build_filtr("destinationId = '%s' " % targetId, **kwargs),
                         **kwargs)))

    @lfu_cache(maxsize=100)
    def getRelationship(self, rel=None, **kwargs):
        """ Return the relationship identified by the identifier
        @param rel: inferred or stated relationship identifier
        @param kwargs: context
        @return: stated or inferred record
        """
        rrec = self._srdb.getRelationship(**kwargs)
        if rrec:
            return rrec
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._fname,
                                                      filter_="id = '%s'" % rel,
                                                      maxtoreturn=1,
                                                      **kwargs)]
        return rlist[0] if len(rlist) else None

    @classmethod
    def refsettype(cls, parms):
        return RF2RelationshipList(parms)


