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
import sys, re
from functools import reduce
import MySQLdb as mysql
import sqlalchemy.pool as pool

from config.ConfigArgs import ConfigArg, ConfigArgs
from config.ConfigManager import ConfigManager

config_parms = ConfigArgs( 'dbparms',
                           [ConfigArg('host', help='MySQL DB Host', default='localhost'),
                            ConfigArg('port', help='MySQL DB Port'),
                            ConfigArg('user', abbrev='u', help='MySQL User Id'),
                            ConfigArg('passwd', abbrev='p', help='MySQL Password'),
                            ConfigArg('db', abbrev='db', help='Database', default='rf2'),
                            ConfigArg('charset', help='MySQL Character Set', default='utf8'),
                            ConfigArg('trace', help='Trace SQL Statements', action='store_true')
                            ])
config = ConfigManager(config_parms)
# TODO: how to we get the configuration file name into here?  Should we?

db = pool.manage(mysql)



class RF2DBConnection(object):

    def __init__(self):
        self._connection = None

    def __iter__(self):
        return self

    def newDB(self, config_mgr):
        nondb_config = config_mgr.section().copy()
        dbname = nondb_config.pop('db')
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
            parms = config.section().copy()
            self._connection = db.connect(**config.section())
            # self._connection.set_character_set("utf8")

    def _disconnect(self):
        """ Close the database connection """
        if self._connection:
            try:
                self._connection.close()
            except Exception:
                pass
            self._connection = None

    def execute(self, stmt, retryCount=0):
        """ Execute stmt.  
        
        @param stmt:  The sql statement to execute
        @type stmt: C{str}
        
        @param retryCount: The number of times the execution has been tried
        @type retryCount: C{int}
        
        @return: Result of cursor.execute(stmt)
        """
        if config.trace:
            print("=====", stmt)
        try:
            self._connect()
            self._cursor = self._connection.cursor()
            return self._cursor.execute(stmt)
        except db.Error as e:
            self._disconnect()
            if retryCount == 0 and e.args[0] == 2006:
                print >> sys.stderr, ("Database timeout error - reconnecting")
                self._connect()
                return self.execute(stmt, retryCount+1)
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

    def build_query(self, table, filter_="", sort=None, active=True, ss=True, start=0, maxtoreturn=0, refdate=None):
        """ Query an RF2 table taking the historical information into account.
        
        @param table: table to query
        @type table: C{str}
        
        @param filter_: filter_ to apply to the query.
        @type filter_: C{str}
        
        @param sort: name of column to sort on
        @type sort: C{str}
        
        @param active: retrieve active only or all
        @type active: C{bool}
        
        @param ss: snapshot or full table query
        @type ss: C{bool}
        
        @param start: first record to retrieve (0 based)
        @type start: C{int}
        
        @param maxtoreturn: maximum number of records to return
        @type maxtoreturn: C{int}
        
        @param refdate: reference date - only retrieve records older than or equal to this date
        @type refdate: C{datetime.datetime}
        
        @return: number of elements
        @rtype: C{String}
        """
        start = int(start)
        maxtoreturn = int(maxtoreturn)
        if not filter_:
            filter_ = "1"
        if ss and refdate:
            raise Exception("Cannot use reference date with snapshot")
        if not ss:
            key_query = "(select id, MAX(effectiveTime) AS effectiveTime from %(table)s WHERE %(filter_)s" % locals()
            if refdate:
                key_query += " AND effectiveTime <= '%s'" % refdate.strftime("%Y%m%d%H%M")
            key_query += " GROUP BY id) as tbl_keys"
        
        
        if not ss:
            tf = self.tweakFilter(filter_)
            query = """ SELECT tbl.* FROM %(table)s tbl, %(key_query)s 
                        WHERE tbl.id = tbl_keys.id AND tbl.effectiveTime = tbl_keys.effectiveTime AND %(tf)s""" % locals()
        else:
            query = """ SELECT tbl.* from %(table)s tbl WHERE %(filter_)s""" %locals()
        if active:
            query += " AND active = 1"
        if sort:
            query += " ORDER BY tbl.%s ASC " % sort

        if maxtoreturn:
            query += " LIMIT %d, %d " % (start, maxtoreturn)
        return query

    def query(self, table, filter_="", sort=None, active=True, ss=True, start=0, maxtoreturn=0, refdate=None):
        """ Query an RF2 table taking the historical information into account.

        @param table: table to query
        @type table: C{str}

        @param filter_: filter_ to apply to the query.
        @type filter_: C{str}

        @param sort: name of column to sort on
        @type sort: C{str}

        @param active: retrieve active only or all
        @type active: C{bool}

        @param ss: snapshot or full table query
        @type ss: C{bool}

        @param start: first record to retrieve (0 based)
        @type start: C{int}

        @param maxtoreturn: maximum number of records to return
        @type maxtoreturn: C{int}

        @param refdate: reference date - only retrieve records older than or equal to this date
        @type refdate: C{datetime.datetime}

        @return: list of records
        @rtype: list of tuple
        """
        return self.ResultsGenerator(self) if self.execute(self.build_query(table, filter_, sort, active, ss, start,
                                                                            maxtoreturn, refdate)) else []

    def executeAndReturn(self, query):
        return self if self.execute(query) else []
    
    def tweakFilter(self, filt):
        """ Adjust the filter to adjust for the fact that id and effectiveTime occur twice in the call """
        flags=re.M+re.S
        subs = [(re.compile(r'^(id|effectiveTime)( |=)',flags=flags), r'tbl.\1\2'), 
                (re.compile(r'( |=)(id|effectiveTime)( |=)',flags=flags),r'\1tbl.\2\3'),
                (re.compile(r'( |=)(id|effectiveTime)$',flags=flags),r'\1tbl.\2')]
        return reduce(lambda text, s_r: s_r[0].sub(s_r[1],text), subs, filt)

            
    @staticmethod
    def tabify(tup):
        # the "decode" part has to do with the fact that some SQL db's won't return in utf8
        try:
            return '\t'.join(map(lambda r: \
                                (r.decode('utf8') if config.dodecode else r) \
                                if isinstance(r,str) else str(r),tup)) if tup else None
        except Exception as e:
            print >> sys.stderr, ("FAILING TUPLE:", tup)
            raise e
        
  
    def commit(self, disconnect=True):
        self._connection.commit()
        if disconnect:
            self._disconnect()

    def close(self):
        self._disconnect()
