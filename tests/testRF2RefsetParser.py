from rf2db.parsers.RF2RefsetParser import *
from rf2db.utils.xmlutils import testxml
           
import unittest

class RF2LanguageTestCase(unittest.TestCase):
    def setUp(self):
        testxml.defaultNS = rf2.Namespace
        
    def test(self):
        l1 = RF2LanguageRefsetEntry('0000097d-42b2-500d-88bb-46066baa9bad    20020131        1       900000000000207008      900000000000508004      132462014       900000000000548007', None)
        l2 = RF2LanguageRefsetEntry('00000b14-886f-5d9f-bba5-64e03752cbbc    20080731        1       900000000000207008      900000000000508004      2731802019      900000000000548007', None)
        self.assertTrue(testxml(l1, """<?xml version="1.0" ?>
<LanguageReferenceSetEntry xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>0000097d-42b2-500d-88bb-46066baa9bad</id>
    <effectiveTime>20020131</effectiveTime>
    <active>1</active>
    <moduleId>900000000000207008</moduleId>
    <refsetId>900000000000508004</refsetId>
    <referencedComponentId>
        <sctid>132462014</sctid>
    </referencedComponentId>
    <acceptabilityId>900000000000548007</acceptabilityId>
</LanguageReferenceSetEntry>"""))
        self.assertTrue(testxml(l2, """<?xml version="1.0" ?>
<LanguageReferenceSetEntry xmlns="http://schema.ihtsdo.org/rf2/schema/Concept">
    <id>00000b14-886f-5d9f-bba5-64e03752cbbc</id>
    <effectiveTime>20080731</effectiveTime>
    <active>1</active>
    <moduleId>900000000000207008</moduleId>
    <refsetId>900000000000508004</refsetId>
    <referencedComponentId>
        <sctid>2731802019</sctid>
    </referencedComponentId>
    <acceptabilityId>900000000000548007</acceptabilityId>
</LanguageReferenceSetEntry>"""))
             
import os 
testFile = lambda f : os.path.join(os.path.dirname(__file__), 'testdata', f + '.xml')            
class BasicTestCase(unittest.TestCase):

        
    def setUp(self):
        testxml.defaultNS = rf2.Namespace
        
    def ftest1(self):


        def saveTestData(f, xml):
            f = open(testFile(f),'w')
            f.write(xml)
            f.close()

        #saveTestData('RF2DescriptorReferenceSetEntry',
        #              util.prettyxml(RF2DescriptorReferenceSetEntry('0daa9880-5875-5de0-9650-21fac667afcb	20020131	1	900000000000207008	900000000000456007	900000000000509007	900000000000510002	900000000000462002	0')))
        self.assertTrue(testxml(RF2DescriptorReferenceSetEntry('0daa9880-5875-5de0-9650-21fac667afcb	20020131	1	900000000000207008	900000000000456007	900000000000509007	900000000000510002	900000000000462002	0'),
                        None, testFile('RF2DescriptorReferenceSetEntry')))
        #saveTestData('RF2SimpleReferenceSetEntry',
        #              util.prettyxml(RF2SimpleReferenceSetEntry('0061d967-1565-50ee-9dcf-11975018860f	20050131	1	900000000000207008	447565001	7947003')))
        self.assertTrue(testxml(RF2SimpleReferenceSetEntry('0061d967-1565-50ee-9dcf-11975018860f	20050131	1	900000000000207008	447565001	7947003'),
                        None, testFile('RF2SimpleReferenceSetEntry')))
        #saveTestData('RF2OrderedReferenceSetEntry',
        #              util.prettyxml(RF2OrderedReferenceSetEntry('0008e8f7-b7ea-576a-854e-9256af76ea0a	20020131	1	900000000000207008	447568004	83678007	1	263353005')))
        self.assertTrue(testxml(RF2OrderedReferenceSetEntry('0008e8f7-b7ea-576a-854e-9256af76ea0a	20020131	1	900000000000207008	447568004	83678007	1	263353005'),
                        None, testFile('RF2OrderedReferenceSetEntry')))
        #saveTestData('RF2AttributeValueReferenceSetEntry',
        #              util.prettyxml(RF2AttributeValueReferenceSetEntry('0001d24b-d872-5077-8955-b9c7e055b015	20080731	0	900000000000207008	900000000000490003	527806011	900000000000495008')))
        self.assertTrue(testxml(RF2AttributeValueReferenceSetEntry('0001d24b-d872-5077-8955-b9c7e055b015	20080731	0	900000000000207008	900000000000490003	527806011	900000000000495008'),
                        None, testFile('RF2AttributeValueReferenceSetEntry')))
        #saveTestData('RF2SimpleMapReferenceSetEntry',
        #              util.prettyxml(RF2SimpleMapReferenceSetEntry('00019a58-45fa-528d-9eba-ef489ada6797	20020131	1	900000000000207008	900000000000498005	56417000	P3-42300')))
        self.assertTrue(testxml(RF2SimpleMapReferenceSetEntry('00019a58-45fa-528d-9eba-ef489ada6797	20020131	1	900000000000207008	900000000000498005	56417000	P3-42300'),
                        None, testFile('RF2SimpleMapReferenceSetEntry')))
        #saveTestData('RF2ComplexMapReferenceSetEntry',
        #              util.prettyxml(RF2ComplexMapReferenceSetEntry('00104c0f-a218-5882-970c-b2054b8b9f30	20030731	0	900000000000207008	447563008	359563005	1	1			593.9	447558009')))
        self.assertTrue(testxml(RF2ComplexMapReferenceSetEntry('00104c0f-a218-5882-970c-b2054b8b9f30	20030731	0	900000000000207008	447563008	359563005	1	1			593.9	447558009'),
                        None, testFile('RF2ComplexMapReferenceSetEntry')))
        #saveTestData('RF2LanguageRefsetEntry',
        #              util.prettyxml(RF2LanguageRefsetEntry('0000ff2d-c40b-52a5-97b4-375eb94c9479	20080131	0	900000000000207008	900000000000509007	21351019	900000000000549004')))
        self.assertTrue(testxml(RF2LanguageRefsetEntry('0000ff2d-c40b-52a5-97b4-375eb94c9479	20080131	0	900000000000207008	900000000000509007	21351019	900000000000549004'),
                        None, testFile('RF2LanguageRefsetEntry')))
                          
        # QuerySpecification
        # Annotation
        #saveTestData('RF2ModuleDependencyReferenceSetEntry',
        #          util.prettyxml(RF2ModuleDependencyReferenceSetEntry('1244116f-fdb5-5645-afcc-5281288409da	20110731	1	900000000000207008	900000000000534007	900000000000012004	20110731	20110731')))
        self.assertTrue(testxml(RF2ModuleDependencyReferenceSetEntry('1244116f-fdb5-5645-afcc-5281288409da	20110731	1	900000000000207008	900000000000534007	900000000000012004	20110731	20110731'),
                        None, testFile('RF2ModuleDependencyReferenceSetEntry')))
        #saveTestData('RF2DescriptionFormatReferenceSetEntry',
        #              util.prettyxml(RF2DescriptionFormatReferenceSetEntry('807f775b-1d66-5069-b58e-a37ace985dcf	20020131	1	900000000000207008	900000000000538005	900000000000550004	900000000000540000	1024')))
        self.assertTrue(testxml(RF2DescriptionFormatReferenceSetEntry('807f775b-1d66-5069-b58e-a37ace985dcf	20020131	1	900000000000207008	900000000000538005	900000000000550004	900000000000540000	1024'),
                        None, testFile('RF2DescriptionFormatReferenceSetEntry')))
                      

    

