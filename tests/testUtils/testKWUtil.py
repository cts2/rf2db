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
from rf2db.utils.kwutil import *

class ParseLangTestCase(unittest.TestCase):
    def testSec14(self):
        self.assertEqual(['da','en-gb','en'], preference_order("da, en-gb;q=0.8, en;q=0.7"))

    def testSingle(self):
        self.assertEqual(['en'], preference_order('en'))

    def testOrder(self):
        self.assertEqual(['da','en','en-gb'], preference_order("da, en-gb;q=0.4, en;q=0.6"))

    def testCoEquals(self):
        self.assertEqual(['en-gb', 'en-us', 'en'], preference_order("en-gb, en-us, en;q=0.9"))

    def testEmpty(self):
        self.assertEqual([], preference_order(""))


class KwgetTestCase(unittest.TestCase):
    def testLangList(self):
        self.assertEqual(['da', 'en-gb', 'en'], kwget(['lang', 'referenceLanguage', 'refLang', 'Accept-Language'],
                                                      {'Accept-Language' : 'da, en-gb;q=0.8, en;q=0.7'},
                                                      preference_order,
                                                      'en'))

    def testTwoLangs(self):
        self.assertEqual(kwget(['lang', 'referenceLanguage', 'refLang', 'Accept-Language'],
                               [{'referencelanguage':'en','maxtoreturn':10}, {'Accept-Language' : 'da, en-gb;q=0.8, en;q=0.7'}],
                               preference_order,
                               'en'),['en'])

    def testDefault(self):
        self.assertEqual(kwget(['lang', 'referenceLanguage', 'refLang', 'accept-Language'],
                               [{'referencelanguage':'en','maxtoreturn':10}, {'Accept-Language' : 'da, en-gb;q=0.8, en;q=0.7'}],
                               preference_order,
                               'es',False),['es'])

    def testEmpty(self):
        self.assertEqual(kwget(['lang', 'referenceLanguage', 'refLang', 'Accept-Language'],
                        {}, preference_order, 'es',False),['es'])


class MatchLangTestCase(unittest.TestCase):
    def testSimpleMatch(self):
        self.assertEqual(best_match(['en','en-gb','en-us','es'],
                                   kwget(['lang', 'referenceLanguage', 'refLang', 'Accept-Language'],
                                         {'Accept-Language' : 'da, en-gb;q=0.8, en;q=0.7'},
                                         preference_order,
                                         'en')),'en-gb')

class FormatTestCase(unittest.TestCase):
    def testAcceptHeader(self):
        self.assertEqual(kwget('Accept',
              {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
              preference_order,
              'application/xml'
              ), ['text/html', 'application/xhtml+xml', 'application/xml', '*/*'])

        self.assertEqual(best_match(['application/xml', 'text/html'], kwget('Accept',
              {'Accept':'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
              preference_order,
              'application/xml'
              )), 'text/html')

        self.assertEqual(best_match(['application/json', 'applicaton/doc'], kwget('Accept',
              {'Accept':'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
              preference_order,
              'application/xml'
              )), 'application/json')

        """  The media type quality factor associated with a given type is determined by finding the media range with the highest precedence which matches that type. For example,

       Accept: text/*;q=0.3, text/html;q=0.7, text/html;level=1,
               text/html;level=2;q=0.4, */*;q=0.5

       would cause the following values to be associated:

       text/html;level=1         = 1
       text/html                 = 0.7
       text/plain                = 0.3

       image/jpeg                = 0.5
       text/html;level=2         = 0.4
       text/html;level=3         = 0.7

        """
        self.assertEqual( kwget('Accept',
            {'Accept':'text/*;q=0.3, text/html;q=0.7, text/html;level=1, \
               text/html;level=2;q=0.4, */*;q=0.5'},
            preference_order,
            None,
            ), ['text/html;level=1', 'text/html', '*/*', 'text/html;level=2', 'text/*'])
        rqst = ['text/html;level=1', 'text/html', '*/*', 'text/html;level=2', 'text/*']
        values = ['text/html;level=1', 'text/html;level=3', 'text/html', 'image/jpeg', 'text/html;level=2', 'text/plain']
        self.assertEqual('text/html;level=1',best_match(values, rqst))
        self.assertEqual('text/html',best_match(values[1:], rqst))
        self.assertEqual('text/html', best_match(values[2:], rqst))
        self.assertEqual('image/jpeg',best_match(values[3:], rqst))
        self.assertEqual('text/html;level=2', best_match(values[4:], rqst))
        self.assertEqual('text/plain', best_match(values[5:], rqst))

        rqst = ['text/html;level=1', 'text/html', 'text/html;level=2', 'text/*']
        self.assertEqual('text/html;level=1',best_match(values, rqst))
        self.assertEqual('text/html',best_match(values[1:], rqst))
        self.assertEqual('text/html', best_match(values[2:], rqst))
        self.assertEqual('text/html;level=2', best_match(values[4:], rqst))
        self.assertEqual('text/plain', best_match(values[5:], rqst))
        self.assertIsNone(best_match(['image/jpeg'], rqst))