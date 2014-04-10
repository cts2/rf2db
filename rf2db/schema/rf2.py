# ../rf2db/schema/rf2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a62023a1e63ecb635c8d1a3482d1f64c6fb3e0f6
# Generated 2014-04-10 16:38:58.573126 by PyXB version 1.2.3
# Namespace http://snomed.info/schema/rf2

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8585ddf0-c0f8-11e3-b324-c82a1438c957')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://snomed.info/schema/rf2', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://snomed.info/schema/rf2}SCTID
class SCTID (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SCTID')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 16, 4)
    _Documentation = None
SCTID._CF_pattern = pyxb.binding.facets.CF_pattern()
SCTID._CF_pattern.addPattern(pattern=u'[0-9]{6,18}')
SCTID._InitializeFacetMap(SCTID._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'SCTID', SCTID)

# Atomic simple type: {http://snomed.info/schema/rf2}UUID
class UUID (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UUID')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 22, 4)
    _Documentation = None
UUID._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'UUID', UUID)

# Atomic simple type: {http://snomed.info/schema/rf2}String
class String (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'String')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 26, 4)
    _Documentation = None
String._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'String', String)

# Atomic simple type: {http://snomed.info/schema/rf2}Integer
class Integer (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Integer')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 30, 4)
    _Documentation = None
Integer._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'Integer', Integer)

# Atomic simple type: {http://snomed.info/schema/rf2}Boolean
class Boolean (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Boolean')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 34, 4)
    _Documentation = None
Boolean._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Boolean, enum_prefix=None)
Boolean._CF_enumeration.addEnumeration(unicode_value=u'0', tag=None)
Boolean._CF_enumeration.addEnumeration(unicode_value=u'1', tag=None)
Boolean._InitializeFacetMap(Boolean._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Boolean', Boolean)

# Atomic simple type: {http://snomed.info/schema/rf2}Time
class Time (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Time')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 49, 4)
    _Documentation = None
Time._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'Time', Time)

# Atomic simple type: {http://snomed.info/schema/rf2}CompleteDirectory
class CompleteDirectory (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether a
                
                contains all of the qualifying entries or only some.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CompleteDirectory')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7543, 4)
    _Documentation = u'An indicator that determines whether a\n                \n                contains all of the qualifying entries or only some.\n            '
CompleteDirectory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompleteDirectory, enum_prefix=None)
CompleteDirectory.COMPLETE = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value=u'COMPLETE', tag=u'COMPLETE')
CompleteDirectory.PARTIAL = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value=u'PARTIAL', tag=u'PARTIAL')
CompleteDirectory._InitializeFacetMap(CompleteDirectory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CompleteDirectory', CompleteDirectory)

# Atomic simple type: {http://snomed.info/schema/rf2}SortDirection
class SortDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The collating order of a sort."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SortDirection')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7568, 4)
    _Documentation = u'The collating order of a sort.'
SortDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortDirection, enum_prefix=None)
SortDirection.ASCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'ASCENDING', tag=u'ASCENDING')
SortDirection.DESCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'DESCENDING', tag=u'DESCENDING')
SortDirection._InitializeFacetMap(SortDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SortDirection', SortDirection)

# Atomic simple type: {http://snomed.info/schema/rf2}ICD-10_map_category_value
class ICD_10_map_category_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ICD-10_map_category_value')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 65, 4)
    _Documentation = u'\n                \n            '
ICD_10_map_category_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ICD_10_map_category_value, enum_prefix=None)
ICD_10_map_category_value.n447635003 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447635003', tag=u'n447635003')
ICD_10_map_category_value.n447636002 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447636002', tag=u'n447636002')
ICD_10_map_category_value.n447637006 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447637006', tag=u'n447637006')
ICD_10_map_category_value.n447638001 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447638001', tag=u'n447638001')
ICD_10_map_category_value.n447639009 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447639009', tag=u'n447639009')
ICD_10_map_category_value.n447640006 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447640006', tag=u'n447640006')
ICD_10_map_category_value.n447641005 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447641005', tag=u'n447641005')
ICD_10_map_category_value.n447642003 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value=u'447642003', tag=u'n447642003')
ICD_10_map_category_value._InitializeFacetMap(ICD_10_map_category_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ICD-10_map_category_value', ICD_10_map_category_value)

# Atomic simple type: {http://snomed.info/schema/rf2}Module
class Module (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Module')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 139, 4)
    _Documentation = u'\n                \n            '
Module._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Module, enum_prefix=None)
Module.n449079008 = Module._CF_enumeration.addEnumeration(unicode_value=u'449079008', tag=u'n449079008')
Module.n449080006 = Module._CF_enumeration.addEnumeration(unicode_value=u'449080006', tag=u'n449080006')
Module.n449081005 = Module._CF_enumeration.addEnumeration(unicode_value=u'449081005', tag=u'n449081005')
Module.n5991000124107 = Module._CF_enumeration.addEnumeration(unicode_value=u'5991000124107', tag=u'n5991000124107')
Module.n900000000000012004 = Module._CF_enumeration.addEnumeration(unicode_value=u'900000000000012004', tag=u'n900000000000012004')
Module.n900000000000207008 = Module._CF_enumeration.addEnumeration(unicode_value=u'900000000000207008', tag=u'n900000000000207008')
Module.n900000000000445007 = Module._CF_enumeration.addEnumeration(unicode_value=u'900000000000445007', tag=u'n900000000000445007')
Module._InitializeFacetMap(Module._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Module', Module)

# Atomic simple type: {http://snomed.info/schema/rf2}Definition_status
class Definition_status (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Definition_status')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 201, 4)
    _Documentation = u'\n                \n            '
Definition_status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Definition_status, enum_prefix=None)
Definition_status.n900000000000073002 = Definition_status._CF_enumeration.addEnumeration(unicode_value=u'900000000000073002', tag=u'n900000000000073002')
Definition_status.n900000000000074008 = Definition_status._CF_enumeration.addEnumeration(unicode_value=u'900000000000074008', tag=u'n900000000000074008')
Definition_status._InitializeFacetMap(Definition_status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Definition_status', Definition_status)

# Atomic simple type: {http://snomed.info/schema/rf2}Description_type
class Description_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Description_type')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 236, 4)
    _Documentation = u'\n                \n            '
Description_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Description_type, enum_prefix=None)
Description_type.n900000000000003001 = Description_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000003001', tag=u'n900000000000003001')
Description_type.n900000000000013009 = Description_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000013009', tag=u'n900000000000013009')
Description_type.n900000000000550004 = Description_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000550004', tag=u'n900000000000550004')
Description_type._InitializeFacetMap(Description_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Description_type', Description_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Case_significance
class Case_significance (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Case_significance')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 274, 4)
    _Documentation = u'\n                \n            '
Case_significance._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Case_significance, enum_prefix=None)
Case_significance.n900000000000017005 = Case_significance._CF_enumeration.addEnumeration(unicode_value=u'900000000000017005', tag=u'n900000000000017005')
Case_significance.n900000000000020002 = Case_significance._CF_enumeration.addEnumeration(unicode_value=u'900000000000020002', tag=u'n900000000000020002')
Case_significance.n900000000000448009 = Case_significance._CF_enumeration.addEnumeration(unicode_value=u'900000000000448009', tag=u'n900000000000448009')
Case_significance._InitializeFacetMap(Case_significance._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Case_significance', Case_significance)

# Atomic simple type: {http://snomed.info/schema/rf2}Linkage_concept
class Linkage_concept (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Linkage_concept')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 312, 4)
    _Documentation = u'\n                \n            '
Linkage_concept._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Linkage_concept, enum_prefix=None)
Linkage_concept.n1241001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'1241001', tag=u'n1241001')
Linkage_concept.n5185003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'5185003', tag=u'n5185003')
Linkage_concept.n7196007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'7196007', tag=u'n7196007')
Linkage_concept.n7883008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'7883008', tag=u'n7883008')
Linkage_concept.n8707003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'8707003', tag=u'n8707003')
Linkage_concept.n8754004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'8754004', tag=u'n8754004')
Linkage_concept.n10546003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'10546003', tag=u'n10546003')
Linkage_concept.n15792004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'15792004', tag=u'n15792004')
Linkage_concept.n18720000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'18720000', tag=u'n18720000')
Linkage_concept.n19096001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'19096001', tag=u'n19096001')
Linkage_concept.n20401003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'20401003', tag=u'n20401003')
Linkage_concept.n21191007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'21191007', tag=u'n21191007')
Linkage_concept.n23981006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'23981006', tag=u'n23981006')
Linkage_concept.n25609006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'25609006', tag=u'n25609006')
Linkage_concept.n28995006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'28995006', tag=u'n28995006')
Linkage_concept.n30294006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'30294006', tag=u'n30294006')
Linkage_concept.n30507006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'30507006', tag=u'n30507006')
Linkage_concept.n35362001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'35362001', tag=u'n35362001')
Linkage_concept.n36612008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'36612008', tag=u'n36612008')
Linkage_concept.n37837009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'37837009', tag=u'n37837009')
Linkage_concept.n40378004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'40378004', tag=u'n40378004')
Linkage_concept.n42752001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'42752001', tag=u'n42752001')
Linkage_concept.n45169001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'45169001', tag=u'n45169001')
Linkage_concept.n47429007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'47429007', tag=u'n47429007')
Linkage_concept.n54776003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'54776003', tag=u'n54776003')
Linkage_concept.n58091002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'58091002', tag=u'n58091002')
Linkage_concept.n60117003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'60117003', tag=u'n60117003')
Linkage_concept.n67780002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'67780002', tag=u'n67780002')
Linkage_concept.n68369002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'68369002', tag=u'n68369002')
Linkage_concept.n68727004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'68727004', tag=u'n68727004')
Linkage_concept.n72589006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'72589006', tag=u'n72589006')
Linkage_concept.n73907009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'73907009', tag=u'n73907009')
Linkage_concept.n75958009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'75958009', tag=u'n75958009')
Linkage_concept.n77879006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'77879006', tag=u'n77879006')
Linkage_concept.n79409006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'79409006', tag=u'n79409006')
Linkage_concept.n85789007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'85789007', tag=u'n85789007')
Linkage_concept.n103335007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103335007', tag=u'n103335007')
Linkage_concept.n103366001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103366001', tag=u'n103366001')
Linkage_concept.n103367005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103367005', tag=u'n103367005')
Linkage_concept.n103368000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103368000', tag=u'n103368000')
Linkage_concept.n103369008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103369008', tag=u'n103369008')
Linkage_concept.n103370009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103370009', tag=u'n103370009')
Linkage_concept.n103371008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103371008', tag=u'n103371008')
Linkage_concept.n103372001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103372001', tag=u'n103372001')
Linkage_concept.n103373006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103373006', tag=u'n103373006')
Linkage_concept.n103374000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103374000', tag=u'n103374000')
Linkage_concept.n103375004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103375004', tag=u'n103375004')
Linkage_concept.n103376003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103376003', tag=u'n103376003')
Linkage_concept.n103377007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103377007', tag=u'n103377007')
Linkage_concept.n103378002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103378002', tag=u'n103378002')
Linkage_concept.n103421006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'103421006', tag=u'n103421006')
Linkage_concept.n112236005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'112236005', tag=u'n112236005')
Linkage_concept.n116673000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116673000', tag=u'n116673000')
Linkage_concept.n116674006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116674006', tag=u'n116674006')
Linkage_concept.n116675007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116675007', tag=u'n116675007')
Linkage_concept.n116676008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116676008', tag=u'n116676008')
Linkage_concept.n116677004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116677004', tag=u'n116677004')
Linkage_concept.n116678009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116678009', tag=u'n116678009')
Linkage_concept.n116679001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116679001', tag=u'n116679001')
Linkage_concept.n116680003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116680003', tag=u'n116680003')
Linkage_concept.n116681004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116681004', tag=u'n116681004')
Linkage_concept.n116682006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116682006', tag=u'n116682006')
Linkage_concept.n116683001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116683001', tag=u'n116683001')
Linkage_concept.n116684007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116684007', tag=u'n116684007')
Linkage_concept.n116685008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116685008', tag=u'n116685008')
Linkage_concept.n116686009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116686009', tag=u'n116686009')
Linkage_concept.n116687000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116687000', tag=u'n116687000')
Linkage_concept.n116688005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116688005', tag=u'n116688005')
Linkage_concept.n116689002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116689002', tag=u'n116689002')
Linkage_concept.n116690006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116690006', tag=u'n116690006')
Linkage_concept.n116691005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116691005', tag=u'n116691005')
Linkage_concept.n116692003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116692003', tag=u'n116692003')
Linkage_concept.n116693008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116693008', tag=u'n116693008')
Linkage_concept.n116694002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116694002', tag=u'n116694002')
Linkage_concept.n116696000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116696000', tag=u'n116696000')
Linkage_concept.n116697009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116697009', tag=u'n116697009')
Linkage_concept.n116698004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116698004', tag=u'n116698004')
Linkage_concept.n116699007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116699007', tag=u'n116699007')
Linkage_concept.n116700008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116700008', tag=u'n116700008')
Linkage_concept.n116701007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116701007', tag=u'n116701007')
Linkage_concept.n116702000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116702000', tag=u'n116702000')
Linkage_concept.n116703005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116703005', tag=u'n116703005')
Linkage_concept.n116704004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116704004', tag=u'n116704004')
Linkage_concept.n116705003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116705003', tag=u'n116705003')
Linkage_concept.n116706002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'116706002', tag=u'n116706002')
Linkage_concept.n118168003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118168003', tag=u'n118168003')
Linkage_concept.n118169006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118169006', tag=u'n118169006')
Linkage_concept.n118170007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118170007', tag=u'n118170007')
Linkage_concept.n118171006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118171006', tag=u'n118171006')
Linkage_concept.n118172004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118172004', tag=u'n118172004')
Linkage_concept.n118173009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'118173009', tag=u'n118173009')
Linkage_concept.n123005000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'123005000', tag=u'n123005000')
Linkage_concept.n127484005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127484005', tag=u'n127484005')
Linkage_concept.n127485006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127485006', tag=u'n127485006')
Linkage_concept.n127486007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127486007', tag=u'n127486007')
Linkage_concept.n127487003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127487003', tag=u'n127487003')
Linkage_concept.n127488008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127488008', tag=u'n127488008')
Linkage_concept.n127489000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'127489000', tag=u'n127489000')
Linkage_concept.n129450000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'129450000', tag=u'n129450000')
Linkage_concept.n129453003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'129453003', tag=u'n129453003')
Linkage_concept.n131195008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'131195008', tag=u'n131195008')
Linkage_concept.n134198009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'134198009', tag=u'n134198009')
Linkage_concept.n149016008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'149016008', tag=u'n149016008')
Linkage_concept.n159083000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'159083000', tag=u'n159083000')
Linkage_concept.n168666000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'168666000', tag=u'n168666000')
Linkage_concept.n178066000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'178066000', tag=u'n178066000')
Linkage_concept.n225794002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'225794002', tag=u'n225794002')
Linkage_concept.n229620004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'229620004', tag=u'n229620004')
Linkage_concept.n229753003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'229753003', tag=u'n229753003')
Linkage_concept.n230117008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'230117008', tag=u'n230117008')
Linkage_concept.n230118003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'230118003', tag=u'n230118003')
Linkage_concept.n230119006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'230119006', tag=u'n230119006')
Linkage_concept.n246061005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246061005', tag=u'n246061005')
Linkage_concept.n246062003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246062003', tag=u'n246062003')
Linkage_concept.n246063008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246063008', tag=u'n246063008')
Linkage_concept.n246064002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246064002', tag=u'n246064002')
Linkage_concept.n246065001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246065001', tag=u'n246065001')
Linkage_concept.n246066000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246066000', tag=u'n246066000')
Linkage_concept.n246067009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246067009', tag=u'n246067009')
Linkage_concept.n246068004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246068004', tag=u'n246068004')
Linkage_concept.n246069007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246069007', tag=u'n246069007')
Linkage_concept.n246070008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246070008', tag=u'n246070008')
Linkage_concept.n246071007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246071007', tag=u'n246071007')
Linkage_concept.n246072000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246072000', tag=u'n246072000')
Linkage_concept.n246073005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246073005', tag=u'n246073005')
Linkage_concept.n246075003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246075003', tag=u'n246075003')
Linkage_concept.n246076002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246076002', tag=u'n246076002')
Linkage_concept.n246077006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246077006', tag=u'n246077006')
Linkage_concept.n246078001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246078001', tag=u'n246078001')
Linkage_concept.n246079009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246079009', tag=u'n246079009')
Linkage_concept.n246080007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246080007', tag=u'n246080007')
Linkage_concept.n246082004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246082004', tag=u'n246082004')
Linkage_concept.n246083009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246083009', tag=u'n246083009')
Linkage_concept.n246084003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246084003', tag=u'n246084003')
Linkage_concept.n246085002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246085002', tag=u'n246085002')
Linkage_concept.n246086001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246086001', tag=u'n246086001')
Linkage_concept.n246087005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246087005', tag=u'n246087005')
Linkage_concept.n246088000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246088000', tag=u'n246088000')
Linkage_concept.n246090004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246090004', tag=u'n246090004')
Linkage_concept.n246091000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246091000', tag=u'n246091000')
Linkage_concept.n246092007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246092007', tag=u'n246092007')
Linkage_concept.n246093002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246093002', tag=u'n246093002')
Linkage_concept.n246094008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246094008', tag=u'n246094008')
Linkage_concept.n246095009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246095009', tag=u'n246095009')
Linkage_concept.n246096005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246096005', tag=u'n246096005')
Linkage_concept.n246097001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246097001', tag=u'n246097001')
Linkage_concept.n246098006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246098006', tag=u'n246098006')
Linkage_concept.n246099003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246099003', tag=u'n246099003')
Linkage_concept.n246101005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246101005', tag=u'n246101005')
Linkage_concept.n246102003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246102003', tag=u'n246102003')
Linkage_concept.n246103008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246103008', tag=u'n246103008')
Linkage_concept.n246104002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246104002', tag=u'n246104002')
Linkage_concept.n246105001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246105001', tag=u'n246105001')
Linkage_concept.n246106000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246106000', tag=u'n246106000')
Linkage_concept.n246107009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246107009', tag=u'n246107009')
Linkage_concept.n246108004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246108004', tag=u'n246108004')
Linkage_concept.n246110002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246110002', tag=u'n246110002')
Linkage_concept.n246111003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246111003', tag=u'n246111003')
Linkage_concept.n246112005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246112005', tag=u'n246112005')
Linkage_concept.n246113000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246113000', tag=u'n246113000')
Linkage_concept.n246114006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246114006', tag=u'n246114006')
Linkage_concept.n246115007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246115007', tag=u'n246115007')
Linkage_concept.n246134007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246134007', tag=u'n246134007')
Linkage_concept.n246136009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246136009', tag=u'n246136009')
Linkage_concept.n246137000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246137000', tag=u'n246137000')
Linkage_concept.n246138005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246138005', tag=u'n246138005')
Linkage_concept.n246140000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246140000', tag=u'n246140000')
Linkage_concept.n246141001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246141001', tag=u'n246141001')
Linkage_concept.n246142008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246142008', tag=u'n246142008')
Linkage_concept.n246143003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246143003', tag=u'n246143003')
Linkage_concept.n246144009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246144009', tag=u'n246144009')
Linkage_concept.n246145005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246145005', tag=u'n246145005')
Linkage_concept.n246146006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246146006', tag=u'n246146006')
Linkage_concept.n246147002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246147002', tag=u'n246147002')
Linkage_concept.n246148007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246148007', tag=u'n246148007')
Linkage_concept.n246149004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246149004', tag=u'n246149004')
Linkage_concept.n246150004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246150004', tag=u'n246150004')
Linkage_concept.n246151000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246151000', tag=u'n246151000')
Linkage_concept.n246152007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246152007', tag=u'n246152007')
Linkage_concept.n246153002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246153002', tag=u'n246153002')
Linkage_concept.n246154008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246154008', tag=u'n246154008')
Linkage_concept.n246155009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246155009', tag=u'n246155009')
Linkage_concept.n246156005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246156005', tag=u'n246156005')
Linkage_concept.n246157001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246157001', tag=u'n246157001')
Linkage_concept.n246158006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246158006', tag=u'n246158006')
Linkage_concept.n246159003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246159003', tag=u'n246159003')
Linkage_concept.n246160008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246160008', tag=u'n246160008')
Linkage_concept.n246161007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246161007', tag=u'n246161007')
Linkage_concept.n246162000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246162000', tag=u'n246162000')
Linkage_concept.n246163005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246163005', tag=u'n246163005')
Linkage_concept.n246164004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246164004', tag=u'n246164004')
Linkage_concept.n246165003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246165003', tag=u'n246165003')
Linkage_concept.n246166002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246166002', tag=u'n246166002')
Linkage_concept.n246167006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246167006', tag=u'n246167006')
Linkage_concept.n246168001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246168001', tag=u'n246168001')
Linkage_concept.n246169009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246169009', tag=u'n246169009')
Linkage_concept.n246170005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246170005', tag=u'n246170005')
Linkage_concept.n246171009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246171009', tag=u'n246171009')
Linkage_concept.n246173007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246173007', tag=u'n246173007')
Linkage_concept.n246174001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246174001', tag=u'n246174001')
Linkage_concept.n246175000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246175000', tag=u'n246175000')
Linkage_concept.n246176004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246176004', tag=u'n246176004')
Linkage_concept.n246177008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246177008', tag=u'n246177008')
Linkage_concept.n246178003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246178003', tag=u'n246178003')
Linkage_concept.n246179006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246179006', tag=u'n246179006')
Linkage_concept.n246181008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246181008', tag=u'n246181008')
Linkage_concept.n246182001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246182001', tag=u'n246182001')
Linkage_concept.n246183006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246183006', tag=u'n246183006')
Linkage_concept.n246185004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246185004', tag=u'n246185004')
Linkage_concept.n246186003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246186003', tag=u'n246186003')
Linkage_concept.n246187007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246187007', tag=u'n246187007')
Linkage_concept.n246189005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246189005', tag=u'n246189005')
Linkage_concept.n246190001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246190001', tag=u'n246190001')
Linkage_concept.n246191002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246191002', tag=u'n246191002')
Linkage_concept.n246192009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246192009', tag=u'n246192009')
Linkage_concept.n246193004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246193004', tag=u'n246193004')
Linkage_concept.n246194005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246194005', tag=u'n246194005')
Linkage_concept.n246195006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246195006', tag=u'n246195006')
Linkage_concept.n246196007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246196007', tag=u'n246196007')
Linkage_concept.n246197003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246197003', tag=u'n246197003')
Linkage_concept.n246198008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246198008', tag=u'n246198008')
Linkage_concept.n246199000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246199000', tag=u'n246199000')
Linkage_concept.n246200002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246200002', tag=u'n246200002')
Linkage_concept.n246201003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246201003', tag=u'n246201003')
Linkage_concept.n246202005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246202005', tag=u'n246202005')
Linkage_concept.n246203000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246203000', tag=u'n246203000')
Linkage_concept.n246204006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246204006', tag=u'n246204006')
Linkage_concept.n246205007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246205007', tag=u'n246205007')
Linkage_concept.n246215001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246215001', tag=u'n246215001')
Linkage_concept.n246216000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246216000', tag=u'n246216000')
Linkage_concept.n246217009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246217009', tag=u'n246217009')
Linkage_concept.n246218004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246218004', tag=u'n246218004')
Linkage_concept.n246219007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246219007', tag=u'n246219007')
Linkage_concept.n246220001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246220001', tag=u'n246220001')
Linkage_concept.n246222009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246222009', tag=u'n246222009')
Linkage_concept.n246224005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246224005', tag=u'n246224005')
Linkage_concept.n246225006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246225006', tag=u'n246225006')
Linkage_concept.n246226007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246226007', tag=u'n246226007')
Linkage_concept.n246227003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246227003', tag=u'n246227003')
Linkage_concept.n246228008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246228008', tag=u'n246228008')
Linkage_concept.n246229000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246229000', tag=u'n246229000')
Linkage_concept.n246230005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246230005', tag=u'n246230005')
Linkage_concept.n246231009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246231009', tag=u'n246231009')
Linkage_concept.n246232002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246232002', tag=u'n246232002')
Linkage_concept.n246233007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246233007', tag=u'n246233007')
Linkage_concept.n246234001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246234001', tag=u'n246234001')
Linkage_concept.n246235000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246235000', tag=u'n246235000')
Linkage_concept.n246236004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246236004', tag=u'n246236004')
Linkage_concept.n246237008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246237008', tag=u'n246237008')
Linkage_concept.n246238003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246238003', tag=u'n246238003')
Linkage_concept.n246240008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246240008', tag=u'n246240008')
Linkage_concept.n246241007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246241007', tag=u'n246241007')
Linkage_concept.n246242000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246242000', tag=u'n246242000')
Linkage_concept.n246243005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246243005', tag=u'n246243005')
Linkage_concept.n246244004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246244004', tag=u'n246244004')
Linkage_concept.n246245003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246245003', tag=u'n246245003')
Linkage_concept.n246246002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246246002', tag=u'n246246002')
Linkage_concept.n246247006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246247006', tag=u'n246247006')
Linkage_concept.n246248001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246248001', tag=u'n246248001')
Linkage_concept.n246249009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246249009', tag=u'n246249009')
Linkage_concept.n246250009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246250009', tag=u'n246250009')
Linkage_concept.n246251008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246251008', tag=u'n246251008')
Linkage_concept.n246252001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246252001', tag=u'n246252001')
Linkage_concept.n246253006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246253006', tag=u'n246253006')
Linkage_concept.n246254000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246254000', tag=u'n246254000')
Linkage_concept.n246255004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246255004', tag=u'n246255004')
Linkage_concept.n246256003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246256003', tag=u'n246256003')
Linkage_concept.n246257007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246257007', tag=u'n246257007')
Linkage_concept.n246258002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246258002', tag=u'n246258002')
Linkage_concept.n246259005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246259005', tag=u'n246259005')
Linkage_concept.n246260000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246260000', tag=u'n246260000')
Linkage_concept.n246261001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246261001', tag=u'n246261001')
Linkage_concept.n246262008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246262008', tag=u'n246262008')
Linkage_concept.n246263003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246263003', tag=u'n246263003')
Linkage_concept.n246264009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246264009', tag=u'n246264009')
Linkage_concept.n246265005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246265005', tag=u'n246265005')
Linkage_concept.n246266006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246266006', tag=u'n246266006')
Linkage_concept.n246267002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246267002', tag=u'n246267002')
Linkage_concept.n246268007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246268007', tag=u'n246268007')
Linkage_concept.n246269004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246269004', tag=u'n246269004')
Linkage_concept.n246270003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246270003', tag=u'n246270003')
Linkage_concept.n246271004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246271004', tag=u'n246271004')
Linkage_concept.n246272006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246272006', tag=u'n246272006')
Linkage_concept.n246273001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246273001', tag=u'n246273001')
Linkage_concept.n246274007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246274007', tag=u'n246274007')
Linkage_concept.n246275008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246275008', tag=u'n246275008')
Linkage_concept.n246276009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246276009', tag=u'n246276009')
Linkage_concept.n246277000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246277000', tag=u'n246277000')
Linkage_concept.n246278005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246278005', tag=u'n246278005')
Linkage_concept.n246280004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246280004', tag=u'n246280004')
Linkage_concept.n246281000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246281000', tag=u'n246281000')
Linkage_concept.n246282007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246282007', tag=u'n246282007')
Linkage_concept.n246283002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246283002', tag=u'n246283002')
Linkage_concept.n246284008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246284008', tag=u'n246284008')
Linkage_concept.n246285009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246285009', tag=u'n246285009')
Linkage_concept.n246286005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246286005', tag=u'n246286005')
Linkage_concept.n246287001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246287001', tag=u'n246287001')
Linkage_concept.n246288006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246288006', tag=u'n246288006')
Linkage_concept.n246289003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246289003', tag=u'n246289003')
Linkage_concept.n246290007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246290007', tag=u'n246290007')
Linkage_concept.n246291006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246291006', tag=u'n246291006')
Linkage_concept.n246293009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246293009', tag=u'n246293009')
Linkage_concept.n246294003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246294003', tag=u'n246294003')
Linkage_concept.n246295002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246295002', tag=u'n246295002')
Linkage_concept.n246296001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246296001', tag=u'n246296001')
Linkage_concept.n246297005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246297005', tag=u'n246297005')
Linkage_concept.n246298000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246298000', tag=u'n246298000')
Linkage_concept.n246299008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246299008', tag=u'n246299008')
Linkage_concept.n246300000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246300000', tag=u'n246300000')
Linkage_concept.n246301001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246301001', tag=u'n246301001')
Linkage_concept.n246302008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246302008', tag=u'n246302008')
Linkage_concept.n246303003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246303003', tag=u'n246303003')
Linkage_concept.n246304009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246304009', tag=u'n246304009')
Linkage_concept.n246305005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246305005', tag=u'n246305005')
Linkage_concept.n246306006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246306006', tag=u'n246306006')
Linkage_concept.n246307002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246307002', tag=u'n246307002')
Linkage_concept.n246308007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246308007', tag=u'n246308007')
Linkage_concept.n246309004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246309004', tag=u'n246309004')
Linkage_concept.n246310009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246310009', tag=u'n246310009')
Linkage_concept.n246311008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246311008', tag=u'n246311008')
Linkage_concept.n246312001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246312001', tag=u'n246312001')
Linkage_concept.n246313006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246313006', tag=u'n246313006')
Linkage_concept.n246314000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246314000', tag=u'n246314000')
Linkage_concept.n246315004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246315004', tag=u'n246315004')
Linkage_concept.n246316003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246316003', tag=u'n246316003')
Linkage_concept.n246317007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246317007', tag=u'n246317007')
Linkage_concept.n246318002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246318002', tag=u'n246318002')
Linkage_concept.n246321000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246321000', tag=u'n246321000')
Linkage_concept.n246322007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246322007', tag=u'n246322007')
Linkage_concept.n246323002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246323002', tag=u'n246323002')
Linkage_concept.n246324008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246324008', tag=u'n246324008')
Linkage_concept.n246325009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246325009', tag=u'n246325009')
Linkage_concept.n246326005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246326005', tag=u'n246326005')
Linkage_concept.n246327001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246327001', tag=u'n246327001')
Linkage_concept.n246328006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246328006', tag=u'n246328006')
Linkage_concept.n246329003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246329003', tag=u'n246329003')
Linkage_concept.n246330008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246330008', tag=u'n246330008')
Linkage_concept.n246331007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246331007', tag=u'n246331007')
Linkage_concept.n246332000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246332000', tag=u'n246332000')
Linkage_concept.n246333005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246333005', tag=u'n246333005')
Linkage_concept.n246334004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246334004', tag=u'n246334004')
Linkage_concept.n246335003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246335003', tag=u'n246335003')
Linkage_concept.n246336002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246336002', tag=u'n246336002')
Linkage_concept.n246337006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246337006', tag=u'n246337006')
Linkage_concept.n246338001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246338001', tag=u'n246338001')
Linkage_concept.n246339009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246339009', tag=u'n246339009')
Linkage_concept.n246340006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246340006', tag=u'n246340006')
Linkage_concept.n246341005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246341005', tag=u'n246341005')
Linkage_concept.n246343008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246343008', tag=u'n246343008')
Linkage_concept.n246344002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246344002', tag=u'n246344002')
Linkage_concept.n246345001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246345001', tag=u'n246345001')
Linkage_concept.n246346000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246346000', tag=u'n246346000')
Linkage_concept.n246347009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246347009', tag=u'n246347009')
Linkage_concept.n246348004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246348004', tag=u'n246348004')
Linkage_concept.n246349007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246349007', tag=u'n246349007')
Linkage_concept.n246351006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246351006', tag=u'n246351006')
Linkage_concept.n246352004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246352004', tag=u'n246352004')
Linkage_concept.n246353009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246353009', tag=u'n246353009')
Linkage_concept.n246354003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246354003', tag=u'n246354003')
Linkage_concept.n246355002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246355002', tag=u'n246355002')
Linkage_concept.n246356001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246356001', tag=u'n246356001')
Linkage_concept.n246358000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246358000', tag=u'n246358000')
Linkage_concept.n246359008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246359008', tag=u'n246359008')
Linkage_concept.n246360003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246360003', tag=u'n246360003')
Linkage_concept.n246361004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246361004', tag=u'n246361004')
Linkage_concept.n246362006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246362006', tag=u'n246362006')
Linkage_concept.n246364007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246364007', tag=u'n246364007')
Linkage_concept.n246365008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246365008', tag=u'n246365008')
Linkage_concept.n246366009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246366009', tag=u'n246366009')
Linkage_concept.n246367000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246367000', tag=u'n246367000')
Linkage_concept.n246368005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246368005', tag=u'n246368005')
Linkage_concept.n246369002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246369002', tag=u'n246369002')
Linkage_concept.n246370001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246370001', tag=u'n246370001')
Linkage_concept.n246371002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246371002', tag=u'n246371002')
Linkage_concept.n246372009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246372009', tag=u'n246372009')
Linkage_concept.n246373004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246373004', tag=u'n246373004')
Linkage_concept.n246375006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246375006', tag=u'n246375006')
Linkage_concept.n246376007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246376007', tag=u'n246376007')
Linkage_concept.n246378008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246378008', tag=u'n246378008')
Linkage_concept.n246379000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246379000', tag=u'n246379000')
Linkage_concept.n246380002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246380002', tag=u'n246380002')
Linkage_concept.n246381003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246381003', tag=u'n246381003')
Linkage_concept.n246382005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246382005', tag=u'n246382005')
Linkage_concept.n246383000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246383000', tag=u'n246383000')
Linkage_concept.n246384006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246384006', tag=u'n246384006')
Linkage_concept.n246385007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246385007', tag=u'n246385007')
Linkage_concept.n246386008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246386008', tag=u'n246386008')
Linkage_concept.n246387004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246387004', tag=u'n246387004')
Linkage_concept.n246388009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246388009', tag=u'n246388009')
Linkage_concept.n246389001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246389001', tag=u'n246389001')
Linkage_concept.n246390005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246390005', tag=u'n246390005')
Linkage_concept.n246391009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246391009', tag=u'n246391009')
Linkage_concept.n246392002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246392002', tag=u'n246392002')
Linkage_concept.n246393007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246393007', tag=u'n246393007')
Linkage_concept.n246394001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246394001', tag=u'n246394001')
Linkage_concept.n246395000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246395000', tag=u'n246395000')
Linkage_concept.n246396004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246396004', tag=u'n246396004')
Linkage_concept.n246397008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246397008', tag=u'n246397008')
Linkage_concept.n246398003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246398003', tag=u'n246398003')
Linkage_concept.n246399006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246399006', tag=u'n246399006')
Linkage_concept.n246400004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246400004', tag=u'n246400004')
Linkage_concept.n246401000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246401000', tag=u'n246401000')
Linkage_concept.n246402007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246402007', tag=u'n246402007')
Linkage_concept.n246403002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246403002', tag=u'n246403002')
Linkage_concept.n246404008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246404008', tag=u'n246404008')
Linkage_concept.n246405009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246405009', tag=u'n246405009')
Linkage_concept.n246406005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246406005', tag=u'n246406005')
Linkage_concept.n246407001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246407001', tag=u'n246407001')
Linkage_concept.n246408006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246408006', tag=u'n246408006')
Linkage_concept.n246409003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246409003', tag=u'n246409003')
Linkage_concept.n246410008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246410008', tag=u'n246410008')
Linkage_concept.n246411007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246411007', tag=u'n246411007')
Linkage_concept.n246412000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246412000', tag=u'n246412000')
Linkage_concept.n246413005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246413005', tag=u'n246413005')
Linkage_concept.n246414004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246414004', tag=u'n246414004')
Linkage_concept.n246415003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246415003', tag=u'n246415003')
Linkage_concept.n246416002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246416002', tag=u'n246416002')
Linkage_concept.n246417006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246417006', tag=u'n246417006')
Linkage_concept.n246418001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246418001', tag=u'n246418001')
Linkage_concept.n246419009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246419009', tag=u'n246419009')
Linkage_concept.n246420003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246420003', tag=u'n246420003')
Linkage_concept.n246421004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246421004', tag=u'n246421004')
Linkage_concept.n246422006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246422006', tag=u'n246422006')
Linkage_concept.n246423001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246423001', tag=u'n246423001')
Linkage_concept.n246424007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246424007', tag=u'n246424007')
Linkage_concept.n246425008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246425008', tag=u'n246425008')
Linkage_concept.n246426009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246426009', tag=u'n246426009')
Linkage_concept.n246427000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246427000', tag=u'n246427000')
Linkage_concept.n246428005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246428005', tag=u'n246428005')
Linkage_concept.n246429002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246429002', tag=u'n246429002')
Linkage_concept.n246430007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246430007', tag=u'n246430007')
Linkage_concept.n246431006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246431006', tag=u'n246431006')
Linkage_concept.n246445000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246445000', tag=u'n246445000')
Linkage_concept.n246446004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246446004', tag=u'n246446004')
Linkage_concept.n246447008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246447008', tag=u'n246447008')
Linkage_concept.n246448003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246448003', tag=u'n246448003')
Linkage_concept.n246449006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246449006', tag=u'n246449006')
Linkage_concept.n246450006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246450006', tag=u'n246450006')
Linkage_concept.n246451005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246451005', tag=u'n246451005')
Linkage_concept.n246452003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246452003', tag=u'n246452003')
Linkage_concept.n246453008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246453008', tag=u'n246453008')
Linkage_concept.n246454002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246454002', tag=u'n246454002')
Linkage_concept.n246456000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246456000', tag=u'n246456000')
Linkage_concept.n246457009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246457009', tag=u'n246457009')
Linkage_concept.n246458004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246458004', tag=u'n246458004')
Linkage_concept.n246459007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246459007', tag=u'n246459007')
Linkage_concept.n246460002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246460002', tag=u'n246460002')
Linkage_concept.n246461003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246461003', tag=u'n246461003')
Linkage_concept.n246462005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246462005', tag=u'n246462005')
Linkage_concept.n246463000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246463000', tag=u'n246463000')
Linkage_concept.n246468009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246468009', tag=u'n246468009')
Linkage_concept.n246469001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246469001', tag=u'n246469001')
Linkage_concept.n246470000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246470000', tag=u'n246470000')
Linkage_concept.n246471001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246471001', tag=u'n246471001')
Linkage_concept.n246472008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246472008', tag=u'n246472008')
Linkage_concept.n246474009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246474009', tag=u'n246474009')
Linkage_concept.n246475005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246475005', tag=u'n246475005')
Linkage_concept.n246476006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246476006', tag=u'n246476006')
Linkage_concept.n246477002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246477002', tag=u'n246477002')
Linkage_concept.n246478007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246478007', tag=u'n246478007')
Linkage_concept.n246479004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246479004', tag=u'n246479004')
Linkage_concept.n246480001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246480001', tag=u'n246480001')
Linkage_concept.n246481002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246481002', tag=u'n246481002')
Linkage_concept.n246482009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246482009', tag=u'n246482009')
Linkage_concept.n246483004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246483004', tag=u'n246483004')
Linkage_concept.n246484005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246484005', tag=u'n246484005')
Linkage_concept.n246485006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246485006', tag=u'n246485006')
Linkage_concept.n246486007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246486007', tag=u'n246486007')
Linkage_concept.n246487003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246487003', tag=u'n246487003')
Linkage_concept.n246488008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246488008', tag=u'n246488008')
Linkage_concept.n246489000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246489000', tag=u'n246489000')
Linkage_concept.n246490009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246490009', tag=u'n246490009')
Linkage_concept.n246491008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246491008', tag=u'n246491008')
Linkage_concept.n246492001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246492001', tag=u'n246492001')
Linkage_concept.n246493006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246493006', tag=u'n246493006')
Linkage_concept.n246494000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246494000', tag=u'n246494000')
Linkage_concept.n246495004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246495004', tag=u'n246495004')
Linkage_concept.n246496003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246496003', tag=u'n246496003')
Linkage_concept.n246497007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246497007', tag=u'n246497007')
Linkage_concept.n246498002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246498002', tag=u'n246498002')
Linkage_concept.n246499005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246499005', tag=u'n246499005')
Linkage_concept.n246500001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246500001', tag=u'n246500001')
Linkage_concept.n246501002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246501002', tag=u'n246501002')
Linkage_concept.n246508008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246508008', tag=u'n246508008')
Linkage_concept.n246509000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246509000', tag=u'n246509000')
Linkage_concept.n246510005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246510005', tag=u'n246510005')
Linkage_concept.n246512002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246512002', tag=u'n246512002')
Linkage_concept.n246513007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246513007', tag=u'n246513007')
Linkage_concept.n246514001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246514001', tag=u'n246514001')
Linkage_concept.n246515000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246515000', tag=u'n246515000')
Linkage_concept.n246516004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246516004', tag=u'n246516004')
Linkage_concept.n246517008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'246517008', tag=u'n246517008')
Linkage_concept.n255234002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'255234002', tag=u'n255234002')
Linkage_concept.n255260001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'255260001', tag=u'n255260001')
Linkage_concept.n255460003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'255460003', tag=u'n255460003')
Linkage_concept.n255711007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'255711007', tag=u'n255711007')
Linkage_concept.n258214002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'258214002', tag=u'n258214002')
Linkage_concept.n260225008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260225008', tag=u'n260225008')
Linkage_concept.n260507000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260507000', tag=u'n260507000')
Linkage_concept.n260664000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260664000', tag=u'n260664000')
Linkage_concept.n260671005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260671005', tag=u'n260671005')
Linkage_concept.n260672003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260672003', tag=u'n260672003')
Linkage_concept.n260673008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260673008', tag=u'n260673008')
Linkage_concept.n260674002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260674002', tag=u'n260674002')
Linkage_concept.n260676000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260676000', tag=u'n260676000')
Linkage_concept.n260677009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260677009', tag=u'n260677009')
Linkage_concept.n260678004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260678004', tag=u'n260678004')
Linkage_concept.n260679007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260679007', tag=u'n260679007')
Linkage_concept.n260680005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260680005', tag=u'n260680005')
Linkage_concept.n260681009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260681009', tag=u'n260681009')
Linkage_concept.n260682002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260682002', tag=u'n260682002')
Linkage_concept.n260683007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260683007', tag=u'n260683007')
Linkage_concept.n260684001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260684001', tag=u'n260684001')
Linkage_concept.n260685000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260685000', tag=u'n260685000')
Linkage_concept.n260686004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260686004', tag=u'n260686004')
Linkage_concept.n260687008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260687008', tag=u'n260687008')
Linkage_concept.n260695007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260695007', tag=u'n260695007')
Linkage_concept.n260697004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260697004', tag=u'n260697004')
Linkage_concept.n260698009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260698009', tag=u'n260698009')
Linkage_concept.n260699001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260699001', tag=u'n260699001')
Linkage_concept.n260701001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260701001', tag=u'n260701001')
Linkage_concept.n260703003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260703003', tag=u'n260703003')
Linkage_concept.n260704009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260704009', tag=u'n260704009')
Linkage_concept.n260705005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260705005', tag=u'n260705005')
Linkage_concept.n260706006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260706006', tag=u'n260706006')
Linkage_concept.n260707002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260707002', tag=u'n260707002')
Linkage_concept.n260708007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260708007', tag=u'n260708007')
Linkage_concept.n260709004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260709004', tag=u'n260709004')
Linkage_concept.n260711008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260711008', tag=u'n260711008')
Linkage_concept.n260713006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260713006', tag=u'n260713006')
Linkage_concept.n260714000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260714000', tag=u'n260714000')
Linkage_concept.n260715004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260715004', tag=u'n260715004')
Linkage_concept.n260716003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260716003', tag=u'n260716003')
Linkage_concept.n260717007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260717007', tag=u'n260717007')
Linkage_concept.n260718002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260718002', tag=u'n260718002')
Linkage_concept.n260719005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260719005', tag=u'n260719005')
Linkage_concept.n260720004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260720004', tag=u'n260720004')
Linkage_concept.n260721000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260721000', tag=u'n260721000')
Linkage_concept.n260722007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260722007', tag=u'n260722007')
Linkage_concept.n260723002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260723002', tag=u'n260723002')
Linkage_concept.n260724008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260724008', tag=u'n260724008')
Linkage_concept.n260726005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260726005', tag=u'n260726005')
Linkage_concept.n260727001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260727001', tag=u'n260727001')
Linkage_concept.n260728006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260728006', tag=u'n260728006')
Linkage_concept.n260730008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260730008', tag=u'n260730008')
Linkage_concept.n260731007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260731007', tag=u'n260731007')
Linkage_concept.n260732000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260732000', tag=u'n260732000')
Linkage_concept.n260733005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260733005', tag=u'n260733005')
Linkage_concept.n260734004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260734004', tag=u'n260734004')
Linkage_concept.n260735003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260735003', tag=u'n260735003')
Linkage_concept.n260736002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260736002', tag=u'n260736002')
Linkage_concept.n260737006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260737006', tag=u'n260737006')
Linkage_concept.n260738001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260738001', tag=u'n260738001')
Linkage_concept.n260739009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260739009', tag=u'n260739009')
Linkage_concept.n260740006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260740006', tag=u'n260740006')
Linkage_concept.n260741005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260741005', tag=u'n260741005')
Linkage_concept.n260742003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260742003', tag=u'n260742003')
Linkage_concept.n260743008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260743008', tag=u'n260743008')
Linkage_concept.n260744002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260744002', tag=u'n260744002')
Linkage_concept.n260745001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260745001', tag=u'n260745001')
Linkage_concept.n260746000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260746000', tag=u'n260746000')
Linkage_concept.n260747009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260747009', tag=u'n260747009')
Linkage_concept.n260748004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260748004', tag=u'n260748004')
Linkage_concept.n260749007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260749007', tag=u'n260749007')
Linkage_concept.n260750007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260750007', tag=u'n260750007')
Linkage_concept.n260751006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260751006', tag=u'n260751006')
Linkage_concept.n260752004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260752004', tag=u'n260752004')
Linkage_concept.n260753009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260753009', tag=u'n260753009')
Linkage_concept.n260754003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260754003', tag=u'n260754003')
Linkage_concept.n260755002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260755002', tag=u'n260755002')
Linkage_concept.n260756001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260756001', tag=u'n260756001')
Linkage_concept.n260757005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260757005', tag=u'n260757005')
Linkage_concept.n260758000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260758000', tag=u'n260758000')
Linkage_concept.n260759008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260759008', tag=u'n260759008')
Linkage_concept.n260760003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260760003', tag=u'n260760003')
Linkage_concept.n260761004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260761004', tag=u'n260761004')
Linkage_concept.n260762006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260762006', tag=u'n260762006')
Linkage_concept.n260763001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260763001', tag=u'n260763001')
Linkage_concept.n260764007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260764007', tag=u'n260764007')
Linkage_concept.n260765008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260765008', tag=u'n260765008')
Linkage_concept.n260766009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260766009', tag=u'n260766009')
Linkage_concept.n260767000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260767000', tag=u'n260767000')
Linkage_concept.n260768005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260768005', tag=u'n260768005')
Linkage_concept.n260770001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260770001', tag=u'n260770001')
Linkage_concept.n260771002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260771002', tag=u'n260771002')
Linkage_concept.n260772009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260772009', tag=u'n260772009')
Linkage_concept.n260774005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260774005', tag=u'n260774005')
Linkage_concept.n260775006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260775006', tag=u'n260775006')
Linkage_concept.n260776007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260776007', tag=u'n260776007')
Linkage_concept.n260780002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260780002', tag=u'n260780002')
Linkage_concept.n260781003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260781003', tag=u'n260781003')
Linkage_concept.n260782005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260782005', tag=u'n260782005')
Linkage_concept.n260783000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260783000', tag=u'n260783000')
Linkage_concept.n260784006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260784006', tag=u'n260784006')
Linkage_concept.n260785007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260785007', tag=u'n260785007')
Linkage_concept.n260788009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260788009', tag=u'n260788009')
Linkage_concept.n260790005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260790005', tag=u'n260790005')
Linkage_concept.n260791009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260791009', tag=u'n260791009')
Linkage_concept.n260792002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260792002', tag=u'n260792002')
Linkage_concept.n260793007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260793007', tag=u'n260793007')
Linkage_concept.n260794001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260794001', tag=u'n260794001')
Linkage_concept.n260795000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260795000', tag=u'n260795000')
Linkage_concept.n260796004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260796004', tag=u'n260796004')
Linkage_concept.n260797008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260797008', tag=u'n260797008')
Linkage_concept.n260798003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260798003', tag=u'n260798003')
Linkage_concept.n260799006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260799006', tag=u'n260799006')
Linkage_concept.n260800005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260800005', tag=u'n260800005')
Linkage_concept.n260801009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260801009', tag=u'n260801009')
Linkage_concept.n260802002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260802002', tag=u'n260802002')
Linkage_concept.n260803007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260803007', tag=u'n260803007')
Linkage_concept.n260804001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260804001', tag=u'n260804001')
Linkage_concept.n260805000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260805000', tag=u'n260805000')
Linkage_concept.n260806004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260806004', tag=u'n260806004')
Linkage_concept.n260807008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260807008', tag=u'n260807008')
Linkage_concept.n260808003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260808003', tag=u'n260808003')
Linkage_concept.n260809006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260809006', tag=u'n260809006')
Linkage_concept.n260810001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260810001', tag=u'n260810001')
Linkage_concept.n260811002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260811002', tag=u'n260811002')
Linkage_concept.n260812009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260812009', tag=u'n260812009')
Linkage_concept.n260813004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260813004', tag=u'n260813004')
Linkage_concept.n260814005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260814005', tag=u'n260814005')
Linkage_concept.n260815006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260815006', tag=u'n260815006')
Linkage_concept.n260816007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260816007', tag=u'n260816007')
Linkage_concept.n260817003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260817003', tag=u'n260817003')
Linkage_concept.n260818008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260818008', tag=u'n260818008')
Linkage_concept.n260819000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260819000', tag=u'n260819000')
Linkage_concept.n260820006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260820006', tag=u'n260820006')
Linkage_concept.n260821005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260821005', tag=u'n260821005')
Linkage_concept.n260822003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260822003', tag=u'n260822003')
Linkage_concept.n260823008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260823008', tag=u'n260823008')
Linkage_concept.n260824002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260824002', tag=u'n260824002')
Linkage_concept.n260826000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260826000', tag=u'n260826000')
Linkage_concept.n260827009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260827009', tag=u'n260827009')
Linkage_concept.n260828004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260828004', tag=u'n260828004')
Linkage_concept.n260829007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260829007', tag=u'n260829007')
Linkage_concept.n260830002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260830002', tag=u'n260830002')
Linkage_concept.n260831003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260831003', tag=u'n260831003')
Linkage_concept.n260832005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260832005', tag=u'n260832005')
Linkage_concept.n260833000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260833000', tag=u'n260833000')
Linkage_concept.n260834006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260834006', tag=u'n260834006')
Linkage_concept.n260835007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260835007', tag=u'n260835007')
Linkage_concept.n260836008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260836008', tag=u'n260836008')
Linkage_concept.n260837004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260837004', tag=u'n260837004')
Linkage_concept.n260838009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260838009', tag=u'n260838009')
Linkage_concept.n260839001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260839001', tag=u'n260839001')
Linkage_concept.n260840004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260840004', tag=u'n260840004')
Linkage_concept.n260841000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260841000', tag=u'n260841000')
Linkage_concept.n260842007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260842007', tag=u'n260842007')
Linkage_concept.n260843002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260843002', tag=u'n260843002')
Linkage_concept.n260844008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260844008', tag=u'n260844008')
Linkage_concept.n260845009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260845009', tag=u'n260845009')
Linkage_concept.n260846005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260846005', tag=u'n260846005')
Linkage_concept.n260847001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260847001', tag=u'n260847001')
Linkage_concept.n260848006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260848006', tag=u'n260848006')
Linkage_concept.n260849003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260849003', tag=u'n260849003')
Linkage_concept.n260850003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260850003', tag=u'n260850003')
Linkage_concept.n260851004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260851004', tag=u'n260851004')
Linkage_concept.n260852006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260852006', tag=u'n260852006')
Linkage_concept.n260853001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260853001', tag=u'n260853001')
Linkage_concept.n260854007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260854007', tag=u'n260854007')
Linkage_concept.n260855008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260855008', tag=u'n260855008')
Linkage_concept.n260856009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260856009', tag=u'n260856009')
Linkage_concept.n260857000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260857000', tag=u'n260857000')
Linkage_concept.n260858005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260858005', tag=u'n260858005')
Linkage_concept.n260859002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260859002', tag=u'n260859002')
Linkage_concept.n260860007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260860007', tag=u'n260860007')
Linkage_concept.n260861006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260861006', tag=u'n260861006')
Linkage_concept.n260862004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260862004', tag=u'n260862004')
Linkage_concept.n260863009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260863009', tag=u'n260863009')
Linkage_concept.n260864003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260864003', tag=u'n260864003')
Linkage_concept.n260865002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260865002', tag=u'n260865002')
Linkage_concept.n260866001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260866001', tag=u'n260866001')
Linkage_concept.n260868000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260868000', tag=u'n260868000')
Linkage_concept.n260869008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260869008', tag=u'n260869008')
Linkage_concept.n260870009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260870009', tag=u'n260870009')
Linkage_concept.n260871008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260871008', tag=u'n260871008')
Linkage_concept.n260872001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260872001', tag=u'n260872001')
Linkage_concept.n260873006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260873006', tag=u'n260873006')
Linkage_concept.n260874000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260874000', tag=u'n260874000')
Linkage_concept.n260875004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260875004', tag=u'n260875004')
Linkage_concept.n260876003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260876003', tag=u'n260876003')
Linkage_concept.n260878002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260878002', tag=u'n260878002')
Linkage_concept.n260879005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260879005', tag=u'n260879005')
Linkage_concept.n260880008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260880008', tag=u'n260880008')
Linkage_concept.n260881007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260881007', tag=u'n260881007')
Linkage_concept.n260882000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260882000', tag=u'n260882000')
Linkage_concept.n260883005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260883005', tag=u'n260883005')
Linkage_concept.n260884004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260884004', tag=u'n260884004')
Linkage_concept.n260885003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260885003', tag=u'n260885003')
Linkage_concept.n260886002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260886002', tag=u'n260886002')
Linkage_concept.n260887006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260887006', tag=u'n260887006')
Linkage_concept.n260888001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260888001', tag=u'n260888001')
Linkage_concept.n260890000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260890000', tag=u'n260890000')
Linkage_concept.n260891001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260891001', tag=u'n260891001')
Linkage_concept.n260892008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260892008', tag=u'n260892008')
Linkage_concept.n260893003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260893003', tag=u'n260893003')
Linkage_concept.n260894009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260894009', tag=u'n260894009')
Linkage_concept.n260895005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260895005', tag=u'n260895005')
Linkage_concept.n260896006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260896006', tag=u'n260896006')
Linkage_concept.n260897002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260897002', tag=u'n260897002')
Linkage_concept.n260898007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260898007', tag=u'n260898007')
Linkage_concept.n260899004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260899004', tag=u'n260899004')
Linkage_concept.n260900009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260900009', tag=u'n260900009')
Linkage_concept.n260902001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260902001', tag=u'n260902001')
Linkage_concept.n260903006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260903006', tag=u'n260903006')
Linkage_concept.n260904000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260904000', tag=u'n260904000')
Linkage_concept.n260905004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260905004', tag=u'n260905004')
Linkage_concept.n260906003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260906003', tag=u'n260906003')
Linkage_concept.n260907007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260907007', tag=u'n260907007')
Linkage_concept.n260909005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260909005', tag=u'n260909005')
Linkage_concept.n260910000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260910000', tag=u'n260910000')
Linkage_concept.n260911001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260911001', tag=u'n260911001')
Linkage_concept.n260913003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260913003', tag=u'n260913003')
Linkage_concept.n260914009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260914009', tag=u'n260914009')
Linkage_concept.n260915005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260915005', tag=u'n260915005')
Linkage_concept.n260916006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260916006', tag=u'n260916006')
Linkage_concept.n260917002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260917002', tag=u'n260917002')
Linkage_concept.n260918007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260918007', tag=u'n260918007')
Linkage_concept.n260919004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260919004', tag=u'n260919004')
Linkage_concept.n260920005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260920005', tag=u'n260920005')
Linkage_concept.n260921009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260921009', tag=u'n260921009')
Linkage_concept.n260922002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260922002', tag=u'n260922002')
Linkage_concept.n260923007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260923007', tag=u'n260923007')
Linkage_concept.n260924001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260924001', tag=u'n260924001')
Linkage_concept.n260925000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260925000', tag=u'n260925000')
Linkage_concept.n260926004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260926004', tag=u'n260926004')
Linkage_concept.n260928003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260928003', tag=u'n260928003')
Linkage_concept.n260929006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260929006', tag=u'n260929006')
Linkage_concept.n260930001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260930001', tag=u'n260930001')
Linkage_concept.n260932009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260932009', tag=u'n260932009')
Linkage_concept.n260933004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260933004', tag=u'n260933004')
Linkage_concept.n260934005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260934005', tag=u'n260934005')
Linkage_concept.n260935006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260935006', tag=u'n260935006')
Linkage_concept.n260936007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260936007', tag=u'n260936007')
Linkage_concept.n260937003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260937003', tag=u'n260937003')
Linkage_concept.n260938008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260938008', tag=u'n260938008')
Linkage_concept.n260939000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260939000', tag=u'n260939000')
Linkage_concept.n260940003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260940003', tag=u'n260940003')
Linkage_concept.n260941004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260941004', tag=u'n260941004')
Linkage_concept.n260942006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260942006', tag=u'n260942006')
Linkage_concept.n260944007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260944007', tag=u'n260944007')
Linkage_concept.n260945008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260945008', tag=u'n260945008')
Linkage_concept.n260946009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260946009', tag=u'n260946009')
Linkage_concept.n260947000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260947000', tag=u'n260947000')
Linkage_concept.n260949002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260949002', tag=u'n260949002')
Linkage_concept.n260950002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260950002', tag=u'n260950002')
Linkage_concept.n260973005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260973005', tag=u'n260973005')
Linkage_concept.n260974004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260974004', tag=u'n260974004')
Linkage_concept.n260977006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260977006', tag=u'n260977006')
Linkage_concept.n260978001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260978001', tag=u'n260978001')
Linkage_concept.n260979009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'260979009', tag=u'n260979009')
Linkage_concept.n261217004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'261217004', tag=u'n261217004')
Linkage_concept.n263485007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263485007', tag=u'n263485007')
Linkage_concept.n263486008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263486008', tag=u'n263486008')
Linkage_concept.n263488009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263488009', tag=u'n263488009')
Linkage_concept.n263490005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263490005', tag=u'n263490005')
Linkage_concept.n263491009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263491009', tag=u'n263491009')
Linkage_concept.n263492002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263492002', tag=u'n263492002')
Linkage_concept.n263493007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263493007', tag=u'n263493007')
Linkage_concept.n263494001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263494001', tag=u'n263494001')
Linkage_concept.n263496004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263496004', tag=u'n263496004')
Linkage_concept.n263497008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263497008', tag=u'n263497008')
Linkage_concept.n263498003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263498003', tag=u'n263498003')
Linkage_concept.n263499006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263499006', tag=u'n263499006')
Linkage_concept.n263502005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263502005', tag=u'n263502005')
Linkage_concept.n263503000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263503000', tag=u'n263503000')
Linkage_concept.n263504006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263504006', tag=u'n263504006')
Linkage_concept.n263505007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263505007', tag=u'n263505007')
Linkage_concept.n263506008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263506008', tag=u'n263506008')
Linkage_concept.n263507004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263507004', tag=u'n263507004')
Linkage_concept.n263508009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263508009', tag=u'n263508009')
Linkage_concept.n263509001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263509001', tag=u'n263509001')
Linkage_concept.n263510006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263510006', tag=u'n263510006')
Linkage_concept.n263511005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263511005', tag=u'n263511005')
Linkage_concept.n263514002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263514002', tag=u'n263514002')
Linkage_concept.n263515001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263515001', tag=u'n263515001')
Linkage_concept.n263516000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263516000', tag=u'n263516000')
Linkage_concept.n263517009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263517009', tag=u'n263517009')
Linkage_concept.n263518004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263518004', tag=u'n263518004')
Linkage_concept.n263519007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263519007', tag=u'n263519007')
Linkage_concept.n263520001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263520001', tag=u'n263520001')
Linkage_concept.n263521002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263521002', tag=u'n263521002')
Linkage_concept.n263522009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263522009', tag=u'n263522009')
Linkage_concept.n263523004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263523004', tag=u'n263523004')
Linkage_concept.n263524005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263524005', tag=u'n263524005')
Linkage_concept.n263525006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263525006', tag=u'n263525006')
Linkage_concept.n263526007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263526007', tag=u'n263526007')
Linkage_concept.n263527003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263527003', tag=u'n263527003')
Linkage_concept.n263528008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263528008', tag=u'n263528008')
Linkage_concept.n263529000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263529000', tag=u'n263529000')
Linkage_concept.n263530005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263530005', tag=u'n263530005')
Linkage_concept.n263531009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263531009', tag=u'n263531009')
Linkage_concept.n263532002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263532002', tag=u'n263532002')
Linkage_concept.n263533007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263533007', tag=u'n263533007')
Linkage_concept.n263534001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263534001', tag=u'n263534001')
Linkage_concept.n263535000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263535000', tag=u'n263535000')
Linkage_concept.n263536004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263536004', tag=u'n263536004')
Linkage_concept.n263538003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263538003', tag=u'n263538003')
Linkage_concept.n263539006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263539006', tag=u'n263539006')
Linkage_concept.n263540008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263540008', tag=u'n263540008')
Linkage_concept.n263541007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263541007', tag=u'n263541007')
Linkage_concept.n263542000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263542000', tag=u'n263542000')
Linkage_concept.n263543005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263543005', tag=u'n263543005')
Linkage_concept.n263544004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263544004', tag=u'n263544004')
Linkage_concept.n263545003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263545003', tag=u'n263545003')
Linkage_concept.n263546002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263546002', tag=u'n263546002')
Linkage_concept.n263547006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263547006', tag=u'n263547006')
Linkage_concept.n263548001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263548001', tag=u'n263548001')
Linkage_concept.n263549009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263549009', tag=u'n263549009')
Linkage_concept.n263550009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263550009', tag=u'n263550009')
Linkage_concept.n263551008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263551008', tag=u'n263551008')
Linkage_concept.n263552001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263552001', tag=u'n263552001')
Linkage_concept.n263553006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263553006', tag=u'n263553006')
Linkage_concept.n263554000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263554000', tag=u'n263554000')
Linkage_concept.n263555004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263555004', tag=u'n263555004')
Linkage_concept.n263556003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263556003', tag=u'n263556003')
Linkage_concept.n263557007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263557007', tag=u'n263557007')
Linkage_concept.n263558002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263558002', tag=u'n263558002')
Linkage_concept.n263559005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263559005', tag=u'n263559005')
Linkage_concept.n263560000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263560000', tag=u'n263560000')
Linkage_concept.n263561001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263561001', tag=u'n263561001')
Linkage_concept.n263562008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263562008', tag=u'n263562008')
Linkage_concept.n263563003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263563003', tag=u'n263563003')
Linkage_concept.n263564009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263564009', tag=u'n263564009')
Linkage_concept.n263565005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263565005', tag=u'n263565005')
Linkage_concept.n263566006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263566006', tag=u'n263566006')
Linkage_concept.n263567002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263567002', tag=u'n263567002')
Linkage_concept.n263568007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263568007', tag=u'n263568007')
Linkage_concept.n263569004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263569004', tag=u'n263569004')
Linkage_concept.n263570003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263570003', tag=u'n263570003')
Linkage_concept.n263571004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263571004', tag=u'n263571004')
Linkage_concept.n263572006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263572006', tag=u'n263572006')
Linkage_concept.n263573001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263573001', tag=u'n263573001')
Linkage_concept.n263574007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263574007', tag=u'n263574007')
Linkage_concept.n263575008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263575008', tag=u'n263575008')
Linkage_concept.n263576009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263576009', tag=u'n263576009')
Linkage_concept.n263577000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263577000', tag=u'n263577000')
Linkage_concept.n263578005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263578005', tag=u'n263578005')
Linkage_concept.n263579002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263579002', tag=u'n263579002')
Linkage_concept.n263580004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263580004', tag=u'n263580004')
Linkage_concept.n263581000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263581000', tag=u'n263581000')
Linkage_concept.n263582007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263582007', tag=u'n263582007')
Linkage_concept.n263583002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263583002', tag=u'n263583002')
Linkage_concept.n263584008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263584008', tag=u'n263584008')
Linkage_concept.n263585009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263585009', tag=u'n263585009')
Linkage_concept.n263586005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263586005', tag=u'n263586005')
Linkage_concept.n263587001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263587001', tag=u'n263587001')
Linkage_concept.n263588006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263588006', tag=u'n263588006')
Linkage_concept.n263589003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263589003', tag=u'n263589003')
Linkage_concept.n263590007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263590007', tag=u'n263590007')
Linkage_concept.n263591006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263591006', tag=u'n263591006')
Linkage_concept.n263592004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263592004', tag=u'n263592004')
Linkage_concept.n263593009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263593009', tag=u'n263593009')
Linkage_concept.n263594003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263594003', tag=u'n263594003')
Linkage_concept.n263595002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263595002', tag=u'n263595002')
Linkage_concept.n263596001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263596001', tag=u'n263596001')
Linkage_concept.n263597005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263597005', tag=u'n263597005')
Linkage_concept.n263598000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263598000', tag=u'n263598000')
Linkage_concept.n263599008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263599008', tag=u'n263599008')
Linkage_concept.n263600006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263600006', tag=u'n263600006')
Linkage_concept.n263601005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263601005', tag=u'n263601005')
Linkage_concept.n263602003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263602003', tag=u'n263602003')
Linkage_concept.n263603008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263603008', tag=u'n263603008')
Linkage_concept.n263606000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263606000', tag=u'n263606000')
Linkage_concept.n263607009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263607009', tag=u'n263607009')
Linkage_concept.n263608004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263608004', tag=u'n263608004')
Linkage_concept.n263609007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263609007', tag=u'n263609007')
Linkage_concept.n263610002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263610002', tag=u'n263610002')
Linkage_concept.n263619001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263619001', tag=u'n263619001')
Linkage_concept.n263620007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263620007', tag=u'n263620007')
Linkage_concept.n263621006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263621006', tag=u'n263621006')
Linkage_concept.n263622004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263622004', tag=u'n263622004')
Linkage_concept.n263623009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263623009', tag=u'n263623009')
Linkage_concept.n263624003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263624003', tag=u'n263624003')
Linkage_concept.n263625002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263625002', tag=u'n263625002')
Linkage_concept.n263628000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263628000', tag=u'n263628000')
Linkage_concept.n263629008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263629008', tag=u'n263629008')
Linkage_concept.n263630003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263630003', tag=u'n263630003')
Linkage_concept.n263631004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263631004', tag=u'n263631004')
Linkage_concept.n263632006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263632006', tag=u'n263632006')
Linkage_concept.n263633001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263633001', tag=u'n263633001')
Linkage_concept.n263635008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263635008', tag=u'n263635008')
Linkage_concept.n263636009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263636009', tag=u'n263636009')
Linkage_concept.n263637000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263637000', tag=u'n263637000')
Linkage_concept.n263639002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263639002', tag=u'n263639002')
Linkage_concept.n263640000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263640000', tag=u'n263640000')
Linkage_concept.n263641001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263641001', tag=u'n263641001')
Linkage_concept.n263642008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263642008', tag=u'n263642008')
Linkage_concept.n263643003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263643003', tag=u'n263643003')
Linkage_concept.n263644009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263644009', tag=u'n263644009')
Linkage_concept.n263645005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263645005', tag=u'n263645005')
Linkage_concept.n263646006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263646006', tag=u'n263646006')
Linkage_concept.n263647002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263647002', tag=u'n263647002')
Linkage_concept.n263648007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263648007', tag=u'n263648007')
Linkage_concept.n263649004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263649004', tag=u'n263649004')
Linkage_concept.n263718001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'263718001', tag=u'n263718001')
Linkage_concept.n264921002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'264921002', tag=u'n264921002')
Linkage_concept.n272732008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272732008', tag=u'n272732008')
Linkage_concept.n272733003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272733003', tag=u'n272733003')
Linkage_concept.n272734009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272734009', tag=u'n272734009')
Linkage_concept.n272735005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272735005', tag=u'n272735005')
Linkage_concept.n272736006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272736006', tag=u'n272736006')
Linkage_concept.n272737002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272737002', tag=u'n272737002')
Linkage_concept.n272739004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272739004', tag=u'n272739004')
Linkage_concept.n272741003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272741003', tag=u'n272741003')
Linkage_concept.n272742005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'272742005', tag=u'n272742005')
Linkage_concept.n273248003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'273248003', tag=u'n273248003')
Linkage_concept.n276131009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276131009', tag=u'n276131009')
Linkage_concept.n276132002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276132002', tag=u'n276132002')
Linkage_concept.n276133007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276133007', tag=u'n276133007')
Linkage_concept.n276134001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276134001', tag=u'n276134001')
Linkage_concept.n276625007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276625007', tag=u'n276625007')
Linkage_concept.n276626008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276626008', tag=u'n276626008')
Linkage_concept.n276731003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276731003', tag=u'n276731003')
Linkage_concept.n276820004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276820004', tag=u'n276820004')
Linkage_concept.n276823002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276823002', tag=u'n276823002')
Linkage_concept.n276824008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276824008', tag=u'n276824008')
Linkage_concept.n276989002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'276989002', tag=u'n276989002')
Linkage_concept.n277035007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277035007', tag=u'n277035007')
Linkage_concept.n277037004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277037004', tag=u'n277037004')
Linkage_concept.n277038009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277038009', tag=u'n277038009')
Linkage_concept.n277039001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277039001', tag=u'n277039001')
Linkage_concept.n277040004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277040004', tag=u'n277040004')
Linkage_concept.n277041000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277041000', tag=u'n277041000')
Linkage_concept.n277042007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277042007', tag=u'n277042007')
Linkage_concept.n277043002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277043002', tag=u'n277043002')
Linkage_concept.n277044008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277044008', tag=u'n277044008')
Linkage_concept.n277045009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277045009', tag=u'n277045009')
Linkage_concept.n277046005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277046005', tag=u'n277046005')
Linkage_concept.n277047001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277047001', tag=u'n277047001')
Linkage_concept.n277052006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277052006', tag=u'n277052006')
Linkage_concept.n277053001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277053001', tag=u'n277053001')
Linkage_concept.n277054007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277054007', tag=u'n277054007')
Linkage_concept.n277055008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277055008', tag=u'n277055008')
Linkage_concept.n277058005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277058005', tag=u'n277058005')
Linkage_concept.n277059002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277059002', tag=u'n277059002')
Linkage_concept.n277060007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277060007', tag=u'n277060007')
Linkage_concept.n277061006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277061006', tag=u'n277061006')
Linkage_concept.n277062004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277062004', tag=u'n277062004')
Linkage_concept.n277063009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277063009', tag=u'n277063009')
Linkage_concept.n277064003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277064003', tag=u'n277064003')
Linkage_concept.n277097002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277097002', tag=u'n277097002')
Linkage_concept.n277327002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277327002', tag=u'n277327002')
Linkage_concept.n277334000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277334000', tag=u'n277334000')
Linkage_concept.n277335004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277335004', tag=u'n277335004')
Linkage_concept.n277405005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277405005', tag=u'n277405005')
Linkage_concept.n277640000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277640000', tag=u'n277640000')
Linkage_concept.n277655009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277655009', tag=u'n277655009')
Linkage_concept.n277795004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277795004', tag=u'n277795004')
Linkage_concept.n277889008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'277889008', tag=u'n277889008')
Linkage_concept.n278109006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278109006', tag=u'n278109006')
Linkage_concept.n278111002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278111002', tag=u'n278111002')
Linkage_concept.n278112009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278112009', tag=u'n278112009')
Linkage_concept.n278114005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278114005', tag=u'n278114005')
Linkage_concept.n278115006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278115006', tag=u'n278115006')
Linkage_concept.n278144008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278144008', tag=u'n278144008')
Linkage_concept.n278155008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278155008', tag=u'n278155008')
Linkage_concept.n278156009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278156009', tag=u'n278156009')
Linkage_concept.n278157000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278157000', tag=u'n278157000')
Linkage_concept.n278158005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278158005', tag=u'n278158005')
Linkage_concept.n278174000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278174000', tag=u'n278174000')
Linkage_concept.n278176003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278176003', tag=u'n278176003')
Linkage_concept.n278200001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278200001', tag=u'n278200001')
Linkage_concept.n278201002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278201002', tag=u'n278201002')
Linkage_concept.n278230009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278230009', tag=u'n278230009')
Linkage_concept.n278269003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278269003', tag=u'n278269003')
Linkage_concept.n278483003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278483003', tag=u'n278483003')
Linkage_concept.n278863006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278863006', tag=u'n278863006')
Linkage_concept.n278924003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'278924003', tag=u'n278924003')
Linkage_concept.n279114001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'279114001', tag=u'n279114001')
Linkage_concept.n279116004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'279116004', tag=u'n279116004')
Linkage_concept.n279229007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'279229007', tag=u'n279229007')
Linkage_concept.n279230002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'279230002', tag=u'n279230002')
Linkage_concept.n280145001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'280145001', tag=u'n280145001')
Linkage_concept.n280147009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'280147009', tag=u'n280147009')
Linkage_concept.n280452008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'280452008', tag=u'n280452008')
Linkage_concept.n280942002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'280942002', tag=u'n280942002')
Linkage_concept.n281041004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281041004', tag=u'n281041004')
Linkage_concept.n281256003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281256003', tag=u'n281256003')
Linkage_concept.n281308007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281308007', tag=u'n281308007')
Linkage_concept.n281343008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281343008', tag=u'n281343008')
Linkage_concept.n281355002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281355002', tag=u'n281355002')
Linkage_concept.n281403002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281403002', tag=u'n281403002')
Linkage_concept.n281407001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281407001', tag=u'n281407001')
Linkage_concept.n281947003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281947003', tag=u'n281947003')
Linkage_concept.n281948008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'281948008', tag=u'n281948008')
Linkage_concept.n282006001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'282006001', tag=u'n282006001')
Linkage_concept.n282079007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'282079007', tag=u'n282079007')
Linkage_concept.n284663008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'284663008', tag=u'n284663008')
Linkage_concept.n285705001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'285705001', tag=u'n285705001')
Linkage_concept.n288508002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'288508002', tag=u'n288508002')
Linkage_concept.n288556008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'288556008', tag=u'n288556008')
Linkage_concept.n288829000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'288829000', tag=u'n288829000')
Linkage_concept.n288830005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'288830005', tag=u'n288830005')
Linkage_concept.n297203006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'297203006', tag=u'n297203006')
Linkage_concept.n297939008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'297939008', tag=u'n297939008')
Linkage_concept.n300591002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300591002', tag=u'n300591002')
Linkage_concept.n300592009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300592009', tag=u'n300592009')
Linkage_concept.n300594005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300594005', tag=u'n300594005')
Linkage_concept.n300596007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300596007', tag=u'n300596007')
Linkage_concept.n300819009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300819009', tag=u'n300819009')
Linkage_concept.n300842002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'300842002', tag=u'n300842002')
Linkage_concept.n303221006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'303221006', tag=u'n303221006')
Linkage_concept.n306987005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'306987005', tag=u'n306987005')
Linkage_concept.n309824003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'309824003', tag=u'n309824003')
Linkage_concept.n311788003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'311788003', tag=u'n311788003')
Linkage_concept.n313044005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'313044005', tag=u'n313044005')
Linkage_concept.n313067007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'313067007', tag=u'n313067007')
Linkage_concept.n313136007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'313136007', tag=u'n313136007')
Linkage_concept.n363589002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363589002', tag=u'n363589002')
Linkage_concept.n363698007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363698007', tag=u'n363698007')
Linkage_concept.n363699004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363699004', tag=u'n363699004')
Linkage_concept.n363700003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363700003', tag=u'n363700003')
Linkage_concept.n363701004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363701004', tag=u'n363701004')
Linkage_concept.n363702006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363702006', tag=u'n363702006')
Linkage_concept.n363703001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363703001', tag=u'n363703001')
Linkage_concept.n363704007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363704007', tag=u'n363704007')
Linkage_concept.n363705008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363705008', tag=u'n363705008')
Linkage_concept.n363706009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363706009', tag=u'n363706009')
Linkage_concept.n363707000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363707000', tag=u'n363707000')
Linkage_concept.n363708005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363708005', tag=u'n363708005')
Linkage_concept.n363709002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363709002', tag=u'n363709002')
Linkage_concept.n363710007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363710007', tag=u'n363710007')
Linkage_concept.n363711006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363711006', tag=u'n363711006')
Linkage_concept.n363712004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363712004', tag=u'n363712004')
Linkage_concept.n363713009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363713009', tag=u'n363713009')
Linkage_concept.n363714003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363714003', tag=u'n363714003')
Linkage_concept.n363715002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'363715002', tag=u'n363715002')
Linkage_concept.n367324007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367324007', tag=u'n367324007')
Linkage_concept.n367326009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367326009', tag=u'n367326009')
Linkage_concept.n367327000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367327000', tag=u'n367327000')
Linkage_concept.n367346004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367346004', tag=u'n367346004')
Linkage_concept.n367409002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367409002', tag=u'n367409002')
Linkage_concept.n367565008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'367565008', tag=u'n367565008')
Linkage_concept.n370124000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370124000', tag=u'n370124000')
Linkage_concept.n370125004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370125004', tag=u'n370125004')
Linkage_concept.n370128002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370128002', tag=u'n370128002')
Linkage_concept.n370129005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370129005', tag=u'n370129005')
Linkage_concept.n370130000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370130000', tag=u'n370130000')
Linkage_concept.n370131001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370131001', tag=u'n370131001')
Linkage_concept.n370132008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370132008', tag=u'n370132008')
Linkage_concept.n370133003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370133003', tag=u'n370133003')
Linkage_concept.n370134009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370134009', tag=u'n370134009')
Linkage_concept.n370135005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'370135005', tag=u'n370135005')
Linkage_concept.n371881003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'371881003', tag=u'n371881003')
Linkage_concept.n371882005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'371882005', tag=u'n371882005')
Linkage_concept.n384598002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'384598002', tag=u'n384598002')
Linkage_concept.n385438008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385438008', tag=u'n385438008')
Linkage_concept.n385641008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385641008', tag=u'n385641008')
Linkage_concept.n385665006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385665006', tag=u'n385665006')
Linkage_concept.n385668008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385668008', tag=u'n385668008')
Linkage_concept.n385675009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385675009', tag=u'n385675009')
Linkage_concept.n385676005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'385676005', tag=u'n385676005')
Linkage_concept.n394736001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'394736001', tag=u'n394736001')
Linkage_concept.n394850002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'394850002', tag=u'n394850002')
Linkage_concept.n394851003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'394851003', tag=u'n394851003')
Linkage_concept.n394852005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'394852005', tag=u'n394852005')
Linkage_concept.n394853000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'394853000', tag=u'n394853000')
Linkage_concept.n397764000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'397764000', tag=u'n397764000')
Linkage_concept.n397987002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'397987002', tag=u'n397987002')
Linkage_concept.n398008005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398008005', tag=u'n398008005')
Linkage_concept.n398009002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398009002', tag=u'n398009002')
Linkage_concept.n398039007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398039007', tag=u'n398039007')
Linkage_concept.n398092000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398092000', tag=u'n398092000')
Linkage_concept.n398101002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398101002', tag=u'n398101002')
Linkage_concept.n398282000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398282000', tag=u'n398282000')
Linkage_concept.n398297002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'398297002', tag=u'n398297002')
Linkage_concept.n404651003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'404651003', tag=u'n404651003')
Linkage_concept.n404652005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'404652005', tag=u'n404652005')
Linkage_concept.n405662005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405662005', tag=u'n405662005')
Linkage_concept.n405671001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405671001', tag=u'n405671001')
Linkage_concept.n405683004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405683004', tag=u'n405683004')
Linkage_concept.n405813007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405813007', tag=u'n405813007')
Linkage_concept.n405814001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405814001', tag=u'n405814001')
Linkage_concept.n405815000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405815000', tag=u'n405815000')
Linkage_concept.n405816004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'405816004', tag=u'n405816004')
Linkage_concept.n406142009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'406142009', tag=u'n406142009')
Linkage_concept.n406524005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'406524005', tag=u'n406524005')
Linkage_concept.n408729009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'408729009', tag=u'n408729009')
Linkage_concept.n408730004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'408730004', tag=u'n408730004')
Linkage_concept.n408731000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'408731000', tag=u'n408731000')
Linkage_concept.n408732007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'408732007', tag=u'n408732007')
Linkage_concept.n408739003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'408739003', tag=u'n408739003')
Linkage_concept.n410608001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410608001', tag=u'n410608001')
Linkage_concept.n410610004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410610004', tag=u'n410610004')
Linkage_concept.n410612007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410612007', tag=u'n410612007')
Linkage_concept.n410615009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410615009', tag=u'n410615009')
Linkage_concept.n410616005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410616005', tag=u'n410616005')
Linkage_concept.n410618006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410618006', tag=u'n410618006')
Linkage_concept.n410653004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410653004', tag=u'n410653004')
Linkage_concept.n410654005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410654005', tag=u'n410654005')
Linkage_concept.n410657003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410657003', tag=u'n410657003')
Linkage_concept.n410658008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410658008', tag=u'n410658008')
Linkage_concept.n410660005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410660005', tag=u'n410660005')
Linkage_concept.n410662002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410662002', tag=u'n410662002')
Linkage_concept.n410663007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410663007', tag=u'n410663007')
Linkage_concept.n410665000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410665000', tag=u'n410665000')
Linkage_concept.n410666004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410666004', tag=u'n410666004')
Linkage_concept.n410667008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410667008', tag=u'n410667008')
Linkage_concept.n410670007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410670007', tag=u'n410670007')
Linkage_concept.n410671006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410671006', tag=u'n410671006')
Linkage_concept.n410673009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410673009', tag=u'n410673009')
Linkage_concept.n410675002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410675002', tag=u'n410675002')
Linkage_concept.n410677005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410677005', tag=u'n410677005')
Linkage_concept.n410678000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410678000', tag=u'n410678000')
Linkage_concept.n410680006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'410680006', tag=u'n410680006')
Linkage_concept.n411116001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'411116001', tag=u'n411116001')
Linkage_concept.n411117005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'411117005', tag=u'n411117005')
Linkage_concept.n414679000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'414679000', tag=u'n414679000')
Linkage_concept.n414680002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'414680002', tag=u'n414680002')
Linkage_concept.n416083004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'416083004', tag=u'n416083004')
Linkage_concept.n416271009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'416271009', tag=u'n416271009')
Linkage_concept.n416586004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'416586004', tag=u'n416586004')
Linkage_concept.n416698001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'416698001', tag=u'n416698001')
Linkage_concept.n416872009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'416872009', tag=u'n416872009')
Linkage_concept.n417151001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'417151001', tag=u'n417151001')
Linkage_concept.n417318003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'417318003', tag=u'n417318003')
Linkage_concept.n417569004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'417569004', tag=u'n417569004')
Linkage_concept.n418775008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'418775008', tag=u'n418775008')
Linkage_concept.n419066007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'419066007', tag=u'n419066007')
Linkage_concept.n422702001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'422702001', tag=u'n422702001')
Linkage_concept.n422809003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'422809003', tag=u'n422809003')
Linkage_concept.n424226004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424226004', tag=u'n424226004')
Linkage_concept.n424244007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424244007', tag=u'n424244007')
Linkage_concept.n424337000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424337000', tag=u'n424337000')
Linkage_concept.n424361007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424361007', tag=u'n424361007')
Linkage_concept.n424528004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424528004', tag=u'n424528004')
Linkage_concept.n424697009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424697009', tag=u'n424697009')
Linkage_concept.n424876005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'424876005', tag=u'n424876005')
Linkage_concept.n425391005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'425391005', tag=u'n425391005')
Linkage_concept.n609096000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value=u'609096000', tag=u'n609096000')
Linkage_concept._InitializeFacetMap(Linkage_concept._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Linkage_concept', Linkage_concept)

# Atomic simple type: {http://snomed.info/schema/rf2}Characteristic_type
class Characteristic_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Characteristic_type')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 5994, 4)
    _Documentation = u'\n                \n            '
Characteristic_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Characteristic_type, enum_prefix=None)
Characteristic_type.n900000000000006009 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000006009', tag=u'n900000000000006009')
Characteristic_type.n900000000000010007 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000010007', tag=u'n900000000000010007')
Characteristic_type.n900000000000011006 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000011006', tag=u'n900000000000011006')
Characteristic_type.n900000000000225001 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000225001', tag=u'n900000000000225001')
Characteristic_type.n900000000000227009 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000227009', tag=u'n900000000000227009')
Characteristic_type._InitializeFacetMap(Characteristic_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Characteristic_type', Characteristic_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Modifier
class Modifier (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Modifier')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 6042, 4)
    _Documentation = u'\n                \n            '
Modifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Modifier, enum_prefix=None)
Modifier.n900000000000451002 = Modifier._CF_enumeration.addEnumeration(unicode_value=u'900000000000451002', tag=u'n900000000000451002')
Modifier.n900000000000452009 = Modifier._CF_enumeration.addEnumeration(unicode_value=u'900000000000452009', tag=u'n900000000000452009')
Modifier._InitializeFacetMap(Modifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Modifier', Modifier)

# Atomic simple type: {http://snomed.info/schema/rf2}Identifier_scheme
class Identifier_scheme (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Identifier_scheme')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 6075, 4)
    _Documentation = u'\n                \n            '
Identifier_scheme._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Identifier_scheme, enum_prefix=None)
Identifier_scheme.n900000000000002006 = Identifier_scheme._CF_enumeration.addEnumeration(unicode_value=u'900000000000002006', tag=u'n900000000000002006')
Identifier_scheme.n900000000000294009 = Identifier_scheme._CF_enumeration.addEnumeration(unicode_value=u'900000000000294009', tag=u'n900000000000294009')
Identifier_scheme._InitializeFacetMap(Identifier_scheme._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Identifier_scheme', Identifier_scheme)

# Atomic simple type: {http://snomed.info/schema/rf2}Reference_set
class Reference_set (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Reference_set')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 6108, 4)
    _Documentation = u'\n                \n            '
Reference_set._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Reference_set, enum_prefix=None)
Reference_set.n446608001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'446608001', tag=u'n446608001')
Reference_set.n446609009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'446609009', tag=u'n446609009')
Reference_set.n447250001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447250001', tag=u'n447250001')
Reference_set.n447258008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447258008', tag=u'n447258008')
Reference_set.n447562003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447562003', tag=u'n447562003')
Reference_set.n447563008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447563008', tag=u'n447563008')
Reference_set.n447565001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447565001', tag=u'n447565001')
Reference_set.n447566000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447566000', tag=u'n447566000')
Reference_set.n447567009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447567009', tag=u'n447567009')
Reference_set.n447568004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447568004', tag=u'n447568004')
Reference_set.n447569007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447569007', tag=u'n447569007')
Reference_set.n447570008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'447570008', tag=u'n447570008')
Reference_set.n448879004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'448879004', tag=u'n448879004')
Reference_set.n450970008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450970008', tag=u'n450970008')
Reference_set.n450971007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450971007', tag=u'n450971007')
Reference_set.n450973005 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450973005', tag=u'n450973005')
Reference_set.n450974004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450974004', tag=u'n450974004')
Reference_set.n450976002 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450976002', tag=u'n450976002')
Reference_set.n450977006 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450977006', tag=u'n450977006')
Reference_set.n450978001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450978001', tag=u'n450978001')
Reference_set.n450980007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450980007', tag=u'n450980007')
Reference_set.n450981006 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450981006', tag=u'n450981006')
Reference_set.n450982004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450982004', tag=u'n450982004')
Reference_set.n450983009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450983009', tag=u'n450983009')
Reference_set.n450984003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450984003', tag=u'n450984003')
Reference_set.n450985002 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450985002', tag=u'n450985002')
Reference_set.n450986001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450986001', tag=u'n450986001')
Reference_set.n450988000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450988000', tag=u'n450988000')
Reference_set.n450989008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450989008', tag=u'n450989008')
Reference_set.n450990004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450990004', tag=u'n450990004')
Reference_set.n450991000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450991000', tag=u'n450991000')
Reference_set.n450992007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450992007', tag=u'n450992007')
Reference_set.n450993002 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450993002', tag=u'n450993002')
Reference_set.n450994008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'450994008', tag=u'n450994008')
Reference_set.n609331003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'609331003', tag=u'n609331003')
Reference_set.n609430003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'609430003', tag=u'n609430003')
Reference_set.n700043003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'700043003', tag=u'n700043003')
Reference_set.n6011000124106 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'6011000124106', tag=u'n6011000124106')
Reference_set.n900000000000456007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000456007', tag=u'n900000000000456007')
Reference_set.n900000000000480006 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000480006', tag=u'n900000000000480006')
Reference_set.n900000000000488004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000488004', tag=u'n900000000000488004')
Reference_set.n900000000000489007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000489007', tag=u'n900000000000489007')
Reference_set.n900000000000490003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000490003', tag=u'n900000000000490003')
Reference_set.n900000000000496009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000496009', tag=u'n900000000000496009')
Reference_set.n900000000000497000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000497000', tag=u'n900000000000497000')
Reference_set.n900000000000498005 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000498005', tag=u'n900000000000498005')
Reference_set.n900000000000506000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000506000', tag=u'n900000000000506000')
Reference_set.n900000000000507009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000507009', tag=u'n900000000000507009')
Reference_set.n900000000000508004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000508004', tag=u'n900000000000508004')
Reference_set.n900000000000509007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000509007', tag=u'n900000000000509007')
Reference_set.n900000000000512005 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000512005', tag=u'n900000000000512005')
Reference_set.n900000000000513000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000513000', tag=u'n900000000000513000')
Reference_set.n900000000000516008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000516008', tag=u'n900000000000516008')
Reference_set.n900000000000517004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000517004', tag=u'n900000000000517004')
Reference_set.n900000000000521006 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000521006', tag=u'n900000000000521006')
Reference_set.n900000000000522004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000522004', tag=u'n900000000000522004')
Reference_set.n900000000000523009 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000523009', tag=u'n900000000000523009')
Reference_set.n900000000000524003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000524003', tag=u'n900000000000524003')
Reference_set.n900000000000525002 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000525002', tag=u'n900000000000525002')
Reference_set.n900000000000526001 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000526001', tag=u'n900000000000526001')
Reference_set.n900000000000527005 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000527005', tag=u'n900000000000527005')
Reference_set.n900000000000528000 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000528000', tag=u'n900000000000528000')
Reference_set.n900000000000529008 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000529008', tag=u'n900000000000529008')
Reference_set.n900000000000530003 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000530003', tag=u'n900000000000530003')
Reference_set.n900000000000531004 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000531004', tag=u'n900000000000531004')
Reference_set.n900000000000534007 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000534007', tag=u'n900000000000534007')
Reference_set.n900000000000538005 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000538005', tag=u'n900000000000538005')
Reference_set.n900000000000547002 = Reference_set._CF_enumeration.addEnumeration(unicode_value=u'900000000000547002', tag=u'n900000000000547002')
Reference_set._InitializeFacetMap(Reference_set._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Reference_set', Reference_set)

# Atomic simple type: {http://snomed.info/schema/rf2}Reference_set_attribute
class Reference_set_attribute (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Reference_set_attribute')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 6543, 4)
    _Documentation = u'\n                \n            '
Reference_set_attribute._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Reference_set_attribute, enum_prefix=None)
Reference_set_attribute.n447247004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447247004', tag=u'n447247004')
Reference_set_attribute.n447255006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447255006', tag=u'n447255006')
Reference_set_attribute.n447257003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447257003', tag=u'n447257003')
Reference_set_attribute.n447556008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447556008', tag=u'n447556008')
Reference_set_attribute.n447557004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447557004', tag=u'n447557004')
Reference_set_attribute.n447558009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447558009', tag=u'n447558009')
Reference_set_attribute.n447559001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447559001', tag=u'n447559001')
Reference_set_attribute.n447560006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447560006', tag=u'n447560006')
Reference_set_attribute.n447561005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447561005', tag=u'n447561005')
Reference_set_attribute.n447634004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447634004', tag=u'n447634004')
Reference_set_attribute.n447635003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447635003', tag=u'n447635003')
Reference_set_attribute.n447636002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447636002', tag=u'n447636002')
Reference_set_attribute.n447637006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447637006', tag=u'n447637006')
Reference_set_attribute.n447638001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447638001', tag=u'n447638001')
Reference_set_attribute.n447639009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447639009', tag=u'n447639009')
Reference_set_attribute.n447640006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447640006', tag=u'n447640006')
Reference_set_attribute.n447641005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447641005', tag=u'n447641005')
Reference_set_attribute.n447642003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'447642003', tag=u'n447642003')
Reference_set_attribute.n449608002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'449608002', tag=u'n449608002')
Reference_set_attribute.n450995009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'450995009', tag=u'n450995009')
Reference_set_attribute.n450996005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'450996005', tag=u'n450996005')
Reference_set_attribute.n450997001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'450997001', tag=u'n450997001')
Reference_set_attribute.n450998006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'450998006', tag=u'n450998006')
Reference_set_attribute.n450999003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'450999003', tag=u'n450999003')
Reference_set_attribute.n451000004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'451000004', tag=u'n451000004')
Reference_set_attribute.n451001000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'451001000', tag=u'n451001000')
Reference_set_attribute.n451002007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'451002007', tag=u'n451002007')
Reference_set_attribute.n451003002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'451003002', tag=u'n451003002')
Reference_set_attribute.n609330002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'609330002', tag=u'n609330002')
Reference_set_attribute.n609431004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'609431004', tag=u'n609431004')
Reference_set_attribute.n609432006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'609432006', tag=u'n609432006')
Reference_set_attribute.n609642003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'609642003', tag=u'n609642003')
Reference_set_attribute.n900000000000007000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000007000', tag=u'n900000000000007000')
Reference_set_attribute.n900000000000216007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000216007', tag=u'n900000000000216007')
Reference_set_attribute.n900000000000218008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000218008', tag=u'n900000000000218008')
Reference_set_attribute.n900000000000226000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000226000', tag=u'n900000000000226000')
Reference_set_attribute.n900000000000458008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000458008', tag=u'n900000000000458008')
Reference_set_attribute.n900000000000459000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000459000', tag=u'n900000000000459000')
Reference_set_attribute.n900000000000460005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000460005', tag=u'n900000000000460005')
Reference_set_attribute.n900000000000461009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000461009', tag=u'n900000000000461009')
Reference_set_attribute.n900000000000462002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000462002', tag=u'n900000000000462002')
Reference_set_attribute.n900000000000463007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000463007', tag=u'n900000000000463007')
Reference_set_attribute.n900000000000464001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000464001', tag=u'n900000000000464001')
Reference_set_attribute.n900000000000465000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000465000', tag=u'n900000000000465000')
Reference_set_attribute.n900000000000466004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000466004', tag=u'n900000000000466004')
Reference_set_attribute.n900000000000467008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000467008', tag=u'n900000000000467008')
Reference_set_attribute.n900000000000468003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000468003', tag=u'n900000000000468003')
Reference_set_attribute.n900000000000469006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000469006', tag=u'n900000000000469006')
Reference_set_attribute.n900000000000470007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000470007', tag=u'n900000000000470007')
Reference_set_attribute.n900000000000471006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000471006', tag=u'n900000000000471006')
Reference_set_attribute.n900000000000472004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000472004', tag=u'n900000000000472004')
Reference_set_attribute.n900000000000473009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000473009', tag=u'n900000000000473009')
Reference_set_attribute.n900000000000474003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000474003', tag=u'n900000000000474003')
Reference_set_attribute.n900000000000475002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000475002', tag=u'n900000000000475002')
Reference_set_attribute.n900000000000476001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000476001', tag=u'n900000000000476001')
Reference_set_attribute.n900000000000477005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000477005', tag=u'n900000000000477005')
Reference_set_attribute.n900000000000478000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000478000', tag=u'n900000000000478000')
Reference_set_attribute.n900000000000479008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000479008', tag=u'n900000000000479008')
Reference_set_attribute.n900000000000481005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000481005', tag=u'n900000000000481005')
Reference_set_attribute.n900000000000482003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000482003', tag=u'n900000000000482003')
Reference_set_attribute.n900000000000483008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000483008', tag=u'n900000000000483008')
Reference_set_attribute.n900000000000484002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000484002', tag=u'n900000000000484002')
Reference_set_attribute.n900000000000485001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000485001', tag=u'n900000000000485001')
Reference_set_attribute.n900000000000486000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000486000', tag=u'n900000000000486000')
Reference_set_attribute.n900000000000487009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000487009', tag=u'n900000000000487009')
Reference_set_attribute.n900000000000491004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000491004', tag=u'n900000000000491004')
Reference_set_attribute.n900000000000492006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000492006', tag=u'n900000000000492006')
Reference_set_attribute.n900000000000493001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000493001', tag=u'n900000000000493001')
Reference_set_attribute.n900000000000494007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000494007', tag=u'n900000000000494007')
Reference_set_attribute.n900000000000495008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000495008', tag=u'n900000000000495008')
Reference_set_attribute.n900000000000499002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000499002', tag=u'n900000000000499002')
Reference_set_attribute.n900000000000500006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000500006', tag=u'n900000000000500006')
Reference_set_attribute.n900000000000501005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000501005', tag=u'n900000000000501005')
Reference_set_attribute.n900000000000502003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000502003', tag=u'n900000000000502003')
Reference_set_attribute.n900000000000503008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000503008', tag=u'n900000000000503008')
Reference_set_attribute.n900000000000504002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000504002', tag=u'n900000000000504002')
Reference_set_attribute.n900000000000505001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000505001', tag=u'n900000000000505001')
Reference_set_attribute.n900000000000510002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000510002', tag=u'n900000000000510002')
Reference_set_attribute.n900000000000511003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000511003', tag=u'n900000000000511003')
Reference_set_attribute.n900000000000514006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000514006', tag=u'n900000000000514006')
Reference_set_attribute.n900000000000515007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000515007', tag=u'n900000000000515007')
Reference_set_attribute.n900000000000518009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000518009', tag=u'n900000000000518009')
Reference_set_attribute.n900000000000519001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000519001', tag=u'n900000000000519001')
Reference_set_attribute.n900000000000520007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000520007', tag=u'n900000000000520007')
Reference_set_attribute.n900000000000532006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000532006', tag=u'n900000000000532006')
Reference_set_attribute.n900000000000533001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000533001', tag=u'n900000000000533001')
Reference_set_attribute.n900000000000535008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000535008', tag=u'n900000000000535008')
Reference_set_attribute.n900000000000536009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000536009', tag=u'n900000000000536009')
Reference_set_attribute.n900000000000537000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000537000', tag=u'n900000000000537000')
Reference_set_attribute.n900000000000539002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000539002', tag=u'n900000000000539002')
Reference_set_attribute.n900000000000540000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000540000', tag=u'n900000000000540000')
Reference_set_attribute.n900000000000541001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000541001', tag=u'n900000000000541001')
Reference_set_attribute.n900000000000542008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000542008', tag=u'n900000000000542008')
Reference_set_attribute.n900000000000543003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000543003', tag=u'n900000000000543003')
Reference_set_attribute.n900000000000544009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000544009', tag=u'n900000000000544009')
Reference_set_attribute.n900000000000545005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000545005', tag=u'n900000000000545005')
Reference_set_attribute.n900000000000546006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000546006', tag=u'n900000000000546006')
Reference_set_attribute.n900000000000548007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000548007', tag=u'n900000000000548007')
Reference_set_attribute.n900000000000549004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value=u'900000000000549004', tag=u'n900000000000549004')
Reference_set_attribute._InitializeFacetMap(Reference_set_attribute._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Reference_set_attribute', Reference_set_attribute)

# Atomic simple type: {http://snomed.info/schema/rf2}Attribute_type
class Attribute_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Attribute_type')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7108, 4)
    _Documentation = u'\n                \n            '
Attribute_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Attribute_type, enum_prefix=None)
Attribute_type.n900000000000460005 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000460005', tag=u'n900000000000460005')
Attribute_type.n900000000000461009 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000461009', tag=u'n900000000000461009')
Attribute_type.n900000000000462002 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000462002', tag=u'n900000000000462002')
Attribute_type.n900000000000463007 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000463007', tag=u'n900000000000463007')
Attribute_type.n900000000000464001 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000464001', tag=u'n900000000000464001')
Attribute_type.n900000000000465000 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000465000', tag=u'n900000000000465000')
Attribute_type.n900000000000466004 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000466004', tag=u'n900000000000466004')
Attribute_type.n900000000000467008 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000467008', tag=u'n900000000000467008')
Attribute_type.n900000000000468003 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000468003', tag=u'n900000000000468003')
Attribute_type.n900000000000469006 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000469006', tag=u'n900000000000469006')
Attribute_type.n900000000000470007 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000470007', tag=u'n900000000000470007')
Attribute_type.n900000000000471006 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000471006', tag=u'n900000000000471006')
Attribute_type.n900000000000472004 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000472004', tag=u'n900000000000472004')
Attribute_type.n900000000000473009 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000473009', tag=u'n900000000000473009')
Attribute_type.n900000000000474003 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000474003', tag=u'n900000000000474003')
Attribute_type.n900000000000475002 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000475002', tag=u'n900000000000475002')
Attribute_type.n900000000000476001 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000476001', tag=u'n900000000000476001')
Attribute_type.n900000000000477005 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000477005', tag=u'n900000000000477005')
Attribute_type.n900000000000478000 = Attribute_type._CF_enumeration.addEnumeration(unicode_value=u'900000000000478000', tag=u'n900000000000478000')
Attribute_type._InitializeFacetMap(Attribute_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Attribute_type', Attribute_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Attribute_value
class Attribute_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Attribute_value')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7230, 4)
    _Documentation = u'\n                \n            '
Attribute_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Attribute_value, enum_prefix=None)
Attribute_value.n450995009 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'450995009', tag=u'n450995009')
Attribute_value.n450996005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'450996005', tag=u'n450996005')
Attribute_value.n450997001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'450997001', tag=u'n450997001')
Attribute_value.n450998006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'450998006', tag=u'n450998006')
Attribute_value.n450999003 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'450999003', tag=u'n450999003')
Attribute_value.n451000004 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'451000004', tag=u'n451000004')
Attribute_value.n451001000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'451001000', tag=u'n451001000')
Attribute_value.n451002007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'451002007', tag=u'n451002007')
Attribute_value.n451003002 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'451003002', tag=u'n451003002')
Attribute_value.n900000000000007000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000007000', tag=u'n900000000000007000')
Attribute_value.n900000000000216007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000216007', tag=u'n900000000000216007')
Attribute_value.n900000000000218008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000218008', tag=u'n900000000000218008')
Attribute_value.n900000000000226000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000226000', tag=u'n900000000000226000')
Attribute_value.n900000000000481005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000481005', tag=u'n900000000000481005')
Attribute_value.n900000000000482003 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000482003', tag=u'n900000000000482003')
Attribute_value.n900000000000483008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000483008', tag=u'n900000000000483008')
Attribute_value.n900000000000484002 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000484002', tag=u'n900000000000484002')
Attribute_value.n900000000000485001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000485001', tag=u'n900000000000485001')
Attribute_value.n900000000000486000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000486000', tag=u'n900000000000486000')
Attribute_value.n900000000000487009 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000487009', tag=u'n900000000000487009')
Attribute_value.n900000000000492006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000492006', tag=u'n900000000000492006')
Attribute_value.n900000000000493001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000493001', tag=u'n900000000000493001')
Attribute_value.n900000000000494007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000494007', tag=u'n900000000000494007')
Attribute_value.n900000000000495008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000495008', tag=u'n900000000000495008')
Attribute_value.n900000000000545005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000545005', tag=u'n900000000000545005')
Attribute_value.n900000000000546006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value=u'900000000000546006', tag=u'n900000000000546006')
Attribute_value._InitializeFacetMap(Attribute_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Attribute_value', Attribute_value)

# Atomic simple type: {http://snomed.info/schema/rf2}SNOMED_CT_source_code_to_target_map_code_correlation_value
class SNOMED_CT_source_code_to_target_map_code_correlation_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SNOMED_CT_source_code_to_target_map_code_correlation_value')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7397, 4)
    _Documentation = u'\n                \n            '
SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SNOMED_CT_source_code_to_target_map_code_correlation_value, enum_prefix=None)
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447556008 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447556008', tag=u'n447556008')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447557004 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447557004', tag=u'n447557004')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447558009 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447558009', tag=u'n447558009')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447559001 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447559001', tag=u'n447559001')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447560006 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447560006', tag=u'n447560006')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447561005 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value=u'447561005', tag=u'n447561005')
SNOMED_CT_source_code_to_target_map_code_correlation_value._InitializeFacetMap(SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SNOMED_CT_source_code_to_target_map_code_correlation_value', SNOMED_CT_source_code_to_target_map_code_correlation_value)

# Atomic simple type: {http://snomed.info/schema/rf2}Acceptability
class Acceptability (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Acceptability')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7464, 4)
    _Documentation = u'\n                \n            '
Acceptability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Acceptability, enum_prefix=None)
Acceptability.n900000000000548007 = Acceptability._CF_enumeration.addEnumeration(unicode_value=u'900000000000548007', tag=u'n900000000000548007')
Acceptability.n900000000000549004 = Acceptability._CF_enumeration.addEnumeration(unicode_value=u'900000000000549004', tag=u'n900000000000549004')
Acceptability._InitializeFacetMap(Acceptability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Acceptability', Acceptability)

# Atomic simple type: {http://snomed.info/schema/rf2}Description_format
class Description_format (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Description_format')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7497, 4)
    _Documentation = u'\n                \n            '
Description_format._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Description_format, enum_prefix=None)
Description_format.n900000000000540000 = Description_format._CF_enumeration.addEnumeration(unicode_value=u'900000000000540000', tag=u'n900000000000540000')
Description_format.n900000000000541001 = Description_format._CF_enumeration.addEnumeration(unicode_value=u'900000000000541001', tag=u'n900000000000541001')
Description_format.n900000000000542008 = Description_format._CF_enumeration.addEnumeration(unicode_value=u'900000000000542008', tag=u'n900000000000542008')
Description_format.n900000000000543003 = Description_format._CF_enumeration.addEnumeration(unicode_value=u'900000000000543003', tag=u'n900000000000543003')
Description_format._InitializeFacetMap(Description_format._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Description_format', Description_format)

# Atomic simple type: [anonymous]
class STD_ANON (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7789, 24)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7836, 24)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.int(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)

# Complex type {http://snomed.info/schema/rf2}SCTIDorUUID with content type ELEMENT_ONLY
class SCTIDorUUID (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}SCTIDorUUID with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SCTIDorUUID')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}sctid uses Python identifier sctid
    __sctid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sctid'), 'sctid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2sctid', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 55, 12), )

    
    sctid = property(__sctid.value, __sctid.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uuid'), 'uuid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2uuid', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 56, 12), )

    
    uuid = property(__uuid.value, __uuid.set, None, None)

    _ElementMap.update({
        __sctid.name() : __sctid,
        __uuid.name() : __uuid
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SCTIDorUUID', SCTIDorUUID)


# Complex type {http://snomed.info/schema/rf2}Base with content type ELEMENT_ONLY
class Base (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Base with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Base')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7622, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active,
        __moduleId.name() : __moduleId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Base', Base)


# Complex type {http://snomed.info/schema/rf2}Identifier with content type ELEMENT_ONLY
class Identifier_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Identifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Identifier')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7712, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}identifierSchemeId uses Python identifier identifierSchemeId
    __identifierSchemeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId'), 'identifierSchemeId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2identifierSchemeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7714, 12), )

    
    identifierSchemeId = property(__identifierSchemeId.value, __identifierSchemeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}alternateIdentifier uses Python identifier alternateIdentifier
    __alternateIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier'), 'alternateIdentifier', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2alternateIdentifier', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7715, 12), )

    
    alternateIdentifier = property(__alternateIdentifier.value, __alternateIdentifier.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7716, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7717, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7718, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referenceComponentId uses Python identifier referenceComponentId
    __referenceComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId'), 'referenceComponentId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2referenceComponentId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7719, 12), )

    
    referenceComponentId = property(__referenceComponentId.value, __referenceComponentId.set, None, None)

    _ElementMap.update({
        __identifierSchemeId.name() : __identifierSchemeId,
        __alternateIdentifier.name() : __alternateIdentifier,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active,
        __moduleId.name() : __moduleId,
        __referenceComponentId.name() : __referenceComponentId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Identifier', Identifier_)


# Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistory with content type ELEMENT_ONLY
class TransitiveClosureHistory_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistory with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistory')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7736, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}subtypeId uses Python identifier subtypeId
    __subtypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'subtypeId'), 'subtypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2subtypeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7738, 12), )

    
    subtypeId = property(__subtypeId.value, __subtypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}supertypeId uses Python identifier supertypeId
    __supertypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supertypeId'), 'supertypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2supertypeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7739, 12), )

    
    supertypeId = property(__supertypeId.value, __supertypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7740, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7741, 12), )

    
    active = property(__active.value, __active.set, None, None)

    _ElementMap.update({
        __subtypeId.name() : __subtypeId,
        __supertypeId.name() : __supertypeId,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TransitiveClosureHistory', TransitiveClosureHistory_)


# Complex type {http://snomed.info/schema/rf2}RefsetBase with content type ELEMENT_ONLY
class RefsetBase (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}RefsetBase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RefsetBase')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7761, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}refsetId uses Python identifier refsetId
    __refsetId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'refsetId'), 'refsetId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2refsetId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12), )

    
    refsetId = property(__refsetId.value, __refsetId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referencedComponentId uses Python identifier referencedComponentId
    __referencedComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId'), 'referencedComponentId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2referencedComponentId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12), )

    
    referencedComponentId = property(__referencedComponentId.value, __referencedComponentId.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active,
        __moduleId.name() : __moduleId,
        __refsetId.name() : __refsetId,
        __referencedComponentId.name() : __referencedComponentId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'RefsetBase', RefsetBase)


# Complex type {http://snomed.info/schema/rf2}Iterator with content type EMPTY
class Iterator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Iterator with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Iterator')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7586, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute complete uses Python identifier complete
    __complete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'complete'), 'complete', '__httpsnomed_infoschemarf2_Iterator_complete', CompleteDirectory, required=True)
    __complete._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7587, 8)
    __complete._UseLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7587, 8)
    
    complete = property(__complete.value, __complete.set, None, u'an indicator that states whether the complete directory listing is included in\n                    \n                    or whether additional retrievals are needed to get the full listing.\n                ')

    
    # Attribute numEntries uses Python identifier numEntries
    __numEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEntries'), 'numEntries', '__httpsnomed_infoschemarf2_Iterator_numEntries', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __numEntries._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7595, 8)
    __numEntries._UseLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7595, 8)
    
    numEntries = property(__numEntries.value, __numEntries.set, None, u'the number of entries in this directory segment. Note that this is\n                    \n                    the total number of entries in the complete directory listing - just the number of entries in this\n                    segment.\n                ')

    
    # Attribute prev uses Python identifier prev
    __prev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'prev'), 'prev', '__httpsnomed_infoschemarf2_Iterator_prev', pyxb.binding.datatypes.anyURI)
    __prev._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7604, 8)
    __prev._UseLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7604, 8)
    
    prev = property(__prev.value, __prev.set, None, u'a URI that, when de-referenced, produces the preceding set of entries in the\n                    directory.\n                ')

    
    # Attribute next uses Python identifier next
    __next = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'next'), 'next', '__httpsnomed_infoschemarf2_Iterator_next', pyxb.binding.datatypes.anyURI)
    __next._DeclarationLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7611, 8)
    __next._UseLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7611, 8)
    
    next = property(__next.value, __next.set, None, u'a URI that, when de-referenced, produces the next set of entries in the directory.\n                ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __complete.name() : __complete,
        __numEntries.name() : __numEntries,
        __prev.name() : __prev,
        __next.name() : __next
    })
Namespace.addCategoryObject('typeBinding', u'Iterator', Iterator)


# Complex type {http://snomed.info/schema/rf2}Concept with content type ELEMENT_ONLY
class Concept_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Concept with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Concept')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7634, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}definitionStatusId uses Python identifier definitionStatusId
    __definitionStatusId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId'), 'definitionStatusId', '__httpsnomed_infoschemarf2_Concept__httpsnomed_infoschemarf2definitionStatusId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7638, 20), )

    
    definitionStatusId = property(__definitionStatusId.value, __definitionStatusId.set, None, None)

    _ElementMap.update({
        __definitionStatusId.name() : __definitionStatusId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Concept', Concept_)


# Complex type {http://snomed.info/schema/rf2}Description with content type ELEMENT_ONLY
class Description_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Description with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Description')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7657, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}conceptId uses Python identifier conceptId
    __conceptId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), 'conceptId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2conceptId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7661, 20), )

    
    conceptId = property(__conceptId.value, __conceptId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}languageCode uses Python identifier languageCode
    __languageCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'languageCode'), 'languageCode', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2languageCode', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7662, 20), )

    
    languageCode = property(__languageCode.value, __languageCode.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7663, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'term'), 'term', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2term', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7664, 20), )

    
    term = property(__term.value, __term.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}caseSignificanceId uses Python identifier caseSignificanceId
    __caseSignificanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId'), 'caseSignificanceId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2caseSignificanceId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7665, 20), )

    
    caseSignificanceId = property(__caseSignificanceId.value, __caseSignificanceId.set, None, None)

    _ElementMap.update({
        __conceptId.name() : __conceptId,
        __languageCode.name() : __languageCode,
        __typeId.name() : __typeId,
        __term.name() : __term,
        __caseSignificanceId.name() : __caseSignificanceId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Description', Description_)


# Complex type {http://snomed.info/schema/rf2}Relationship with content type ELEMENT_ONLY
class Relationship_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Relationship with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Relationship')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7684, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}sourceId uses Python identifier sourceId
    __sourceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceId'), 'sourceId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2sourceId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7688, 20), )

    
    sourceId = property(__sourceId.value, __sourceId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}destinationId uses Python identifier destinationId
    __destinationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'destinationId'), 'destinationId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2destinationId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7689, 20), )

    
    destinationId = property(__destinationId.value, __destinationId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}relationshipGroup uses Python identifier relationshipGroup
    __relationshipGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup'), 'relationshipGroup', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2relationshipGroup', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7690, 20), )

    
    relationshipGroup = property(__relationshipGroup.value, __relationshipGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7691, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}characteristicTypeId uses Python identifier characteristicTypeId
    __characteristicTypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId'), 'characteristicTypeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2characteristicTypeId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7692, 20), )

    
    characteristicTypeId = property(__characteristicTypeId.value, __characteristicTypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}modifierId uses Python identifier modifierId
    __modifierId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'modifierId'), 'modifierId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2modifierId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7693, 20), )

    
    modifierId = property(__modifierId.value, __modifierId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}isCanonical uses Python identifier isCanonical
    __isCanonical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'isCanonical'), 'isCanonical', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2isCanonical', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7694, 20), )

    
    isCanonical = property(__isCanonical.value, __isCanonical.set, None, None)

    _ElementMap.update({
        __sourceId.name() : __sourceId,
        __destinationId.name() : __destinationId,
        __relationshipGroup.name() : __relationshipGroup,
        __typeId.name() : __typeId,
        __characteristicTypeId.name() : __characteristicTypeId,
        __modifierId.name() : __modifierId,
        __isCanonical.name() : __isCanonical
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Relationship', Relationship_)


# Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSetEntry with content type ELEMENT_ONLY
class DescriptorReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7775, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}attributeDescription uses Python identifier attributeDescription
    __attributeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription'), 'attributeDescription', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeDescription', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7786, 20), )

    
    attributeDescription = property(__attributeDescription.value, __attributeDescription.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeType'), 'attributeType', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeType', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7787, 20), )

    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeOrder uses Python identifier attributeOrder
    __attributeOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder'), 'attributeOrder', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeOrder', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7788, 20), )

    
    attributeOrder = property(__attributeOrder.value, __attributeOrder.set, None, None)

    _ElementMap.update({
        __attributeDescription.name() : __attributeDescription,
        __attributeType.name() : __attributeType,
        __attributeOrder.name() : __attributeOrder
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptorReferenceSetEntry', DescriptorReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}SimpleReferenceSetEntry with content type ELEMENT_ONLY
class SimpleReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}SimpleReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7813, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleReferenceSetEntry', SimpleReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}OrderedReferenceSetEntry with content type ELEMENT_ONLY
class OrderedReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}OrderedReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7831, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}order uses Python identifier order
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2order', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7835, 20), )

    
    order = property(__order.value, __order.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}linkedTo uses Python identifier linkedTo
    __linkedTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'linkedTo'), 'linkedTo', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2linkedTo', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7842, 20), )

    
    linkedTo = property(__linkedTo.value, __linkedTo.set, None, None)

    _ElementMap.update({
        __order.name() : __order,
        __linkedTo.name() : __linkedTo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'OrderedReferenceSetEntry', OrderedReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSetEntry with content type ELEMENT_ONLY
class AttributeValueReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7861, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}valueId uses Python identifier valueId
    __valueId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'valueId'), 'valueId', '__httpsnomed_infoschemarf2_AttributeValueReferenceSetEntry__httpsnomed_infoschemarf2valueId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7865, 20), )

    
    valueId = property(__valueId.value, __valueId.set, None, None)

    _ElementMap.update({
        __valueId.name() : __valueId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributeValueReferenceSetEntry', AttributeValueReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSetEntry with content type ELEMENT_ONLY
class SimpleMapReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7884, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}mapTarget uses Python identifier mapTarget
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_SimpleMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7888, 20), )

    
    mapTarget = property(__mapTarget.value, __mapTarget.set, None, None)

    _ElementMap.update({
        __mapTarget.name() : __mapTarget
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleMapReferenceSetEntry', SimpleMapReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSetEntry with content type ELEMENT_ONLY
class ComplexMapReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7907, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}mapGroup uses Python identifier mapGroup
    __mapGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapGroup'), 'mapGroup', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapGroup', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7911, 20), )

    
    mapGroup = property(__mapGroup.value, __mapGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapPriority uses Python identifier mapPriority
    __mapPriority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapPriority'), 'mapPriority', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapPriority', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7912, 20), )

    
    mapPriority = property(__mapPriority.value, __mapPriority.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapRule uses Python identifier mapRule
    __mapRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), 'mapRule', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapRule', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7913, 20), )

    
    mapRule = property(__mapRule.value, __mapRule.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapAdvice uses Python identifier mapAdvice
    __mapAdvice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice'), 'mapAdvice', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapAdvice', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7914, 20), )

    
    mapAdvice = property(__mapAdvice.value, __mapAdvice.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapTarget uses Python identifier mapTarget
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7915, 20), )

    
    mapTarget = property(__mapTarget.value, __mapTarget.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}correlationId uses Python identifier correlationId
    __correlationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'correlationId'), 'correlationId', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2correlationId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7916, 20), )

    
    correlationId = property(__correlationId.value, __correlationId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapCategoryId uses Python identifier mapCategoryId
    __mapCategoryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapCategoryId'), 'mapCategoryId', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapCategoryId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7917, 20), )

    
    mapCategoryId = property(__mapCategoryId.value, __mapCategoryId.set, None, None)

    _ElementMap.update({
        __mapGroup.name() : __mapGroup,
        __mapPriority.name() : __mapPriority,
        __mapRule.name() : __mapRule,
        __mapAdvice.name() : __mapAdvice,
        __mapTarget.name() : __mapTarget,
        __correlationId.name() : __correlationId,
        __mapCategoryId.name() : __mapCategoryId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ComplexMapReferenceSetEntry', ComplexMapReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}LanguageReferenceSetEntry with content type ELEMENT_ONLY
class LanguageReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}LanguageReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7935, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}acceptabilityId uses Python identifier acceptabilityId
    __acceptabilityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId'), 'acceptabilityId', '__httpsnomed_infoschemarf2_LanguageReferenceSetEntry__httpsnomed_infoschemarf2acceptabilityId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7939, 20), )

    
    acceptabilityId = property(__acceptabilityId.value, __acceptabilityId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}conceptId uses Python identifier conceptId
    __conceptId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), 'conceptId', '__httpsnomed_infoschemarf2_LanguageReferenceSetEntry__httpsnomed_infoschemarf2conceptId', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7941, 20), )

    
    conceptId = property(__conceptId.value, __conceptId.set, None, None)

    _ElementMap.update({
        __acceptabilityId.name() : __acceptabilityId,
        __conceptId.name() : __conceptId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'LanguageReferenceSetEntry', LanguageReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSetEntry with content type ELEMENT_ONLY
class QuerySpecificationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7959, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}query uses Python identifier query
    __query = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'query'), 'query', '__httpsnomed_infoschemarf2_QuerySpecificationReferenceSetEntry__httpsnomed_infoschemarf2query', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7963, 20), )

    
    query = property(__query.value, __query.set, None, None)

    _ElementMap.update({
        __query.name() : __query
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QuerySpecificationReferenceSetEntry', QuerySpecificationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSetEntry with content type ELEMENT_ONLY
class AnnotationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7982, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'annotation'), 'annotation', '__httpsnomed_infoschemarf2_AnnotationReferenceSetEntry__httpsnomed_infoschemarf2annotation', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7986, 20), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    _ElementMap.update({
        __annotation.name() : __annotation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AnnotationReferenceSetEntry', AnnotationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AssociationReferenceSetEntry with content type ELEMENT_ONLY
class AssociationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AssociationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8004, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}targetComponent uses Python identifier targetComponent
    __targetComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetComponent'), 'targetComponent', '__httpsnomed_infoschemarf2_AssociationReferenceSetEntry__httpsnomed_infoschemarf2targetComponent', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8008, 20), )

    
    targetComponent = property(__targetComponent.value, __targetComponent.set, None, None)

    _ElementMap.update({
        __targetComponent.name() : __targetComponent
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AssociationReferenceSetEntry', AssociationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ModuleDependencyReferenceSetEntry with content type ELEMENT_ONLY
class ModuleDependencyReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}ModuleDependencyReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModuleDependencyReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8027, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}sourceEffectiveTime uses Python identifier sourceEffectiveTime
    __sourceEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime'), 'sourceEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2sourceEffectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8031, 20), )

    
    sourceEffectiveTime = property(__sourceEffectiveTime.value, __sourceEffectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}targetEffectiveTime uses Python identifier targetEffectiveTime
    __targetEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime'), 'targetEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2targetEffectiveTime', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8032, 20), )

    
    targetEffectiveTime = property(__targetEffectiveTime.value, __targetEffectiveTime.set, None, None)

    _ElementMap.update({
        __sourceEffectiveTime.name() : __sourceEffectiveTime,
        __targetEffectiveTime.name() : __targetEffectiveTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ModuleDependencyReferenceSetEntry', ModuleDependencyReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSetEntry with content type ELEMENT_ONLY
class DescriptionFormatReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8051, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}descriptionFormat uses Python identifier descriptionFormat
    __descriptionFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat'), 'descriptionFormat', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionFormat', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8055, 20), )

    
    descriptionFormat = property(__descriptionFormat.value, __descriptionFormat.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}descriptionLength uses Python identifier descriptionLength
    __descriptionLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength'), 'descriptionLength', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionLength', False, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8056, 20), )

    
    descriptionLength = property(__descriptionLength.value, __descriptionLength.set, None, None)

    _ElementMap.update({
        __descriptionFormat.name() : __descriptionFormat,
        __descriptionLength.name() : __descriptionLength
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptionFormatReferenceSetEntry', DescriptionFormatReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ConceptList with content type ELEMENT_ONLY
class ConceptList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ConceptList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConceptList')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7645, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_ConceptList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7649, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ConceptList', ConceptList_)


# Complex type {http://snomed.info/schema/rf2}DescriptionList with content type ELEMENT_ONLY
class DescriptionList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptionList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionList')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7673, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptionList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7677, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptionList', DescriptionList_)


# Complex type {http://snomed.info/schema/rf2}RelationshipList with content type ELEMENT_ONLY
class RelationshipList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}RelationshipList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelationshipList')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7701, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_RelationshipList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7705, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'RelationshipList', RelationshipList_)


# Complex type {http://snomed.info/schema/rf2}IdentifierList with content type ELEMENT_ONLY
class IdentifierList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}IdentifierList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdentifierList')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7724, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_IdentifierList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7728, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IdentifierList', IdentifierList_)


# Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistoryList with content type ELEMENT_ONLY
class TransitiveClosureHistoryList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistoryList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistoryList')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7747, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_TransitiveClosureHistoryList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7751, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TransitiveClosureHistoryList', TransitiveClosureHistoryList_)


# Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSet with content type ELEMENT_ONLY
class DescriptorReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7801, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptorReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7805, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptorReferenceSet', DescriptorReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}SimpleReferenceSet with content type ELEMENT_ONLY
class SimpleReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}SimpleReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7820, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_SimpleReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7824, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleReferenceSet', SimpleReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}OrderedReferenceSet with content type ELEMENT_ONLY
class OrderedReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}OrderedReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7849, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_OrderedReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7853, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'OrderedReferenceSet', OrderedReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSet with content type ELEMENT_ONLY
class AttributeValueReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7871, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_AttributeValueReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7875, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributeValueReferenceSet', AttributeValueReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSet with content type ELEMENT_ONLY
class SimpleMapReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7895, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_SimpleMapReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7899, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SimpleMapReferenceSet', SimpleMapReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSet with content type ELEMENT_ONLY
class ComplexMapReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7923, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_ComplexMapReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7927, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ComplexMapReferenceSet', ComplexMapReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}LanguageReferenceSet with content type ELEMENT_ONLY
class LanguageReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}LanguageReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7947, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_LanguageReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7951, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'LanguageReferenceSet', LanguageReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSet with content type ELEMENT_ONLY
class QuerySpecificationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7969, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_QuerySpecificationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7973, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QuerySpecificationReferenceSet', QuerySpecificationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSet with content type ELEMENT_ONLY
class AnnotationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7992, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_AnnotationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7996, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AnnotationReferenceSet', AnnotationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AssociationReferenceSet with content type ELEMENT_ONLY
class AssociationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AssociationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8014, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_AssociationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8018, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AssociationReferenceSet', AssociationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ModuleDepencencyReferenceSet with content type ELEMENT_ONLY
class ModuleDepencencyReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ModuleDepencencyReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModuleDepencencyReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8039, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_ModuleDepencencyReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8043, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ModuleDepencencyReferenceSet', ModuleDepencencyReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSet with content type ELEMENT_ONLY
class DescriptionFormatReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8062, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8066, 20), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute complete inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute numEntries inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute prev inherited from {http://snomed.info/schema/rf2}Iterator
    
    # Attribute next inherited from {http://snomed.info/schema/rf2}Iterator
    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptionFormatReferenceSet', DescriptionFormatReferenceSet_)


Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7711, 4))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

TransitiveClosureHistory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistory'), TransitiveClosureHistory_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7735, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistory.name().localName(), TransitiveClosureHistory)

Concept = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Concept'), Concept_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7633, 4))
Namespace.addCategoryObject('elementBinding', Concept.name().localName(), Concept)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7656, 4))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

Relationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Relationship'), Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7683, 4))
Namespace.addCategoryObject('elementBinding', Relationship.name().localName(), Relationship)

DescriptorReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSetEntry'), DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7774, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSetEntry.name().localName(), DescriptorReferenceSetEntry)

SimpleReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSetEntry'), SimpleReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7812, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSetEntry.name().localName(), SimpleReferenceSetEntry)

OrderedReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSetEntry'), OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7830, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSetEntry.name().localName(), OrderedReferenceSetEntry)

AttributeValueReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSetEntry'), AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7860, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSetEntry.name().localName(), AttributeValueReferenceSetEntry)

SimpleMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSetEntry'), SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7883, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSetEntry.name().localName(), SimpleMapReferenceSetEntry)

ComplexMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSetEntry'), ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7906, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSetEntry.name().localName(), ComplexMapReferenceSetEntry)

LanguageReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSetEntry'), LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7934, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSetEntry.name().localName(), LanguageReferenceSetEntry)

QuerySpecificationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSetEntry'), QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7958, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSetEntry.name().localName(), QuerySpecificationReferenceSetEntry)

AnnotationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSetEntry'), AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7981, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSetEntry.name().localName(), AnnotationReferenceSetEntry)

AssociationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSetEntry'), AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8003, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSetEntry.name().localName(), AssociationReferenceSetEntry)

ModuleDependencyReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModuleDependencyReferenceSetEntry'), ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8026, 4))
Namespace.addCategoryObject('elementBinding', ModuleDependencyReferenceSetEntry.name().localName(), ModuleDependencyReferenceSetEntry)

DescriptionFormatReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSetEntry'), DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8050, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSetEntry.name().localName(), DescriptionFormatReferenceSetEntry)

ConceptList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptList'), ConceptList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7644, 4))
Namespace.addCategoryObject('elementBinding', ConceptList.name().localName(), ConceptList)

DescriptionList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionList'), DescriptionList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7672, 4))
Namespace.addCategoryObject('elementBinding', DescriptionList.name().localName(), DescriptionList)

RelationshipList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelationshipList'), RelationshipList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7700, 4))
Namespace.addCategoryObject('elementBinding', RelationshipList.name().localName(), RelationshipList)

IdentifierList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdentifierList'), IdentifierList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7723, 4))
Namespace.addCategoryObject('elementBinding', IdentifierList.name().localName(), IdentifierList)

TransitiveClosureHistoryList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistoryList'), TransitiveClosureHistoryList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7746, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistoryList.name().localName(), TransitiveClosureHistoryList)

DescriptorReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSet'), DescriptorReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7800, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSet.name().localName(), DescriptorReferenceSet)

SimpleReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSet'), SimpleReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7819, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSet.name().localName(), SimpleReferenceSet)

OrderedReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSet'), OrderedReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7848, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSet.name().localName(), OrderedReferenceSet)

AttributeValueReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSet'), AttributeValueReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7870, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSet.name().localName(), AttributeValueReferenceSet)

SimpleMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSet'), SimpleMapReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7894, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSet.name().localName(), SimpleMapReferenceSet)

ComplexMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSet'), ComplexMapReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7922, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSet.name().localName(), ComplexMapReferenceSet)

LanguageReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSet'), LanguageReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7946, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSet.name().localName(), LanguageReferenceSet)

QuerySpecificationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSet'), QuerySpecificationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7968, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSet.name().localName(), QuerySpecificationReferenceSet)

AnnotationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSet'), AnnotationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7991, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSet.name().localName(), AnnotationReferenceSet)

AssociationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSet'), AssociationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8013, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSet.name().localName(), AssociationReferenceSet)

ModuleDepencencyReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModuleDepencencyReferenceSet'), ModuleDepencencyReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8038, 4))
Namespace.addCategoryObject('elementBinding', ModuleDepencencyReferenceSet.name().localName(), ModuleDepencencyReferenceSet)

DescriptionFormatReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSet'), DescriptionFormatReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8061, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSet.name().localName(), DescriptionFormatReferenceSet)



SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sctid'), SCTID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 55, 12)))

SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uuid'), UUID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 56, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sctid')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 55, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uuid')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 56, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SCTIDorUUID._Automaton = _BuildAutomaton()




Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), SCTID, scope=Base, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=Base, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=Base, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), SCTID, scope=Base, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Base._Automaton = _BuildAutomaton_()




Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId'), Identifier_scheme, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7714, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier'), String, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7715, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7716, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7717, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), Module, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7718, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId'), SCTID, scope=Identifier_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7719, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7714, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7715, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7716, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7717, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7718, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7719, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Identifier_._Automaton = _BuildAutomaton_2()




TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subtypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7738, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supertypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7739, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7740, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7741, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subtypeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7738, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supertypeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7739, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7740, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7741, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TransitiveClosureHistory_._Automaton = _BuildAutomaton_3()




RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), UUID, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), SCTID, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'refsetId'), SCTID, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId'), SCTIDorUUID, scope=RefsetBase, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RefsetBase._Automaton = _BuildAutomaton_4()




Concept_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId'), Definition_status, scope=Concept_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7638, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7638, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Concept_._Automaton = _BuildAutomaton_5()




Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), SCTID, scope=Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7661, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'languageCode'), String, scope=Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7662, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeId'), Description_type, scope=Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7663, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'term'), String, scope=Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7664, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId'), Case_significance, scope=Description_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7665, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'conceptId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7661, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'languageCode')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7662, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7663, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'term')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7664, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7665, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Description_._Automaton = _BuildAutomaton_6()




Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7688, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'destinationId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7689, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup'), Integer, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7690, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeId'), Linkage_concept, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7691, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId'), Characteristic_type, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7692, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'modifierId'), Modifier, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7693, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'isCanonical'), Boolean, scope=Relationship_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7694, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7688, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'destinationId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7689, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7690, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7691, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7692, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'modifierId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7693, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'isCanonical')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7694, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Relationship_._Automaton = _BuildAutomaton_7()




DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription'), Reference_set_attribute, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7786, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeType'), Attribute_type, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7787, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder'), STD_ANON, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7788, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7786, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeType')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7787, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7788, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DescriptorReferenceSetEntry_._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleReferenceSetEntry_._Automaton = _BuildAutomaton_9()




OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), STD_ANON_, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7835, 20)))

OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'linkedTo'), SCTID, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7842, 20)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7842, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7835, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'linkedTo')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7842, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OrderedReferenceSetEntry_._Automaton = _BuildAutomaton_10()




AttributeValueReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'valueId'), Attribute_value, scope=AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7865, 20)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'valueId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7865, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AttributeValueReferenceSetEntry_._Automaton = _BuildAutomaton_11()




SimpleMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), String, scope=SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7888, 20)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTarget')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7888, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SimpleMapReferenceSetEntry_._Automaton = _BuildAutomaton_12()




ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapGroup'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7911, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapPriority'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7912, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7913, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7914, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7915, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'correlationId'), SNOMED_CT_source_code_to_target_map_code_correlation_value, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7916, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapCategoryId'), ICD_10_map_category_value, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7917, 20)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7913, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7914, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7915, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7916, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7917, 20))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapGroup')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7911, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapPriority')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7912, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapRule')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7913, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7914, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTarget')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7915, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'correlationId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7916, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapCategoryId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7917, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComplexMapReferenceSetEntry_._Automaton = _BuildAutomaton_13()




LanguageReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId'), Acceptability, scope=LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7939, 20)))

LanguageReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), SCTID, scope=LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7941, 20)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7941, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7939, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'conceptId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7941, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LanguageReferenceSetEntry_._Automaton = _BuildAutomaton_14()




QuerySpecificationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'query'), String, scope=QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7963, 20)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'query')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7963, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
QuerySpecificationReferenceSetEntry_._Automaton = _BuildAutomaton_15()




AnnotationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'annotation'), String, scope=AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7986, 20)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7986, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AnnotationReferenceSetEntry_._Automaton = _BuildAutomaton_16()




AssociationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetComponent'), SCTID, scope=AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8008, 20)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetComponent')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8008, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssociationReferenceSetEntry_._Automaton = _BuildAutomaton_17()




ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8031, 20)))

ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8032, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8031, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8032, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ModuleDependencyReferenceSetEntry_._Automaton = _BuildAutomaton_18()




DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat'), Description_format, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8055, 20)))

DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength'), Integer, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8056, 20)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7765, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7767, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7769, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7770, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8055, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8056, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DescriptionFormatReferenceSetEntry_._Automaton = _BuildAutomaton_19()




ConceptList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Concept_, scope=ConceptList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7649, 20)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7649, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConceptList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7649, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConceptList_._Automaton = _BuildAutomaton_20()




DescriptionList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Description_, scope=DescriptionList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7677, 20)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7677, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7677, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptionList_._Automaton = _BuildAutomaton_21()




RelationshipList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Relationship_, scope=RelationshipList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7705, 20)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7705, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelationshipList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7705, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelationshipList_._Automaton = _BuildAutomaton_22()




IdentifierList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Identifier_, scope=IdentifierList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7728, 20)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7728, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7728, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentifierList_._Automaton = _BuildAutomaton_23()




TransitiveClosureHistoryList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), TransitiveClosureHistory_, scope=TransitiveClosureHistoryList_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7751, 20)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7751, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistoryList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7751, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransitiveClosureHistoryList_._Automaton = _BuildAutomaton_24()




DescriptorReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), DescriptorReferenceSetEntry_, scope=DescriptorReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7805, 20)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7805, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7805, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptorReferenceSet_._Automaton = _BuildAutomaton_25()




SimpleReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), SimpleReferenceSetEntry_, scope=SimpleReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7824, 20)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7824, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7824, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleReferenceSet_._Automaton = _BuildAutomaton_26()




OrderedReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), OrderedReferenceSetEntry_, scope=OrderedReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7853, 20)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7853, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7853, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrderedReferenceSet_._Automaton = _BuildAutomaton_27()




AttributeValueReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AttributeValueReferenceSetEntry_, scope=AttributeValueReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7875, 20)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7875, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7875, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AttributeValueReferenceSet_._Automaton = _BuildAutomaton_28()




SimpleMapReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), SimpleMapReferenceSetEntry_, scope=SimpleMapReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7899, 20)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7899, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7899, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleMapReferenceSet_._Automaton = _BuildAutomaton_29()




ComplexMapReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), ComplexMapReferenceSetEntry_, scope=ComplexMapReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7927, 20)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7927, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7927, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ComplexMapReferenceSet_._Automaton = _BuildAutomaton_30()




LanguageReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), LanguageReferenceSetEntry_, scope=LanguageReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7951, 20)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7951, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7951, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LanguageReferenceSet_._Automaton = _BuildAutomaton_31()




QuerySpecificationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), QuerySpecificationReferenceSetEntry_, scope=QuerySpecificationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7973, 20)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7973, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7973, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
QuerySpecificationReferenceSet_._Automaton = _BuildAutomaton_32()




AnnotationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AnnotationReferenceSetEntry_, scope=AnnotationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7996, 20)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7996, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 7996, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnnotationReferenceSet_._Automaton = _BuildAutomaton_33()




AssociationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AssociationReferenceSetEntry_, scope=AssociationReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8018, 20)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8018, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8018, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AssociationReferenceSet_._Automaton = _BuildAutomaton_34()




ModuleDepencencyReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), ModuleDependencyReferenceSetEntry_, scope=ModuleDepencencyReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8043, 20)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8043, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModuleDepencencyReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8043, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ModuleDepencencyReferenceSet_._Automaton = _BuildAutomaton_35()




DescriptionFormatReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), DescriptionFormatReferenceSetEntry_, scope=DescriptionFormatReferenceSet_, location=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8066, 20)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8066, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://localhost:8081/rf2/xsd/rf2.xsd', 8066, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptionFormatReferenceSet_._Automaton = _BuildAutomaton_36()

