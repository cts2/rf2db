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
from __future__ import print_function       # This shouldn't be needed but...

""" SQL Table Connection package
"""
import sys
import re
from functools import reduce
import mysql.connector as mysql
from mysql.connector.errorcode import CR_SERVER_GONE_ERROR, CR_CONNECTION_ERROR
import sqlalchemy.pool as pool

from ConfigManager.ConfigArgs import ConfigArg, ConfigArgs
from ConfigManager.ConfigManager import ConfigManager
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import booleanparam

if sys.version_info.major > 2:
    basestr = str


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


def singleresultargs(**kwargs):
    """ Filter out the parameters in kwargs that are for lists.  This is used to allow calls
    for designations, validation, etc. within othe calls to not get executed as a list query.
    @param kwargs: complete set of args
    @return: filtered set
    """
    rval = kwargs.copy()
    rval['maxtoreturn'] = 1
    rval.pop('start', None)
    rval.pop('page', None)
    return rval


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

    def __next__(self):
        return self.next()

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
            self._connection.autocommit = True

    def _disconnect(self):
        """ Close the database connection """
        if self._connection:
            try:
                self._connection.close()
            except Exception:
                pass
            self._connection = None

    def _dosql(self, func, stmt, retrycount=0):
        """ Execute a create/delete/update statement
        @paramm func: function to execute
        @param stmt:  The sql statement to execute
        @type stmt: C{str}

        @param retrycount: The number of times the execution has been tried
        @type retrycount: C{int}

        @return: Result of cursor.execute(stmt)
        """
        if booleanparam.v(db_values.trace, False):
            print("===== %s" % stmt)
        try:
            self._connect()
            return func(self, stmt)
        except db.Error as e:
            self._disconnect()
            if retrycount == 0 and e.errno in (CR_SERVER_GONE_ERROR, CR_CONNECTION_ERROR, -1):
                print("Database timeout error - reconnecting", file=sys.stderr)
                return self._dosql(func, stmt, retrycount+1)
            else:
                raise e

    def execute_query(self, stmt, retrycount=0):
        """ Execute a create/delete/update statement

        @param stmt:  The sql statement to execute
        @type stmt: C{str}

        @param retrycount: The number of times the execution has been tried
        @type retrycount: C{int}

        @return: Result of cursor.execute(stmt)
        """
        return self._dosql(lambda self, stmt: self._connection.cmd_query(stmt), stmt)


    def execute(self, stmt):
        """ Execute stmt.  
        
        @param stmt:  The sql statement to execute
        @type stmt: C{str}

        @return: Result of cursor.execute(stmt)
        """
        def f(self, stmt):
            self._cursor = self._connection.cursor()
            self._cursor.execute(stmt)
            return self
        return self._dosql(f, stmt)

    class ResultsGenerator(object):
        """ Generator wrapper for sql cursor.  Returns tab separated value list for the query """

        def __init__(self, dbconnection):
            self._db = dbconnection

        def __iter__(self):
            return self

        def __next__(self):
            t = next(self._db)
            if t:
                return RF2DBConnection.tabify(t)
            raise StopIteration

    @staticmethod
    def build_query(table, filter_="", sort=None, active=True, start=0, maxtoreturn=None, refdate=None,
                    moduleid=None, order='asc', changeset=None, ignore_locks=False, locked=False,  **_):
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

        @param moduleid: list of module ids to constrain the query
        @type moduleid: C{sctid} or C{list{sctid}}

        @param changeset: changeset to include in the query
        @type changeset: C{uuid}

        @param ignore_locks: True means pay no attention to ock settings
        @type ignore_locks: C{bool}
        
        @return: query
        @rtype: C{String}
        """
        if changeset:
            from rf2db.db.RF2FileCommon import RF2FileWrapper
            changeset = RF2FileWrapper.tochangesetuuid(changeset)

        start = int(start) if start is not None else 0
        if maxtoreturn is None:
            from rf2db.db.RF2FileCommon import rf2_values
            maxtoreturn = int(rf2_values.defaultblocksize)
        else:
            maxtoreturn = int(maxtoreturn)
        if not filter_:
            filter_ = "1"
        if cp_values.ss and refdate:
            raise Exception("Cannot use reference date with snapshot")
        if not cp_values.ss:
            key_query = "(SELECT id, MAX(effectiveTime) AS effectiveTime from %(table)s WHERE %(filter_)s" % locals()
            if refdate:
                key_query += " AND effectiveTime <= '%s'" % refdate.strftime("%Y%m%d%H%M")
            key_query += " GROUP BY id) as tbl_keys"

        # TODO: Count doesn't work in non ss mode
        if not cp_values.ss:
            tf = RF2DBConnection.tweakFilter(filter_)
            query = """ SELECT tbl.* FROM %(table)s tbl, %(key_query)s 
                        WHERE tbl.id = tbl_keys.id AND tbl.effectiveTime = tbl_keys.effectiveTime AND %(tf)s""" % locals()
        else:
            sel = 'tbl.*' if maxtoreturn else 'count(*)'
            query = """ SELECT %(sel)s FROM %(table)s tbl WHERE %(filter_)s """ % locals()
        if not changeset and locked and not ignore_locks:
            query += " AND False "
        if active:
            query += " AND active = 1 "
        if moduleid:
            query += " AND (" + ' OR '.join(['moduleid = %s' % m for m in listify(moduleid)]) + ') '
        if not ignore_locks:
            if locked and not changeset:
                query += " AND locked = 1 "
            elif locked and changeset:
                query += " AND (changeset = '%s' AND locked = 1) " % changeset
            elif changeset:
                query += " AND (changeset = '%s' OR locked = 0) " % changeset
            else:
                query += ' AND locked = 0 '
        if sort:
            query += " ORDER BY " + ', '.join([('tbl.%s' % e) for e in listify(sort)]) + ' %s ' % order
        if maxtoreturn > 0:
            query += " LIMIT %d" % (maxtoreturn+1)
        if start:
            query += " OFFSET %d" % start
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

    def singleton_query(self, table, cls, **kwargs):
        """ Query that returns at most one element.
        @param table: table name to be queried
        @param kwargs: Same as query
        @return: Singleton instance of cls else nothing
        """
        rlist = [cls(c) for c in self.query(table, **singleresultargs(**kwargs))]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    @staticmethod
    def tweakFilter(filt):
        """ Adjust the filter to adjust for the fact that id and effectiveTime occur twice in the call """
        return reduce(lambda text, s_r: s_r[0].sub(s_r[1], text), sub_subs, filt)

    @staticmethod
    def tabify(tup):
        # the "decode" part has to do with the fact that some SQL db's won't return in utf8
        try:
            return '\t'.join([r if isinstance(r, str) else
                              bytearray.decode(r) if isinstance(r, bytearray)
                              else str(r) for r in tup]) if tup else None
        except Exception as e:
            print(("FAILING TUPLE:", tup))
            raise e

    def commit(self, disconnect=True):
        if self._connection:
            self._connection.commit()
            if disconnect:
                self._disconnect()

    def close(self):
        self._disconnect()
