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
import sys
import check_digit


class sctid(object):
    """ sctid wrapper - exists because sctid's wander through this module sometimes as longs and
        sometimes as strings.  This makes sure that long and strings compare.
    """
    def __init__(self, value):
        assert self.isValid(value), "Invalid sctid: " + str(value)
        self._value = long(value) if sys.version_info.major < 3 else int(value)

    @staticmethod
    def isValid(sctid):
        """ Determine whether the expression is a legitimate sctid """
        if len(str(sctid)) == 0:
            return False
        try:
            return check_digit.validate_verhoeff(sctid)
        except ValueError:
            return False

    def __hash__(self):
        return self._value.__hash__()

    def __eq__(self, that):
        return long(that) == self._value


    def __ne__(self, that):
        return long(that) != self._value
    
    def __str__(self):
        return str(self._value)
    
    def __add__(self, other):
        return str(self) + other
    
    def __radd__(self, other):
        return other + str(self)

    def __long__(self):
        return self._value

    def __int__(self):
        return int(self._value)
    
    def __repr__(self):
        return str(self._value)
