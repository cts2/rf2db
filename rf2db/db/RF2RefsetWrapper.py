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

from rf2db.db.RF2FileCommon import RF2FileWrapper, global_rf2_parms
from rf2db.db.RF2DBConnection import RF2DBConnection
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, strparam

global_refset_parms = ParameterDefinitionList(global_rf2_parms)
global_refset_parms.uuid = strparam()

class RF2RefsetWrapper(RF2FileWrapper):

    _file_base_ = '''id char(36) COLLATE utf8_bin NOT NULL,
effectiveTime int(11) NOT NULL,
active tinyint(1) NOT NULL,
moduleId bigint(20) NOT NULL,
refsetId bigint(20) NOT NULL,'''
    _file_base = _file_base_ + '''
referencedComponentId bigint(20) NOT NULL '''

    _wrapper_keys = '''KEY ars (active, refsetId),
KEY rac (refsetId, referencedComponentId),
KEY refset (refsetId),
KEY component (referencedComponentId)'''

    _keys_ss = RF2FileWrapper._keys_ss + ',' + _wrapper_keys
    _keys_full = RF2FileWrapper._keys_full + ',' + _wrapper_keys

    _wrapper_cls = None

    def __init__(self, *args, **kwargs):
        RF2FileWrapper.__init__(self, *args, **kwargs)
        self._known_refsets = None
        self._refset_names = None

    def known_refsets(self, language='en', refresh=False):
        if not self._known_refsets or refresh:
            self._build_knowns(language)
        return self._known_refsets

    def refset_names(self, language='en', refresh=False):
        if not self._refset_names or refresh:
            self._build_knowns(language)
        return self._refset_names

    def _build_knowns(self, language):
        # Note: LanguageDB must be local, as it inherits from this class
        self._known_refsets = self.valid_refsets(self._fname)
        from rf2db.db.RF2LanguageFile import LanguageDB
        self._refset_names = {k:v[0] for k,v in LanguageDB().preferred_term_for_concepts(self._known_refsets,
                                                                                         language=language).items()}

    def read(self, uuid=None, **kwargs):
        """
        Read the language record
        @param uuid: language refset id
        @return: language record if found else None
        """
        db = self.connect()
        # TODO: Sanitize uuid (!)
        return db.singleton_query(self._fname, self._wrapper_cls, filter_="id='%s'" % uuid, **kwargs)

    def valid_refsets(self, active=True, moduleids=None):
        stmt = "SELECT DISTINCT refsetId FROM %s WHERE " % self._fname
        stmt += 'active=1 ' if active else 'True '
        if moduleids:
            stmt += "AND moduleId in (" + ', '.join(str(m) for m in moduleids)
        db = RF2DBConnection()
        db.execute(stmt)
        return list(db.ResultsGenerator(db))


