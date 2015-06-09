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

import functools
import collections
from heapq import nsmallest
from operator import itemgetter

from rf2db.db.RF2DBConnection import db_values
from rf2db.parameterparser.ParmParser import booleanparam

class Counter(dict):
    """Dictionary where default values are zero"""
    def __missing__(self, key):
        return 0


class Cache():
    kwd_mark = object()     # separate positional and keyword args

    def __init__(self, maxsize=100):
        self.maxsize = maxsize
        self.cache = {}
        self.use_count = Counter()
        self.hits = self.misses = self.bypasses = self.resets = 0

    def clear(self, clear_counts=False):
        """ Clear all caches
        @param clear_counts: Reset counts.  Primarily testing.
        """
        self.cache.clear()
        self.use_count.clear()
        self.resets += 1
        if clear_counts:
            self.hits = self.misses = self.bypasses = 0

    def stats(self):
        return self.hits, self.misses, self.bypasses

all_caches = []


def clear_caches(clear_counts=False):
    list(c.clear(clear_counts) for c in all_caches)


def sum_tuples(t):
    if not t:
        return 0,
    return functools.reduce(lambda a, b: list(map(lambda e: e[0] + e[1], zip(a, b))), t, [0] * len(t[0]))


def cache_stats():
    l = list(c.stats() for c in all_caches)
    return sum_tuples(l)

def lfu_cache(maxsize=100):
    """Least-frequenty-used cache decorator.

    Arguments to the cached function must be hashable.
    Cache performance statistics stored in f.hits and f.misses.
    Clear the cache with f.clear().
    http://en.wikipedia.org/wiki/Least_Frequently_Used

    @param maxsize: maximum cache size
    @type maxsize: C{int}

    """

    def decorating_function(user_function):
        cache = Cache(maxsize)

        @functools.wraps(user_function)
        def wrapper(*args, **kwargs):
            if booleanparam.v(db_values.nocache, False):
                return user_function(*args, **kwargs)
            key = tuple(tuple(e) if isinstance(e, list) else e for e in args[1:])
            kwkey = tuple(sorted((k, v if isinstance(v, collections.Hashable) else str(v))
                                 for k, v in kwargs.items()  if not k.startswith('_')))
            if kwkey:
                key += (Cache.kwd_mark,) + kwkey
            # Refresh the cache if needed
            if kwargs.pop('_nocache', False):
                cache.cache.pop(key, None)
                cache.bypasses += 1
            # get cache entry or compute if not found
            try:
                result = cache.cache[key]
                cache.use_count[key] += 1
                cache.hits += 1
            except KeyError:
                # need to add something to the cache, make room if necessary
                if len(cache.cache) == cache.maxsize:
                    for k, _ in nsmallest(cache.maxsize // 10 or 1,
                                            cache.use_count.items(),
                                            key=itemgetter(1)):
                        del cache.cache[k], cache.use_count[k]
                cache.cache[key] = user_function(*args, **kwargs)
                result = cache.cache[key]
                cache.use_count[key] += 1
                cache.misses += 1
            return result

        wrapper.cache = cache
        all_caches.append(cache)
        return wrapper

    return decorating_function