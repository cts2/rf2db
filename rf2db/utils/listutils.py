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
import collections
import sys

if sys.version_info.major > 2:
    basestring = str

def to_str(item):
    return bytearray.decode(item) if isinstance(item, bytearray) else str(item)

def listify(item, default=None, itemlen=0):
    """ 
    Convert C{item} to a list if it isn't one already
    
    @param item: thing to be converted to a list if it isn't already
    @type item: any

    @param default: default value if not supplied
    @type default: any

    @param itemlen: minimum number of elements to return.
    @type itemlen: int
    """
    if not item:
        item = default
    if not isinstance(item, (list, tuple)):
        item = [item]
    return list(item) + ([default] * max(itemlen - len(item), 0))

def isList(possible_list):
    return isinstance(possible_list, collections.Iterable) and not isinstance(possible_list, basestring)

def flatten(possible_list):
    """ Flatten a list by one level.

    >>> flatten(None)

    >>> flatten([])
    []

    >>> flatten([None])
    [None]

    >>> flatten("abc")
    'abc'

    >>> flatten([1,2,3])
    [1, 2, 3]

    >>> flatten([[1,2],[3,4,[5]]])
    [1, 2, 3, 4, [5]]

    @param possible_list: the list to be flattened.
    @return: flattening
    """
    def flatten_(pl):
        if isList(pl):
            for e in pl:
                if isList(e):
                    for e1 in e:
                        yield e1
                else:
                    yield e
        else:
            yield pl

    return list(flatten_(possible_list)) if isList(possible_list) else possible_list

