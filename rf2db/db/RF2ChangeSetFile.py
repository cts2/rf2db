# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
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
""" Change Set Table access
"""
import uuid
from time import gmtime, strftime

from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.db.RF2FileCommon import global_rf2_parms, extensionParms
from rf2db.parsers.RF2RefsetParser import RF2ChangeSetReferenceEntry
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam, strparam
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB

changeset_parms = ParameterDefinitionList(global_rf2_parms)
changeset_parms.open = booleanparam(default=True)

add_changeset_parms = ParameterDefinitionList(global_rf2_parms)
add_changeset_parms.creator = strparam(splittable=False)
add_changeset_parms.description = strparam(splittable=False)

validate_changeset_parms = ParameterDefinitionList(global_rf2_parms)

class RollbackInfo():
    pass

class CommitInfo():
    pass


class ChangeSetDB(RF2RefsetWrapper):
    """
    The changeset file:
    The header is the usual refset header, where:
    refsetId -- is the changeset reference set
    referencedComponentId -- the UUID of the changeset itself
    creator -- URI of the changeset creator
    changeSetDescription -- a description of the changeset purpose and contents
    isFinal -- 0 means set is open, 1 means final
    inRelease -- release identifier that contains the changset (meaning it has been distributed.
    """
    directory = 'Refset/Language'
    # TODO: Correct file name
    prefixes = ['der2_cRefset_Changeset']
    table = 'changeset'

    createSTMT = "CREATE TABLE IF NOT EXISTS %(table)s (" + RF2RefsetWrapper._file_base_ + """
      referencedComponentId char(36) COLLATE utf8_bin NOT NULL,
      creator char(128),
      description text(8192) CHARACTER SET utf8,
      isFinal tinyint(1) NOT NULL DEFAULT 0,
      inRelease int(11),
       %(keys)s );"""


    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def get_changeset(self, parmlist):
        """ Retrieve the accompanying changeset record
        Read the changeset record
        @param parmlist: changeset_parms.
        """
        filter_ = "refsetId=%s AND referencedComponentId='%s' " % (changeSetRefSet, parmlist.changeset)
        db = self.connect()
        rlist = [RF2ChangeSetReferenceEntry(c) for c in db.query_p(self._tname(parmlist.ss), parmlist, filter=filter_)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def new_changeset(self, parmlist):
        fname = self._tname(parmlist.ss)
        db = self.connect()
        guid = uuid.uuid4()
        effectiveTime = strftime("%Y%m%d", gmtime())
        moduleId = extensionParms.moduleid
        refsetId = changeSetRefSet
        csid = uuid.uuid4()
        creator = parmlist.creator
        description = parmlist.description

        query = "INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, refsetId, referencedComponentId, changeset, locked"
        query += ", creator" if parmlist.creator else ""
        query += ", description" if parmlist.description else ""
        query += ") values ('%(guid)s', %(effectiveTime)s, 1, %(moduleId)s, %(refsetId)s, '%(csid)s', '%(csid)s', 1"
        query += ", '%(creator)s'" if parmlist.creator else ""
        query += ", '%(description)s'" if parmlist.description else ""
        query += ")"
        db = self.connect()
        db.execute(query % vars())
        db.commit()
        parmlist.changeset = csid
        return self.get_changeset(parmlist)

    def isValid(self, parmlist):
        """ Determine whether the changeset accompanying the parameter list is valid.
        :param parmlist: validate_changeset_parms entry
        :return: True if valid.
        """
        return self.get_changeset(parmlist) is not None

    def rollback(self, parmlist):
        db = self.connect()
        rval = RollbackInfo()
        rval.nConcepts = ConceptDB._rollback(db, parmlist.ss, parmlist.changeset)['affected_rows']
        rval.nChangesets = self._rollback(db, parmlist.ss, parmlist.changeset)['affected_rows']
        db.commit()
        return rval

    def commit(self,parmlist):
        db = self.connect()
        rval = CommitInfo()
        rval.nConcepts = ConceptDB._commit(db, parmlist.ss, parmlist.changeset)['affected_rows']
        rval.nChangesets = self._commit(db, parmlist.ss, parmlist.changeset)['affected_rows']
        db.commit()
        return rval

