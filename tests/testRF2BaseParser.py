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
#     Neither the name of the Mayo Clinic nor the names of its contributors
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


from rf2db.parsers.RF2BaseParser import *
from rf2db.parsers.RF2RefsetParser import *
from rf2db.utils.xmlutils import testxml, defaultNS
from rf2db.schema import rf2

           
import unittest


class RF2ConceptTestCase(unittest.TestCase):
    
    def setUp(self):
        xmlutils.defaultNS = rf2.Namespace
        
    def test(self):
        c = RF2Concept('10027005	20020131	1	900000000000207008	900000000000074008')
        self.assertTrue(c.isPrimitive)
        self.assertTrue(testxml(c, """<?xml version="1.0" ?>
<Concept xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>10027005</id>
    <effectiveTime>20020131</effectiveTime>
    <active>1</active>
    <moduleId>900000000000207008</moduleId>
    <definitionStatusId>900000000000074008</definitionStatusId>
</Concept>"""))
        self.assertEqual(str(c),"RF2Concept(id:10027005, effectiveTime:20020131, active:1, "
                                "moduleId:900000000000207008, definitionStatusId:900000000000074008)")

class RF2DescriptionTestCase(unittest.TestCase):
    
    def setUp(self):
        defaultNS = rf2.Namespace
        
    def test(self):    
        d = RF2Description('517048016	20100131	1	900000000000380005	10027005	en	900000000000003001	Patchy (qualifier value)	900000000000022005')
        self.assertTrue(testxml(d, """<?xml version="1.0" ?>
<Description xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>517048016</id>
    <effectiveTime>20100131</effectiveTime>
    <active>1</active>
    <moduleId>900000000000380005</moduleId>
    <conceptId>10027005</conceptId>
    <languageCode>en</languageCode>
    <typeId>900000000000003001</typeId>
    <term>Patchy (qualifier value)</term>
    <caseSignificanceId>900000000000022005</caseSignificanceId>
</Description>"""))
        self.assertEqual(str(d), "RF2Description(id:517048016, effectiveTime:20100131, active:1, "
                                 "moduleId:900000000000380005, conceptId:10027005, languageCode:en, "
                                 "typeId:900000000000003001, term:Patchy (qualifier value), caseSignificanceId:900000000000022005)")
     
        d1 = RF2Description('525229014	20100131	1	900000000000380005	145945003	en	900000000000003001	Entire muscular branches of occipital artery (body structure)	900000000000022005')
        self.assertTrue(testxml(d1, """<?xml version="1.0" ?>
<Description xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>525229014</id>
    <effectiveTime>20100131</effectiveTime>
    <active>1</active>
    <moduleId>900000000000380005</moduleId>
    <conceptId>145945003</conceptId>
    <languageCode>en</languageCode>
    <typeId>900000000000003001</typeId>
    <term>Entire muscular branches of occipital artery (body structure)</term>
    <caseSignificanceId>900000000000022005</caseSignificanceId>
</Description>"""))
        self.assertEqual(str(d1), "RF2Description(id:525229014, effectiveTime:20100131, active:1, "
                                  "moduleId:900000000000380005, conceptId:145945003, languageCode:en, "
                                  "typeId:900000000000003001, term:Entire muscular branches of occipital artery (body structure), "
                                  "caseSignificanceId:900000000000022005)")

     
class RF2RelationshipTestCase(unittest.TestCase):
    
    def setUp(self):
        defaultNS = rf2.Namespace
        
    def test(self): 
        r = RF2Relationship('452025|20100131|1|900000000000380005|10027005|106234000|0|116680003|900000000000006009|900000000000451002|0','|')
        print r.toxml()
        self.assertTrue(testxml(r, """<?xml version="1.0" ?>
<Relationship xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>452025</id>
    <effectiveTime>20100131</effectiveTime>
    <active>1</active>
    <moduleId>900000000000380005</moduleId>
    <sourceId>10027005</sourceId>
    <destinationId>106234000</destinationId>
    <relationshipGroup>0</relationshipGroup>
    <typeId>116680003</typeId>
    <characteristicTypeId>900000000000006009</characteristicTypeId>
    <modifierId>900000000000451002</modifierId>
    <isCanonical>0</isCanonical>
</Relationship>"""))
        self.assertEqual(str(r), "RF2Relationship(id:452025, effectiveTime:20100131, active:1, "
                                 "moduleId:900000000000380005, sourceId:10027005, destinationId:106234000, "
                                 "relationshipGroup:0, typeId:116680003, characteristicTypeId:900000000000006009, modifierId:900000000000451002, isCanonical:0)")

class RF2ReprTestCase(unittest.TestCase):
    def test1(self):
        conc = '10027005\t20020131\t1\t900000000000207008\t900000000000074008'
        desc = '517048016\t20100131\t1\t900000000000380005\t10027005\ten\t900000000000003001\tPatchy (qualifier value)\t900000000000022005'
        rel  = '452025\t20100131\t1\t900000000000380005\t10027005\t106234000\t0\t116680003\t900000000000006009\t900000000000451002\t0'
        lang = '0000097d-42b2-500d-88bb-46066baa9bad\t20020131\t1\t900000000000207008\t900000000000508004\t132462014\t900000000000548007'
	    
        self.assertEqual(repr(RF2Concept(conc)),conc)
        self.assertEqual(repr(RF2Description(desc)),desc)
        self.assertEqual(repr(RF2Relationship(rel)),rel)
        self.assertEqual(repr(RF2LanguageRefsetEntry(lang)),lang)
        self.assertEqual(repr(RF2Concept(repr(RF2Concept(conc)))), conc)


if __name__ == '__main__':
    unittest.main()
