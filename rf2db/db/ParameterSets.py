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
from rf2db.utils.ParmParser import KwParms
#from rf2db.db.RF2ModuleVersionsFile import ModuleVersionsDB

#mvdb = ModuleVersionsDB()

class base_parms(object):
    """ Baseline parameters that control what is retrieved
    """
    def __init__(self, **kwargs):
        self._p = KwParms(**kwargs)
        self.ss = True
        self.active = self._p.bool('active', True)
        mods = self._p.sctid('moduleid')
        self.moduleids = str(mods).split() if mods else None

    # TODO: Get the validate calls into the routines
    def validate(self):
        #if not mvdb.validModuleids(self.moduleids):
        #   return False, ' '.join(filter(lambda m: not mvdb.getModuleid(m),self.moduleids))
        return True,''


orders = ['asc', 'desc']

class iter_parms(base_parms):
    """ Parameters that controle list iteration
    """
    def __init__(self, **kwargs):
        base_parms.__init__(self, **kwargs)
        self.page = self._p.int('page', 0)
        self.maxtoreturn = self._p.int('maxtoreturn', 100)
        self.start = self.page * self.maxtoreturn
        self.order = self._p.enum('order', orders)

    def validate(self):
        return base_parms.validate(self)