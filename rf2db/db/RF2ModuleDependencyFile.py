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
# Redistributions in binary form must reproduce the above copyright notice,
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

""" RF2 ModuleDependency reference file
"""

from rf2db.db.RF2RefsetWrapper import RF2RefsetWrapper, global_refset_parms
from rf2db.parsers.RF2RefsetParser import RF2ModuleDependencyReferenceSetEntry


class ModuleDependencyDB(RF2RefsetWrapper):
    directory = 'Refset/Metadata'
    prefixes = ['der2_ssRefset_ModuleDependency']
    table = 'moduleDependency'

    _wrapper_cls = lambda self, e: RF2ModuleDependencyReferenceSetEntry(e)

    createSTMT = """CREATE TABLE IF NOT EXISTS %(table)s (
     %(base)s,
      sourceEffectiveTime int(11) NOT NULL,
      targetEffectiveTime int(11) NOT NULL,
      %(keys)s );"""


    def __init__(self, *args, **kwargs):
        RF2RefsetWrapper.__init__(self, *args, **kwargs)

    hasrf2rec = True

    @classmethod
    def rf2rec(cls, *args, **kwargs):
        return RF2ModuleDependencyReferenceSetEntry(*args, **kwargs)









