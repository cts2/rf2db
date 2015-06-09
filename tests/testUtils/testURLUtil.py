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

from rf2db.utils.urlutil import append_params, strip_control_params

class TestAppendParms(unittest.TestCase):

    def test1(self):
        baseURL = "http://localhost:8080/cts2/resolvedvalueset/sctid:7400120?bypass=1&page=2&maxtoreturn=500&format=json"
        parms = {'page':3, 'maxtoreturn':20}
        expected = "http://localhost:8080/cts2/resolvedvalueset/sctid:7400120?bypass=1&format=json&page=3&maxtoreturn=20"
        # there is no guarantee on the order of appendParams
        # If this gets to be an issue, the test needs diff the query lists instead of this
        self.assertEqual(len(expected), len(append_params(baseURL, parms)))

    def test2(self):
        baseURL = "http://jim:jimspassword@localhost:8080/cts2/resolvedvalueset/sctid:7400120?bypass=1&page=2&maxtoreturn=500&format=json"
        expected = "http://localhost:8080/cts2/resolvedvalueset/sctid:7400120?maxtoreturn=500&page=2&format=json"
        self.assertEqual(len(expected), len(strip_control_params(baseURL)))


if __name__ == '__main__':
    unittest.main()
