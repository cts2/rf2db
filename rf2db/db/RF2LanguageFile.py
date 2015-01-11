# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
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

""" RF2 Language Refset access routines
"""
import uuid

from rf2db.parsers.RF2RefsetParser import RF2LanguageRefsetEntry
from rf2db.parsers.RF2Iterator import RF2LanguageReferenceSet, iter_parms
from rf2db.db.RF2FileCommon import global_rf2_parms
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper, global_refset_parms
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, enumparam, sctidparam
from rf2db.constants.RF2ValueSets import us_english, gb_english, spanish, preferred, synonym

# Note: the following gyrations are needed because the language file is used to build other refset names, so
#       it can't actually depend on the RF2RefsetWrapper


# Parameters for language file access
language_parms = global_refset_parms

language_list_parms = ParameterDefinitionList(global_rf2_parms)
language_list_parms.add(iter_parms)
language_list_parms.language = enumparam(['en'])

language_concept_parms = ParameterDefinitionList(language_list_parms)
language_concept_parms.concept = sctidparam()

language_desc_parms = ParameterDefinitionList(language_list_parms)
language_desc_parms.desc = sctidparam()

""" Map from short form of language to refset id """
language_map = {'en': us_english,
                'en-us': us_english,
                'en-gb': gb_english,
                'es': spanish}


class LanguageDB(RF2RefsetWrapper):
    directory = 'Refset/Language'
    prefixes = ['der2_cRefset_Language']
    table = 'language'

    _wrapper_cls = lambda self, e: RF2LanguageRefsetEntry(e)

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      acceptabilityId bigint(20) NOT NULL,
      conceptId bigint(20) DEFAULT 0,
      KEY concept (conceptId) USING BTREE,
      KEY rcc (referencedComponentId, conceptId) USING BTREE,
       %(keys)s ); """

    updateSTMT = """UPDATE %(table)s l
        INNER JOIN %(desctbl)s d
        ON d.id = l.referencedcomponentid
        SET l.conceptid = d.conceptid"""


    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    hasrf2rec = True
    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2LanguageRefsetEntry(*args, **kwargs)

    # We have to override the refset wrapper because the call would be recursive otherwise
    def _build_knowns(self, language):
        self._known_refsets = self.valid_refsets(self._fname)
        self._refset_names = {k: v[0] for k, v in self.preferred_term_for_concepts(self._known_refsets.items(),
                                                                                   language=language)}
        for k, v in list(language_map.items()):
            if v not in self._known_refsets:
                language_map.pop(k)

    def loadTable(self, rf2file):
        from rf2db.db.RF2DescriptionFile import DescriptionDB
        if not DescriptionDB().hascontent():
            print("Description database must be loaded before loading %s" % self._fname)
            return

        import warnings

        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(LanguageDB, self).loadTable(rf2file)
        db = self.connect()
        print("\t...adding concept identifiers")
        db.execute(self.updateSTMT % {'table': self._fname, 'desctbl': DescriptionDB.fname()})
        db.commit()

    @staticmethod
    def _langfltr(fltr, language=None, **kwargs):
        return (fltr + " AND refsetId=%s " % language_map[language]) if (language and language in language_map) else fltr


    @lfu_cache(maxsize=100)
    def get_entries_for_description(self, desc=None, maxtoreturn=None, **kwargs):
        db = self.connect()
        db.execute(db.build_query(self._fname,
                                  filter_=self._langfltr(
                                        "referencedComponentId = %s" % desc, **kwargs),
                                  maxtoreturn=maxtoreturn, **kwargs))
        return [RF2LanguageRefsetEntry(d) for d in db.ResultsGenerator(db)] if maxtoreturn \
            else list(db.ResultsGenerator(db))


    @lfu_cache(maxsize=20)
    def get_entries_for_concept(self, concept=None, maxtoreturn=None, **kwargs):
        db = self.connect()
        db.execute(db.build_query(self._fname,
                                  filter_=self._langfltr("conceptId = %s" % concept, **kwargs),
                                  maxtoreturn=maxtoreturn, **kwargs))
        return [RF2LanguageRefsetEntry(d) for d in db.ResultsGenerator(db)] if maxtoreturn \
            else list(db.ResultsGenerator(db))

    @lfu_cache()
    def preferred_term_for_concepts(self, conceptids, language='en', active=True, moduleid=None, **kwargs):
        """ Return a list of concept id to prefname/desc id.  Note: If you just want the PN or FSN, use RF2PnAndFSN instead

        @param conceptids: concept id(s) too lookup
        @param language: limit language
        @param parmlist: parameters.  We use active, moduleid, language.
        @return: dictionary - key is concept id, value is (prefname/description id) tuple
        """
        from rf2db.db.RF2DescriptionFile import DescriptionDB
        db = self.connect()
        conceptids = listify(conceptids)
        stmt = "SELECT l.conceptId, d.id, d.term FROM %s l, %s d " \
               "WHERE l.conceptId IN (%s) AND l.referencedComponentId = d.id " \
               "AND l.acceptabilityId = %s AND d.typeid = %s" % \
               (self._fname,
                DescriptionDB.fname(),
                ', '.join(str(c) for c in conceptids),
                preferred,
                synonym)
        if active:
            stmt += ' AND l.active=1 '
        if moduleid:
            stmt += " AND d.moduleId in (" + ', '.join(str(m) for m in listify(moduleid)) + ") "
        stmt += self._langfltr('', language=language, **kwargs)
        db.execute(stmt)
        return {e[0]: (e[2], e[1]) for e in map(lambda r: r.split('\t', 2), db.ResultsGenerator(db))}

    def add(self, db, effectivetime, moduleid, language, descid, acceptabilityid, concept,  changeset, **kwargs):
        """ Add a new language entry.  It is assumed that this function is invoked from the DescriptionDB
             and the parameters have all been validated.
        @param db: database to insert the entry into
        @param effectivetime: timestamp
        @param moduleid: module identifier
        @param language: the language name ("en", "en-gb", "es", etc.)
        @param descid: description identifier
        @param acceptibilityid: acceptibilityid id
        @param concept: reference concept (not an RF2 parameter)
        @param changeset: change set identifier
        """
        id = str(uuid.uuid4())
        fname = self._fname
        refsetid = language_map.get(language, None)
        if not refsetid:
            raise Exception("Unknown language code: %s" % language)
        db.execute_query("INSERT INTO %(fname)s (id, effectiveTime, active, moduleId, "
                         "refsetId, referencedComponentId, acceptabilityId, conceptId, changeset, locked) "
                         "VALUES ('%(id)s', %(effectivetime)s, 1, %(moduleid)s, "
                         "%(refsetid)s, %(descid)s, %(acceptabilityid)s, %(concept)s, '%(changeset)s', 1)" % vars())
        db.commit()



    @classmethod
    def refsettype(cls, parms):
        return RF2LanguageReferenceSet(parms)