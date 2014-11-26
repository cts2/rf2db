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



from rf2db.db.RF2ChangeSetFile import ChangeSetDB, add_changeset_parms, validate_changeset_parms
from rf2db.db.RF2FileCommon import extensionParms
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB

import SetConfig

uuidre = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
tsre = '[0-9]{8}'
rsid = changeSetRefSet
moduleid = extensionParms.moduleid
matchptn_ =  (r'RF2ChangeSetReferenceEntry\(id:%(uuidre)s, '
        r'effectiveTime:%(tsre)s, active:1, moduleId:%(moduleid)s, '
        r'refsetId:%(rsid)s, referencedComponentId:%(uuidre)s, ' % vars())
matchptn1 = re.compile(matchptn_ + r'creator:None, changeDescription:None, isFinal:0, inRelease:None\)')
matchptn2 = re.compile(matchptn_ + r'creator:Joel Stevens, changeDescription:my really happy changeset, isFinal:0, inRelease:None\)')


class NewChangeSetTestCase(unittest.TestCase):
    def setUp(self):
        self.csdb = ChangeSetDB()
        self.concdb = ConceptDB()
        self.addedSets = []

    def tearDown(self):
        for e in self.addedSets:
            parms = validate_changeset_parms.parse(**{'changeset': e.referencedComponentId.uuid})
            self.csdb.rollback(parms)

    def testNew(self):
        self.addedSets.append(self.csdb.new_changeset(add_changeset_parms.parse(**{})))
        print(self.addedSets[-1])
        self.assertIsNotNone(matchptn1.match(str(self.addedSets[-1])))
        parms = {'creator':'Joel Stevens', 'description':'my really happy changeset'}
        self.addedSets.append(self.csdb.new_changeset(add_changeset_parms.parse(**parms)))
        self.assertIsNotNone(matchptn2.match(str(self.addedSets[-1])))

    def testValid(self):
        parms = validate_changeset_parms.parse(**{'changeset': uuid.uuid4()})
        self.assertFalse(self.csdb.isValid(parms), "Random UUID should not be valid")
        csrec = self.csdb.new_changeset(add_changeset_parms.parse(**{}))
        parms = validate_changeset_parms.parse(**{'changeset': csrec.referencedComponentId.uuid})
        self.assertTrue(self.csdb.isValid(parms))
        self.assertEqual(self.csdb.rollback(parms).nChangesets, 1)

    def testHidden(self):
        csrec = self.csdb.new_changeset(add_changeset_parms.parse(**{}))
        parms = validate_changeset_parms.parse(**{'changeset': csrec.referencedComponentId.uuid})
        concRef = self.concdb.newConcept(parms)
        self.assertEqual(self.concdb.getConcept(concRef.id, parms).id, concRef.id)
        parms.changeset = uuid.uuid4()
        self.assertIsNone(self.concdb.getConcept(concRef.id, parms))
        parms.changeset = None
        self.assertIsNone(self.concdb.getConcept(concRef.id, parms))
        parms.changeset = concRef.changeset
        self.assertEqual(self.concdb.getConcept(concRef.id, parms).id, concRef.id)
        self.addedSets.append(csrec)

    def testRollback(self):
        csrec = self.csdb.new_changeset(add_changeset_parms.parse())
        parms = validate_changeset_parms.parse(changeset = csrec.referencedComponentId.uuid)
        self.concdb.newConcept(parms)
        # TODO: Issue -- parms gets additional information added to it in the above call
        parms = validate_changeset_parms.parse(changeset = csrec.referencedComponentId.uuid)
        self.concdb.newConcept(parms)
        rval = self.csdb.rollback(parms)
        self.assertEqual(2, rval.nConcepts)
        self.assertEqual(1, rval.nChangesets)

    def testCommit(self):
        csrec = self.csdb.new_changeset(add_changeset_parms.parse())
        parms = validate_changeset_parms.parse(changeset = csrec.referencedComponentId.uuid)
        self.concdb.newConcept(parms)
        # TODO: Issue -- parms gets additional information added to it in the above call
        parms = validate_changeset_parms.parse(changeset = csrec.referencedComponentId.uuid)
        self.concdb.newConcept(parms)
        rval = self.csdb.commit(parms)
        self.assertEqual(2, rval.nConcepts)
        self.assertEqual(1, rval.nChangesets)



