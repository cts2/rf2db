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

""" RF2 Language Refset access routines
"""

from rf2db.parsers.RF2RefsetParser import RF2LanguageRefsetEntry
from rf2db.parsers.RF2Iterator import RF2LanguageReferenceSet, iter_parms
from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms
from rf2db.utils.lfu_cache import lfu_cache
from rf2db.parameterparser.ParmParser import ParameterDefinitionList

""" Parameters for language file access """
language_parms = global_rf2_parms
language_list_parms = ParameterDefinitionList(global_rf2_parms)
language_list_parms.add(iter_parms)


class LanguageDB(RF2FileWrapper):
    directory   = 'Refset/Language'
    prefixes    = ['der2_cRefset_Language']
    table       = 'language'
    
    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
      id char(36) COLLATE utf8_bin NOT NULL,
      effectiveTime int(11) NOT NULL,
      active tinyint(1) NOT NULL,
      moduleId bigint(20) NOT NULL,
      refsetId bigint(20) NOT NULL,
      referencedComponentId bigint(20) NOT NULL,
      acceptabilityId bigint(20) NOT NULL,
      conceptId bigint(20) DEFAULT 0,
      KEY component (referencedComponentId),
      KEY conceptId (conceptId),
       %(primkey)s ); """

    updateSTMT = """UPDATE %(table)s l
        INNER JOIN description_ss d
        ON d.id = l.referencedcomponentid
        SET l.conceptid = d.conceptid"""
    
    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)

    def loadTable(self, rf2file, ss, cfg):
        from rf2db.db.RF2DescriptionFile import DescriptionDB
        if not DescriptionDB().hascontent(ss):
            print("Description database must be loaded before loading %s" % self._tname(ss))
            return

        import warnings
        warnings.filterwarnings("ignore", ".*doesn't contain data for all columns.*")
        super(LanguageDB,self).loadTable(rf2file,ss,cfg)
        db = self.connect()
        db.execute(self.updateSTMT % {'table':self._tname(ss)})
        db.commit()


    @lfu_cache(maxsize=100)
    def get_entries_for_description(self, descId, parmlist):
        db = self.connect()
        return [RF2LanguageRefsetEntry(d) for d in db.query_p(self._tname(parmlist.ss), parmlist, "referencedComponentId = %s" % descId)]


    @lfu_cache(maxsize=20)
    def get_entries_for_concept(self, conceptId, parmlist):
        db = self.connect()
        return [RF2LanguageRefsetEntry(d) for d in db.query_p(self._tname(parmlist.ss), parmlist, "conceptId = %s" % conceptId)]

    @staticmethod
    def as_reference_set(llist, parmlist):
        thelist=RF2LanguageReferenceSet(parmlist)
        if not parmlist.maxtoreturn:
            return thelist.finish(True, total=list(llist)[0])
        for l in llist:
            if thelist.at_end:
                return thelist.finish(True)
            thelist.append(l)
        return thelist.finish(False)
