# ./rf2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a62023a1e63ecb635c8d1a3482d1f64c6fb3e0f6
# Generated 2013-12-16 16:33:51.810717 by PyXB version 1.2.3
# Namespace http://snomed.info/schema/rf2

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:23623123-66a2-11e3-8f56-c82a1438c957')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 9, 4)
    _Documentation = None
SCTID._CF_pattern = pyxb.binding.facets.CF_pattern()
SCTID._CF_pattern.addPattern(pattern=u'[0-9]{6,18}')
SCTID._InitializeFacetMap(SCTID._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'SCTID', SCTID)

# Atomic simple type: {http://snomed.info/schema/rf2}UUID
class UUID (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UUID')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 15, 4)
    _Documentation = None
UUID._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'UUID', UUID)

# Atomic simple type: {http://snomed.info/schema/rf2}String
class String (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'String')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 19, 4)
    _Documentation = None
String._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'String', String)

# Atomic simple type: {http://snomed.info/schema/rf2}Integer
class Integer (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Integer')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 23, 4)
    _Documentation = None
Integer._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'Integer', Integer)

# Atomic simple type: {http://snomed.info/schema/rf2}Boolean
class Boolean (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Boolean')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 27, 4)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 42, 4)
    _Documentation = None
Time._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'Time', Time)

# Atomic simple type: {http://snomed.info/schema/rf2}CompleteDirectory
class CompleteDirectory (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether a  contains all of the qualifying entries or only some."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CompleteDirectory')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 338, 4)
    _Documentation = u'An indicator that determines whether a  contains all of the qualifying entries or only some.'
CompleteDirectory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompleteDirectory, enum_prefix=None)
CompleteDirectory.COMPLETE = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value=u'COMPLETE', tag=u'COMPLETE')
CompleteDirectory.PARTIAL = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value=u'PARTIAL', tag=u'PARTIAL')
CompleteDirectory._InitializeFacetMap(CompleteDirectory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CompleteDirectory', CompleteDirectory)

# Atomic simple type: {http://snomed.info/schema/rf2}SortDirection
class SortDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The collating order of a sort."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SortDirection')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 356, 4)
    _Documentation = u'The collating order of a sort.'
SortDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortDirection, enum_prefix=None)
SortDirection.ASCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'ASCENDING', tag=u'ASCENDING')
SortDirection.DESCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value=u'DESCENDING', tag=u'DESCENDING')
SortDirection._InitializeFacetMap(SortDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SortDirection', SortDirection)

# Atomic simple type: {http://snomed.info/schema/rf2}VSModule
class VSModule (SCTID):

    """Descendent of 900000000000443000|module|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSModule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 57, 4)
    _Documentation = u'Descendent of 900000000000443000|module|'
VSModule._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSModule', VSModule)

# Atomic simple type: {http://snomed.info/schema/rf2}VSDefinitionStatus
class VSDefinitionStatus (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000444006|definition status|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSDefinitionStatus')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 64, 4)
    _Documentation = u'Child of 900000000000444006|definition status|'
VSDefinitionStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSDefinitionStatus, enum_prefix=None)
VSDefinitionStatus.n900000000000073002 = VSDefinitionStatus._CF_enumeration.addEnumeration(unicode_value=u'900000000000073002', tag=u'n900000000000073002')
VSDefinitionStatus.n900000000000074008 = VSDefinitionStatus._CF_enumeration.addEnumeration(unicode_value=u'900000000000074008', tag=u'n900000000000074008')
VSDefinitionStatus._InitializeFacetMap(VSDefinitionStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSDefinitionStatus', VSDefinitionStatus)

# Atomic simple type: {http://snomed.info/schema/rf2}VSDescriptionType
class VSDescriptionType (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000446008|description type|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSDescriptionType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 82, 4)
    _Documentation = u'Child of 900000000000446008|description type|'
VSDescriptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSDescriptionType, enum_prefix=None)
VSDescriptionType.n900000000000550004 = VSDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'900000000000550004', tag=u'n900000000000550004')
VSDescriptionType.n900000000000003001 = VSDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'900000000000003001', tag=u'n900000000000003001')
VSDescriptionType.n900000000000187000 = VSDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'900000000000187000', tag=u'n900000000000187000')
VSDescriptionType.n900000000000013009 = VSDescriptionType._CF_enumeration.addEnumeration(unicode_value=u'900000000000013009', tag=u'n900000000000013009')
VSDescriptionType._InitializeFacetMap(VSDescriptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSDescriptionType', VSDescriptionType)

# Atomic simple type: {http://snomed.info/schema/rf2}VSCaseSignificance
class VSCaseSignificance (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000447004|case significance|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSCaseSignificance')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 110, 4)
    _Documentation = u'Child of 900000000000447004|case significance|'
VSCaseSignificance._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSCaseSignificance, enum_prefix=None)
VSCaseSignificance.n900000000000448009 = VSCaseSignificance._CF_enumeration.addEnumeration(unicode_value=u'900000000000448009', tag=u'n900000000000448009')
VSCaseSignificance.n900000000000016001 = VSCaseSignificance._CF_enumeration.addEnumeration(unicode_value=u'900000000000016001', tag=u'n900000000000016001')
VSCaseSignificance.n900000000000017005 = VSCaseSignificance._CF_enumeration.addEnumeration(unicode_value=u'900000000000017005', tag=u'n900000000000017005')
VSCaseSignificance.n900000000000022005 = VSCaseSignificance._CF_enumeration.addEnumeration(unicode_value=u'900000000000022005', tag=u'n900000000000022005')
VSCaseSignificance.n900000000000020002 = VSCaseSignificance._CF_enumeration.addEnumeration(unicode_value=u'900000000000020002', tag=u'n900000000000020002')
VSCaseSignificance._InitializeFacetMap(VSCaseSignificance._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSCaseSignificance', VSCaseSignificance)

# Atomic simple type: {http://snomed.info/schema/rf2}VSRelationshipType
class VSRelationshipType (SCTID):

    """Descendant of 106237007|linkage concept|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSRelationshipType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 143, 4)
    _Documentation = u'Descendant of 106237007|linkage concept|'
VSRelationshipType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSRelationshipType', VSRelationshipType)

# Atomic simple type: {http://snomed.info/schema/rf2}VSCharacteristicType
class VSCharacteristicType (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Descendant of 900000000000449001|characteristic type|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSCharacteristicType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 150, 4)
    _Documentation = u'Descendant of 900000000000449001|characteristic type|'
VSCharacteristicType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSCharacteristicType, enum_prefix=None)
VSCharacteristicType.n900000000000227009 = VSCharacteristicType._CF_enumeration.addEnumeration(unicode_value=u'900000000000227009', tag=u'n900000000000227009')
VSCharacteristicType.n900000000000409009 = VSCharacteristicType._CF_enumeration.addEnumeration(unicode_value=u'900000000000409009', tag=u'n900000000000409009')
VSCharacteristicType.n900000000000006009 = VSCharacteristicType._CF_enumeration.addEnumeration(unicode_value=u'900000000000006009', tag=u'n900000000000006009')
VSCharacteristicType.n900000000000011006 = VSCharacteristicType._CF_enumeration.addEnumeration(unicode_value=u'900000000000011006', tag=u'n900000000000011006')
VSCharacteristicType.n900000000000010007 = VSCharacteristicType._CF_enumeration.addEnumeration(unicode_value=u'900000000000010007', tag=u'n900000000000010007')
VSCharacteristicType._InitializeFacetMap(VSCharacteristicType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSCharacteristicType', VSCharacteristicType)

# Atomic simple type: {http://snomed.info/schema/rf2}VSModifier
class VSModifier (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000450001|modifier|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSModifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 187, 4)
    _Documentation = u'Child of 900000000000450001|modifier|'
VSModifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSModifier, enum_prefix=None)
VSModifier.n900000000000452009 = VSModifier._CF_enumeration.addEnumeration(unicode_value=u'900000000000452009', tag=u'n900000000000452009')
VSModifier.n900000000000451002 = VSModifier._CF_enumeration.addEnumeration(unicode_value=u'900000000000451002', tag=u'n900000000000451002')
VSModifier._InitializeFacetMap(VSModifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSModifier', VSModifier)

# Atomic simple type: {http://snomed.info/schema/rf2}VSIdentifierScheme
class VSIdentifierScheme (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000453004|identifier scheme|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSIdentifierScheme')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 205, 4)
    _Documentation = u'Child of 900000000000453004|identifier scheme|'
VSIdentifierScheme._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSIdentifierScheme, enum_prefix=None)
VSIdentifierScheme.n900000000000118003 = VSIdentifierScheme._CF_enumeration.addEnumeration(unicode_value=u'900000000000118003', tag=u'n900000000000118003')
VSIdentifierScheme.n900000000000002006 = VSIdentifierScheme._CF_enumeration.addEnumeration(unicode_value=u'900000000000002006', tag=u'n900000000000002006')
VSIdentifierScheme._InitializeFacetMap(VSIdentifierScheme._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSIdentifierScheme', VSIdentifierScheme)

# Atomic simple type: {http://snomed.info/schema/rf2}VSRefSet
class VSRefSet (SCTID):

    """Descendant of 900000000000455006|reference set|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSRefSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 223, 4)
    _Documentation = u'Descendant of 900000000000455006|reference set|'
VSRefSet._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSRefSet', VSRefSet)

# Atomic simple type: {http://snomed.info/schema/rf2}VSAttributeDescription
class VSAttributeDescription (SCTID):

    """Descendant of 900000000000457003|reference set attribute|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSAttributeDescription')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 230, 4)
    _Documentation = u'Descendant of 900000000000457003|reference set attribute|'
VSAttributeDescription._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSAttributeDescription', VSAttributeDescription)

# Atomic simple type: {http://snomed.info/schema/rf2}VSAttributeType
class VSAttributeType (SCTID):

    """Descendant of 900000000000459000|attribute type|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 237, 4)
    _Documentation = u'Descendant of 900000000000459000|attribute type|'
VSAttributeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSAttributeType', VSAttributeType)

# Atomic simple type: {http://snomed.info/schema/rf2}VSAttributeValue
class VSAttributeValue (SCTID):

    """Grandchild of 900000000000491004|attribute value|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSAttributeValue')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 244, 4)
    _Documentation = u'Grandchild of 900000000000491004|attribute value|'
VSAttributeValue._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'VSAttributeValue', VSAttributeValue)

# Atomic simple type: {http://snomed.info/schema/rf2}VSMapCorrelation
class VSMapCorrelation (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 447247004|SNOMED CT source code to target map code correlation value|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSMapCorrelation')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 251, 4)
    _Documentation = u'Child of 447247004|SNOMED CT source code to target map code correlation value|'
VSMapCorrelation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSMapCorrelation, enum_prefix=None)
VSMapCorrelation.n447556008 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447556008', tag=u'n447556008')
VSMapCorrelation.n447557004 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447557004', tag=u'n447557004')
VSMapCorrelation.n447558009 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447558009', tag=u'n447558009')
VSMapCorrelation.n447559001 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447559001', tag=u'n447559001')
VSMapCorrelation.n447560006 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447560006', tag=u'n447560006')
VSMapCorrelation.n447561005 = VSMapCorrelation._CF_enumeration.addEnumeration(unicode_value=u'447561005', tag=u'n447561005')
VSMapCorrelation._InitializeFacetMap(VSMapCorrelation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSMapCorrelation', VSMapCorrelation)

# Atomic simple type: {http://snomed.info/schema/rf2}VSAcceptability
class VSAcceptability (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Descendant of 900000000000511003|acceptability"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSAcceptability')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 289, 4)
    _Documentation = u'Descendant of 900000000000511003|acceptability'
VSAcceptability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSAcceptability, enum_prefix=None)
VSAcceptability.n900000000000549004 = VSAcceptability._CF_enumeration.addEnumeration(unicode_value=u'900000000000549004', tag=u'n900000000000549004')
VSAcceptability.n900000000000548007 = VSAcceptability._CF_enumeration.addEnumeration(unicode_value=u'900000000000548007', tag=u'n900000000000548007')
VSAcceptability._InitializeFacetMap(VSAcceptability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSAcceptability', VSAcceptability)

# Atomic simple type: {http://snomed.info/schema/rf2}VSDescriptionFormat
class VSDescriptionFormat (SCTID, pyxb.binding.basis.enumeration_mixin):

    """Child of 900000000000539002|description format|"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VSDescriptionFormat')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 307, 4)
    _Documentation = u'Child of 900000000000539002|description format|'
VSDescriptionFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VSDescriptionFormat, enum_prefix=None)
VSDescriptionFormat.n900000000000543003 = VSDescriptionFormat._CF_enumeration.addEnumeration(unicode_value=u'900000000000543003', tag=u'n900000000000543003')
VSDescriptionFormat.n900000000000541001 = VSDescriptionFormat._CF_enumeration.addEnumeration(unicode_value=u'900000000000541001', tag=u'n900000000000541001')
VSDescriptionFormat.n900000000000540000 = VSDescriptionFormat._CF_enumeration.addEnumeration(unicode_value=u'900000000000540000', tag=u'n900000000000540000')
VSDescriptionFormat.n900000000000542008 = VSDescriptionFormat._CF_enumeration.addEnumeration(unicode_value=u'900000000000542008', tag=u'n900000000000542008')
VSDescriptionFormat._InitializeFacetMap(VSDescriptionFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'VSDescriptionFormat', VSDescriptionFormat)

# Atomic simple type: [anonymous]
class STD_ANON (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 564, 24)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 611, 24)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}sctid uses Python identifier sctid
    __sctid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sctid'), 'sctid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2sctid', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 48, 12), )

    
    sctid = property(__sctid.value, __sctid.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uuid'), 'uuid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2uuid', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 49, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 401, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 490, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}identifierSchemeId uses Python identifier identifierSchemeId
    __identifierSchemeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId'), 'identifierSchemeId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2identifierSchemeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 492, 12), )

    
    identifierSchemeId = property(__identifierSchemeId.value, __identifierSchemeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}alternateIdentifier uses Python identifier alternateIdentifier
    __alternateIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier'), 'alternateIdentifier', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2alternateIdentifier', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 493, 12), )

    
    alternateIdentifier = property(__alternateIdentifier.value, __alternateIdentifier.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 494, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 495, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 496, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referenceComponentId uses Python identifier referenceComponentId
    __referenceComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId'), 'referenceComponentId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2referenceComponentId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 497, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 515, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}subtypeId uses Python identifier subtypeId
    __subtypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'subtypeId'), 'subtypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2subtypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 517, 12), )

    
    subtypeId = property(__subtypeId.value, __subtypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}supertypeId uses Python identifier supertypeId
    __supertypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'supertypeId'), 'supertypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2supertypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 518, 12), )

    
    supertypeId = property(__supertypeId.value, __supertypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 519, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 520, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 541, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'active'), 'active', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}refsetId uses Python identifier refsetId
    __refsetId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'refsetId'), 'refsetId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2refsetId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12), )

    
    refsetId = property(__refsetId.value, __refsetId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referencedComponentId uses Python identifier referencedComponentId
    __referencedComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId'), 'referencedComponentId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2referencedComponentId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 374, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute complete uses Python identifier complete
    __complete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'complete'), 'complete', '__httpsnomed_infoschemarf2_Iterator_complete', CompleteDirectory, required=True)
    __complete._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 375, 8)
    __complete._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 375, 8)
    
    complete = property(__complete.value, __complete.set, None, u'an indicator that states whether the complete directory listing is included in  or whether additional retrievals are needed to get the full listing.')

    
    # Attribute numEntries uses Python identifier numEntries
    __numEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'numEntries'), 'numEntries', '__httpsnomed_infoschemarf2_Iterator_numEntries', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __numEntries._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 380, 8)
    __numEntries._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 380, 8)
    
    numEntries = property(__numEntries.value, __numEntries.set, None, u'the number of entries in this directory segment. Note that this is  the total number of entries in the complete directory listing - just the number of entries in this\n                    segment.')

    
    # Attribute prev uses Python identifier prev
    __prev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'prev'), 'prev', '__httpsnomed_infoschemarf2_Iterator_prev', pyxb.binding.datatypes.anyURI)
    __prev._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 386, 8)
    __prev._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 386, 8)
    
    prev = property(__prev.value, __prev.set, None, u'a URI that, when de-referenced, produces the preceding set of entries in the directory.')

    
    # Attribute next uses Python identifier next
    __next = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'next'), 'next', '__httpsnomed_infoschemarf2_Iterator_next', pyxb.binding.datatypes.anyURI)
    __next._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 391, 8)
    __next._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 391, 8)
    
    next = property(__next.value, __next.set, None, u'a URI that, when de-referenced, produces the next set of entries in the directory.')

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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 412, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}definitionStatusId uses Python identifier definitionStatusId
    __definitionStatusId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId'), 'definitionStatusId', '__httpsnomed_infoschemarf2_Concept__httpsnomed_infoschemarf2definitionStatusId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 416, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 435, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}conceptId uses Python identifier conceptId
    __conceptId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), 'conceptId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2conceptId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 439, 20), )

    
    conceptId = property(__conceptId.value, __conceptId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}languageCode uses Python identifier languageCode
    __languageCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'languageCode'), 'languageCode', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2languageCode', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 440, 20), )

    
    languageCode = property(__languageCode.value, __languageCode.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 441, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'term'), 'term', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2term', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 442, 20), )

    
    term = property(__term.value, __term.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}caseSignificanceId uses Python identifier caseSignificanceId
    __caseSignificanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId'), 'caseSignificanceId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2caseSignificanceId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 443, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 462, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}sourceId uses Python identifier sourceId
    __sourceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceId'), 'sourceId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2sourceId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 466, 20), )

    
    sourceId = property(__sourceId.value, __sourceId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}destinationId uses Python identifier destinationId
    __destinationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'destinationId'), 'destinationId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2destinationId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 467, 20), )

    
    destinationId = property(__destinationId.value, __destinationId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}relationshipGroup uses Python identifier relationshipGroup
    __relationshipGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup'), 'relationshipGroup', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2relationshipGroup', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 468, 20), )

    
    relationshipGroup = property(__relationshipGroup.value, __relationshipGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 469, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}characteristicTypeId uses Python identifier characteristicTypeId
    __characteristicTypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId'), 'characteristicTypeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2characteristicTypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 470, 20), )

    
    characteristicTypeId = property(__characteristicTypeId.value, __characteristicTypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}modifierId uses Python identifier modifierId
    __modifierId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'modifierId'), 'modifierId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2modifierId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 471, 20), )

    
    modifierId = property(__modifierId.value, __modifierId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}isCanonical uses Python identifier isCanonical
    __isCanonical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'isCanonical'), 'isCanonical', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2isCanonical', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 472, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 553, 4)
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
    __attributeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription'), 'attributeDescription', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeDescription', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 561, 20), )

    
    attributeDescription = property(__attributeDescription.value, __attributeDescription.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeType'), 'attributeType', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeType', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 562, 20), )

    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeOrder uses Python identifier attributeOrder
    __attributeOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder'), 'attributeOrder', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeOrder', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 563, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 588, 4)
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 606, 4)
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
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2order', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 610, 20), )

    
    order = property(__order.value, __order.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}linkedTo uses Python identifier linkedTo
    __linkedTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'linkedTo'), 'linkedTo', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2linkedTo', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 617, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 635, 4)
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
    __valueId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'valueId'), 'valueId', '__httpsnomed_infoschemarf2_AttributeValueReferenceSetEntry__httpsnomed_infoschemarf2valueId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 639, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 658, 4)
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
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_SimpleMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 662, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 681, 4)
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
    __mapGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapGroup'), 'mapGroup', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapGroup', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 685, 20), )

    
    mapGroup = property(__mapGroup.value, __mapGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapPriority uses Python identifier mapPriority
    __mapPriority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapPriority'), 'mapPriority', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapPriority', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 686, 20), )

    
    mapPriority = property(__mapPriority.value, __mapPriority.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapRule uses Python identifier mapRule
    __mapRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), 'mapRule', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapRule', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 687, 20), )

    
    mapRule = property(__mapRule.value, __mapRule.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapAdvice uses Python identifier mapAdvice
    __mapAdvice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice'), 'mapAdvice', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapAdvice', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 688, 20), )

    
    mapAdvice = property(__mapAdvice.value, __mapAdvice.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapTarget uses Python identifier mapTarget
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 689, 20), )

    
    mapTarget = property(__mapTarget.value, __mapTarget.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapCategory uses Python identifier mapCategory
    __mapCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mapCategory'), 'mapCategory', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapCategory', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 690, 20), )

    
    mapCategory = property(__mapCategory.value, __mapCategory.set, None, None)

    _ElementMap.update({
        __mapGroup.name() : __mapGroup,
        __mapPriority.name() : __mapPriority,
        __mapRule.name() : __mapRule,
        __mapAdvice.name() : __mapAdvice,
        __mapTarget.name() : __mapTarget,
        __mapCategory.name() : __mapCategory
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 708, 4)
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
    __acceptabilityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId'), 'acceptabilityId', '__httpsnomed_infoschemarf2_LanguageReferenceSetEntry__httpsnomed_infoschemarf2acceptabilityId', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 712, 20), )

    
    acceptabilityId = property(__acceptabilityId.value, __acceptabilityId.set, None, None)

    _ElementMap.update({
        __acceptabilityId.name() : __acceptabilityId
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 730, 4)
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
    __query = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'query'), 'query', '__httpsnomed_infoschemarf2_QuerySpecificationReferenceSetEntry__httpsnomed_infoschemarf2query', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 734, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 752, 4)
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
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'annotation'), 'annotation', '__httpsnomed_infoschemarf2_AnnotationReferenceSetEntry__httpsnomed_infoschemarf2annotation', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 756, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 774, 4)
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
    __targetComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetComponent'), 'targetComponent', '__httpsnomed_infoschemarf2_AssociationReferenceSetEntry__httpsnomed_infoschemarf2targetComponent', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 778, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 797, 4)
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
    __sourceEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime'), 'sourceEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2sourceEffectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 801, 20), )

    
    sourceEffectiveTime = property(__sourceEffectiveTime.value, __sourceEffectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}targetEffectiveTime uses Python identifier targetEffectiveTime
    __targetEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime'), 'targetEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2targetEffectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 802, 20), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 821, 4)
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
    __descriptionFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat'), 'descriptionFormat', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionFormat', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 825, 20), )

    
    descriptionFormat = property(__descriptionFormat.value, __descriptionFormat.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}descriptionLength uses Python identifier descriptionLength
    __descriptionLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength'), 'descriptionLength', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionLength', False, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 826, 20), )

    
    descriptionLength = property(__descriptionLength.value, __descriptionLength.set, None, None)

    _ElementMap.update({
        __descriptionFormat.name() : __descriptionFormat,
        __descriptionLength.name() : __descriptionLength
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptionFormatReferenceSetEntry', DescriptionFormatReferenceSetEntry_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 423, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 427, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 450, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 454, 24), )

    
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



# Complex type {http://snomed.info/schema/rf2}RelationshipList_ with content type ELEMENT_ONLY
class RelationshipList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}RelationshipList_ with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelationshipList_')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 479, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_RelationshipList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 483, 24), )

    
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
Namespace.addCategoryObject('typeBinding', u'RelationshipList_', RelationshipList_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 502, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_2_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 506, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 526, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_3_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 530, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 576, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_4_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 580, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 594, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_5_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 598, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 623, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_6_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 627, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 645, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_7_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 649, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 669, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_8_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 673, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 696, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_9_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 700, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 718, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_10_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 722, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 740, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_11_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 744, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 762, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_12_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 766, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 784, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_13_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 788, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 809, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_14_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 813, 24), )

    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (Iterator):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 832, 8)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpsnomed_infoschemarf2_CTD_ANON_15_httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 836, 24), )

    
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



Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 489, 4))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

TransitiveClosureHistory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistory'), TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 514, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistory.name().localName(), TransitiveClosureHistory)

Concept = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Concept'), Concept_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 411, 4))
Namespace.addCategoryObject('elementBinding', Concept.name().localName(), Concept)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 434, 4))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

Relationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Relationship'), Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 461, 4))
Namespace.addCategoryObject('elementBinding', Relationship.name().localName(), Relationship)

DescriptorReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSetEntry'), DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 552, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSetEntry.name().localName(), DescriptorReferenceSetEntry)

SimpleReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSetEntry'), SimpleReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 587, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSetEntry.name().localName(), SimpleReferenceSetEntry)

OrderedReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSetEntry'), OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 605, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSetEntry.name().localName(), OrderedReferenceSetEntry)

AttributeValueReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSetEntry'), AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 634, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSetEntry.name().localName(), AttributeValueReferenceSetEntry)

SimpleMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSetEntry'), SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 657, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSetEntry.name().localName(), SimpleMapReferenceSetEntry)

ComplexMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSetEntry'), ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 680, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSetEntry.name().localName(), ComplexMapReferenceSetEntry)

LanguageReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSetEntry'), LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 707, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSetEntry.name().localName(), LanguageReferenceSetEntry)

QuerySpecificationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSetEntry'), QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 729, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSetEntry.name().localName(), QuerySpecificationReferenceSetEntry)

AnnotationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSetEntry'), AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 751, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSetEntry.name().localName(), AnnotationReferenceSetEntry)

AssociationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSetEntry'), AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 773, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSetEntry.name().localName(), AssociationReferenceSetEntry)

ModuleDependencyReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModuleDependencyReferenceSetEntry'), ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 796, 4))
Namespace.addCategoryObject('elementBinding', ModuleDependencyReferenceSetEntry.name().localName(), ModuleDependencyReferenceSetEntry)

DescriptionFormatReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSetEntry'), DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 820, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSetEntry.name().localName(), DescriptionFormatReferenceSetEntry)

ConceptList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConceptList'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 422, 4))
Namespace.addCategoryObject('elementBinding', ConceptList.name().localName(), ConceptList)

DescriptionList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionList'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 449, 4))
Namespace.addCategoryObject('elementBinding', DescriptionList.name().localName(), DescriptionList)

RelationshipList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelationshipList'), RelationshipList_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 478, 4))
Namespace.addCategoryObject('elementBinding', RelationshipList.name().localName(), RelationshipList)

IdentifierList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IdentifierList'), CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 501, 4))
Namespace.addCategoryObject('elementBinding', IdentifierList.name().localName(), IdentifierList)

TransitiveClosureHistoryList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransitiveClosureHistoryList'), CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 525, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistoryList.name().localName(), TransitiveClosureHistoryList)

DescriptorReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptorReferenceSet'), CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 575, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSet.name().localName(), DescriptorReferenceSet)

SimpleReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleReferenceSet'), CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 593, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSet.name().localName(), SimpleReferenceSet)

OrderedReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OrderedReferenceSet'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 622, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSet.name().localName(), OrderedReferenceSet)

AttributeValueReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeValueReferenceSet'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 644, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSet.name().localName(), AttributeValueReferenceSet)

SimpleMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SimpleMapReferenceSet'), CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 668, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSet.name().localName(), SimpleMapReferenceSet)

ComplexMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComplexMapReferenceSet'), CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 695, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSet.name().localName(), ComplexMapReferenceSet)

LanguageReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LanguageReferenceSet'), CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 717, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSet.name().localName(), LanguageReferenceSet)

QuerySpecificationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'QuerySpecificationReferenceSet'), CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 739, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSet.name().localName(), QuerySpecificationReferenceSet)

AnnotationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AnnotationReferenceSet'), CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 761, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSet.name().localName(), AnnotationReferenceSet)

AssociationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AssociationReferenceSet'), CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 783, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSet.name().localName(), AssociationReferenceSet)

ModuleDepencencyReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ModuleDepencencyReferenceSet'), CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 808, 4))
Namespace.addCategoryObject('elementBinding', ModuleDepencencyReferenceSet.name().localName(), ModuleDepencencyReferenceSet)

DescriptionFormatReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DescriptionFormatReferenceSet'), CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 831, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSet.name().localName(), DescriptionFormatReferenceSet)



SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sctid'), SCTID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 48, 12)))

SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uuid'), UUID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 49, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sctid')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uuid')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 49, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SCTIDorUUID._Automaton = _BuildAutomaton()




Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), SCTID, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), VSModule, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12))
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




Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId'), VSIdentifierScheme, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 492, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier'), String, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 493, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 494, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 495, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), VSModule, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 496, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId'), SCTID, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 497, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'identifierSchemeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 492, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternateIdentifier')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 493, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 494, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 495, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 496, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referenceComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 497, 12))
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




TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subtypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 517, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'supertypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 518, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 519, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 520, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subtypeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 517, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'supertypeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 518, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 519, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 520, 12))
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




RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), UUID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime'), Time, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'active'), Boolean, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moduleId'), VSModule, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'refsetId'), VSRefSet, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId'), SCTIDorUUID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
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




Concept_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId'), VSDefinitionStatus, scope=Concept_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 416, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'definitionStatusId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 416, 20))
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




Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'conceptId'), SCTID, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 439, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'languageCode'), String, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 440, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeId'), VSDescriptionType, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 441, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'term'), String, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 442, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId'), VSCaseSignificance, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 443, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'conceptId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 439, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'languageCode')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 440, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 441, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'term')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 442, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseSignificanceId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 443, 20))
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




Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 466, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'destinationId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 467, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup'), Integer, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 468, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'typeId'), VSRelationshipType, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 469, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId'), VSCharacteristicType, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 470, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'modifierId'), VSModifier, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 471, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'isCanonical'), Boolean, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 472, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 403, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 404, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 405, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 406, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 466, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'destinationId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 467, 20))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'relationshipGroup')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 468, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'typeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 469, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'characteristicTypeId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 470, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'modifierId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 471, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'isCanonical')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 472, 20))
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




DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription'), VSAttributeDescription, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 561, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeType'), VSAttributeType, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 562, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder'), STD_ANON, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 563, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeDescription')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 561, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeType')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 562, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'attributeOrder')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 563, 20))
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
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
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




OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), STD_ANON_, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 610, 20)))

OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'linkedTo'), SCTID, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 617, 20)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 617, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 610, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'linkedTo')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 617, 20))
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




AttributeValueReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'valueId'), VSAttributeValue, scope=AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 639, 20)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'valueId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 639, 20))
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




SimpleMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), String, scope=SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 662, 20)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTarget')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 662, 20))
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




ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapGroup'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 685, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapPriority'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 686, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapRule'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 687, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 688, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapTarget'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 689, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mapCategory'), VSMapCorrelation, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 690, 20)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 687, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 688, 20))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapGroup')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 685, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapPriority')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 686, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapRule')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 687, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapAdvice')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 688, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapTarget')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 689, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mapCategory')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 690, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ComplexMapReferenceSetEntry_._Automaton = _BuildAutomaton_13()




LanguageReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId'), VSAcceptability, scope=LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 712, 20)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'acceptabilityId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 712, 20))
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
LanguageReferenceSetEntry_._Automaton = _BuildAutomaton_14()




QuerySpecificationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'query'), String, scope=QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 734, 20)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'query')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 734, 20))
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




AnnotationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'annotation'), String, scope=AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 756, 20)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 756, 20))
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




AssociationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetComponent'), SCTID, scope=AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 778, 20)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetComponent')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 778, 20))
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




ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 801, 20)))

ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 802, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sourceEffectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 801, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetEffectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 802, 20))
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




DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat'), VSDescriptionFormat, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 825, 20)))

DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength'), Integer, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 826, 20)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 544, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'active')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 545, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 546, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 547, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 548, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'descriptionFormat')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 825, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'descriptionLength')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 826, 20))
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




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Concept_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 427, 24)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 427, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 427, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_20()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Description_, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 454, 24)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 454, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 454, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_21()




RelationshipList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Relationship_, scope=RelationshipList_, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 483, 24)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 483, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelationshipList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 483, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelationshipList_._Automaton = _BuildAutomaton_22()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), Identifier_, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 506, 24)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 506, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 506, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_23()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), TransitiveClosureHistory_, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 530, 24)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 530, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 530, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_24()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), DescriptorReferenceSetEntry_, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 580, 24)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 580, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 580, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_25()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), SimpleReferenceSetEntry_, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 598, 24)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 598, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 598, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_26()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), OrderedReferenceSetEntry_, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 627, 24)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 627, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 627, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_27()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AttributeValueReferenceSetEntry_, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 649, 24)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 649, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 649, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_28()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), SimpleMapReferenceSetEntry_, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 673, 24)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 673, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 673, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_29()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), ComplexMapReferenceSetEntry_, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 700, 24)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 700, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 700, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_30()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), LanguageReferenceSetEntry_, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 722, 24)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 722, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 722, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_31()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), QuerySpecificationReferenceSetEntry_, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 744, 24)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 744, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 744, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_32()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AnnotationReferenceSetEntry_, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 766, 24)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 766, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 766, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_33()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), AssociationReferenceSetEntry_, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 788, 24)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 788, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 788, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_34()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), ModuleDependencyReferenceSetEntry_, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 813, 24)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 813, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 813, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_35()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), DescriptionFormatReferenceSetEntry_, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 836, 24)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 836, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('/Users/mrf7578/PycharmProjects/rf2db/rf2db/static/xsd/rf2.xsd', 836, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_36()

