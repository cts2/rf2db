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
# Redistributions in binary form must reproduce the above copyright notice,
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
from SetConfig import setConfig
from rf2db.db.RF2DescriptionFile import DescriptionDB, new_description_parms, update_description_parms, \
    delete_description_parms
from rf2db.db.RF2ChangeSetFile import ChangeSetDB, add_changeset_parms, changeset_parms
from rf2db.constants.RF2ValueSets import cimiModule
from rf2db.utils.effectivetime import effectivetimenow

test_concept = 74400008  # Appendicitis
test_changeset = 'a1e09280-db9b-4fd9-97f5-0abad6e2b622'
test_description = 41000160117

target_desc1 = 'RF2Description(id:%s, effectiveTime:%d, active:1, moduleId:11000160102, conceptId:74400008,' \
               ' languageCode:en, typeId:900000000000013009, term:Appendixes for the masses, ' \
               'caseSignificanceId:900000000000020002)'


class NewDescriptionTestCase(unittest.TestCase):
    def setUp(self):
        setConfig()
        self.descdb = DescriptionDB()
        self.csdb = ChangeSetDB()

    def testNew1(self):
        testchangeset = str(self.csdb.new(**add_changeset_parms.parse().dict).referencedComponentId.uuid)
        parms = new_description_parms.parse(effectiveTime='20141131',
                                            moduleId=str(cimiModule),
                                            changeset=testchangeset,
                                            concept=test_concept,
                                            term="Appendicies for the masses")
        dbrec = self.descdb.add(**parms.dict)
        # We would like to do the test below, but RF2Concept has a wrapper and, as such, evaluates as a function
        # self.assertTrue(isinstance(dbrec, RF2Concept))
        self.assertEqual('RF2Description(id:%s, effectiveTime:20141131, active:1, moduleId:11000160102, '
                         'conceptId:74400008, languageCode:en, typeId:900000000000013009, '
                         'term:Appendicies for the masses, caseSignificanceId:900000000000020002)' % dbrec.id,
                         str(dbrec))
        self.csdb.rollback(**changeset_parms.parse(changeset=testchangeset).dict)

    def testUpdate(self):
        testchangeset = str(self.csdb.new(**add_changeset_parms.parse().dict).referencedComponentId.uuid)
        parms = new_description_parms.parse(effectiveTime='20141131',
                                            moduleId=str(cimiModule),
                                            changeset=testchangeset,
                                            concept=test_concept,
                                            term="Appendicies for the masses")
        dbrec = self.descdb.add(**parms.dict)
        dbrec = self.descdb.update(desc=dbrec.id, changeset=testchangeset, term="Appendixes for the masses")
        # Note: The assertion below may occassionaly fail at midnight GMT.  Run it again
        self.assertEqual(target_desc1 % (dbrec.id, effectivetimenow()), str(dbrec))
        self.assertRaises(self.descdb.read(dbrec.id))
        self.csdb.commit(**changeset_parms.parse(changeset=testchangeset).dict)


if __name__ == '__main__':
    unittest.main()
