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

from rf2db.utils.SCTID import SCTID

def boolparam(p, default=False):
    if p is None: return default
    if str(p).lower() in ['y','yes','true', '1', 'on']: return True
    if str(p).lower() in ['n', 'no','false', '0', 'off']: return False
    return None

def intparam(p, default=0):
    if p is None: p = default
    return int(p)

class KwParms(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def bool(self, arg, default=True):
        return boolparam(self._kwargs.get(arg), default)

    def int(self, arg, default=0):
        return intparam(self._kwargs.get(arg), default)

    def str(self, arg, default=None):
        return self._kwargs.get(arg, default)

    def sctid(self, arg, default=None):
        id = self._kwargs.get(arg, default)
        if id and SCTID.isValid(id):
            return SCTID(id)
        return None

    def enum(self, arg, list, default=None):
        rval = self._kwargs.get(arg, default if default else list[0]).lower()
        return rval if rval in list else None

    def __getattr__(self, item):
        return self.__dict__[item] if item.startswith('_') else self._kwargs.get(item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
