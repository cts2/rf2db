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
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB

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
      KEY source (sourceId) USING HASH,
      KEY target (destinationId) USING HASH,
      KEY predicate (typeId),
      %(primkey)s );"""

    def __init__(self, *args, **kwargs):
        self._srdb = StatedRelationshipDB()
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @staticmethod
    def relId(r):
        """ Creates the identity of a relationship record """
        return r.moduleId, r.sourceId, r.destinationId, r.relationshipGroup, r.typeId, r.modifierId

    def existsSourceRecs(self, sourceId, active=True, inferred=True, ss=True, **_):
        db = self.connect()
        return bool(
            [r for r in db.query(self._tname(ss), 'sourceId = %s' % sourceId, active=active, ss=ss, maxtoreturn=1)])

    def existsTargetRecs(self, targetId, active=True, inferred=True, ss=True, **_):
        db = self.connect()
        return bool([r for r in
                     db.query(self._tname(ss), 'destinationId = %s' % targetId, active=active, ss=ss, maxtoreturn=1)])

    def existsPredicateRecs(self, predicateId, active=True, inferred=True, ss=True, **_):
        db = self.connect()
        return bool(
            [r for r in db.query(self._tname(ss), 'typeId = %s' % predicateId, active=active, ss=ss, maxtoreturn=1)])

    def _getRecs(self, filtr, active, inferred, ss=True):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        """
        returnRels = self._srdb._getRecs(filtr, active, inferred, ss)
        if inferred:
            statedRecs = [self.relId(r) for r in returnRels]
            db = self.connect()
            for e in db.query(self._tname(ss), filtr, active=active, ss=ss, sort="relationshipGroup, id"):
                r = RF2Relationship(e)
                if self.relId(r) not in statedRecs:
                    returnRels.append(r)
        return returnRels


    def getSourceRecs(self, sourceId, active=True, inferred=True, ss=True, **_):
        """ Return all relationship records with the given sourceId. """
        if not inferred:
            return self._srdb.getSourceRecs(sourceId, active, inferred, ss)
        return self._getRecs("sourceId = '%s'" % sourceId, active, inferred, ss)

    def getPredicateRecs(self, predicateId, active=True, inferred=True, ss=True, **_):
        if not inferred:
            return self._srdb.getPredicateRecs(predicateId, active, inferred, ss)
        return self._getRecs("typeId = '%s'" % predicateId, active, inferred, ss)


    def getTargetRecs(self, targetId, active=True, inferred=True, ss=True, **_):
        """ Return all Relationship records associated with the given targetId """
        if not inferred:
            return self._srdb.getTargetRecs(targetId, active, inferred, ss)
        return self._getRecs("destinationId = '%s'" % targetId, active, inferred, ss)

    def getSourcesForTarget(self, targetId, active=True, inferred=True, ss=True, **_):
        """ Return a list of sourceId's connected with the given targetId."""
        if not inferred:
            return self._srdb.getSourcesForTarget(targetId, active, inferred, ss)
        db = self.connect()
        return map(lambda r: RF2Relationship(r).sourceId,
                db.query(self._tname(ss), "destinationId = '%s' " % targetId, active=active, ss=ss))

    def getRelationship(self, relId, active=False, ss=True, **_):
        """ Return the relationship record identified by relId"""
        rel = self._srdb.getRelationship(relId, active, ss)
        if rel:
            return rel
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._tname(ss), "id = '%s'" % relId, active=active, ss=ss)]
        return rlist[0] if len(rlist) else None



