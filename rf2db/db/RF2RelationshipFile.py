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
from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB, canon_filtr, rel_id
from rf2db.parsers.RF2Iterator import RF2RelationshipList
from rf2db.db.ParameterSets import iter_parms

class rel_parms(iter_parms):
    def __init__(self, **kwargs):
        iter_parms.__init__(self, **kwargs)
        self.stated = self._p.bool('stated', True)
        self.inferred = self._p.bool('inferred', True)
        self.canonical = self._p.bool('canonical', False)

    def __getattr__(self, item):
        return self._p.__getattr__(item)

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

    def _existsRecs(self, filtr, p):
        if p.stated and self._srcb._existsRecs(filtr, p.active, p.canonical, p.ss):
            return True
        db = self.connect()
        return bool([r for r in db.query(self._tname(p.ss), canon_filtr(filtr, p.canonical),
                                 active=p.active, ss=p.ss, maxtoreturn=1)])

    def loadTable(self, rf2file, ss, cfg):
        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(RelationshipDB,self).loadTable(rf2file, ss, cfg)

    def updateFromCanonical(self, canon_fname, ss):
        db = self.connect()
        db.execute("""UPDATE %s s, %s c SET isCanonical=1
            WHERE conceptid1 = sourceId AND conceptid2 = destinationId AND relationshiptype = typeId
            AND s.relationshipgroup=c.relationshipgroup""" % (self._tname(ss), canon_fname))
        db.commit()

    def existsSourceRecs(self, sourceId, **kwargs):
        return self._existsRecs('sourceId = %s ' % sourceId, rel_parms(**kwargs))

    def existsPredicateRecs(self, predicateId, **kwargs):
        return self._existsRecs('typeId = %s ' % predicateId, rel_parms(**kwargs))

    def existsTargetRecs(self, targetId, **kwargs):
        return self._existsRecs('destinationId = %s ' % targetId, rel_parms(**kwargs))



    def _getRecs(self, filtr, p, key):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        """
        rval = {k:v for k,v in map(lambda r:(rel_id(r), r),
                                   map(lambda r: RF2Relationship(r),
                                       self.connect().query(self._tname(p.ss),
                                                            canon_filtr(filtr, p.canonical),
                                                            active=p.active, ss=p.ss, start=p.start, maxtoreturn=p.maxtoreturn)))} if p.inferred else {}
        if p.stated:
            for r in self._srdb._getRecs(filtr, p.active, p.canonical, p.ss):
                rval[rel_id(r)] = r

        return sorted(rval.values(), key=key)


    def getSourceRecs(self, sourceId, **kwargs):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs('sourceId = %s ' % sourceId, rel_parms(**kwargs), lambda r: (r.relationshipGroup, r.destinationId))


    def getPredicateRecs(self, predicateId, **kwargs):
        return self._getRecs('typeId = %s ' % predicateId, rel_parms(**kwargs), lambda r: (r.sourceId, r.relationshipGroup, r.destinationId))


    def getTargetRecs(self, targetId, **kwargs):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs('destinationId = %s ' % targetId, rel_parms(**kwargs), lambda r: (r.relationshipGroup, r.sourceId))


    def getSourcesForTarget(self, targetId, **kwargs):
        """ Return a list of sourceId's connected with the given targetId."""
        p = rel_parms(**kwargs)

        sources = self._srdb.getSourcesForTarget(targetId, active=p.active, canonical=p.canonical, ss=p.ss) if p.stated else set()
        if p.inferred:
            db = self.connect()
            return sources.union(map(lambda r: RF2Relationship(r).sourceId,
                db.query(self._tname(p.ss), canon_filtr("destinationId = '%s' " % targetId, p.canonical), active=p.active, ss=p.ss)))

    def getRelationship(self, relId, **kwargs):
        """ Return the relationship record identified by relId"""
        p = rel_parms(**kwargs)
        rel = self._srdb.getRelationship(relId, ss=p.ss)
        if rel:
            return rel
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._tname(p.ss), "id = '%s'" % relId, active=False, ss=p.ss)]
        return rlist[0] if len(rlist) else None

    def asRelationshipList(self, rels, **kwargs):
        """ Format rels as a Relationship List """
        thelist = RF2RelationshipList(**kwargs)
        for d in rels:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(d)
        return thelist.finish(False)



