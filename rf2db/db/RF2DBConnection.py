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

""" SQL Table Connection package
"""
import sys
import re
from functools import reduce
import mysql.connector as mysql
import sqlalchemy.pool as pool

from ConfigManager.ConfigArgs import ConfigArg, ConfigArgs
from ConfigManager.ConfigManager import ConfigManager
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import booleanparam

config_parms = ConfigArgs('dbparms',
                          [ConfigArg('host', help='MySQL DB Host', default='localhost'),
                           ConfigArg('port', help='MySQL DB Port'),
                           ConfigArg('user', abbrev='u', help='MySQL User Id'),
                           ConfigArg('passwd', abbrev='p', help='MySQL Password'),
                           ConfigArg('db', abbrev='db', help='Database', default='rf2'),
                           ConfigArg('charset', help='MySQL Character Set', default='utf8'),
                           ConfigArg('dodecode', help='If true, convert data to UTF8 for return.  '
                                                      'Needed for some implementations.'),
                           ConfigArg('ss', help="Snapshot(True) or Full(False) tables", default='True')
                          ])
cp_values = ConfigManager(config_parms)

debug_parms = ConfigArgs('debug',
                         [ConfigArg('trace', help='Trace SQL Calls', action='store_true'),
                          ConfigArg('nocache', help='Turn off cache for debugging', action='store_true')
                         ])
db_values = ConfigManager(debug_parms)

db = pool.manage(mysql)

sub_flags = re.M + re.S
sub_subs = [(re.compile(r'^(id|effectiveTime)( |=)', flags=sub_flags), r'tbl.\1\2'),
            (re.compile(r'( |=)(id|effectiveTime)( |=)', flags=sub_flags), r'\1tbl.\2\3'),
            (re.compile(r'( |=)(id|effectiveTime)$', flags=sub_flags), r'\1tbl.\2')]


class RF2DBConnection(object):
    def __init__(self):
        self._connection = None

    def __iter__(self):
        return self

    def newDB(self):
        nondb_config = cp_values.asdict().copy()
        dbname = nondb_config.pop('db')
        nondb_config.pop('dodecode', None)
        nondb_config.pop('ss', None)
        self._connection = db.connect(**nondb_config)
        self._cursor = self._connection.cursor()
        self._cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % dbname)

    def next(self):
        rval = self._cursor.fetchone()
        if not rval:
            self._disconnect()
            raise StopIteration
        return rval

    def _connect(self):
        """ Make sure there is a database connection active """
        if not self._connection:
            parms = cp_values.asdict().copy()
            parms.pop('dodecode', None)
            parms.pop('ss', None)
            self._connection = db.connect(**parms)
            # self._connection.set_character_set("utf8")

    def _disconnect(self):
        """ Close the database connection """
        if self._connection:
            try:
                self._connection.close()
            except Exception:
                pass
            self._connection = None

    # TODO: merge this with execute
    def execute_query(self, stmt, retryCount=0):
        """ Execute a create/delete/update statement

        @param stmt:  The sql statement to execute
        @type stmt: C{str}

        @param retryCount: The number of times the execution has been tried
        @type retryCount: C{int}

        @return: Result of cursor.execute(stmt)
        """
        if booleanparam.v(db_values.trace, False):
            print("===== %s" % stmt)
        try:
            self._connect()
            return self._connection.cmd_query(stmt)
        except db.Error as e:
            self._disconnect()
            if retryCount == 0 and e.args[0] == 2006:
                print >> sys.stderr, ("Database timeout error - reconnecting")
                self._connect()
                return self.execute_query(stmt, retryCount + 1)
            else:
                print >> sys.stderr, ("**********", stmt)
                raise e

    def execute(self, stmt, retryCount=0):
        """ Execute stmt.  
        
        @param stmt:  The sql statement to execute
        @type stmt: C{str}
        
        @param retryCount: The number of times the execution has been tried
        @type retryCount: C{int}
        
        @return: Result of cursor.execute(stmt)
        """
        if booleanparam.v(db_values.trace, False):
            print("===== %s" % stmt)
        try:
            self._connect()
            self._cursor = self._connection.cursor()
            rval = self._cursor.execute(stmt)
            return self._cursor
        except db.Error as e:
            self._disconnect()
            if retryCount == 0 and e.args[0] == 2006:
                print >> sys.stderr, ("Database timeout error - reconnecting")
                self._connect()
                return self.execute(stmt, retryCount + 1)
            else:
                print >> sys.stderr, ("**********", stmt)
                raise e

    class ResultsGenerator(object):
        """ Generator wrapper for sql cursor.  Returns tab separated value list for the query """

        def __init__(self, dbconnection):
            self._db = dbconnection

        def __iter__(self):
            return self

        def next(self):
            t = self._db.next()
            if t:
                return RF2DBConnection.tabify(t)
            raise StopIteration

    @staticmethod
    def build_query(table, filter_="", sort=[], active=True, start=0, maxtoreturn=100, refdate=None,
                    moduleids=None, order='asc', changeset=None, **_):
        """ Query an RF2 table taking the historical information into account.
        
        @param table: table to query
        @type table: C{str}
        
        @param filter_: filter_ to apply to the query.
        @type filter_: C{str}
        
        @param sort: name of column or ordered list of columns to sort on
        @type sort: C{str}
        
        @param active: retrieve active only or all
        @type active: C{bool}
        
        @param start: first record to retrieve (0 based)
        @type start: C{int}
        
        @param maxtoreturn: maximum number of records to return
        @type maxtoreturn: C{int}
        
        @param refdate: reference date - only retrieve records older than or equal to this date
        @type refdate: C{datetime.datetime}

        @param moduleids: list of module ids to constrain the query
        @type moduleids: C{sctid} or C{list{sctid}}

        @param changeset: changeset to include in the query
        @type changeset: C{uuid}
        
        @return: query
        @rtype: C{String}
        """
        start = int(start) if start is not None else 0
        maxtoreturn = int(maxtoreturn) if maxtoreturn is not None else 100
        if not filter_:
            filter_ = "1"
        if cp_values.ss and refdate:
            raise Exception("Cannot use reference date with snapshot")
        if not cp_values.ss:
            key_query = "(SELECT id, MAX(effectiveTime) AS effectiveTime from %(table)s WHERE %(filter_)s" % locals()
            if refdate:
                key_query += " AND effectiveTime <= '%s'" % refdate.strftime("%Y%m%d%H%M")
            key_query += " GROUP BY id) as tbl_keys"

        if not cp_values.ss:
            tf = RF2DBConnection.tweakFilter(filter_)
            query = """ SELECT tbl.* FROM %(table)s tbl, %(key_query)s 
                        WHERE tbl.id = tbl_keys.id AND tbl.effectiveTime = tbl_keys.effectiveTime AND %(tf)s""" % locals()
        else:
            sel = 'tbl.*' if maxtoreturn else 'count(*)'
            query = """ SELECT %(sel)s FROM %(table)s tbl WHERE %(filter_)s """ % locals()
        if active:
            query += " AND active = 1 "
        if moduleids:
            query += " AND (" + ' OR '.join(['moduleid = %s' % m for m in listify(moduleids)]) + ') '
        if changeset:
            query += " AND (changeset = '%s' OR locked = 0)" % changeset
        else:
            query += " AND locked = 0"
        if sort:
            query += " ORDER BY " + ', '.join([('tbl.%s' % e) for e in listify(sort)]) + ' %s ' % order
        if maxtoreturn:
            query += " LIMIT %d, %d " % (start, maxtoreturn + 1)
        return query

    def query(self, table, **kwargs):
        """ Query an RF2 table taking the historical information into account.

        @param table: table to query
        @type table: C{str}

        @param filter_: filter_ to apply to the query.
        @type filter_: C{str}

        @param sort: name of column to sort on
        @type sort: C{str}

        @param active: retrieve active only or all
        @type active: C{bool}

        @param start: first record to retrieve (0 based)
        @type start: C{int}

        @param maxtoreturn: maximum number of records to return
        @type maxtoreturn: C{int}

        @param refdate: reference date - only retrieve records older than or equal to this date
        @type refdate: C{datetime.datetime}

        @param moduleids: list of module ids to constrain query to
        @type moduleids: C{sctid} or C{list{sctid}}

        @return: record generator
        """
        return self.ResultsGenerator(self) if self.execute(self.build_query(table, **kwargs)) else []

    def executeAndReturn(self, query):
        return self._cursor if self.execute(query) else []


    @staticmethod
    def tweakFilter(filt):
        """ Adjust the filter to adjust for the fact that id and effectiveTime occur twice in the call """
        return reduce(lambda text, s_r: s_r[0].sub(s_r[1], text), sub_subs, filt)


    @staticmethod
    def tabify(tup):
        # the "decode" part has to do with the fact that some SQL db's won't return in utf8
        try:
            return '\t'.join(map(lambda r: \
                                     (r.decode('utf8') if booleanparam.v(cp_values.dodecode, False) else r) \
                                         if isinstance(r, basestring) else str(r), tup)) if tup else None
        except Exception as e:
            print ("FAILING TUPLE:", tup)
            raise e


    def commit(self, disconnect=True):
        self._connection.commit()
        if disconnect:
            self._disconnect()

    def close(self):
        self._disconnect()
