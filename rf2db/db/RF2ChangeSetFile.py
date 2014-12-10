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

from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.db.RF2FileCommon import global_rf2_parms
from rf2db.parsers.RF2RefsetParser import RF2ChangeSetReferenceEntry
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam, strparam
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.db.RF2DescriptionTextFile import DescriptionTextDB
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB
from rf2db.db.RF2RelationshipFile import RelationshipDB
from rf2db.db.RF2LanguageFile import LanguageDB
from rf2db.db.RF2SimpleReferencesetFile import SimpleReferencesetDB

changeset_parms = ParameterDefinitionList(global_rf2_parms)
changeset_parms.open = booleanparam(default=True)
changeset_parms.csname = strparam(splittable=False)

add_changeset_parms = ParameterDefinitionList(global_rf2_parms)
add_changeset_parms.csname = strparam(splittable=False)
add_changeset_parms.creator = strparam(splittable=False)
add_changeset_parms.description = strparam(splittable=False)

validate_changeset_parms = ParameterDefinitionList(changeset_parms)

class CountList(object):
    """ This carries various counts of things that rolled back.  Anything not referenced
    returns a count of 0
    """
    def __getattr__(self, item):
        return self.__dict__.get(item, 0)

    def setcount(self, name, count):
        self.__dict__[name] = count


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
      name char(36) COLLATE utf8_bin NOT NULL,
      creator char(128),
      description text(8192) CHARACTER SET utf8,
      isFinal tinyint(1) NOT NULL DEFAULT 0,
      inRelease int(11),
      UNIQUE INDEX %(table)s_name (name),
       %(keys)s );"""


    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def read(self, changeset=None, csname=None, **kwargs):
        """ Read the supplied changeset record
        @param changeset: UUID of the changeset
        @param csname: unique name of the changeset
        @param kwargs: Contextual arguments
        @return: RF2ChangeSetReferenceEntry or None if changeset doesn't exist
        """
        if not changeset:
            return self.read_by_name(csname, **kwargs)
        filter_ = "refsetId=%s AND referencedComponentId='%s' " % (changeSetRefSet, changeset)
        if csname:
            filter_ += "AND name='%s' " % csname
        db = self.connect()
        return db.singleton_query(self._fname,
                                  RF2ChangeSetReferenceEntry,
                                  filter_=filter_,
                                  changeset=changeset, **kwargs)

    def read_by_name(self, csname, **kwargs):
        """ Read the supplied changeset record by csname
        @param csname: name of the changeset
        @param kwargs: Contextual arguments
        @return: RF2ChangeSetReferenceEntry or None if changeset doesn't exist
        """
        fname = self._fname
        query = "SELECT * FROM %(fname)s WHERE name='%(csname)s'" % vars()
        db = self.connect()
        db.execute(query)
        rlist = list(RF2ChangeSetReferenceEntry(c) for c in db.ResultsGenerator(db))
        assert (len(rlist) < 2)
        return rlist[0] if len(rlist) else None

    def invalid_new_reason(self, changeset=None, creator=None, description=None, csname=None, **kwargs):
        if csname and self.read_by_name(csname):
            return "Changeset name: '%s' already exists" % csname
        if changeset and self.read(changeset, **kwargs):
            return "Changeset %s already exists" % changeset
        return None

    def new(self, changeset=None, creator=None, description=None, csname=None, **kwargs):
        """ Create a new locked changeset record
        @param creator: Changeset creator
        @param description: Changeset description
        @return: New record or None if error
        """
        if self.invalid_new_reason(changeset, creator, description, csname, **kwargs):
            return None
        fname = self._fname
        db = self.connect()
        guid = str(uuid.uuid4())
        effectivetime, moduleid = self.effectivetime_and_moduleid(None, None)
        refsetid = changeSetRefSet
        csid = str(uuid.uuid4()) if not changeset else changeset
        if not csname:
            csname = csid

        query = "INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, " \
                "refsetId, referencedComponentId, name, changeset, locked"
        query += ", creator" if creator is not None else ""
        query += ", description" if description is not None else ""
        query += ") values ('%(guid)s', %(effectivetime)s, 1, %(moduleid)s, %(refsetid)s, '%(csid)s', " \
                 "'%(csname)s', '%(csid)s', 1"
        query += ", '%(creator)s'" if creator is not None else ""
        query += ", '%(description)s'" if description is not None else ""
        query += ")"
        db = self.connect()
        results = db.execute_query(query % vars())['affected_rows']
        if results:
            db.commit()
            kwargs['changeset'] = csid
        return self.read(**kwargs)

    def invalid_update_reason(self, changeset=None, creator=None, description=None, csname=None, **kwargs):
        if changeset:
            csrec = self.read(changeset, **kwargs)
            if not csrec:
                return "Changeset %s does not exist" % changeset
        elif csname:
            csrec = self.read_by_name(csname, **kwargs)
            if not csrec:
                return "Changeset name: '%'s does not exist" % csname
        else:
            return "Either a changeset name or a changeset id must be supplied"
        if csrec.isFinal:
            return "Changeset is finalized -- cannot be modified"
        return None

    def update(self, changeset=None, creator=None, description=None, csname=None, **kwargs):
        """ Update a locked changeset record
        @param changeset: changeset to update (if missing use name)
        @param creator: Changeset creator
        @param description: Changeset description
        @param csname: Name of changeset
        @return: New record or None if error
        """
        if self.invalid_update_reason(changeset, creator, description, csname, **kwargs):
            return None
        fname = self._fname
        db = self.connect()
        guid = str(uuid.uuid4())
        effectivetime, moduleid = self.effectivetime_and_moduleid(None, None)
        refsetid = changeSetRefSet
        csid = str(uuid.uuid4()) if not changeset else changeset
        if not csname:
            csname = csid

        query = "INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, " \
                "refsetId, referencedComponentId, name, changeset, locked"
        query += ", creator" if creator is not None else ""
        query += ", description" if description is not None else ""
        query += ") values ('%(guid)s', %(effectivetime)s, 1, %(moduleid)s, %(refsetid)s, '%(csid)s', " \
                 "'%(csname)s', '%(csid)s', 1"
        query += ", '%(creator)s'" if creator is not None else ""
        query += ", '%(description)s'" if description is not None else ""
        query += ")"
        db = self.connect()
        results = db.execute_query(query % vars())['affected_rows']
        if results:
            db.commit()
            kwargs['changeset'] = csid
        return self.read(**kwargs)

    def isValid(self, changeset=None, **kwargs):
        """ Determine whether the supplied changeset is valid in the given context
        @param changeset: uuid of changeset
        @param kwargs: contextual args
        @return: True if valid
        """
        return self.read(changeset=changeset, **kwargs) is not None

    changesetFiles = [(ConceptDB, 'nConcepts'),
                      (DescriptionDB, 'nDescriptions'),
                      (DescriptionTextDB, 'nDescTexts'),
                      (LanguageDB, 'nLanguages'),
                      (StatedRelationshipDB, 'nStatedRelationships'),
                      (RelationshipDB, 'nRelationships'),
                      (SimpleReferencesetDB, 'nSimpleRefsets')]

    def rollback(self, changeset=None, csname=None, **kwargs):
        """ Roll back all of the changes identified in the supplied changeset. If the changeset isn't supplied or
        there is no record of it existing, the function returns success.  This function is always considered successful,
        and has no impact on records that aren't locked.
        @param changeset: uuid of changeset
        @param csname: name of the changeset
        @param kwargs: context
        @return: Count of things that are rolled back or None if error.  Call invalid_update_reason to find out why
        """
        rval = CountList()
        if self.invalid_update_reason(changeset=changeset, csname=csname, **kwargs):
            return None
        if csname and not changeset:
            changeset = self.read_by_name(csname, **kwargs).referencedComponentId.uuid
        if changeset:
            db = self.connect()
            for f, a in ChangeSetDB.changesetFiles:
                rval.setcount(a, f._rollback(db, changeset, **kwargs)['affected_rows'])
                db.commit(False)
            rval.setcount('nChangesets', self._rollback(db, changeset, **kwargs)['affected_rows'])
            db.commit()
        return rval

    def commit(self, changeset=None, csname=None, **kwargs):
        """ Commit all of the changes identified in the supplied changeset. If the changeset isn't supplied or
        there is no record of it existing, the function returns success.  This function is always considered successful,
        and has no impact on records that aren't locked.
        @param changeset: uuid of changeset
        @param csname: name of the changeset
        @param kwargs: context
        @return: Count of things that are rolled back.
        """
        rval = CountList()
        if changeset:
            db = self.connect()
            for f, a in ChangeSetDB.changesetFiles:
                rval.setcount(a, f._commit(db, changeset, **kwargs)['affected_rows'])
                db.commit(False)
            rval.setcount('nChangesets', self._commit(db, changeset, **kwargs)['affected_rows'])
            db.commit()
        return rval



