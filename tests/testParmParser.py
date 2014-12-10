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

from rf2db.parameterparser import ParmParser
from rf2db.utils.sctid import sctid
from rf2db.db.RF2FileCommon import moduleidparam

from SetConfig import setConfig


class ParmParserTestCase(unittest.TestCase):
    def test_parse(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.isActive = ParmParser.booleanparam(default=True)
        arglist.numEntries = ParmParser.intparam()
        arglist.another = ParmParser.booleanparam(default=True)
        arglist.yetanother = ParmParser.booleanparam()
        args = arglist.parse(isActive=0, numentries="17")
        self.assertFalse(args.isactive, False)
        self.assertEqual(args.NUMENTRIES, 17)
        self.assertTrue(args.another)
        self.assertIsNone(args.yetanother)
        args = arglist.parse(isactive="no", unk="abc", numentries=0, multvals=[1, 2, 3])
        self.assertFalse(args.isActive)
        self.assertEqual(args.numEntries, 0)
        self.assertEqual(sorted(args._remainingargs), sorted({'unk': 'abc', 'multvals': [1, 2, 3]}))

    def test_baddefault(self):
        arglist = ParmParser.ParameterDefinitionList()
        self.assertRaises(ValueError, ParmParser.enumparam, ["Buy", "SELL", "Hold"], default="hold", casesensitive=True)

    def test_multiple(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.intparam()
        arglist.p2 = ParmParser.intparam()
        args = arglist.parse(p1=17, p2=[1, 2, 3])
        self.assertEqual(args.p1, 17)
        self.assertEqual(args.p2, [1, 2, 3])

    def test_validate(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.booleanparam()
        arglist.p2 = ParmParser.booleanparam()
        arglist.p3 = ParmParser.booleanparam()
        self.assertTrue(arglist.validate(p1=True, p2="no", P3=0))
        self.assertFalse(arglist.validate(p1='sam'))
        self.assertFalse(arglist.validate(p1=17))
        invalidargs, remargs = arglist.invalidParms(p1=True, p2="sam", s1="foo")
        self.assertEqual(sorted(invalidargs), sorted({'p2': 'sam'}))
        self.assertEqual(sorted(remargs), sorted({"s1": "foo"}))

    def test_boolean(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.booleanparam(default=True)
        arglist.p2 = ParmParser.booleanparam(default="No")
        arglist.p3 = ParmParser.booleanparam()
        args = arglist.parse()
        self.assertTrue(args.p1)
        self.assertFalse(args.p2)
        self.assertIsNone(args.p3)
        self.assertRaises(ValueError, ParmParser.booleanparam, default='sam')


    def test_integer(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.intparam(default=-143)
        arglist.p2 = ParmParser.intparam(default="0")
        arglist.p3 = ParmParser.intparam()
        arglist.p4 = ParmParser.intparam()
        args = arglist.parse(**{'p4': "10001771"})
        self.assertEqual(args.p1, -143)
        self.assertEqual(args.p2, 0)
        self.assertIsNone(args.p3)
        self.assertEqual(args.p4, 10001771)
        self.assertRaises(ValueError, ParmParser.intparam, default='123a')

    def test_string(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.strparam(default=-143)
        arglist.p2 = ParmParser.strparam(default="sell")
        arglist.p3 = ParmParser.strparam()
        arglist.p4 = ParmParser.strparam()
        args = arglist.parse(**{'p4': "10001771"})
        self.assertEqual(args.p1, "-143")
        self.assertEqual(args.p2, "sell")
        self.assertIsNone(args.p3)
        self.assertEqual(args.p4, "10001771")
        args = arglist.parse(**{'p1': ["a", 17, True]})
        self.assertEqual(args.p1, ["a", "17", "True"])
        self.assertRaises(ValueError, ParmParser.intparam, default='a')
        self.assertFalse(arglist.validate(**{'p1': ""}))

    def test_sctid(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.sctidparam(default=0)
        arglist.p2 = ParmParser.strparam(default="74400008")
        arglist.p3 = ParmParser.strparam()
        arglist.p4 = ParmParser.strparam()
        args = arglist.parse(**{'p4': ["447565001", 0], 'P3': 900000000000020002, 'p2': sctid(74400008)})
        self.assertEqual(args.p1, sctid(0))
        self.assertEqual(str(args.p2), "74400008")
        self.assertEqual(args.p3, sctid(900000000000020002))
        self.assertEqual(args.p4, [sctid("447565001"), sctid(0)])
        self.assertRaises(ValueError, ParmParser.sctidparam, default='17')
        self.assertFalse(arglist.validate(**{'p1': ""}))
        self.assertFalse(arglist.validate(**{'p1': "17"}))

    def test_enum(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.enumparam(["Buy", "SELL", "hold"], default="hold")
        arglist.p2 = ParmParser.enumparam(["Buy", "SELL", "Hold"], default="hold")
        arglist.p3 = ParmParser.enumparam(["Buy", "SELL", "Hold"], default="Hold", casesensitive=True)
        arglist.p4 = ParmParser.enumparam(["Canada", "UnitedSnakes", "Mexico"])
        args = arglist.parse(p1='Buy', p4="unitedsnakes")
        self.assertEqual(args.p1, 'buy')
        self.assertEqual(args.p2, 'hold')
        self.assertEqual(args.p3, 'Hold')
        self.assertEqual(args.p4, 'unitedsnakes')

    def test_splittable(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.booleanparam()
        arglist.p2 = ParmParser.strparam()
        arglist.p3 = ParmParser.intparam()
        arglist.p4 = ParmParser.sctidparam()
        args = arglist.parse(p1 = "true false", p2="abc def", p3="1 2 17", p4="74400008 900000000000020002 447565001")
        self.assertEqual(args.p1, [True, False])
        self.assertEqual(args.p2, ['abc', 'def'])
        self.assertEqual(args.p3, [1, 2, 17])
        self.assertEqual(args.p4, ['74400008', '900000000000020002', '447565001'])
        self.assertIsInstance(args.p4[0], sctid)
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.booleanparam(splittable=False)
        arglist.p2 = ParmParser.strparam(splittable=False)
        arglist.p3 = ParmParser.intparam(splittable=False)
        arglist.p4 = ParmParser.sctidparam(splittable=False)
        self.assertRaises(ValueError, arglist.parse, p1='true true')
        self.assertRaises(ValueError, arglist.parse, p3="1 2 17")
        self.assertRaises(ValueError, arglist.parse, p4="74400008 900000000000020002 447565001")
        args = arglist.parse(p2="abc def")
        self.assertEqual(args.p2, 'abc def')


    def test_defaulted(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.booleanparam(default=True)
        arglist.p2 = ParmParser.booleanparam(default=True)
        args = arglist.parse(p2=True)
        self.assertTrue(args.defaulted('p1'))
        self.assertFalse(args.defaulted('p2'))

    def test_fixed(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.sctidparam(default=74400008, fixed=True)
        arglist.p2 = ParmParser.sctidparam(default=74400008)
        args = arglist.parse(p1=447565001, p2=447565001)
        self.assertEqual(args.p1, 74400008)
        self.assertEqual(args.p2, 447565001)

    def test_computed(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.intparam(default=6)
        arglist.p2 = ParmParser.intparam(default=7)
        arglist.p3 = ParmParser.booleanparam(default=False)
        arglist.p4 = ParmParser.computedparam(formula=lambda p: p.p1 * (p.p2 if p.p3 else 2))
        args = arglist.parse(p1=9, p2=5, p3=True)
        self.assertEqual(args.p4, 45)
        args = arglist.parse()
        self.assertEqual(args.p4, 12)

    def test_moduleid(self):
        setConfig()
        arglist = ParmParser.ParameterDefinitionList()

        arglist.p1 = moduleidparam()
        args = arglist.parse(p1='900000000000207008')
        self.assertEqual(args.p1, 900000000000207008)
        self.assertRaises(ValueError, arglist.parse, p1='74400008')


    def test_sql_escape(self):
        arglist = ParmParser.ParameterDefinitionList()
        arglist.p1 = ParmParser.strparam(splittable=False)
        args = arglist.parse(p1="';drop table Student;")
        self.assertEqual("\\';drop table Student;", args.p1)
        inval = "\0 ' \" \b \n \r \t \x1a \\ % _"
        args = arglist.parse(p1=inval)
        self.assertEqual('\\0 \\\' \\" \\b \\n \\r \\t \\Z \\\\ \\% \\_', args.p1)


if __name__ == '__main__':
    unittest.main()
