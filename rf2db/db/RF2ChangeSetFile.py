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
from rf2db.db.RF2FileCommon import global_rf2_parms, ep_values
from rf2db.parsers.RF2RefsetParser import RF2ChangeSetReferenceEntry
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam, strparam
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.db.RF2DescriptionTextFile import DescriptionTextDB
from rf2db.db.RF2RelationshipFile import RelationshipDB
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB

changeset_parms = ParameterDefinitionList(global_rf2_parms)
changeset_parms.open = booleanparam(default=True)

add_changeset_parms = ParameterDefinitionList(global_rf2_parms)
add_changeset_parms.creator = strparam(splittable=False)
add_changeset_parms.description = strparam(splittable=False)

validate_changeset_parms = ParameterDefinitionList(global_rf2_parms)

class CountList():
    """ This carries various counts of things that rolled back.  Anything not referenced
    returns a count of 0
    """
    def __getattribute__(self, item):
        return self.__dict__.get(item, 0)


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
    prefixes = ['der2_sssiiRefset_Changeset']
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

    def get_changeset(self, changeset, **kwargs):
        """ Read the supplied changeset record
        @param changeset: UUID of the changeset
        @param kwargs: Contextual arguments
        @return: RF2ChangeSetReferenceEntry or None if refset doesn't exist
        """
        if not changeset:
            return None
        filter_ = "refsetId=%s AND referencedComponentId='%s' " % (changeSetRefSet, changeset)
        db = self.connect()
        rlist = [RF2ChangeSetReferenceEntry(c) for c in db.query(self._fname, filter_=filter_, changeset=changeset, **kwargs)]
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def new_changeset(self, creator=None, description=None, **kwargs):
        """ Create a new locked changeset record
        @param creator: Changeset creator
        @param description: Changeset description
        @return: New record
        """
        fname = self._fname
        db = self.connect()
        guid = str(uuid.uuid4())
        effectivetime = strftime("%Y%m%d", gmtime())
        moduleid = ep_values.moduleid
        refsetid = changeSetRefSet
        csid = str(uuid.uuid4())

        query = "INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, " \
                "refsetId, referencedComponentId, changeset, locked"
        query += ", creator" if creator is not None else ""
        query += ", description" if description is not None else ""
        query += ") values ('%(guid)s', %(effectivetime)s, 1, %(moduleid)s, %(refsetid)s, '%(csid)s', '%(csid)s', 1"
        query += ", '%(creator)s'" if creator is not None else ""
        query += ", '%(description)s'" if description is not None else ""
        query += ")"
        db = self.connect()
        db.execute(query % vars())
        db.commit()
        kwargs['changeset'] = csid
        return self.get_changeset(**kwargs)

    def isValid(self, changeset=None, **kwargs):
        """ Determine whether the supplied changeset is valid in the given context
        @param changeset: uuid of changeset
        @param kwargs: contextual args
        @return: True if valid
        """
        return self.get_changeset(changeset=changeset, **kwargs) is not None


    def rollback(self, changeset=None, **kwargs):
        """ Roll back all of the changes identified in the supplied changeset. If the changeset isn't supplied or
        there is no record of it existing, the function returns success.  This function is always considered successful,
        and has no impact on records that aren't locked.
        @param changeset: uuid of changeset
        @param kwargs: context
        @return: Count of things that are rolled back.
        """
        rval = CountList()
        if changeset:
            db = self.connect()
            rval.nConcepts = ConceptDB._rollback(db, changeset, **kwargs)['affected_rows']
            rval.nChangesets = self._rollback(db, changeset, **kwargs)['affected_rows']
            db.commit()
        return rval

    def commit(self, changeset=None, **kwargs):
        """ Commit all of the changes identified in the supplied changeset. If the changeset isn't supplied or
        there is no record of it existing, the function returns success.  This function is always considered successful,
        and has no impact on records that aren't locked.
        @param changeset: uuid of changeset
        @param kwargs: context
        @return: Count of things that are rolled back.
        """
        rval = CountList()
        if changeset:
            db = self.connect()
            rval.nConcepts = ConceptDB._commit(db, changeset, **kwargs)['affected_rows']
            rval.nChangesets = self._commit(db, changeset, **kwargs)['affected_rows']
            db.commit()
        return rval



