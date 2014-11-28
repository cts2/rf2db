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

""" Processor to create a table of moduleid to known versions table
"""

from rf2db.db.RF2FileCommon import RF2FileWrapper
from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.db.RF2RelationshipFile import RelationshipDB
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB
from rf2db.db.RF2LanguageFile import LanguageDB
from rf2db.constants.RF2ValueSets import acceptable, synonym, preferred
from rf2db.utils.listutils import listify
from rf2db.utils.lfu_cache import lfu_cache


class ModuleVersionsDB(RF2FileWrapper):
    
    table = 'moduleversions'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      moduleId      bigint(20) NOT NULL,
      effectiveTime int(11) NOT NULL,
       PRIMARY KEY (moduleId,effectiveTime),
       KEY id (moduleId)
    ); """

    createModulesSTMT = """CREATE OR REPLACE VIEW moduleids AS
        SELECT DISTINCT m.moduleid, d.term, d.languagecode FROM %(mvtable)s m, %(desctable)s d, %(langtable)s l
        WHERE d.conceptid = m.moduleid AND l.referencedcomponentid=d.id AND
              l.acceptabilityid in (%(acceptable)s, %(preferred)s) AND d.typeid=%(synonym)s;"""
    
    # A list of tables that carry significant version identifiers.  Used to determine possible module changes
    _versionTables = [ConceptDB(),
                      DescriptionDB(),
                      RelationshipDB(),
                      StatedRelationshipDB()]
    
    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    @staticmethod
    def _d(**kwargs):
        return vars()['kwargs']
               
    def loadTable(self, rf2file):
        for vt in self._versionTables:
            if not vt.hascontent():
                print(vt._tname(), "is empty - load it first")
        for vt in self._versionTables:
            # print("Loading", vt.table, '...',end='')
            print('Reading versions from %s ...' % vt.table)
            db = self.connect()
            db.execute('INSERT IGNORE INTO %s (moduleId, effectiveTime) VALUES' % self._fname + \
                            ','.join(["("+ str(m) + "," +str(e) + ")" for (m,e) in vt.moduleVersions()]))
            db.commit()
        db = self.connect()
        print "Loading moduleid view"
        db.execute(self.createModulesSTMT % self._d(mvtable=self._fname, desctable=DescriptionDB.fname(),
                                                    langtable=LanguageDB.fname(), acceptable=acceptable,
                                                    preferred=preferred, synonym=synonym))
        db.commit()

            
    def loadFile(self, fname):
        print(self.table, "must be loaded from", ConceptDB.fname(), "and", DescriptionDB.fname(), "tables")
        
    def getVersions(self, moduleId):
        """ Return module id versions in descending order """
        db = self.connect()
        db.execute("SELECT effectiveTime FROM %s WHERE moduleId = %s ORDER by effectiveTime DESC" % (self._fname, moduleId) )
        return list(db.ResultsGenerator(db))


    def knownVersions(self, refdate=None):
        """
        @param refdate: reference date (format: YYYYMMDD) - return entries <= date
        @return: ordered list of dates in descending order
        """
        whereStmt = " WHERE effectiveTime <= '%s' " % refdate if refdate else ""
        db = self.connect()
        db.execute("SELECT distinct effectiveTime FROM %s %s ORDER by effectiveTime DESC" % (self._fname, whereStmt))
        return list(db.ResultsGenerator(db))

    def getModulesids(self):
        db = self.connect()
        db.execute("SELECT * FROM moduleids")
        return list(db.ResultsGenerator(db))

    @lfu_cache(20)
    def getModuleid(self, moduleid):
        db = self.connect()
        db.execute("SELECT * FROM moduleids WHERE moduleid=%s" % moduleid)
        rval = list(db.ResultsGenerator(db))
        return rval[0] if rval else None

    @lfu_cache(20)
    def validModuleids(self, moduleids):
        moduleids = list(set(listify(moduleids)))
        if moduleids:
            db = self.connect()
            db.execute("SELECT distinct(moduleid) FROM moduleids WHERE moduleid IN (" + ', '.join(moduleids) + ");")
            rval = list(db.ResultsGenerator(db))
            return len(rval) == len(moduleids)

        return True

        
