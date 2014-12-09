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
import uuid

from tests.SetConfig import setConfig

from rf2db.db.RF2RelationshipFile import RelationshipDB, new_rel_parms
from rf2db.db.RF2ConceptFile import ConceptDB, new_concept_parms

from rf2db.db.RF2ChangeSetFile import ChangeSetDB, add_changeset_parms, changeset_parms
from rf2db.constants.RF2ValueSets import cimiModule
from rf2db.utils.effectivetime import effectivetimenow

test_source = 74400008   # Appendicitis
test_target = 85315007   # Yorkshire pig


class NewDescriptionTestCase(unittest.TestCase):
    def setUp(self):
        setConfig()
        self.reldb = RelationshipDB()
        self.csdb = ChangeSetDB()
        self.concdb = ConceptDB()
        self.testchangeset = str(self.csdb.new_changeset(**add_changeset_parms.parse().dict).referencedComponentId.uuid)
        self.concrec = self.concdb.add(self.testchangeset, moduleid=str(cimiModule))
        self.concid = self.concrec.id

    def tearDown(self):
        self.csdb.rollback(self.testchangeset)

    def testaddexisting(self):
        parms = new_rel_parms.parse(effectiveTime='20141131',
                                    moduleId=str(cimiModule),
                                    changeset=self.testchangeset,
                                    source=test_source,
                                    target=test_target)
        dbrec = self.reldb.add(**parms.dict)
        self.assertIsNone(dbrec)
        self.assertEqual("Cannot change the definition of an existing concept (74400008)",
                         self.reldb.invalid_add_reason(**parms.dict))

    def testaddnew(self):
        parms = new_rel_parms.parse(moduleId=str(cimiModule),
                                    changeset=self.testchangeset,
                                    source=self.concid,
                                    target=test_target)
        dbrec = self.reldb.add(**parms.dict)
        etn = effectivetimenow()
        relid = dbrec.id
        self.assertEqual('RF2Relationship(id:%s, effectiveTime:%s, active:1, moduleId:11000160102, '
                         'sourceId:%s, destinationId:85315007, relationshipGroup:0, typeId:116680003, '
                         'characteristicTypeId:900000000000010007, modifierId:900000000000451002, isCanonical:0)'
                         % (relid, etn, self.concid),
                         str(dbrec))


if __name__ == '__main__':
    unittest.main()
