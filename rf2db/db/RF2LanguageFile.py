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

from rf2db.parsers.RF2RefsetParser import RF2LanguageRefsetEntry
from rf2db.parsers.RF2Iterator import RF2LanguageReferenceSet, iter_parms
from rf2db.db.RF2FileCommon import global_rf2_parms
from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper
from rf2db.db.RF2DescriptionFile import DescriptionDB
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.utils.listutils import listify
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, enumparam
from rf2db.constants.RF2ValueSets import us_english, gb_english, spanish, preferred, synonym

# Note: the following gyrations are needed because the language file is used to build other refset names, so
#       it can't actually depend on the RF2RefsetWrapper


# Parameters for language file access
language_parms = global_rf2_parms

language_list_parms = ParameterDefinitionList(global_rf2_parms)
language_list_parms.add(iter_parms)
language_list_parms.language = enumparam(['en'])

""" Map from short form of language to refset id """
language_map = {'en': us_english,
                'en-us': us_english,
                'en-gb': gb_english,
                'es': spanish}


class LanguageDB(RF2RefsetWrapper):
    directory = 'Refset/Language'
    prefixes = ['der2_cRefset_Language']
    table = 'language'

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      acceptabilityId bigint(20) NOT NULL,
      conceptId bigint(20) DEFAULT 0,
      KEY concept (conceptId) USING BTREE,
       %(keys)s ); """

    updateSTMT = """UPDATE %(table)s l
        INNER JOIN description_ss d
        ON d.id = l.referencedcomponentid
        SET l.conceptid = d.conceptid"""

    descdb = DescriptionDB()

    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

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
        db.execute(self.updateSTMT % {'table': self._fname})
        db.commit()

    @staticmethod
    def _langfltr(fltr, language=None, **kwargs):
        return (fltr + " AND refsetId=%s " % language_map[language]) if (language and language in language_map) else fltr

    @lfu_cache(maxsize=100)
    def get_entries_for_description(self, descId, **kwargs):
        db = self.connect()
        return [RF2LanguageRefsetEntry(d) for d in db.query(self._fname,
                                                            self._langfltr(
                                                                  "referencedComponentId = %s" % descId, **kwargs),
                                                              **kwargs)]


    @lfu_cache(maxsize=20)
    def get_entries_for_concept(self, conceptId, **kwargs):
        db = self.connect()
        return [RF2LanguageRefsetEntry(d) for d in db.query(self._fname,
                                                            self._langfltr("conceptId = %s" % conceptId, **kwargs),
                                                            **kwargs)]

    # This can't be cached because it returns a list...
    def preferred_term_for_concepts(self, conceptIds, language='en', active=True, moduleid=[], **kwargs):
        """ Return a list of concept id to prefname/desc id.  Note: If you just want the PN or FSN, use RF2PnAndFSN instead

        @param conceptIds: concept id(s) too lookup
        @param language: limit language
        @param parmlist: parameters.  We use active, moduleid, language.
        @return: dictionary - key is concept id, value is (prefname/description id) tuple
        """
        db = self.connect()
        conceptIds = listify(conceptIds)
        stmt = "SELECT l.conceptId, d.id, d.term FROM %s l, %s d WHERE l.conceptId IN(%s) AND l.referencedComponentId = d.id " \
               "AND l.acceptabilityId = %s AND d.typeid = %s" % \
               (self._fname,
                self.descdb.fname(),
                ', '.join(str(c) for c in conceptIds),
                preferred,
                synonym)
        stmt += ' AND l.active=1 AND d.active=1' if active else 'True '
        if moduleid:
            stmt += "AND moduleId in (" + ', '.join(str(m) for m in moduleid)
        stmt += self._langfltr('', language=language **kwargs)
        db.execute(stmt)
        return {e[0]: (e[2], e[1]) for e in map(lambda r: r.split('\t', 2), db.ResultsGenerator(db))}


    @staticmethod
    def as_reference_set(llist, maxtoreturn=None, **kwargs):
        thelist = RF2LanguageReferenceSet(maxtoreturn=maxtoreturn, **kwargs)
        if maxtoreturn == 0:
            return thelist.finish(True, total=list(llist)[0])
        for l in llist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.add_entry(l)
        return thelist.finish(False)


