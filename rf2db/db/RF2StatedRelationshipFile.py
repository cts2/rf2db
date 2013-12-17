
from rf2db.parsers.RF2BaseParser import RF2Relationship
from rf2db.db.RF2FileCommon import RF2FileWrapper

    
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
      KEY source (sourceId) USING HASH,
      KEY target (destinationId) USING HASH,
      KEY predicate (typeId),
      %(primkey)s );"""
    
    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @staticmethod    
    def relId(r):
        """ Creates the identity of a relationship record """
        return r.moduleId, r.sourceId, r.destinationId, r.relationshipGroup, r.typeId, r.modifierId

    def existsSourceRecs(self, sourceId, active=True, inferred=True, ss=True):
        db = self.connect()
        return bool([r for r in db.query(self._tname(ss), 'sourceId = %s' % sourceId, active=active, ss=ss, maxtoreturn=1)])
     
    def existsTargetRecs(self, targetId, active=True, inferred=True, ss=True):
        db = self.connect()
        return bool([r for r in db.query(self._tname(ss), 'destinationId = %s' % targetId, active=active, ss=ss, maxtoreturn=1)])
    
    def existsPredicateRecs(self, predicateId, active=True, inferred=True, ss=True):
        db = self.connect()
        return bool([r for r in db.query(self._tname(ss), 'typeId = %s' % predicateId, active=active, ss=ss, maxtoreturn=1)])
    
    def _getRecs(self, filtr, active, inferred, ss=True):
        """ Return all relationship records matching the given filter. Inferred is ignored in the stated relationship file
        """
        db = self.connect()
        return map(lambda r:RF2Relationship(r), db.query(self._tname(ss), filtr, active=active, ss=ss, sort="relationshipGroup, id"))
        
        
    def getSourceRecs(self, sourceId, active=True, inferred=True, ss=True):
        """ Return all relationship records with the given sourceId. """
        return self._getRecs("sourceId = '%s'" % sourceId, active, inferred, ss)
    
    def getPredicateRecs(self, predicateId, active=True, inferred=True, ss=True):
        return self._getRecs("typeId = '%s'" % predicateId, active, inferred, ss)


    def getTargetRecs(self, targetId, active=True, inferred=True, ss=True):
        """ Return all Relationship records associated with the given targetId """
        return self._getRecs("destinationId = '%s'" %targetId, active, inferred, ss)
    
    def getSourcesForTarget(self, targetId, active=True, inferred=True, ss=True):
        """ Return a list of sourceId's connected with the given targetId.  Inferred is ignored"""
        db = self.connect()
        return map(lambda r:RF2Relationship(r).sourceId,  db.query(self._tname(ss), "destinationId = '%s' " % targetId, active=active, ss=ss))

    def getRelationship(self, relId, active=False, ss=True):
        """ Return the relationship record identified by relId"""
        db = self.connect()
        rlist = [RF2Relationship(r) for r in db.query(self._tname(ss), "id = '%s'" % relId, active=active, ss=ss)]
        return rlist[0] if len(rlist) else None

    def getRelationships(self, active=True, ss=True):
        pass


