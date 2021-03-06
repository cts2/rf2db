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
import sys
from rf2db.utils.sctid import *
from rf2db.utils.check_digit import generate_verhoeff

# sctid won't construct an entry unless it is valid.  It treats
# an sctid as either a string or a long depending on context
class testSCTID(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(sctid(74400008),74400008)
        with self.assertRaises(AssertionError):
            sctid(74400007)
        self.assertEqual(sctid(74400008), "74400008")
        self.assertEqual(sctid(74400008) + "A", "74400008A")
        self.assertEqual("B" + sctid(74400008), "B74400008")
        self.assertEqual(74400008, sctid(74400008))
        self.assertEqual("74400008", sctid(74400008))
        target = sctid(generate_verhoeff(10**17 - 1))
        self.assertEqual(str(target), "999999999999999994")
        self.assertEqual(int(target), 999999999999999994)
        if sys.version_info.major < 3:
            self.assertEqual(long(target), 999999999999999994)



if __name__ == '__main__':
    unittest.main()
