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

from testUtils import path

from rf2db.db.RF2ConceptFile import ConceptDB, new_concept_parms
from rf2db.constants.RF2ValueSets import cimiModule
from rf2db.db.RF2Namespaces import RF2Namespace
from rf2db.utils.sctid_generator import CIMI_Namespace



testChangeSet = 'F95FE83F-3B93-4193-B922-8B9D82097B07'



class NewConceptTestCase(unittest.TestCase):
    def setUp(self):
        import SetConfig
        self.concdb = ConceptDB()

    def testNew1(self):
        sctid = RF2Namespace(CIMI_Namespace).nextConceptId()
        parms = new_concept_parms.parse(**{'effectiveTime': '20141131',
                                         'moduleId': str(cimiModule),
                                         'changesetid': testChangeSet,
                                         'sctid': sctid,
                                        })
        dbrec = self.concdb.newConcept(parms)
        print(dbrec)


