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
from rf2db.db.RF2FileCommon import ep_values
from rf2db.constants.RF2ValueSets import changeSetRefSet
from rf2db.db.RF2ConceptFile import ConceptDB
from tests.SetConfig import setConfig
from tests.ClearConfig import clearConfig

# NOTE: If you start getting Duplicate entry errors below, the database hasn't been cleaned up.  What we really need
#       to do is to create a testing module identifier that we can strip with impunity but, for the moment, the
#       cleanup is probably the best way to do it
#
# NOTE 2: Also note that, at the moment we don't update the moduleVersions file.  If you get a whole mess 'o errors
#         you might consider seeing whether 11000160102 / 20150601 is in the module versions file

class NewChangeSetTestCase(unittest.TestCase):
    def setUp(self):
        setConfig()
        moduleid = ep_values.moduleid
        uuidre = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        tsre = '[0-9]{8}'
        rsid = changeSetRefSet

        matchptn_ = (r'RF2ChangeSetReferenceSetEntry\(id:%(uuidre)s, '
                     r'effectiveTime:%(tsre)s, active:1, moduleId:%(moduleid)s, '
                     r'refsetId:%(rsid)s, referencedComponentId:%(uuidre)s, name:%(uuidre)s, ') % vars()
        self.matchptn1 = re.compile(matchptn_ + r'owner:None, '
                                                r'changeDescription:None, '
                                                r'isFinal:0, '
                                                r'inRelease:None\)')
        self.matchptn2 = re.compile(matchptn_ + r'owner:Joel Stevens, '
                                                r'changeDescription:my really happy changeset, '
                                                r'isFinal:0, '
                                                r'inRelease:None\)')
        self.csdb = ChangeSetDB()
        self.concdb = ConceptDB()
        self.addedSets = []

    def tearDown(self):
        for e in self.addedSets:
            if e:
                parms = validate_changeset_parms.parse(changeset=e.referencedComponentId.uuid).dict
                self.csdb.rollback(**parms)
        clearConfig()

    @staticmethod
    def _d(**kwargs):
        return vars()['kwargs']

    def testNew(self):
        self.addedSets.append(self.csdb.new(**add_changeset_parms.parse().dict))
        print(self.matchptn1.pattern)
        print(str(self.addedSets[-1]))
        self.assertIsNotNone(self.matchptn1.match(str(self.addedSets[-1])))
        parms = add_changeset_parms.parse(owner='Joel Stevens', description='my really happy changeset')
        self.addedSets.append(self.csdb.new(**parms.dict))
        self.assertIsNotNone(self.matchptn2.match(str(self.addedSets[-1])))

    def testValid(self):
        parms = validate_changeset_parms.parse(changeset=str(uuid.uuid4()))
        self.assertFalse(self.csdb.isValid(**parms.dict), "Random UUID should not be valid")
        csrec = self.csdb.new(**add_changeset_parms.parse().dict)
        parms = validate_changeset_parms.parse(changeset=csrec.referencedComponentId.uuid)
        self.assertTrue(self.csdb.isValid(**parms.dict))
        self.assertEqual(self.csdb.rollback(**parms.dict).nChangesets, 1)

    def testHidden(self):
        csrec = self.csdb.new(**add_changeset_parms.parse().dict)
        parms = validate_changeset_parms.parse(changeset = csrec.referencedComponentId.uuid)
        conc_ref = self.concdb.add(**parms.dict)
        self.assertEqual(self.concdb.read(conc_ref.id, **parms.dict).id, conc_ref.id)
        parms.changeset = str(uuid.uuid4())
        self.assertIsNone(self.concdb.read(conc_ref.id, **parms.dict))
        parms.changeset = None
        self.assertIsNone(self.concdb.read(conc_ref.id, **parms.dict))
        parms.changeset = conc_ref.changeset
        self.assertEqual(self.concdb.read(conc_ref.id, **parms.dict).id, conc_ref.id)
        self.addedSets.append(csrec)

    def testRollback(self):
        csrec = self.csdb.new(**add_changeset_parms.parse().dict)
        parms = validate_changeset_parms.parse(changeset=csrec.referencedComponentId.uuid)
        self.concdb.add(**parms.dict)
        self.concdb.add(**parms.dict)
        rval = self.csdb.rollback(**parms.dict)
        self.assertEqual(2, rval.nConcepts)
        self.assertEqual(1, rval.nChangesets)

    def testCommit(self):
        csrec = self.csdb.new(**add_changeset_parms.parse().dict)
        parms = validate_changeset_parms.parse(changeset=csrec.referencedComponentId.uuid)
        self.concdb.add(**parms.dict)
        self.concdb.add(**parms.dict)
        rval = self.csdb.commit(**parms.dict)
        self.assertEqual(2, rval.nConcepts)
        self.assertEqual(1, rval.nChangesets)

    def testName(self):
        parms = add_changeset_parms.parse(csname='testing')
        self.addedSets.append(self.csdb.new(**parms.dict))
        self.assertIsNotNone(self.addedSets[-1])
        self.assertTrue(self.csdb.isValid(**parms.dict))
        self.assertEqual("Changeset (testing) already exists", self.csdb.new(**parms.dict))
        self.assertEqual(self.csdb.rollback(**parms.dict).nChangesets, 1)
