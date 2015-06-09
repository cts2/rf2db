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

import unittest
from rf2db.utils.sctid_generator import *
from rf2db.utils.sctid import sctid


class GeneratorTestCase(unittest.TestCase):
    def test_gen(self):
        generator = sctid_generator(MAYO_Namespace, sctid_generator.RELATIONSHIP, 1000)
        self.assertEqual(10001000134127, generator.next())
        self.assertEqual([(1, 10011000134125), (2, 10021000134121), (3, 10031000134123),
                          (4, 10041000134129), (5, 10051000134126), (6, 10061000134128),
                          (7, 10071000134120), (8, 10081000134122), (9, 10091000134124)],
                         list(zip(range(1, 10), generator)))
        self.assertEqual(171000160104, (sctid_generator(CIMI_Namespace, sctid_generator.CONCEPT, 17)).next())
        self.assertEqual(911431000160119, (sctid_generator(CIMI_Namespace, sctid_generator.DESCRIPTION, 91143)).next())

        self.assertEqual(10101000134126, sctid(generator.next()))
        self.assertEqual([(1, 10111000134129), (2, 10121000134120), (3, 10131000134122),
                          (4, 10141000134128), (5, 10151000134125), (6, 10161000134127),
                          (7, 10171000134124), (8, 10181000134121), (9, 10191000134123)],
                         [(a, sctid(generator.next())) for a in range(1, 10)])
        self.assertEqual(171000160104, sctid((sctid_generator(CIMI_Namespace, sctid_generator.CONCEPT, 17)).next()))
        self.assertEqual(911431000160119, sctid((sctid_generator(CIMI_Namespace, sctid_generator.DESCRIPTION, 91143)).next()))

    def test_zero_partition(self):
        self.assertEqual(123456001, sctid_generator(0, sctid_generator.CONCEPT, 123456).next())
        self.assertEqual(654321026, sctid_generator(0, sctid_generator.RELATIONSHIP, 654321).next())
        self.assertEqual(5349010, sctid_generator(0, sctid_generator.DESCRIPTION, 5349).next())

if __name__ == '__main__':
    unittest.main()
