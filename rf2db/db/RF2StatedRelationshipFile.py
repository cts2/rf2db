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

def canon_filtr(filtr, canonical):
    return (filtr + ' AND isCanonical=1 ') if canonical else filtr

def rel_id(r):
    """ Creates the identity of a relationship record """
    return r.moduleId, r.sourceId, r.destinationId, r.relationshipGroup, r.typeId, r.modifierId

    
class StatedRelationshipDB(RF2FileWrapper):
    
    directory   = 'Terminology'
    prefixes    = ['sct2_StatedRelationship_']
    table       = 'statedRelationship'
    
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
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def _existsRecs(self, filtr, active, canonical, ss):
        db = self.connect()
        return bool([r for r in db.query(self._tname(ss), canon_filtr(filtr, canonical),
                                         active=active, ss=ss, maxtoreturn=1)])

    def loadTable(self, rf2file, ss, cfg):
        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(StatedRelationshipDB,self).loadTable(rf2file, ss, cfg)

    def updateFromCanonical(self, canon_fname, ss):
        db = self.connect()
        db.execute("""UPDATE %s s, %s c SET isCanonical=1
            WHERE conceptid1 = sourceId AND conceptid2 = destinationId AND relationshiptype = typeId
            AND s.relationshipgroup=c.relationshipgroup""" % (self._tname(ss), canon_fname))
        db.commit()


    def existsSourceRecs(self, sourceId, active=True, canonical=False, ss=True):
        return self._existsRecs('sourceId = %s ' % sourceId, active, canonical, ss)
     
    def existsTargetRecs(self, targetId, active=True, canonical=False, ss=True):
        return self._existsRecs('destinationId = %s ' % targetId, active, canonical, ss)
    
    def existsPredicateRecs(self, predicateId, active=True, canonical=False, ss=True):
        return self._existsRecs('typeId = %s ' % predicateId, active, canonical, ss)


    def _getRecs(self, filtr, active, canonical, ss):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        """
        db = self.connect()
        return map(lambda r:RF2Relationship(r), db.query(self._tname(ss), canon_filtr(filtr, canonical), 
                                                         active=active, ss=ss, sort="relationshipGroup, id"))
        
        
    def getSourceRecs(self, sourceId, active=True, canonical=False, ss=True):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs("sourceId = '%s'" % sourceId, active, canonical, ss)
    
    def getPredicateRecs(self, predicateId, active=True, canonical=False, ss=True):
        return self._getRecs("typeId = '%s'" % predicateId, active, canonical, ss)


    def getTargetRecs(self, targetId, active=True, canonical=False, ss=True):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs("destinationId = '%s'" %targetId, active, canonical, ss)
    
    def getSourcesForTarget(self, targetId, active=True, canonical=False, ss=True):
        """ Return a list of sourceId's connected with the given targetId.  Inferred is ignored"""
        db = self.connect()
        return set(map(lambda r:RF2Relationship(r).sourceId,  db.query(self._tname(ss),
                                                                   canon_filtr("destinationId = '%s' " % targetId, canonical), 
                                                                   active=active, ss=ss)))

    def getRelationship(self, relId, ss=True):
        """ Return the relationship record identified by relId"""
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._tname(ss), "id = '%s'" % relId, active=False, ss=ss)]
        return rlist[0] if len(rlist) else None




