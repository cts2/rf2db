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


import os
import rf2db.db.RF2DBConnection
from config.ConfigArgs import ConfigArg, ConfigArgs
from rf2db.utils.ParmParser import KwParms

config_parms = ConfigArgs( 'rf2',
                           [ConfigArg('fileloc', abbrev='f', help='Location of primary RF2 Distribution'),
                            ConfigArg('addloc', abbrev='a',help='Add the location of a secondary RF2 Distribution'),
                            ConfigArg('canonical', abbrev='c', help='Add the RF1 Canonical ')
                            ])

# TODO: initialize the PYTHONPATH variable - use WebServer as an example
# TODO: load script for SNOMED_STY file
#  Query: create table rf2.UMLS_STY as SELECT sty.cui CUI, tui TUI, sty STU, scui SCUI, sab SAB from MRSTY sty, MRCONSO con
#         WHERE con.cui = sty.cui
#         Index is (SCUI, SAB)
#         Second index is (TUI, SAB)



class RF2FileWrapper(object):
    """ Abstract wrapper class for RF2 files """
    # ================== Virtual parameters ===============
    directory  = None    # 'Terminology' or 'Refset/Content', 'Refset/Language', etc
    prefixes   = []      # 'sct2_Concept_', 'der2_cRefset_AttributeValue', 'der2_Refset_Simple', etc.
    table      = None    # 'concept', 'description', 'simplemap', etc.
    createSTMT = None    # SQL create statement for table. 'table' is available as a parameter
    isRF1File  = False   # True means this is an RF1 table w/ different behavior

    # Directory layout
    # - py4cts2/RF2/rf2_source
    #      - symbolic link to RF2Release directory 1
    #          - Full
    #              - Terminology
    #              - Refset
    #          - Snapshot
    #              - Terminology
    #              - Refset
    #      - symbolic link to RF2Release directory 2
    #          - Full
    #              - Terminology
    #              - Refset
    #          ...


    _loadSTMT = """LOAD DATA  local INFILE '%(tsvfile)s'
              INTO TABLE %(table)s  
              FIELDS TERMINATED BY '\\t' 
              LINES TERMINATED BY '\\r\\n'  
              IGNORE 1 LINES;"""

    _hasContentSTMT = """SELECT * FROM %s LIMIT 1;"""


    _existsQuery = """SHOW TABLES LIKE '%s';"""



    def __init__(self, load=False, noaction=False):
        self._existsss     = self._existsfull = False
        self._hascontentss = self._hascontentfull = False
        self._tabless      = self.table + '_ss'
        self._tablefull    = self.table + '_full'

    def connect(self):
        return rf2db.db.RF2DBConnection.RF2DBConnection()

    def exists(self, ss):
        if ss:
            if not self._existsss:
                db = self.connect()
                self._existsss   = db.execute(self._existsQuery % self._tabless) > 0
                db.close()
            return self._existsss
        else:
            if not self._existsfull:
                db = self.connect()
                self._existsfull = db.execute(self._existsQuery % self._tablefull) > 0
                db.close()
            return self._existsfull

    def createTable(self, ss):
        import warnings
        warnings.filterwarnings("ignore", r"Table .* already exists.*")
        if ss:
            db = self.connect()
            db.execute(self.createSTMT % {'table':self._tabless,   'primkey': 'PRIMARY KEY (id)' })
            db.commit()
            self._existsss = True
        else:
            db = self.connect()
            db.execute(self.createSTMT % {'table':self._tablefull, 'primkey': 'PRIMARY KEY (id,effectiveTime)' })
            db.commit()
            self._existsfull = True

    def hascontent(self, ss):
        if ss:
            if not self._hascontentss:
                db = self.connect()
                self._hascontentss   = db.execute(self._hasContentSTMT % self._tabless) if self.exists(ss) else False
                db.close()
            return self._hascontentss
        else:
            if not self._hascontentfull:
                db = self.connect()
                self._hascontentfull = db.execute(self._hasContentSTMT % self._tabless) if self.exists(ss) else False
                db.close()
            return self._hascontentfull

    def numrecs(self, ss):
        db = self.connect()
        if db.execute("SELECT COUNT(*) FROM %s" % self._tname(ss) ):
            rval = db.next()[0]
            db.close()
            return rval

    def loadTable(self, rf2file, ss, cfg):
        for fname,fullpath in rf2file._filesToLoad(ss, cfg):
            self.loadFile(fullpath, ss)

    def loadFile(self, fname, ss):
        db = self.connect()
        db.execute(self._loadSTMT % {'table':self._tname(ss), 'tsvfile':fname})
        db.commit()


    def dropTable(self, ss):
        db = self.connect()
        db.execute("DROP TABLE IF EXISTS %s" % self._tname(ss))
        db.commit()

    def truncateTable(self, ss):
        db = self.connect()
        db.execute("TRUNCATE TABLE %s" % self._tname(ss))
        db.commit()

    def moduleVersions(self, ss):
        db = self.connect()
        if db.execute("SELECT DISTINCT moduleId, effectiveTime FROM %s ORDER BY moduleid ASC, effectiveTime DESC" % self._tname(ss)):
            rval = list(db)
            db.close()
            return rval
        db.close()
        return []

    def _tname(self, ss):
        return self._tabless if ss else self._tablefull

    def _filesToLoad(self, ss, cfg):
        reldir = ('Snapshot' if ss else 'Full') if not self.isRF1File else ''
        if cfg.fileloc:
            base = os.path.join(cfg.fileloc, 'RF1Release' if self.isRF1File else 'RF2Release', reldir, self.directory)
            if os.path.exists(base):
                for fname in os.listdir(base):
                    for p in self.prefixes:
                        if fname.startswith(p) or fname.startswith('x'+p):
                            yield fname, os.path.join(base, fname)
            else:
                print ("Directory %s does not exist!" % base)



