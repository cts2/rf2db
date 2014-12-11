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

""" RF2 Description File Access Routines
"""
import re

from rf2db.parsers.RF2BaseParser import RF2Description
from rf2db.parsers.RF2Iterator import RF2DescriptionList, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms
from rf2db.utils.lfu_cache import lfu_cache, clear_caches
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, sctidparam, intparam, enumparam, strparam
from rf2db.constants.RF2ValueSets import definition, fsn, synonym, initialChar, preferred, acceptable, us_english, \
    gb_english, spanish
from rf2db.db.RF2DBConnection import cp_values
from rf2db.db.RF2LanguageFile import LanguageDB
from rf2db.constants.RF2ValueSets import fsn
import rf2db.utils.lfu_cache

# Parameters for description access
description_parms = ParameterDefinitionList(global_rf2_parms)
description_parms.desc = sctidparam()

fsn_parms = ParameterDefinitionList(global_rf2_parms)
fsn_parms.language = enumparam(['en', 'es', 'de'], default='en')
fsn_parms.concept = sctidparam()

base_parms = fsn_parms

description_list_parms = ParameterDefinitionList(global_rf2_parms)
description_list_parms.add(iter_parms)

pref_description_parms = ParameterDefinitionList(global_rf2_parms)
pref_description_parms.concept = sctidparam()

description_for_concept_parms = ParameterDefinitionList(global_rf2_parms)
description_for_concept_parms.add(iter_parms)
description_for_concept_parms.concept = sctidparam()

new_description_parms = ParameterDefinitionList(global_rf2_parms)
new_description_parms.concept = sctidparam()
new_description_parms.descid = sctidparam()
new_description_parms.effectiveTime = intparam()
new_description_parms.language = enumparam(['en', 'es', 'de'], default='en')
new_description_parms.type = enumparam(['d', 'f', 'p', 's'], default='p')
new_description_parms.term = strparam(splittable=False)

update_description_parms = ParameterDefinitionList(global_rf2_parms)
update_description_parms.language = enumparam(['en', 'es', 'de'])
update_description_parms.type = enumparam(['d', 'f', 's'])
update_description_parms.term = strparam(splittable=False)

delete_description_parms = ParameterDefinitionList(global_rf2_parms)

    
class DescriptionDB(RF2FileWrapper):
     
    directory = 'Terminology'
    prefixes  = ['sct2_Description_', 'sct2_TextDefinition_']
    table = 'description'

    idGenerator = None
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      conceptId bigint(20) NOT NULL,
      languageCode varchar(10) COLLATE utf8_bin NOT NULL,
      typeId bigint(20) NOT NULL,
      term text(16384) CHARACTER SET utf8 NOT NULL,
      caseSignificanceId bigint(20) NOT NULL,
      KEY concept (conceptId) USING BTREE,
       %(keys)s ); """
    
    def __init__(self, *args, **kwargs): 
        RF2FileWrapper.__init__(self, *args, **kwargs)
        self._descTextDB = None
        self._concDB = None

    hasrf2rec = True
    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2Description(*args, **kwargs)
    
    @lfu_cache(maxsize=100)
    def getConceptDescription(self, conceptId, maxtoreturn=None, **kwargs):
        db = self.connect()
        rval = db.query(self._fname, filter_="conceptId = %s" % conceptId, maxtoreturn=maxtoreturn, **kwargs)
        return [RF2Description(d) for d in rval] if maxtoreturn != 0 else list(rval)

    def getConceptIdForDescription(self, descId, **kwargs):
        rlist = self.read(descId, **kwargs)
        return str(rlist.conceptId) if rlist else None

    @lfu_cache(maxsize=20)
    def read(self, descid, **kwargs):
        db = self.connect()
        return db.singleton_query(self._fname, RF2Description, filter_="id = %s" % descid, **kwargs)

    def _doupdate(self, descid, changeset, languagecode, typeid, term, effectivetime=None, **kwargs):
        """ Helper function to update a concept record
        @param cid: concept id to update
        @param changeset: changeset
        @param effectivetime: new effective time
        @param definitionstatusid: new definition status is not empty
        @param kwargs: context
        """
        fname = self._fname
        effectivetime, _ = self.effectivetime_and_moduleid(effectivetime, None)
        query = "UPDATE %(fname)s SET effectiveTime=%(effectivetime)s, "
        query += "languageCode='%(languagecode)s', typeId=%(typeid)s, term='%(term)s' "
        query += "WHERE id=%(descid)s AND changeset='%(changeset)s' AND locked=1"
        db = self.connect()
        db.execute_query(query % vars(), **kwargs)
        db.commit()
        clear_caches()

    def fsn(self, concept=None, language='en', changeset=None, **kwargs):
        if not self.validconcept(concept, changeset, **kwargs):
            return "Unrecognized concept identifier: %s" % concept
        db = self.connect()
        typ = fsn
        filter_ = "conceptId=%(concept)s AND languageCode='%(language)s' AND typeId=%(typ)s" % vars()
        return db.singleton_query(self._fname, RF2Description, filter_=filter_, **kwargs)

    def base(self, **kwargs):
        """ Return the bit for the concept that constructs the root FSN
        @param concept: concept to look up
        @param kwargs:
        @return:
        """
        descrec = self.fsn(**kwargs)
        if descrec:
            return re.sub(r'.*(\(.*\))\s*$','\\1', descrec.term, flags=re.MULTILINE)
        return None

    def add(self, changeset, concept=None, descid=None, effectivetime=None,
            moduleid=None, language='en', type='p', term='', **kwargs):
        """ Add a new description / language refset entry
        @param changeset: Changeset identifier.
        @type changeset: UUID
        @param concept: concept identifier for description
        @param descid: description identifier.  Default: next description id in server namespace
        @param effectivetime: Timestamp for record.  Default: today's date
        @param moduleid: owning module.  Default: service module (ep_values.moduleId)
        @param language: list of languages.  default: ['en']
        @param type: 'd', 'f', 's', 'p' (definition, fsn, synonym, preferred). Default: Preferred
        @param term: actual description
        @return: Description record or none if error.
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)
        if not self.validconcept(concept, changeset, **kwargs):
            return "Unrecognized concept identifier: %s" % concept
        term = term.strip()
        if not term:
            return "Nonblank term must be supplied"
        from rf2db.db.RF2DescriptionTextFile import DescriptionTextDB
        db = self.connect()
        if not descid:
            descid = self.newdescriptionid()
        language = language.lower()
        typeid = definition if type == 'd' else fsn if type == 'f' else synonym
        effectivetime, moduleid = self.effectivetime_and_moduleid(effectivetime, moduleid)
        fname = self._fname
        csig = initialChar
        db.execute_query("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, "
                   "conceptId, languageCode, typeId, term, caseSignificanceId, changeset, locked) "
                   "VALUES (%(descid)s, %(effectivetime)s, 1, %(moduleid)s, "
                   "%(concept)s, '%(language)s', %(typeid)s, '%(term)s', %(csig)s, '%(changeset)s', 1 )" % vars())
        fname = DescriptionTextDB.fname()
        db.execute_query("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, "
                   "conceptId, languageCode, typeId, term, caseSignificanceId, changeset, locked) "
                   "VALUES (%(descid)s, %(effectivetime)s, 1, %(moduleid)s, "
                   "%(concept)s, '%(language)s', %(typeid)s, '%(term)s', %(csig)s, '%(changeset)s', 1 )" % vars())
        if (type == 'p' or type == 's') and language in ('en'):
            acc = preferred if type == 'p' else acceptable
            # TODO: There is already a language map on the language side.  This code id redundant
            if language == 'en':
                # 'en' means the same in both languages
                LanguageDB().add(db, effectivetime, moduleid, us_english, descid, acc, concept,  changeset, **kwargs)
                LanguageDB().add(db, effectivetime, moduleid, gb_english, descid, acc, concept,  changeset, **kwargs)
            elif language == 'en-gb':
                LanguageDB().add(db, effectivetime, moduleid, gb_english, descid, acc, concept,  changeset, **kwargs)
            elif language == 'en-us':
                LanguageDB().add(db, effectivetime, moduleid, gb_english, descid, acc, concept,  changeset, **kwargs)
            elif language == 'es':
                LanguageDB().add(db, effectivetime, moduleid, spanish, descid, acc, concept,  changeset, **kwargs)
            else:
                return "Unknown language code: %s" % language
        db.commit()
        clear_caches()
        return self.read(descid, changeset=changeset, **kwargs)

    # TODO: allow case significance add and update
    def update(self, desc, changeset=None, language=None, type=None, term=None, **kwargs):
        """ Update an existing concept record
        @param desc: description identifier.
        @param changeset: containing changeset
        @param language: language.  Default: 'en'
        @param type: 'd', 'f', 's' (definition, fsn, synonym). Default: Synonym
        @param term: actual description
        @param kwargs: context
        @return: new record if update successful, otherwise an error message.
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)
        current_value = self.read(desc, changeset=changeset, **kwargs)
        if not current_value:
            return "UnknownEntity - description not found"
        if term is not None:
            term = term.strip() if term is not None else current_value.term
        typeid = current_value.typeId if type is None else definition if type == 'd' else fsn if type == 'f' else synonym
        language = current_value.languageCode if language is None else language
        changed = current_value.typeId != typeid or current_value.term != term or current_value.languageCode != language

        if not current_value.locked:
            if current_value.changeset != changeset or changed:
                if cp_values.ss:
                    return "Description: Cannot update an existing snapshot record"
                else:
                    return "Description: Full record update is not implemented"
            else:
                return current_value
        else:
            if current_value.changeset == changeset:
                if cp_values.ss:
                    self._doupdate(desc, changeset, language, typeid, term, **kwargs)
                    clear_caches()
                    return self.read(desc, _nocache=True, changeset=changeset, **kwargs)
                else:
                    return "Description: Full record update is not implemented"
            else:
                return "Description: Record is locked under a different changeset"


    def delete(self, desc, changeset=None, **kwargs):
        """ Delete or deactivate a description
        @param desc: description identifier
        @param changeset: containing changeset
        @param kwargs: context
        @return: None if success otherwise an error message
        """
        if not self.changesetisvalid(changeset):
            return self.changeseterror(changeset)

        # delete is idempotent, so if we can't find it or it is already gone claim success
        kwargs['active'] = 0        # read even if inactive
        current_value = self.read(desc, **kwargs)
        if not current_value or not current_value.isActive():
            return None

        if not current_value.locked:
            if cp_values.ss:
                return "Cannot delete committed descriptions in a snapshot database"
            else:
                return "Description: Full record delete is not implemented"
        else:
            if current_value.changeset == changeset:
                db = self.connect()
                db.execute_query("DELETE FROM %(fname)s WHERE id=%(desc)s AND changeset='%(changeset)s' AND locked=1" % vars())
                db.commit()
                clear_caches()
                return None
            else:
                return "Description: Record is locked under a different changeset"

    @classmethod
    def refsettype(cls, parms):
        return RF2DescriptionList(parms)

