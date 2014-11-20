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
from rf2db.db.RF2Namespaces import RF2Namespace
from rf2db.utils.sctid_generator import CIMI_Namespace


class RF2NamespaceTestCase(unittest.TestCase):
    def setUp(self):
        import SetConfig

    def test_CIMI(self):
        RF2Namespace(CIMI_Namespace)
        print(RF2Namespace(CIMI_Namespace).nextConceptId())
        x = RF2Namespace(CIMI_Namespace)
        print x.nextConceptId()
        print x.nextConceptId()
        print x.nextRelationshipId()
        print x.nextDescriptionId()
        ns = 1000087
        print(RF2Namespace(ns).nextConceptId())
        print(RF2Namespace(ns).nextConceptId())
        print(RF2Namespace(ns).nextDescriptionId())
        print(RF2Namespace(ns).nextRelationshipId())

    def test_strNS(self):
        ns = "1000087"
        print(RF2Namespace(ns).nextConceptId())


if __name__ == '__main__':
    unittest.main()
