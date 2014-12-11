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

""" RF2 File Wrapper
"""
from __future__ import print_function

import os
import sys
from time import gmtime, strftime

from rf2db.db.RF2DBConnection import RF2DBConnection, cp_values, singleresultargs
from rf2db.parameterparser.ParmParser import booleanparam, sctidparam, strparam
from rf2db.utils.sctid_generator import sctid_generator
from rf2db.db.RF2Namespaces import DecodedNamespace
from rf2db.utils.lfu_cache import lfu_cache

from ConfigManager.ConfigArgs import ConfigArg, ConfigArgs
from ConfigManager.ConfigManager import ConfigManager

# config_parms are used for file loading
config_parms = ConfigArgs('rf2',
                           [ConfigArg('fileloc', abbrev='f', help='Location of primary RF2 Distribution'),
                            ConfigArg('addloc', abbrev='a', help='Add the location of a secondary RF2 Distribution'),
                            ConfigArg('release', abbrev='r', help='Current RF2 Revision (yyyymmdd)'),
                            ConfigArg('defaultblocksize', help="Default return block size", default='100')
                           ])
rf2_values = ConfigManager(config_parms)

# extension_parms are used for managing a read/write space
extension_parms = ConfigArgs('extension',
                              [ConfigArg('namespace', abbrev='n', help='Namespace for new identifiers'),
                               ConfigArg('moduleid', abbrev='m', help='ModuleId for new entries'),
                               ])
ep_values = ConfigManager(extension_parms)

# TODO: load script for SNOMED_STY file
#  Query: create table rf2.UMLS_STY as SELECT sty.cui CUI, tui TUI, sty STU, scui SCUI, sab SAB from MRSTY sty, MRCONSO con
#         WHERE con.cui = sty.cui
#         Index is (SCUI, SAB)
#         Second index is (TUI, SAB)

from rf2db.parameterparser.ParmParser import ParameterDefinitionList

#  Base line parameters used for the REST RF2 Services
#
# Global Parameters
#     - active - C{True} means inactive entries will not be visible.  C{False} means that both active
#     and inactive entries are treated as present.  Default: C{True}
#     - moduleid - a list of module id's.  If supplied access will be restricted to the specific modules.
#     - changeset - a changeset id.  If supplied and the changeset is open, values will be visible in service
global_rf2_parms = ParameterDefinitionList()
global_rf2_parms.active = booleanparam(default=True)
global_rf2_parms.changeset = strparam(required=False)

class moduleidparam(sctidparam):
    """ Module id parameter.  Validate sctid's that are also children of the module file
    """

    def __init__(self, **args):
        self._mvdb = None
        sctidparam.__init__(self, **args)

    def _isValid(self, val):
        if not val:
            return True
        if not self._mvdb:
            from RF2ModuleVersionsFile import ModuleVersionsDB
            self._mvdb = ModuleVersionsDB()

        return self._mvdb.validModuleids(val)

global_rf2_parms.moduleid = moduleidparam()


class RF2FileWrapper(object):
    """ Abstract wrapper class for RF2 files """
    # ================== Virtual parameters ===============
    directory = None    # 'Terminology' or 'Refset/Content', 'Refset/Language', etc
    prefixes = []       # 'sct2_Concept_', 'der2_cRefset_AttributeValue', 'der2_Refset_Simple', etc.
    table = None        # 'concept', 'description', 'simplemap', etc.
    createSTMT = None   # SQL create statement for table. 'table' is available as a parameter
    isRF1File = False   # True means this is an RF1 table w/ different behavior

    _file_base = '''id bigint(20) NOT NULL,
effectiveTime int(11) NOT NULL,
active tinyint(1) NOT NULL,
moduleId bigint(20) NOT NULL '''

    _file_extension = 'changeset char(36), locked tinyint(1) NOT NULL DEFAULT 0,'

    _keys_ss = 'KEY (changeset), PRIMARY KEY (id)'
    _keys_full = 'KEY (changeset), PRIMARY KEY (id, effectiveTime)'

    _loadSTMT = ("LOAD DATA  local INFILE '%(tsvfile)s'\n"
                 " INTO TABLE %(table)s  \n"
                 " FIELDS TERMINATED BY '\\t' \n"
                 " LINES TERMINATED BY '\\r\\n'  \n"
                 " IGNORE 1 LINES;"
    )

    _hasContentSTMT = "SELECT * FROM %s LIMIT 1;"

    _existsQuery = "SHOW TABLES LIKE '%s';"
    _csdb = None
    _concdb = None


    def __init__(self, load=False, noaction=False):
        """
        @param load:
        @param noaction:
        @return:
        """
        self._exists= False
        self._hascontents = False

    hasrf2rec = False

    def connect(self):
        """
        @return: Database connection.
        """
        return RF2DBConnection()

    def exists(self):
        """ Determine whether the table exists
        @param ss: Not used
        @return: True if the table is there false otherwise
        """
        if not self._exists:
            db = self.connect()
            self._exists = len(db.execute(self._existsQuery % self._fname).fetchall()) > 0
            db.close()
        return self._exists

    def create(self):
        """ Create the table
        """
        db = self.connect()
        db.execute(self.createSTMT % {'table': self._fname,
                                      'base': self._file_base,
                                      'keys': self._file_extension + (self._keys_ss if cp_values.ss else self._keys_full)})
        db.commit()
        self._exists = True

    def hascontent(self):
        """ Determine whether the table exists and has something in it
        @return: True if the table has something in it, false otherwise
        """
        if not self._hascontents:
            db = self.connect()
            self._hascontents = db.execute(self._hasContentSTMT % self._fname) if self.exists() else False
            db.close()
        return self._hascontents


    def numrecs(self):
        """ Return the number of records in the table
        @return: Number of records in the table
        """
        rval = 0
        if self.exists():
            db = self.connect()
            if db.execute("SELECT COUNT(*) FROM %s" % self._fname):
                rval = db.next()[0]
            db.close()
        return rval

    def loadTable(self, rf2file):
        """ Load the table from the contents of the supplied rf2 file
        @param rf2file: Descendant of RF2FileWrapper to load
        """
        for fname,fullpath in rf2file._filestoload():
            self.loadFile(fullpath)

    def loadFile(self, fname):
        """ Load the supplied file into the table
        @param fname: Name of file to load
        """
        db = self.connect()
        table = self._fname
        tsvfile = fname
        db.execute(self._loadSTMT % vars())
        db.commit()


    def dropTable(self):
        """ Drop the table
        """
        db = self.connect()
        db.execute("DROP TABLE IF EXISTS %s" % self._fname)
        db.commit()

    def truncateTable(self):
        """ Truncate the table
        """
        db = self.connect()
        db.execute("TRUNCATE TABLE %s" % self._fname)
        db.commit()


    def getMaxId(self, namespace):
        """ Return the highest identifier value in the table for the supplied namespace.
        This is only meaningful on core tables, not refsets...
        @param namespace: 7 digit namespace to be tested.
        @return: DecodedNamespace entry for highest value
        """
        db = self.connect()
        query = 'SELECT MAX(id) from %s WHERE (id %% 10000000000) div 1000 = %s' % (self._fname, namespace)
        db.execute(query)
        ns = db.next()[0]
        return DecodedNamespace(0 if ns is None else ns)


    def moduleVersions(self):
        """ Return a set of module identifiers and versions from the file.
        @return: list of moduleId/effectiveTime tuples
        """
        db = self.connect()
        if db.execute("SELECT DISTINCT moduleId, effectiveTime FROM %s "
                      "ORDER BY moduleid ASC, effectiveTime DESC" % self._fname):
            rval = list(db)
            db.close()
            return rval
        db.close()
        return []

    @staticmethod
    def _generator():
        from rf2db.db.RF2Namespaces import IDGenerator
        return IDGenerator(ep_values.namespace)

    @staticmethod
    def newconceptid():
        return RF2FileWrapper._generator().next(sctid_generator.CONCEPT)

    @staticmethod
    def newdescriptionid():
        return RF2FileWrapper._generator().next(sctid_generator.DESCRIPTION)

    @staticmethod
    def newrelationshipid():
        return RF2FileWrapper._generator().next(sctid_generator.RELATIONSHIP)

    @classmethod
    def _rollback(cls, db, changeset, **_):
        fname = cls.fname()
        return db.execute_query("DELETE FROM %(fname)s WHERE changeset = '%(changeset)s' AND locked=1" % vars())

    @classmethod
    def _commit(cls, db, changeset, **_):
        fname = cls.fname()
        return db.execute_query("UPDATE %(fname)s SET locked=0 WHERE changeset = '%(changeset)s'" % vars())

    @classmethod
    def changesetisvalid(cls, changeset):
        return cls.changeseterror(changeset) is None

    @classmethod
    def changeseterror(cls, changeset):
        if not changeset:
            return "Changeset identifier must be supplied"
        if not cls._csdb:
            from rf2db.db.RF2ChangeSetFile import ChangeSetDB
            cls._csdb = ChangeSetDB()
        if not cls._csdb.isValid(changeset):
            return "Change set (%s) is not valid or has been committed" % changeset
        return None

    @property
    def _fname(self):
        return (self.table + '_ss') if cp_values.ss else (self.table + '_full')

    @classmethod
    def fname(cls):
        """
        @return: The name of the wrappered file
        """
        return (cls.table + '_ss') if cp_values.ss else (cls.table + '_full')

    @classmethod
    def refsettype(cls, parms):
        pass

    @classmethod
    def as_list(cls, mlist, parms):
        """ Return a list within a reference set wrapper
        @param mlist: List of elements to return
        @param parms: Parameters
        @return: _refsettype
        """
        if parms.maxtoreturn is None:
            parms.maxtoreturn=rf2_values.defaultblocksize
        thelist = cls.refsettype(parms)
        if parms.maxtoreturn == 0:
            return thelist.finish(True, total=list(mlist)[0])
        for m in mlist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(m)
        return thelist.finish(False)

    def _filestoload(self):
        """ Return a list of paths to files that need to be loaded
        @return: Generator of files to return
        """
        reldir = ('Snapshot' if cp_values.ss else 'Full') if not self.isRF1File else ''
        if rf2_values.fileloc:
            base = os.path.join(rf2_values.fileloc, 'RF1Release' if self.isRF1File else 'RF2Release', reldir, self.directory)
            if os.path.exists(base):
                for fname in os.listdir(base):
                    for p in self.prefixes:
                        if fname.startswith(p) or fname.startswith('x'+p):
                            yield fname, os.path.join(base, fname)
            else:
                print("Directory %s does not exist!" % base, file=sys.stderr)
                raise StopIteration

    lfu_cache()
    def validconcept(self, conceptid, changeset, **kwargs):
        """ Determine whether the supplied concept is valid (active or inactive)
        @param conceptid: concept
        @param changeset: context
        @param kwargs: context
        @return: True if valid false otherwise
        """
        if not conceptid:
            return False
        if not self._concdb:
            from rf2db.db.RF2ConceptFile import ConceptDB
            self._concdb = ConceptDB()
        localargs = singleresultargs(**kwargs)
        localargs['active'] = False
        return bool(self._concdb.read(conceptid, changeset=changeset, **localargs))

    @staticmethod
    def effectivetime_and_moduleid(effectivetime, moduleid):
        """
        @param effectivetime:
        @param moduleid:
        @return:
        """
        if not effectivetime:
            effectivetime = strftime("%Y%m%d", gmtime())
        if not moduleid:
            moduleid = ep_values.moduleid
        return effectivetime, moduleid