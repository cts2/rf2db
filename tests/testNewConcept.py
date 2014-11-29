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
import re
import uuid

from rf2db.db.RF2ConceptFile import ConceptDB, new_concept_parms
from rf2db.constants.RF2ValueSets import cimiModule
from rf2db.db.RF2Namespaces import RF2Namespace
from rf2db.db.RF2ChangeSetFile import ChangeSetDB, add_changeset_parms, changeset_parms
from rf2db.utils.sctid_generator import CIMI_Namespace


from SetConfig import setConfig




class NewConceptTestCase(unittest.TestCase):
    def setUp(self):
        setConfig()
        self.concdb = ConceptDB()
        self.csdb = ChangeSetDB()
        self.testChangeSet = self.csdb.new_changeset(**add_changeset_parms.parse().dict).referencedComponentId.uuid

    def tearDown(self):
        self.csdb.rollback(**changeset_parms.parse(changeset=self.testChangeSet).dict)

    def testNew1(self):
        sctid = RF2Namespace(CIMI_Namespace).nextConceptId()
        parms = new_concept_parms.parse(effectiveTime='20141131',
                                         moduleId=str(cimiModule),
                                         changeset=self.testChangeSet,
                                         sctid=sctid)
        dbrec = self.concdb.add(**parms.dict)
        # We would like to do the test below, but RF2Concept has a wrapper and, as such, evaluates as a function
        # self.assertTrue(isinstance(dbrec, RF2Concept))
        self.assertIsNotNone(re.match(r'RF2Concept\(id:[0-9]+100016010[0-9], effectiveTime:20141131, active:1, moduleId:11000160102, definitionStatusId:900000000000074008\)', str(dbrec)))

    def testNew2(self):
        parms = new_concept_parms.parse(sctid=RF2Namespace(CIMI_Namespace).nextConceptId(),
                                       effectivetime='20141131',
                                       moduleid=str(cimiModule),
                                       definitionstatus='p',
                                       changeset=self.testChangeSet)
        dbrec = self.concdb.add(**parms.dict)
        self.assertIsNotNone(re.match(r'RF2Concept\(id:[0-9]+100016010[0-9], effectiveTime:20141131, active:1, moduleId:11000160102, definitionStatusId:900000000000074008\)', str(dbrec)))


    def testNew3(self):
        dbrec = self.concdb.add(**new_concept_parms.parse(changeset=self.testChangeSet).dict)
        self.assertIsNotNone(re.match(r'RF2Concept\(id:[0-9]+100016010[0-9], effectiveTime:[0-9]{8}, active:1, moduleId:11000160102, definitionStatusId:900000000000074008\)', str(dbrec)))


    def testNewNoChangeset(self):
        self.assertEqual('Changeset identifier must be supplied', self.concdb.add(**new_concept_parms.parse().dict))

    def testInvalidChangeset(self):
        self.assertEqual('Change set is not valid or has been committed', self.concdb.add(**new_concept_parms.parse(changeset=str(uuid.uuid4())).dict))
