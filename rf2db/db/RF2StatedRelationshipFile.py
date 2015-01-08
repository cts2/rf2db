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

from rf2db.parsers.RF2BaseParser import RF2Relationship
from rf2db.db.RF2FileCommon import RF2FileWrapper

def canon_filtr(filtr, canonical=False, **_):
    return (filtr + ' AND isCanonical=1 ') if canonical else filtr

def rel_id(r):
    """ Creates the identity of a relationship record.  Note that a given record cannot be
        simultaneously canonical and not, so this isn't included in the identity
    """
    return r.moduleId, r.sourceId, r.destinationId, r.relationshipGroup, r.typeId, r.modifierId

    
class StatedRelationshipDB(RF2FileWrapper):
    
    directory = 'Terminology'
    prefixes = ['sct2_StatedRelationship_']
    table = 'statedRelationship'
    
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
        RF2FileWrapper.__init__(self, *args, **kwargs)

    hasrf2rec = True
    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2Relationship(*args, **kwargs)

    def recsexist(self, filtr, **kwargs):
        db = self.connect()
        kwargs['maxtoreturn'] = 1
        return bool([r for r in db.query(self._fname,
                                         filter_=canon_filtr(filtr, **kwargs),
                                         **kwargs)])


    def loadTable(self, rf2file):
        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(StatedRelationshipDB,self).loadTable(rf2file)

    def updateFromCanonical(self, canon_fname, **_):
        db = self.connect()
        db.execute("""UPDATE %s s, %s c SET isCanonical=1
            WHERE conceptid1 = sourceId AND conceptid2 = destinationId AND relationshiptype = typeId
            AND s.relationshipgroup=c.relationshipgroup""" % (self._fname, canon_fname))
        db.commit()

    def existsSourceRecs(self, sourceId, **kwargs):
        return self.recsexist('sourceId = %s ' % sourceId, **kwargs)
     
    def existsTargetRecs(self, targetId, **kwargs):
        return self.recsexist('destinationId = %s ' % targetId, **kwargs)
    
    def existsPredicateRecs(self, predicateId, **kwargs):
        return self.recsexist('typeId = %s ' % predicateId, **kwargs)

    def _getRecs(self, filtr, maxtoreturn=None, **kwargs):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        """
        db = self.connect()
        if maxtoreturn == 0:    # we're getting counts
            return int(list(self.connect().query(self._fname,
                                                 filter_=canon_filtr(filtr, **kwargs),
                                                 maxtoreturn=maxtoreturn,
                                                 **kwargs))[0])
        return map(lambda r:RF2Relationship(r), db.query(self._fname,
                                                         filter_=canon_filtr(filtr, **kwargs),
                                                         maxtoreturn=maxtoreturn,
                                                         **kwargs))

    def getSourceRecs(self, sourceId, **kwargs):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs("sourceId = '%s'" % sourceId, **kwargs)
    
    def getPredicateRecs(self, predicateId, **kwargs):
        return self._getRecs("typeId = '%s'" % predicateId, **kwargs)

    def getTargetRecs(self, targetId, **kwargs):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs("destinationId = '%s'" %targetId, **kwargs)
    
    def getSourcesForTarget(self, targetId, **kwargs):
        """ Return a list of sourceId's connected with the given targetId.  Inferred is ignored"""
        db = self.connect()
        return set(map(lambda r: RF2Relationship(r).sourceId, db.query_p(self._fname,
                                                                         filter_=canon_filtr("destinationId = '%s' " % targetId, **kwargs),
                                                                         **kwargs)))
    @classmethod
    def subjs(cls, db, changeset):
        """ Return all the unique subjects
        @param db:
        @param changeset:
        @return: list of subjects
        """
        fname = cls.fname()
        db.execute("SELECT DISTINCT sourceId FROM %(fname)s WHERE changeset = '%(changeset)s'" % vars())
        return db.ResultsGenerator(db)



    def getRelationship(self, rel=None, **kwargs):
        """ Return the relationship record identified by relId"""
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._fname, filter_="id = '%s'" % rel, maxtoreturn=1, **kwargs)]
        return rlist[0] if len(rlist) else None


    @classmethod
    def _rollback(cls, db, changeset, **args):
        for subj in cls.subjs(db, changeset):
            RF2Relationship._tcdb().remove(db, subj)
        return super(StatedRelationshipDB, cls)._rollback(db, changeset, **args)

