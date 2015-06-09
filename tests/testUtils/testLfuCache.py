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

import unittest

from tests.SetConfig import setConfig
from rf2db.utils.lfu_cache import lfu_cache, clear_caches, cache_stats


class Foo():
    side_effect = "State 1"

    @lfu_cache(maxsize=10)
    def op1(self, a, b, c=1, d='foo', e=None, **kwargs):
        return str(a+b+c) + d + self.side_effect


class TestLFUCache(unittest.TestCase):
    def setUp(self):
        setConfig()

    def test_cache(self):
        t = Foo()
        self.assertEqual('111fooState 1', t.op1(10, 100))
        t.side_effect = "State 2"
        self.assertEqual('111fooState 1', t.op1(10, 100))
        self.assertEqual('111fooState 1', t.op1(10, 100, _nocache=False))
        self.assertEqual('111fooState 2', t.op1(10, 100, _nocache=True))
        clear_caches(clear_counts=True)

    def test_parameters(self):
        t = Foo()
        z = Foo()
        self.assertEqual('222barState 1', (t.op1(2, 20, c=200, d='bar', fie=z)))
        t.side_effect = "State 2"
        self.assertEqual('222barState 1', (t.op1(2, 20, c=200, d='bar', fie=z)))
        z = Foo()
        self.assertEqual('222barState 2', (t.op1(2, 20, c=200, d='bar', fie=z)))
        clear_caches(clear_counts=True)

    def test_clear(self):
        t = Foo()
        z = Foo()
        self.assertEqual('222barState 1', (t.op1(2, 20, c=200, d='bar', fie=z)))
        t.side_effect = "State 2"
        self.assertEqual('222barState 1', (t.op1(2, 20, c=200, d='bar', fie=z)))
        clear_caches()
        self.assertEqual('222barState 2', (t.op1(2, 20, c=200, d='bar', fie=z)))
        clear_caches(clear_counts=True)

    def test_stats(self):
        t = Foo()
        self.assertEqual(cache_stats(), [0, 0, 0])
        t.op1(2, 20, c=200, d='bar')
        self.assertEqual(cache_stats(), [0, 1, 0])
        t.op1(2, 20, c=200, d='bar')
        self.assertEqual(cache_stats(), [1, 1, 0])
        list(t.op1(i, i*10) for i in range(0, 20))
        self.assertEqual(cache_stats(), [1, 21, 0])
        list(t.op1(i, i*10) for i in range(0, 20))
        self.assertEqual(cache_stats(), [9, 33, 0])
        list(t.op1(i, i*10) for i in range(0, 20))
        self.assertEqual(cache_stats(), [17, 45, 0])
        t.op1(2, 20, c=200, d='bar')
        self.assertEqual(cache_stats(), [18, 45, 0])
        t.op1(2, 20, c=200, d='bar', _nocache=True)
        self.assertEqual(cache_stats(), [18, 46, 1])
        t.op1(2, 20, c=200, d='bar')
        self.assertEqual(cache_stats(), [19, 46, 1])
        clear_caches(clear_counts=True)

if __name__ == '__main__':
    unittest.main()
