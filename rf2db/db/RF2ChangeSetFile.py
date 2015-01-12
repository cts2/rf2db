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
import re

from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper, global_refset_parms
from rf2db.parsers.RF2Iterator import RF2ChangeSetReferenceSet, iter_parms
from rf2db.parsers.RF2RefsetParser import RF2ChangeSetReferenceSetEntry, RF2ChangeSetDetails
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, booleanparam, strparam
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.db.RF2DescriptionTextFile import DescriptionTextDB
from rf2db.db.RF2StatedRelationshipFile import StatedRelationshipDB
from rf2db.db.RF2RelationshipFile import RelationshipDB
from rf2db.db.RF2LanguageFile import LanguageDB
from rf2db.db.RF2SimpleReferencesetFile import SimpleReferencesetDB
from rf2db.db.RF2ModuleDependencyFile import ModuleDependencyDB
from rf2db.db.AllFiles import read_by_changeset
from rf2db.utils.listutils import listify

changeset_parms = ParameterDefinitionList(global_refset_parms)
changeset_parms.open = booleanparam(default=True)
changeset_parms.csname = strparam(splittable=False)

add_changeset_parms = ParameterDefinitionList(global_refset_parms)
add_changeset_parms.csname = strparam(splittable=False)
add_changeset_parms.owner = strparam(splittable=False)
add_changeset_parms.description = strparam(splittable=False)

validate_changeset_parms = ParameterDefinitionList(changeset_parms)

update_changeset_parms = ParameterDefinitionList(add_changeset_parms)

list_changeset_parms = ParameterDefinitionList(iter_parms)
list_changeset_parms.open = booleanparam(default=True)
list_changeset_parms.final = booleanparam(default=False)
list_changeset_parms.released = booleanparam(default=None)
list_changeset_parms.owner = strparam(splittable=True)
list_changeset_parms.release = strparam(splittable=True)

class CountList(object):
    """ This carries various counts of things that rolled back.  Anything not referenced
    returns a count of 0
    """
    def __getattr__(self, item):
        return self.__dict__.get(item, 0)

    def setcount(self, name, count):
        self.__dict__[name] = count

uuidre = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')

def csorname(changeset, csname):
    """ Return a uuid if id parses as such, otherwise a name
    @param changeset: changeset identifier or name
    @param csname: changeset name
    @return: updated args
    """
    if isinstance(changeset, list):
        changeset = ' '.join(changeset)
    if isinstance(csname, list):
        csname = ' '.join(changeset)
    if changeset and not csname:
        return (changeset, None) if uuidre.match(changeset) else (None, changeset)
    return changeset, csname


class ChangeSetDB(RF2RefsetWrapper):
    """
    The changeset file:
    The header is the usual refset header, where:
    refsetId -- is the changeset reference set
    referencedComponentId -- the UUID of the changeset itself
    owner -- name of the changeset owner
    changeSetDescription -- a description of the changeset purpose and contents
    isFinal -- 0 means set is open, 1 means final
    inRelease -- release identifier that contains the changset (meaning it has been distributed.
    """
    directory = 'Refset/Metadata'
    prefixes = ['der2_sssiiRefset_Changeset']
    table = 'changeset'

    def _wrapper(self, e):
        return RF2ChangeSetReferenceSetEntry(e)

    _wrapper_cls = _wrapper

    # _wrapper_cls = lambda self, e: RF2ChangeSetReferenceSetEntry(self, e)

    createSTMT = "CREATE TABLE IF NOT EXISTS %(table)s (" + RF2RefsetWrapper._file_base_ + """
      referencedComponentId char(36) COLLATE utf8_bin NOT NULL,
      name char(36) COLLATE utf8_bin NOT NULL,
      owner char(128),
      description text(8192) CHARACTER SET utf8,
      isFinal tinyint(1) NOT NULL DEFAULT 0,
      inRelease int(11),
      UNIQUE INDEX %(table)s_name (name),
       %(keys)s );"""


    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        return RF2RefsetWrapper.__new__(cls, *args, **kwargs)

    def read(self, changeset=None, csname=None, uuid=None, **kwargs):
        """ Read the supplied changeset record
        @param changeset: UUID of the changeset
        @param csname: unique name of the changeset
        @param kwargs: Contextual arguments
        @return: RF2ChangeSetReferenceEntry or None if changeset doesn't exist
        """
        if uuid:
            rval = super(ChangeSetDB, self).read(changset=changeset, csname=csname, uuid=uuid, **kwargs)
            if rval:
                return rval
            changeset = uuid
            uuid=None
        changeset, csname = csorname(changeset, csname)
        if not changeset:
            changeset = self._read_by_name(csname, **kwargs)
        filter_ = "refsetId=%s AND referencedComponentId='%s' " % (changeSetRefSet, changeset)
        if csname:
            filter_ += "AND name='%s' " % csname
        db = self.connect()
        return db.singleton_query(self._fname,
                                  RF2ChangeSetReferenceSetEntry,
                                  filter_=filter_,
                                  changeset=changeset, **kwargs)



    def _read_by_name(self, csname, changeset=None, **kwargs):
        """ Read the supplied changeset record by csname
        @param csname: name of the changeset
        @param kwargs: Contextual arguments
        @return: changeset id for name or None
        """
        db = self.connect()
        base = db.singleton_query(self._fname,
                                  RF2ChangeSetReferenceSetEntry,
                                  filter_="name='%s'" % csname,
                                  changeset=changeset,
                                  ignore_locks=True,
                                  **kwargs)
        return base.referencedComponentId.uuid if base else None

    def read_details(self, changeset=None, csname=None, **kwargs):
        """ Read the supplied changeset record and all associated files
        @param changeset: UUID of the changeset
        @param csname: unique name of the changeset
        @param kwargs: Contextual arguments
        @return: RF2ChangeSetReferenceEntry or None if changeset doesn't exist
        """
        changeset, csname = csorname(changeset, csname)
        if not changeset:
            changeset = self._read_by_name(csname, **kwargs)
            if not changeset:
                return None
        filter_ = "refsetId=%s AND referencedComponentId='%s' " % (changeSetRefSet, changeset)
        if csname:
            filter_ += "AND name='%s' " % csname
        db = self.connect()
        base = db.singleton_query(self._fname,
                                  RF2ChangeSetDetails,
                                  filter_=filter_,
                                  changeset=changeset, **kwargs)
        if not base:
            return None
        details = read_by_changeset(changeset)
        for k, v in details.items():
            base.__setattr__(k, v)
        return base

    def invalid_new_reason(self, changeset=None, owner=None, description=None, csname=None, **kwargs):
        if csname and self._read_by_name(csname, **kwargs):
            return "Changeset name: '%s' already exists" % csname
        if changeset and self.read(changeset, **kwargs):
            return "Changeset %s already exists" % changeset
        return None

    def new(self, changeset=None, owner=None, description=None, csname=None, **kwargs):
        """ Create a new open changeset
        @param changeset: uuid of the changeset to create.  None means create a new one
        @param owner: name of the changeset owner
        @param description: description of the changeset
        @param csname: name of the changeset.  If absent, will become the changset URI
        @param kwargs: context
        @return: New changeset record or None if there is an error.  Use invalid_new_reason to find out why.
        """
        changeset, csname = csorname(changeset, csname)
        if self.invalid_new_reason(changeset, owner, description, csname, **kwargs):
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
        query += ", owner" if owner is not None else ""
        query += ", description" if description is not None else ""
        query += ") values ('%(guid)s', %(effectivetime)s, 1, %(moduleid)s, %(refsetid)s, '%(csid)s', " \
                 "'%(csname)s', '%(csid)s', 1"
        query += ", '%(owner)s'" if owner is not None else ""
        query += ", '%(description)s'" if description is not None else ""
        query += ")"
        db = self.connect()
        results = db.execute_query(query % vars())['affected_rows']
        if results:
            db.commit()
            kwargs['changeset'] = csid
        return self.read(**kwargs)

    def invalid_update_reason(self, changeset=None, owner=None, description=None, csname=None, **kwargs):
        if changeset:
            csrec = self.read(changeset, **kwargs)
            if not csrec:
                return "Changeset %s does not exist" % changeset
        elif csname:
            changeset = self._read_by_name(csname, **kwargs)
            if not changeset:
                return "Changeset name: '%s' does not exist" % csname
            csrec = self.read(changeset)
        else:
            return "Either a changeset name or a changeset id must be supplied"
        if csrec.isFinal:
            return "Changeset is finalized -- cannot be modified"
        return None

    def update(self, changeset=None, owner=None, description=None, csname=None, **kwargs):
        """ Update a locked changeset record
        @param changeset: changeset to update (if missing use name)
        @param owner: Changeset owner
        @param description: Changeset description
        @param csname: Name of changeset
        @return: New record or None if error
        """
        changeset, csname = csorname(changeset, csname)
        if self.invalid_update_reason(changeset, owner, description, csname, **kwargs):
            return None
        if not changeset:
            changeset = self._read_by_name(csname, **kwargs)
        query = "UPDATE %s SET " % self._fname
        parms = []
        if owner:
            parms.append("owner='%s' " % owner)
        if description:
            parms.append("description='%s' " % description)
        if csname and changeset:
            parms.append("name='%s' " % csname)
        if parms:
            query += ', '.join(parms) + " WHERE referencedComponentId = '%s' " % changeset
            db = self.connect()
            db.execute_query(query)
            db.commit()
        return self.read(changeset=changeset, csname=csname, **kwargs)

    def isValid(self, changeset=None, csname=None, **kwargs):
        """ Determine whether the supplied changeset is valid in the given context
        @param changeset: uuid of changeset
        @param kwargs: contextual args
        @return: True if valid
        """
        changeset, csname = csorname(changeset, csname)
        return self.read(changeset=changeset, csname=csname, **kwargs) is not None

    changesetFiles = [(ConceptDB, 'nConcepts'),
                      (DescriptionDB, 'nDescriptions'),
                      (DescriptionTextDB, 'nDescTexts'),
                      (LanguageDB, 'nLanguages'),
                      (StatedRelationshipDB, 'nStatedRelationships'),
                      (RelationshipDB, 'nRelationships'),
                      (SimpleReferencesetDB, 'nSimpleRefsets'),
                      (ModuleDependencyDB, 'nModuleDependencies')]

    def rollback(self, changeset=None, csname=None, **kwargs):
        """ Roll back all of the changes identified in the supplied changeset. If the changeset isn't supplied or
        there is no record of it existing, the function returns success.  This function is always considered successful,
        and has no impact on records that aren't locked.
        @param changeset: uuid of changeset
        @param csname: name of the changeset
        @param kwargs: context
        @return: Count of things that are rolled back or None if error.  Call invalid_update_reason to find out why
        """
        changeset, csname = csorname(changeset, csname)
        rval = CountList()
        if self.invalid_update_reason(changeset=changeset, csname=csname, **kwargs):
            return None
        if csname and not changeset:
            changeset = self._read_by_name(csname, **kwargs)
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
        changeset, csname = csorname(changeset, csname)
        rval = CountList()
        if self.invalid_update_reason(changeset=changeset, csname=csname, **kwargs):
            return None
        if csname and not changeset:
            changeset = self._read_by_name(csname, **kwargs)
        if changeset:
            db = self.connect()
            for f, a in ChangeSetDB.changesetFiles:
                rval.setcount(a, f._commit(db, changeset, **kwargs)['affected_rows'])
                db.commit(False)
            rval.setcount('nChangesets', self._commit(db, changeset, **kwargs)['affected_rows'])
            db.commit()
        return rval

    @classmethod
    def _commit(cls, db, changeset, **_):
        fname = cls.fname()
        return db.execute_query("UPDATE %(fname)s SET locked=0, isFinal=1 WHERE changeset = '%(changeset)s'" % vars())

    def list(self, open=True, final=False, released=None, release=None, owner=None, ignore_locks=False, maxtoreturn=None, **kwargs):
        filtr = "TRUE "

        # Open changesets are necessarily locked.  Override the other setting
        if open:
            ignore_locks = True
        if open and not final:
            filtr += " AND isFinal = 0 "
        elif final and not open:
            filtr += " AND isFinal = 1 "
        elif not open and not final:
            # TODO: return nothing or an error message
            pass
        # TODO: redefine released so we can different
        if released is not None:
            filtr += "AND inRelease is " + ('not' if released else '') + " null "
        if release:
            filtr += "AND inRelease in (" + ','.join("'%s'" %r for r in listify(release)) + ") "
        if owner:
            filtr += "AND owner in (" + ','.join("'%s'" % r for r in listify(owner)) + ") "
        db = self.connect()
        db.execute(db.build_query(self._fname, filter_=filtr, ignore_locks=ignore_locks, maxtoreturn=maxtoreturn, **kwargs))
        return [RF2ChangeSetReferenceSetEntry(c) for c in db.ResultsGenerator(db)] \
            if maxtoreturn else list(db.ResultsGenerator(db))


    @classmethod
    def refsettype(cls, parms):
        return RF2ChangeSetReferenceSet(parms)
