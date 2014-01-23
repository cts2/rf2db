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
from rf2db.utils.check_digit import *

class CheckDigitTestCase1(unittest.TestCase):
    def test1(self):
        # Some tests and also usage examples)
        self.assertEqual(calcsum('75872'), 2)
        self.assertEqual(checksum('758722'), 0)
        self.assertEqual(calcsum('12345'), 1)
        self.assertEqual(checksum('123451'), 0)
        self.assertEqual(calcsum('142857'), 0)
        self.assertEqual(checksum('1428570'), 0)
        self.assertEqual(calcsum('123456789012'), 0)
        self.assertEqual(checksum('1234567890120'), 0)
        self.assertEqual(calcsum('8473643095483728456789'), 2)
        self.assertEqual(checksum('84736430954837284567892'), 0)
        self.assertEqual(generate_verhoeff('12345'), '123451')
        self.assertTrue(validate_verhoeff('123451'))
        self.assertFalse(validate_verhoeff('122451'))
        self.assertFalse(validate_verhoeff('128451'))


class CheckDigitSnomedTestCase(unittest.TestCase):

    def test2(self):
        """
        Pass over the concept file validating the check digit on all the entries.
        Note that this seems simple because sctid does a check digit validation
        """
        from rf2db.utils.sctid import sctid
        self.assertRaises(AssertionError, sctid, 100004)
        self.assertEqual(long(sctid(100005)), 100005)

        from rf2db.db.RF2DBConnection import RF2DBConnection

        db = RF2DBConnection()
        db.execute('SELECT id FROM concept_ss limit 1000')
        for row in db:
            self.assertEqual(long(sctid(row[0])), row[0])