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
from rf2db.db.RF2Namespaces import RF2Namespace, DecodedNamespace
from rf2db.utils.sctid_generator import sctid_generator, CIMI_Namespace

from SetConfig import setConfig
from ClearConfig import clearConfig

class RF2NamespaceTestCase(unittest.TestCase):
    def setUp(self):
        setConfig()

    def tearDown(self):
        clearConfig()

    def nsTest(self, ns):
        x = RF2Namespace(ns)
        dns = DecodedNamespace(x.nextConceptId())
        self.assertEqual(ns, dns.namespace)
        self.assertEqual(sctid_generator.CONCEPT._lid, dns.partition)
        base = dns.item
        dns2 = DecodedNamespace(x.nextConceptId())
        self.assertEqual(ns, dns2.namespace)
        self.assertEqual(sctid_generator.CONCEPT._lid, dns2.partition)
        self.assertEqual(dns2.item, base+1)
        dns = DecodedNamespace(x.nextRelationshipId())
        self.assertEqual(ns, dns.namespace)
        self.assertEqual(sctid_generator.RELATIONSHIP._lid, dns.partition)
        dns = DecodedNamespace(x.nextDescriptionId())
        self.assertEqual(ns, dns.namespace)
        self.assertEqual(sctid_generator.DESCRIPTION._lid, dns.partition)

    def test_CIMI(self):
        self.nsTest(CIMI_Namespace)
        self.nsTest(100087)

    def test_strNS(self):
        ns = "1000087"
        x = RF2Namespace(ns)
        dns = DecodedNamespace(x.nextConceptId())
        self.assertEqual(ns, str(dns.namespace))
        self.assertEqual(sctid_generator.CONCEPT._lid, dns.partition)

    def testDecodedNamespace(self):
        dns1 = DecodedNamespace(101291013)
        self.assertEqual(3, dns1.checkdigit)
        self.assertEqual(1, dns1.partition)
        self.assertEqual(101291, dns1.item)
        self.assertEqual(0, dns1.namespace)

        dns1 = DecodedNamespace(101291111)
        self.assertEqual(1, dns1.checkdigit)
        self.assertEqual(11, dns1.partition)
        self.assertEqual(101291, dns1.namespace)
        self.assertEqual(0, dns1.item)

        dns1 = DecodedNamespace(999999990989121104)
        self.assertEqual(4, dns1.checkdigit)
        self.assertEqual(10, dns1.partition)
        self.assertEqual(99999999, dns1.item)
        self.assertEqual(989121, dns1.namespace)



if __name__ == '__main__':
    unittest.main()
