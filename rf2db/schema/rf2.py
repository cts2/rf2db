# ../rf2db/schema/rf2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a62023a1e63ecb635c8d1a3482d1f64c6fb3e0f6
# Generated 2015-01-06 15:11:26.101084 by PyXB version 1.2.4 using Python 2.7.8.final.0
# Namespace http://snomed.info/schema/rf2

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9292824f-95e8-11e4-bccc-6c40088fdb3a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://snomed.info/schema/rf2', create_if_missing=True)
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCTID')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 16, 4)
    _Documentation = None
SCTID._CF_pattern = pyxb.binding.facets.CF_pattern()
SCTID._CF_pattern.addPattern(pattern='[0-9]{6,18}')
SCTID._InitializeFacetMap(SCTID._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'SCTID', SCTID)

# Atomic simple type: {http://snomed.info/schema/rf2}UUID
class UUID (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UUID')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 22, 4)
    _Documentation = None
UUID._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'UUID', UUID)

# Atomic simple type: {http://snomed.info/schema/rf2}String
class String (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'String')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 26, 4)
    _Documentation = None
String._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'String', String)

# Atomic simple type: {http://snomed.info/schema/rf2}Integer
class Integer (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Integer')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 30, 4)
    _Documentation = None
Integer._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Integer', Integer)

# Atomic simple type: {http://snomed.info/schema/rf2}Boolean
class Boolean (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Boolean')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 34, 4)
    _Documentation = None
Boolean._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Boolean, enum_prefix=None)
Boolean._CF_enumeration.addEnumeration(unicode_value='0', tag=None)
Boolean._CF_enumeration.addEnumeration(unicode_value='1', tag=None)
Boolean._InitializeFacetMap(Boolean._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Boolean', Boolean)

# Atomic simple type: {http://snomed.info/schema/rf2}Time
class Time (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Time')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 49, 4)
    _Documentation = None
Time._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'Time', Time)

# Atomic simple type: {http://snomed.info/schema/rf2}CompleteDirectory
class CompleteDirectory (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An indicator that determines whether a
                
                contains all of the qualifying entries or only some.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CompleteDirectory')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7543, 4)
    _Documentation = 'An indicator that determines whether a\n                \n                contains all of the qualifying entries or only some.\n            '
CompleteDirectory._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CompleteDirectory, enum_prefix=None)
CompleteDirectory.COMPLETE = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value='COMPLETE', tag='COMPLETE')
CompleteDirectory.PARTIAL = CompleteDirectory._CF_enumeration.addEnumeration(unicode_value='PARTIAL', tag='PARTIAL')
CompleteDirectory._InitializeFacetMap(CompleteDirectory._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CompleteDirectory', CompleteDirectory)

# Atomic simple type: {http://snomed.info/schema/rf2}SortDirection
class SortDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The collating order of a sort."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SortDirection')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7568, 4)
    _Documentation = 'The collating order of a sort.'
SortDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SortDirection, enum_prefix=None)
SortDirection.ASCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value='ASCENDING', tag='ASCENDING')
SortDirection.DESCENDING = SortDirection._CF_enumeration.addEnumeration(unicode_value='DESCENDING', tag='DESCENDING')
SortDirection._InitializeFacetMap(SortDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SortDirection', SortDirection)

# Atomic simple type: {http://snomed.info/schema/rf2}ICD-10_map_category_value
class ICD_10_map_category_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ICD-10_map_category_value')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 65, 4)
    _Documentation = '\n                \n            '
ICD_10_map_category_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ICD_10_map_category_value, enum_prefix=None)
ICD_10_map_category_value.n447635003 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447635003', tag='n447635003')
ICD_10_map_category_value.n447636002 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447636002', tag='n447636002')
ICD_10_map_category_value.n447637006 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447637006', tag='n447637006')
ICD_10_map_category_value.n447638001 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447638001', tag='n447638001')
ICD_10_map_category_value.n447639009 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447639009', tag='n447639009')
ICD_10_map_category_value.n447640006 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447640006', tag='n447640006')
ICD_10_map_category_value.n447641005 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447641005', tag='n447641005')
ICD_10_map_category_value.n447642003 = ICD_10_map_category_value._CF_enumeration.addEnumeration(unicode_value='447642003', tag='n447642003')
ICD_10_map_category_value._InitializeFacetMap(ICD_10_map_category_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ICD-10_map_category_value', ICD_10_map_category_value)

# Atomic simple type: {http://snomed.info/schema/rf2}Module
class Module (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Module')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 139, 4)
    _Documentation = '\n                \n            '
Module._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Module, enum_prefix=None)
Module.n449079008 = Module._CF_enumeration.addEnumeration(unicode_value='449079008', tag='n449079008')
Module.n449080006 = Module._CF_enumeration.addEnumeration(unicode_value='449080006', tag='n449080006')
Module.n449081005 = Module._CF_enumeration.addEnumeration(unicode_value='449081005', tag='n449081005')
Module.n5991000124107 = Module._CF_enumeration.addEnumeration(unicode_value='5991000124107', tag='n5991000124107')
Module.n900000000000012004 = Module._CF_enumeration.addEnumeration(unicode_value='900000000000012004', tag='n900000000000012004')
Module.n900000000000207008 = Module._CF_enumeration.addEnumeration(unicode_value='900000000000207008', tag='n900000000000207008')
Module.n900000000000445007 = Module._CF_enumeration.addEnumeration(unicode_value='900000000000445007', tag='n900000000000445007')
Module._InitializeFacetMap(Module._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Module', Module)

# Atomic simple type: {http://snomed.info/schema/rf2}Definition_status
class Definition_status (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Definition_status')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 201, 4)
    _Documentation = '\n                \n            '
Definition_status._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Definition_status, enum_prefix=None)
Definition_status.n900000000000073002 = Definition_status._CF_enumeration.addEnumeration(unicode_value='900000000000073002', tag='n900000000000073002')
Definition_status.n900000000000074008 = Definition_status._CF_enumeration.addEnumeration(unicode_value='900000000000074008', tag='n900000000000074008')
Definition_status._InitializeFacetMap(Definition_status._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Definition_status', Definition_status)

# Atomic simple type: {http://snomed.info/schema/rf2}Description_type
class Description_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Description_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 236, 4)
    _Documentation = '\n                \n            '
Description_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Description_type, enum_prefix=None)
Description_type.n900000000000003001 = Description_type._CF_enumeration.addEnumeration(unicode_value='900000000000003001', tag='n900000000000003001')
Description_type.n900000000000013009 = Description_type._CF_enumeration.addEnumeration(unicode_value='900000000000013009', tag='n900000000000013009')
Description_type.n900000000000550004 = Description_type._CF_enumeration.addEnumeration(unicode_value='900000000000550004', tag='n900000000000550004')
Description_type._InitializeFacetMap(Description_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Description_type', Description_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Case_significance
class Case_significance (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Case_significance')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 274, 4)
    _Documentation = '\n                \n            '
Case_significance._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Case_significance, enum_prefix=None)
Case_significance.n900000000000017005 = Case_significance._CF_enumeration.addEnumeration(unicode_value='900000000000017005', tag='n900000000000017005')
Case_significance.n900000000000020002 = Case_significance._CF_enumeration.addEnumeration(unicode_value='900000000000020002', tag='n900000000000020002')
Case_significance.n900000000000448009 = Case_significance._CF_enumeration.addEnumeration(unicode_value='900000000000448009', tag='n900000000000448009')
Case_significance._InitializeFacetMap(Case_significance._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Case_significance', Case_significance)

# Atomic simple type: {http://snomed.info/schema/rf2}Linkage_concept
class Linkage_concept (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Linkage_concept')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 312, 4)
    _Documentation = '\n                \n            '
Linkage_concept._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Linkage_concept, enum_prefix=None)
Linkage_concept.n1241001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='1241001', tag='n1241001')
Linkage_concept.n5185003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='5185003', tag='n5185003')
Linkage_concept.n7196007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='7196007', tag='n7196007')
Linkage_concept.n7883008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='7883008', tag='n7883008')
Linkage_concept.n8707003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='8707003', tag='n8707003')
Linkage_concept.n8754004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='8754004', tag='n8754004')
Linkage_concept.n10546003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='10546003', tag='n10546003')
Linkage_concept.n15792004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='15792004', tag='n15792004')
Linkage_concept.n18720000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='18720000', tag='n18720000')
Linkage_concept.n19096001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='19096001', tag='n19096001')
Linkage_concept.n20401003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='20401003', tag='n20401003')
Linkage_concept.n21191007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='21191007', tag='n21191007')
Linkage_concept.n23981006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='23981006', tag='n23981006')
Linkage_concept.n25609006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='25609006', tag='n25609006')
Linkage_concept.n28995006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='28995006', tag='n28995006')
Linkage_concept.n30294006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='30294006', tag='n30294006')
Linkage_concept.n30507006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='30507006', tag='n30507006')
Linkage_concept.n35362001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='35362001', tag='n35362001')
Linkage_concept.n36612008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='36612008', tag='n36612008')
Linkage_concept.n37837009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='37837009', tag='n37837009')
Linkage_concept.n40378004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='40378004', tag='n40378004')
Linkage_concept.n42752001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='42752001', tag='n42752001')
Linkage_concept.n45169001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='45169001', tag='n45169001')
Linkage_concept.n47429007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='47429007', tag='n47429007')
Linkage_concept.n54776003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='54776003', tag='n54776003')
Linkage_concept.n58091002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='58091002', tag='n58091002')
Linkage_concept.n60117003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='60117003', tag='n60117003')
Linkage_concept.n67780002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='67780002', tag='n67780002')
Linkage_concept.n68369002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='68369002', tag='n68369002')
Linkage_concept.n68727004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='68727004', tag='n68727004')
Linkage_concept.n72589006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='72589006', tag='n72589006')
Linkage_concept.n73907009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='73907009', tag='n73907009')
Linkage_concept.n75958009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='75958009', tag='n75958009')
Linkage_concept.n77879006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='77879006', tag='n77879006')
Linkage_concept.n79409006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='79409006', tag='n79409006')
Linkage_concept.n85789007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='85789007', tag='n85789007')
Linkage_concept.n103335007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103335007', tag='n103335007')
Linkage_concept.n103366001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103366001', tag='n103366001')
Linkage_concept.n103367005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103367005', tag='n103367005')
Linkage_concept.n103368000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103368000', tag='n103368000')
Linkage_concept.n103369008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103369008', tag='n103369008')
Linkage_concept.n103370009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103370009', tag='n103370009')
Linkage_concept.n103371008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103371008', tag='n103371008')
Linkage_concept.n103372001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103372001', tag='n103372001')
Linkage_concept.n103373006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103373006', tag='n103373006')
Linkage_concept.n103374000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103374000', tag='n103374000')
Linkage_concept.n103375004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103375004', tag='n103375004')
Linkage_concept.n103376003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103376003', tag='n103376003')
Linkage_concept.n103377007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103377007', tag='n103377007')
Linkage_concept.n103378002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103378002', tag='n103378002')
Linkage_concept.n103421006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='103421006', tag='n103421006')
Linkage_concept.n112236005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='112236005', tag='n112236005')
Linkage_concept.n116673000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116673000', tag='n116673000')
Linkage_concept.n116674006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116674006', tag='n116674006')
Linkage_concept.n116675007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116675007', tag='n116675007')
Linkage_concept.n116676008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116676008', tag='n116676008')
Linkage_concept.n116677004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116677004', tag='n116677004')
Linkage_concept.n116678009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116678009', tag='n116678009')
Linkage_concept.n116679001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116679001', tag='n116679001')
Linkage_concept.n116680003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116680003', tag='n116680003')
Linkage_concept.n116681004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116681004', tag='n116681004')
Linkage_concept.n116682006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116682006', tag='n116682006')
Linkage_concept.n116683001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116683001', tag='n116683001')
Linkage_concept.n116684007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116684007', tag='n116684007')
Linkage_concept.n116685008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116685008', tag='n116685008')
Linkage_concept.n116686009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116686009', tag='n116686009')
Linkage_concept.n116687000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116687000', tag='n116687000')
Linkage_concept.n116688005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116688005', tag='n116688005')
Linkage_concept.n116689002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116689002', tag='n116689002')
Linkage_concept.n116690006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116690006', tag='n116690006')
Linkage_concept.n116691005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116691005', tag='n116691005')
Linkage_concept.n116692003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116692003', tag='n116692003')
Linkage_concept.n116693008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116693008', tag='n116693008')
Linkage_concept.n116694002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116694002', tag='n116694002')
Linkage_concept.n116696000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116696000', tag='n116696000')
Linkage_concept.n116697009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116697009', tag='n116697009')
Linkage_concept.n116698004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116698004', tag='n116698004')
Linkage_concept.n116699007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116699007', tag='n116699007')
Linkage_concept.n116700008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116700008', tag='n116700008')
Linkage_concept.n116701007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116701007', tag='n116701007')
Linkage_concept.n116702000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116702000', tag='n116702000')
Linkage_concept.n116703005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116703005', tag='n116703005')
Linkage_concept.n116704004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116704004', tag='n116704004')
Linkage_concept.n116705003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116705003', tag='n116705003')
Linkage_concept.n116706002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='116706002', tag='n116706002')
Linkage_concept.n118168003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118168003', tag='n118168003')
Linkage_concept.n118169006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118169006', tag='n118169006')
Linkage_concept.n118170007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118170007', tag='n118170007')
Linkage_concept.n118171006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118171006', tag='n118171006')
Linkage_concept.n118172004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118172004', tag='n118172004')
Linkage_concept.n118173009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='118173009', tag='n118173009')
Linkage_concept.n123005000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='123005000', tag='n123005000')
Linkage_concept.n127484005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127484005', tag='n127484005')
Linkage_concept.n127485006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127485006', tag='n127485006')
Linkage_concept.n127486007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127486007', tag='n127486007')
Linkage_concept.n127487003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127487003', tag='n127487003')
Linkage_concept.n127488008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127488008', tag='n127488008')
Linkage_concept.n127489000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='127489000', tag='n127489000')
Linkage_concept.n129450000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='129450000', tag='n129450000')
Linkage_concept.n129453003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='129453003', tag='n129453003')
Linkage_concept.n131195008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='131195008', tag='n131195008')
Linkage_concept.n134198009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='134198009', tag='n134198009')
Linkage_concept.n149016008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='149016008', tag='n149016008')
Linkage_concept.n159083000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='159083000', tag='n159083000')
Linkage_concept.n168666000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='168666000', tag='n168666000')
Linkage_concept.n178066000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='178066000', tag='n178066000')
Linkage_concept.n225794002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='225794002', tag='n225794002')
Linkage_concept.n229620004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='229620004', tag='n229620004')
Linkage_concept.n229753003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='229753003', tag='n229753003')
Linkage_concept.n230117008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='230117008', tag='n230117008')
Linkage_concept.n230118003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='230118003', tag='n230118003')
Linkage_concept.n230119006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='230119006', tag='n230119006')
Linkage_concept.n246061005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246061005', tag='n246061005')
Linkage_concept.n246062003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246062003', tag='n246062003')
Linkage_concept.n246063008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246063008', tag='n246063008')
Linkage_concept.n246064002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246064002', tag='n246064002')
Linkage_concept.n246065001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246065001', tag='n246065001')
Linkage_concept.n246066000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246066000', tag='n246066000')
Linkage_concept.n246067009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246067009', tag='n246067009')
Linkage_concept.n246068004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246068004', tag='n246068004')
Linkage_concept.n246069007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246069007', tag='n246069007')
Linkage_concept.n246070008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246070008', tag='n246070008')
Linkage_concept.n246071007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246071007', tag='n246071007')
Linkage_concept.n246072000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246072000', tag='n246072000')
Linkage_concept.n246073005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246073005', tag='n246073005')
Linkage_concept.n246075003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246075003', tag='n246075003')
Linkage_concept.n246076002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246076002', tag='n246076002')
Linkage_concept.n246077006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246077006', tag='n246077006')
Linkage_concept.n246078001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246078001', tag='n246078001')
Linkage_concept.n246079009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246079009', tag='n246079009')
Linkage_concept.n246080007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246080007', tag='n246080007')
Linkage_concept.n246082004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246082004', tag='n246082004')
Linkage_concept.n246083009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246083009', tag='n246083009')
Linkage_concept.n246084003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246084003', tag='n246084003')
Linkage_concept.n246085002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246085002', tag='n246085002')
Linkage_concept.n246086001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246086001', tag='n246086001')
Linkage_concept.n246087005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246087005', tag='n246087005')
Linkage_concept.n246088000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246088000', tag='n246088000')
Linkage_concept.n246090004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246090004', tag='n246090004')
Linkage_concept.n246091000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246091000', tag='n246091000')
Linkage_concept.n246092007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246092007', tag='n246092007')
Linkage_concept.n246093002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246093002', tag='n246093002')
Linkage_concept.n246094008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246094008', tag='n246094008')
Linkage_concept.n246095009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246095009', tag='n246095009')
Linkage_concept.n246096005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246096005', tag='n246096005')
Linkage_concept.n246097001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246097001', tag='n246097001')
Linkage_concept.n246098006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246098006', tag='n246098006')
Linkage_concept.n246099003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246099003', tag='n246099003')
Linkage_concept.n246101005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246101005', tag='n246101005')
Linkage_concept.n246102003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246102003', tag='n246102003')
Linkage_concept.n246103008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246103008', tag='n246103008')
Linkage_concept.n246104002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246104002', tag='n246104002')
Linkage_concept.n246105001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246105001', tag='n246105001')
Linkage_concept.n246106000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246106000', tag='n246106000')
Linkage_concept.n246107009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246107009', tag='n246107009')
Linkage_concept.n246108004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246108004', tag='n246108004')
Linkage_concept.n246110002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246110002', tag='n246110002')
Linkage_concept.n246111003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246111003', tag='n246111003')
Linkage_concept.n246112005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246112005', tag='n246112005')
Linkage_concept.n246113000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246113000', tag='n246113000')
Linkage_concept.n246114006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246114006', tag='n246114006')
Linkage_concept.n246115007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246115007', tag='n246115007')
Linkage_concept.n246134007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246134007', tag='n246134007')
Linkage_concept.n246136009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246136009', tag='n246136009')
Linkage_concept.n246137000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246137000', tag='n246137000')
Linkage_concept.n246138005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246138005', tag='n246138005')
Linkage_concept.n246140000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246140000', tag='n246140000')
Linkage_concept.n246141001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246141001', tag='n246141001')
Linkage_concept.n246142008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246142008', tag='n246142008')
Linkage_concept.n246143003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246143003', tag='n246143003')
Linkage_concept.n246144009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246144009', tag='n246144009')
Linkage_concept.n246145005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246145005', tag='n246145005')
Linkage_concept.n246146006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246146006', tag='n246146006')
Linkage_concept.n246147002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246147002', tag='n246147002')
Linkage_concept.n246148007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246148007', tag='n246148007')
Linkage_concept.n246149004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246149004', tag='n246149004')
Linkage_concept.n246150004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246150004', tag='n246150004')
Linkage_concept.n246151000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246151000', tag='n246151000')
Linkage_concept.n246152007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246152007', tag='n246152007')
Linkage_concept.n246153002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246153002', tag='n246153002')
Linkage_concept.n246154008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246154008', tag='n246154008')
Linkage_concept.n246155009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246155009', tag='n246155009')
Linkage_concept.n246156005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246156005', tag='n246156005')
Linkage_concept.n246157001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246157001', tag='n246157001')
Linkage_concept.n246158006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246158006', tag='n246158006')
Linkage_concept.n246159003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246159003', tag='n246159003')
Linkage_concept.n246160008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246160008', tag='n246160008')
Linkage_concept.n246161007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246161007', tag='n246161007')
Linkage_concept.n246162000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246162000', tag='n246162000')
Linkage_concept.n246163005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246163005', tag='n246163005')
Linkage_concept.n246164004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246164004', tag='n246164004')
Linkage_concept.n246165003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246165003', tag='n246165003')
Linkage_concept.n246166002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246166002', tag='n246166002')
Linkage_concept.n246167006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246167006', tag='n246167006')
Linkage_concept.n246168001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246168001', tag='n246168001')
Linkage_concept.n246169009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246169009', tag='n246169009')
Linkage_concept.n246170005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246170005', tag='n246170005')
Linkage_concept.n246171009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246171009', tag='n246171009')
Linkage_concept.n246173007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246173007', tag='n246173007')
Linkage_concept.n246174001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246174001', tag='n246174001')
Linkage_concept.n246175000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246175000', tag='n246175000')
Linkage_concept.n246176004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246176004', tag='n246176004')
Linkage_concept.n246177008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246177008', tag='n246177008')
Linkage_concept.n246178003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246178003', tag='n246178003')
Linkage_concept.n246179006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246179006', tag='n246179006')
Linkage_concept.n246181008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246181008', tag='n246181008')
Linkage_concept.n246182001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246182001', tag='n246182001')
Linkage_concept.n246183006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246183006', tag='n246183006')
Linkage_concept.n246185004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246185004', tag='n246185004')
Linkage_concept.n246186003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246186003', tag='n246186003')
Linkage_concept.n246187007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246187007', tag='n246187007')
Linkage_concept.n246189005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246189005', tag='n246189005')
Linkage_concept.n246190001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246190001', tag='n246190001')
Linkage_concept.n246191002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246191002', tag='n246191002')
Linkage_concept.n246192009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246192009', tag='n246192009')
Linkage_concept.n246193004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246193004', tag='n246193004')
Linkage_concept.n246194005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246194005', tag='n246194005')
Linkage_concept.n246195006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246195006', tag='n246195006')
Linkage_concept.n246196007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246196007', tag='n246196007')
Linkage_concept.n246197003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246197003', tag='n246197003')
Linkage_concept.n246198008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246198008', tag='n246198008')
Linkage_concept.n246199000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246199000', tag='n246199000')
Linkage_concept.n246200002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246200002', tag='n246200002')
Linkage_concept.n246201003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246201003', tag='n246201003')
Linkage_concept.n246202005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246202005', tag='n246202005')
Linkage_concept.n246203000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246203000', tag='n246203000')
Linkage_concept.n246204006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246204006', tag='n246204006')
Linkage_concept.n246205007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246205007', tag='n246205007')
Linkage_concept.n246215001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246215001', tag='n246215001')
Linkage_concept.n246216000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246216000', tag='n246216000')
Linkage_concept.n246217009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246217009', tag='n246217009')
Linkage_concept.n246218004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246218004', tag='n246218004')
Linkage_concept.n246219007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246219007', tag='n246219007')
Linkage_concept.n246220001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246220001', tag='n246220001')
Linkage_concept.n246222009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246222009', tag='n246222009')
Linkage_concept.n246224005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246224005', tag='n246224005')
Linkage_concept.n246225006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246225006', tag='n246225006')
Linkage_concept.n246226007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246226007', tag='n246226007')
Linkage_concept.n246227003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246227003', tag='n246227003')
Linkage_concept.n246228008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246228008', tag='n246228008')
Linkage_concept.n246229000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246229000', tag='n246229000')
Linkage_concept.n246230005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246230005', tag='n246230005')
Linkage_concept.n246231009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246231009', tag='n246231009')
Linkage_concept.n246232002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246232002', tag='n246232002')
Linkage_concept.n246233007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246233007', tag='n246233007')
Linkage_concept.n246234001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246234001', tag='n246234001')
Linkage_concept.n246235000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246235000', tag='n246235000')
Linkage_concept.n246236004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246236004', tag='n246236004')
Linkage_concept.n246237008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246237008', tag='n246237008')
Linkage_concept.n246238003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246238003', tag='n246238003')
Linkage_concept.n246240008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246240008', tag='n246240008')
Linkage_concept.n246241007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246241007', tag='n246241007')
Linkage_concept.n246242000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246242000', tag='n246242000')
Linkage_concept.n246243005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246243005', tag='n246243005')
Linkage_concept.n246244004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246244004', tag='n246244004')
Linkage_concept.n246245003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246245003', tag='n246245003')
Linkage_concept.n246246002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246246002', tag='n246246002')
Linkage_concept.n246247006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246247006', tag='n246247006')
Linkage_concept.n246248001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246248001', tag='n246248001')
Linkage_concept.n246249009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246249009', tag='n246249009')
Linkage_concept.n246250009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246250009', tag='n246250009')
Linkage_concept.n246251008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246251008', tag='n246251008')
Linkage_concept.n246252001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246252001', tag='n246252001')
Linkage_concept.n246253006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246253006', tag='n246253006')
Linkage_concept.n246254000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246254000', tag='n246254000')
Linkage_concept.n246255004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246255004', tag='n246255004')
Linkage_concept.n246256003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246256003', tag='n246256003')
Linkage_concept.n246257007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246257007', tag='n246257007')
Linkage_concept.n246258002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246258002', tag='n246258002')
Linkage_concept.n246259005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246259005', tag='n246259005')
Linkage_concept.n246260000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246260000', tag='n246260000')
Linkage_concept.n246261001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246261001', tag='n246261001')
Linkage_concept.n246262008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246262008', tag='n246262008')
Linkage_concept.n246263003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246263003', tag='n246263003')
Linkage_concept.n246264009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246264009', tag='n246264009')
Linkage_concept.n246265005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246265005', tag='n246265005')
Linkage_concept.n246266006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246266006', tag='n246266006')
Linkage_concept.n246267002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246267002', tag='n246267002')
Linkage_concept.n246268007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246268007', tag='n246268007')
Linkage_concept.n246269004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246269004', tag='n246269004')
Linkage_concept.n246270003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246270003', tag='n246270003')
Linkage_concept.n246271004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246271004', tag='n246271004')
Linkage_concept.n246272006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246272006', tag='n246272006')
Linkage_concept.n246273001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246273001', tag='n246273001')
Linkage_concept.n246274007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246274007', tag='n246274007')
Linkage_concept.n246275008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246275008', tag='n246275008')
Linkage_concept.n246276009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246276009', tag='n246276009')
Linkage_concept.n246277000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246277000', tag='n246277000')
Linkage_concept.n246278005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246278005', tag='n246278005')
Linkage_concept.n246280004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246280004', tag='n246280004')
Linkage_concept.n246281000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246281000', tag='n246281000')
Linkage_concept.n246282007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246282007', tag='n246282007')
Linkage_concept.n246283002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246283002', tag='n246283002')
Linkage_concept.n246284008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246284008', tag='n246284008')
Linkage_concept.n246285009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246285009', tag='n246285009')
Linkage_concept.n246286005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246286005', tag='n246286005')
Linkage_concept.n246287001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246287001', tag='n246287001')
Linkage_concept.n246288006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246288006', tag='n246288006')
Linkage_concept.n246289003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246289003', tag='n246289003')
Linkage_concept.n246290007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246290007', tag='n246290007')
Linkage_concept.n246291006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246291006', tag='n246291006')
Linkage_concept.n246293009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246293009', tag='n246293009')
Linkage_concept.n246294003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246294003', tag='n246294003')
Linkage_concept.n246295002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246295002', tag='n246295002')
Linkage_concept.n246296001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246296001', tag='n246296001')
Linkage_concept.n246297005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246297005', tag='n246297005')
Linkage_concept.n246298000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246298000', tag='n246298000')
Linkage_concept.n246299008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246299008', tag='n246299008')
Linkage_concept.n246300000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246300000', tag='n246300000')
Linkage_concept.n246301001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246301001', tag='n246301001')
Linkage_concept.n246302008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246302008', tag='n246302008')
Linkage_concept.n246303003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246303003', tag='n246303003')
Linkage_concept.n246304009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246304009', tag='n246304009')
Linkage_concept.n246305005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246305005', tag='n246305005')
Linkage_concept.n246306006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246306006', tag='n246306006')
Linkage_concept.n246307002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246307002', tag='n246307002')
Linkage_concept.n246308007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246308007', tag='n246308007')
Linkage_concept.n246309004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246309004', tag='n246309004')
Linkage_concept.n246310009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246310009', tag='n246310009')
Linkage_concept.n246311008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246311008', tag='n246311008')
Linkage_concept.n246312001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246312001', tag='n246312001')
Linkage_concept.n246313006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246313006', tag='n246313006')
Linkage_concept.n246314000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246314000', tag='n246314000')
Linkage_concept.n246315004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246315004', tag='n246315004')
Linkage_concept.n246316003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246316003', tag='n246316003')
Linkage_concept.n246317007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246317007', tag='n246317007')
Linkage_concept.n246318002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246318002', tag='n246318002')
Linkage_concept.n246321000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246321000', tag='n246321000')
Linkage_concept.n246322007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246322007', tag='n246322007')
Linkage_concept.n246323002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246323002', tag='n246323002')
Linkage_concept.n246324008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246324008', tag='n246324008')
Linkage_concept.n246325009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246325009', tag='n246325009')
Linkage_concept.n246326005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246326005', tag='n246326005')
Linkage_concept.n246327001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246327001', tag='n246327001')
Linkage_concept.n246328006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246328006', tag='n246328006')
Linkage_concept.n246329003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246329003', tag='n246329003')
Linkage_concept.n246330008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246330008', tag='n246330008')
Linkage_concept.n246331007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246331007', tag='n246331007')
Linkage_concept.n246332000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246332000', tag='n246332000')
Linkage_concept.n246333005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246333005', tag='n246333005')
Linkage_concept.n246334004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246334004', tag='n246334004')
Linkage_concept.n246335003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246335003', tag='n246335003')
Linkage_concept.n246336002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246336002', tag='n246336002')
Linkage_concept.n246337006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246337006', tag='n246337006')
Linkage_concept.n246338001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246338001', tag='n246338001')
Linkage_concept.n246339009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246339009', tag='n246339009')
Linkage_concept.n246340006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246340006', tag='n246340006')
Linkage_concept.n246341005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246341005', tag='n246341005')
Linkage_concept.n246343008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246343008', tag='n246343008')
Linkage_concept.n246344002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246344002', tag='n246344002')
Linkage_concept.n246345001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246345001', tag='n246345001')
Linkage_concept.n246346000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246346000', tag='n246346000')
Linkage_concept.n246347009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246347009', tag='n246347009')
Linkage_concept.n246348004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246348004', tag='n246348004')
Linkage_concept.n246349007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246349007', tag='n246349007')
Linkage_concept.n246351006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246351006', tag='n246351006')
Linkage_concept.n246352004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246352004', tag='n246352004')
Linkage_concept.n246353009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246353009', tag='n246353009')
Linkage_concept.n246354003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246354003', tag='n246354003')
Linkage_concept.n246355002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246355002', tag='n246355002')
Linkage_concept.n246356001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246356001', tag='n246356001')
Linkage_concept.n246358000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246358000', tag='n246358000')
Linkage_concept.n246359008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246359008', tag='n246359008')
Linkage_concept.n246360003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246360003', tag='n246360003')
Linkage_concept.n246361004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246361004', tag='n246361004')
Linkage_concept.n246362006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246362006', tag='n246362006')
Linkage_concept.n246364007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246364007', tag='n246364007')
Linkage_concept.n246365008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246365008', tag='n246365008')
Linkage_concept.n246366009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246366009', tag='n246366009')
Linkage_concept.n246367000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246367000', tag='n246367000')
Linkage_concept.n246368005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246368005', tag='n246368005')
Linkage_concept.n246369002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246369002', tag='n246369002')
Linkage_concept.n246370001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246370001', tag='n246370001')
Linkage_concept.n246371002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246371002', tag='n246371002')
Linkage_concept.n246372009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246372009', tag='n246372009')
Linkage_concept.n246373004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246373004', tag='n246373004')
Linkage_concept.n246375006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246375006', tag='n246375006')
Linkage_concept.n246376007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246376007', tag='n246376007')
Linkage_concept.n246378008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246378008', tag='n246378008')
Linkage_concept.n246379000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246379000', tag='n246379000')
Linkage_concept.n246380002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246380002', tag='n246380002')
Linkage_concept.n246381003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246381003', tag='n246381003')
Linkage_concept.n246382005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246382005', tag='n246382005')
Linkage_concept.n246383000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246383000', tag='n246383000')
Linkage_concept.n246384006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246384006', tag='n246384006')
Linkage_concept.n246385007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246385007', tag='n246385007')
Linkage_concept.n246386008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246386008', tag='n246386008')
Linkage_concept.n246387004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246387004', tag='n246387004')
Linkage_concept.n246388009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246388009', tag='n246388009')
Linkage_concept.n246389001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246389001', tag='n246389001')
Linkage_concept.n246390005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246390005', tag='n246390005')
Linkage_concept.n246391009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246391009', tag='n246391009')
Linkage_concept.n246392002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246392002', tag='n246392002')
Linkage_concept.n246393007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246393007', tag='n246393007')
Linkage_concept.n246394001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246394001', tag='n246394001')
Linkage_concept.n246395000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246395000', tag='n246395000')
Linkage_concept.n246396004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246396004', tag='n246396004')
Linkage_concept.n246397008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246397008', tag='n246397008')
Linkage_concept.n246398003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246398003', tag='n246398003')
Linkage_concept.n246399006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246399006', tag='n246399006')
Linkage_concept.n246400004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246400004', tag='n246400004')
Linkage_concept.n246401000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246401000', tag='n246401000')
Linkage_concept.n246402007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246402007', tag='n246402007')
Linkage_concept.n246403002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246403002', tag='n246403002')
Linkage_concept.n246404008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246404008', tag='n246404008')
Linkage_concept.n246405009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246405009', tag='n246405009')
Linkage_concept.n246406005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246406005', tag='n246406005')
Linkage_concept.n246407001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246407001', tag='n246407001')
Linkage_concept.n246408006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246408006', tag='n246408006')
Linkage_concept.n246409003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246409003', tag='n246409003')
Linkage_concept.n246410008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246410008', tag='n246410008')
Linkage_concept.n246411007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246411007', tag='n246411007')
Linkage_concept.n246412000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246412000', tag='n246412000')
Linkage_concept.n246413005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246413005', tag='n246413005')
Linkage_concept.n246414004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246414004', tag='n246414004')
Linkage_concept.n246415003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246415003', tag='n246415003')
Linkage_concept.n246416002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246416002', tag='n246416002')
Linkage_concept.n246417006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246417006', tag='n246417006')
Linkage_concept.n246418001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246418001', tag='n246418001')
Linkage_concept.n246419009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246419009', tag='n246419009')
Linkage_concept.n246420003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246420003', tag='n246420003')
Linkage_concept.n246421004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246421004', tag='n246421004')
Linkage_concept.n246422006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246422006', tag='n246422006')
Linkage_concept.n246423001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246423001', tag='n246423001')
Linkage_concept.n246424007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246424007', tag='n246424007')
Linkage_concept.n246425008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246425008', tag='n246425008')
Linkage_concept.n246426009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246426009', tag='n246426009')
Linkage_concept.n246427000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246427000', tag='n246427000')
Linkage_concept.n246428005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246428005', tag='n246428005')
Linkage_concept.n246429002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246429002', tag='n246429002')
Linkage_concept.n246430007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246430007', tag='n246430007')
Linkage_concept.n246431006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246431006', tag='n246431006')
Linkage_concept.n246445000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246445000', tag='n246445000')
Linkage_concept.n246446004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246446004', tag='n246446004')
Linkage_concept.n246447008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246447008', tag='n246447008')
Linkage_concept.n246448003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246448003', tag='n246448003')
Linkage_concept.n246449006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246449006', tag='n246449006')
Linkage_concept.n246450006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246450006', tag='n246450006')
Linkage_concept.n246451005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246451005', tag='n246451005')
Linkage_concept.n246452003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246452003', tag='n246452003')
Linkage_concept.n246453008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246453008', tag='n246453008')
Linkage_concept.n246454002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246454002', tag='n246454002')
Linkage_concept.n246456000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246456000', tag='n246456000')
Linkage_concept.n246457009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246457009', tag='n246457009')
Linkage_concept.n246458004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246458004', tag='n246458004')
Linkage_concept.n246459007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246459007', tag='n246459007')
Linkage_concept.n246460002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246460002', tag='n246460002')
Linkage_concept.n246461003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246461003', tag='n246461003')
Linkage_concept.n246462005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246462005', tag='n246462005')
Linkage_concept.n246463000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246463000', tag='n246463000')
Linkage_concept.n246468009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246468009', tag='n246468009')
Linkage_concept.n246469001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246469001', tag='n246469001')
Linkage_concept.n246470000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246470000', tag='n246470000')
Linkage_concept.n246471001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246471001', tag='n246471001')
Linkage_concept.n246472008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246472008', tag='n246472008')
Linkage_concept.n246474009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246474009', tag='n246474009')
Linkage_concept.n246475005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246475005', tag='n246475005')
Linkage_concept.n246476006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246476006', tag='n246476006')
Linkage_concept.n246477002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246477002', tag='n246477002')
Linkage_concept.n246478007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246478007', tag='n246478007')
Linkage_concept.n246479004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246479004', tag='n246479004')
Linkage_concept.n246480001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246480001', tag='n246480001')
Linkage_concept.n246481002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246481002', tag='n246481002')
Linkage_concept.n246482009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246482009', tag='n246482009')
Linkage_concept.n246483004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246483004', tag='n246483004')
Linkage_concept.n246484005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246484005', tag='n246484005')
Linkage_concept.n246485006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246485006', tag='n246485006')
Linkage_concept.n246486007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246486007', tag='n246486007')
Linkage_concept.n246487003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246487003', tag='n246487003')
Linkage_concept.n246488008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246488008', tag='n246488008')
Linkage_concept.n246489000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246489000', tag='n246489000')
Linkage_concept.n246490009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246490009', tag='n246490009')
Linkage_concept.n246491008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246491008', tag='n246491008')
Linkage_concept.n246492001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246492001', tag='n246492001')
Linkage_concept.n246493006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246493006', tag='n246493006')
Linkage_concept.n246494000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246494000', tag='n246494000')
Linkage_concept.n246495004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246495004', tag='n246495004')
Linkage_concept.n246496003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246496003', tag='n246496003')
Linkage_concept.n246497007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246497007', tag='n246497007')
Linkage_concept.n246498002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246498002', tag='n246498002')
Linkage_concept.n246499005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246499005', tag='n246499005')
Linkage_concept.n246500001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246500001', tag='n246500001')
Linkage_concept.n246501002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246501002', tag='n246501002')
Linkage_concept.n246508008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246508008', tag='n246508008')
Linkage_concept.n246509000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246509000', tag='n246509000')
Linkage_concept.n246510005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246510005', tag='n246510005')
Linkage_concept.n246512002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246512002', tag='n246512002')
Linkage_concept.n246513007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246513007', tag='n246513007')
Linkage_concept.n246514001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246514001', tag='n246514001')
Linkage_concept.n246515000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246515000', tag='n246515000')
Linkage_concept.n246516004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246516004', tag='n246516004')
Linkage_concept.n246517008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='246517008', tag='n246517008')
Linkage_concept.n255234002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='255234002', tag='n255234002')
Linkage_concept.n255260001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='255260001', tag='n255260001')
Linkage_concept.n255460003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='255460003', tag='n255460003')
Linkage_concept.n255711007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='255711007', tag='n255711007')
Linkage_concept.n258214002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='258214002', tag='n258214002')
Linkage_concept.n260225008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260225008', tag='n260225008')
Linkage_concept.n260507000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260507000', tag='n260507000')
Linkage_concept.n260664000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260664000', tag='n260664000')
Linkage_concept.n260671005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260671005', tag='n260671005')
Linkage_concept.n260672003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260672003', tag='n260672003')
Linkage_concept.n260673008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260673008', tag='n260673008')
Linkage_concept.n260674002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260674002', tag='n260674002')
Linkage_concept.n260676000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260676000', tag='n260676000')
Linkage_concept.n260677009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260677009', tag='n260677009')
Linkage_concept.n260678004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260678004', tag='n260678004')
Linkage_concept.n260679007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260679007', tag='n260679007')
Linkage_concept.n260680005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260680005', tag='n260680005')
Linkage_concept.n260681009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260681009', tag='n260681009')
Linkage_concept.n260682002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260682002', tag='n260682002')
Linkage_concept.n260683007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260683007', tag='n260683007')
Linkage_concept.n260684001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260684001', tag='n260684001')
Linkage_concept.n260685000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260685000', tag='n260685000')
Linkage_concept.n260686004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260686004', tag='n260686004')
Linkage_concept.n260687008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260687008', tag='n260687008')
Linkage_concept.n260695007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260695007', tag='n260695007')
Linkage_concept.n260697004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260697004', tag='n260697004')
Linkage_concept.n260698009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260698009', tag='n260698009')
Linkage_concept.n260699001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260699001', tag='n260699001')
Linkage_concept.n260701001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260701001', tag='n260701001')
Linkage_concept.n260703003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260703003', tag='n260703003')
Linkage_concept.n260704009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260704009', tag='n260704009')
Linkage_concept.n260705005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260705005', tag='n260705005')
Linkage_concept.n260706006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260706006', tag='n260706006')
Linkage_concept.n260707002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260707002', tag='n260707002')
Linkage_concept.n260708007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260708007', tag='n260708007')
Linkage_concept.n260709004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260709004', tag='n260709004')
Linkage_concept.n260711008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260711008', tag='n260711008')
Linkage_concept.n260713006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260713006', tag='n260713006')
Linkage_concept.n260714000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260714000', tag='n260714000')
Linkage_concept.n260715004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260715004', tag='n260715004')
Linkage_concept.n260716003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260716003', tag='n260716003')
Linkage_concept.n260717007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260717007', tag='n260717007')
Linkage_concept.n260718002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260718002', tag='n260718002')
Linkage_concept.n260719005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260719005', tag='n260719005')
Linkage_concept.n260720004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260720004', tag='n260720004')
Linkage_concept.n260721000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260721000', tag='n260721000')
Linkage_concept.n260722007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260722007', tag='n260722007')
Linkage_concept.n260723002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260723002', tag='n260723002')
Linkage_concept.n260724008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260724008', tag='n260724008')
Linkage_concept.n260726005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260726005', tag='n260726005')
Linkage_concept.n260727001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260727001', tag='n260727001')
Linkage_concept.n260728006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260728006', tag='n260728006')
Linkage_concept.n260730008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260730008', tag='n260730008')
Linkage_concept.n260731007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260731007', tag='n260731007')
Linkage_concept.n260732000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260732000', tag='n260732000')
Linkage_concept.n260733005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260733005', tag='n260733005')
Linkage_concept.n260734004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260734004', tag='n260734004')
Linkage_concept.n260735003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260735003', tag='n260735003')
Linkage_concept.n260736002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260736002', tag='n260736002')
Linkage_concept.n260737006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260737006', tag='n260737006')
Linkage_concept.n260738001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260738001', tag='n260738001')
Linkage_concept.n260739009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260739009', tag='n260739009')
Linkage_concept.n260740006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260740006', tag='n260740006')
Linkage_concept.n260741005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260741005', tag='n260741005')
Linkage_concept.n260742003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260742003', tag='n260742003')
Linkage_concept.n260743008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260743008', tag='n260743008')
Linkage_concept.n260744002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260744002', tag='n260744002')
Linkage_concept.n260745001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260745001', tag='n260745001')
Linkage_concept.n260746000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260746000', tag='n260746000')
Linkage_concept.n260747009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260747009', tag='n260747009')
Linkage_concept.n260748004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260748004', tag='n260748004')
Linkage_concept.n260749007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260749007', tag='n260749007')
Linkage_concept.n260750007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260750007', tag='n260750007')
Linkage_concept.n260751006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260751006', tag='n260751006')
Linkage_concept.n260752004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260752004', tag='n260752004')
Linkage_concept.n260753009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260753009', tag='n260753009')
Linkage_concept.n260754003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260754003', tag='n260754003')
Linkage_concept.n260755002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260755002', tag='n260755002')
Linkage_concept.n260756001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260756001', tag='n260756001')
Linkage_concept.n260757005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260757005', tag='n260757005')
Linkage_concept.n260758000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260758000', tag='n260758000')
Linkage_concept.n260759008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260759008', tag='n260759008')
Linkage_concept.n260760003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260760003', tag='n260760003')
Linkage_concept.n260761004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260761004', tag='n260761004')
Linkage_concept.n260762006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260762006', tag='n260762006')
Linkage_concept.n260763001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260763001', tag='n260763001')
Linkage_concept.n260764007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260764007', tag='n260764007')
Linkage_concept.n260765008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260765008', tag='n260765008')
Linkage_concept.n260766009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260766009', tag='n260766009')
Linkage_concept.n260767000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260767000', tag='n260767000')
Linkage_concept.n260768005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260768005', tag='n260768005')
Linkage_concept.n260770001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260770001', tag='n260770001')
Linkage_concept.n260771002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260771002', tag='n260771002')
Linkage_concept.n260772009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260772009', tag='n260772009')
Linkage_concept.n260774005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260774005', tag='n260774005')
Linkage_concept.n260775006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260775006', tag='n260775006')
Linkage_concept.n260776007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260776007', tag='n260776007')
Linkage_concept.n260780002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260780002', tag='n260780002')
Linkage_concept.n260781003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260781003', tag='n260781003')
Linkage_concept.n260782005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260782005', tag='n260782005')
Linkage_concept.n260783000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260783000', tag='n260783000')
Linkage_concept.n260784006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260784006', tag='n260784006')
Linkage_concept.n260785007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260785007', tag='n260785007')
Linkage_concept.n260788009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260788009', tag='n260788009')
Linkage_concept.n260790005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260790005', tag='n260790005')
Linkage_concept.n260791009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260791009', tag='n260791009')
Linkage_concept.n260792002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260792002', tag='n260792002')
Linkage_concept.n260793007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260793007', tag='n260793007')
Linkage_concept.n260794001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260794001', tag='n260794001')
Linkage_concept.n260795000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260795000', tag='n260795000')
Linkage_concept.n260796004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260796004', tag='n260796004')
Linkage_concept.n260797008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260797008', tag='n260797008')
Linkage_concept.n260798003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260798003', tag='n260798003')
Linkage_concept.n260799006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260799006', tag='n260799006')
Linkage_concept.n260800005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260800005', tag='n260800005')
Linkage_concept.n260801009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260801009', tag='n260801009')
Linkage_concept.n260802002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260802002', tag='n260802002')
Linkage_concept.n260803007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260803007', tag='n260803007')
Linkage_concept.n260804001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260804001', tag='n260804001')
Linkage_concept.n260805000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260805000', tag='n260805000')
Linkage_concept.n260806004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260806004', tag='n260806004')
Linkage_concept.n260807008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260807008', tag='n260807008')
Linkage_concept.n260808003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260808003', tag='n260808003')
Linkage_concept.n260809006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260809006', tag='n260809006')
Linkage_concept.n260810001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260810001', tag='n260810001')
Linkage_concept.n260811002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260811002', tag='n260811002')
Linkage_concept.n260812009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260812009', tag='n260812009')
Linkage_concept.n260813004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260813004', tag='n260813004')
Linkage_concept.n260814005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260814005', tag='n260814005')
Linkage_concept.n260815006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260815006', tag='n260815006')
Linkage_concept.n260816007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260816007', tag='n260816007')
Linkage_concept.n260817003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260817003', tag='n260817003')
Linkage_concept.n260818008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260818008', tag='n260818008')
Linkage_concept.n260819000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260819000', tag='n260819000')
Linkage_concept.n260820006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260820006', tag='n260820006')
Linkage_concept.n260821005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260821005', tag='n260821005')
Linkage_concept.n260822003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260822003', tag='n260822003')
Linkage_concept.n260823008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260823008', tag='n260823008')
Linkage_concept.n260824002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260824002', tag='n260824002')
Linkage_concept.n260826000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260826000', tag='n260826000')
Linkage_concept.n260827009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260827009', tag='n260827009')
Linkage_concept.n260828004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260828004', tag='n260828004')
Linkage_concept.n260829007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260829007', tag='n260829007')
Linkage_concept.n260830002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260830002', tag='n260830002')
Linkage_concept.n260831003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260831003', tag='n260831003')
Linkage_concept.n260832005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260832005', tag='n260832005')
Linkage_concept.n260833000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260833000', tag='n260833000')
Linkage_concept.n260834006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260834006', tag='n260834006')
Linkage_concept.n260835007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260835007', tag='n260835007')
Linkage_concept.n260836008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260836008', tag='n260836008')
Linkage_concept.n260837004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260837004', tag='n260837004')
Linkage_concept.n260838009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260838009', tag='n260838009')
Linkage_concept.n260839001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260839001', tag='n260839001')
Linkage_concept.n260840004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260840004', tag='n260840004')
Linkage_concept.n260841000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260841000', tag='n260841000')
Linkage_concept.n260842007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260842007', tag='n260842007')
Linkage_concept.n260843002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260843002', tag='n260843002')
Linkage_concept.n260844008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260844008', tag='n260844008')
Linkage_concept.n260845009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260845009', tag='n260845009')
Linkage_concept.n260846005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260846005', tag='n260846005')
Linkage_concept.n260847001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260847001', tag='n260847001')
Linkage_concept.n260848006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260848006', tag='n260848006')
Linkage_concept.n260849003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260849003', tag='n260849003')
Linkage_concept.n260850003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260850003', tag='n260850003')
Linkage_concept.n260851004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260851004', tag='n260851004')
Linkage_concept.n260852006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260852006', tag='n260852006')
Linkage_concept.n260853001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260853001', tag='n260853001')
Linkage_concept.n260854007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260854007', tag='n260854007')
Linkage_concept.n260855008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260855008', tag='n260855008')
Linkage_concept.n260856009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260856009', tag='n260856009')
Linkage_concept.n260857000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260857000', tag='n260857000')
Linkage_concept.n260858005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260858005', tag='n260858005')
Linkage_concept.n260859002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260859002', tag='n260859002')
Linkage_concept.n260860007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260860007', tag='n260860007')
Linkage_concept.n260861006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260861006', tag='n260861006')
Linkage_concept.n260862004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260862004', tag='n260862004')
Linkage_concept.n260863009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260863009', tag='n260863009')
Linkage_concept.n260864003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260864003', tag='n260864003')
Linkage_concept.n260865002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260865002', tag='n260865002')
Linkage_concept.n260866001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260866001', tag='n260866001')
Linkage_concept.n260868000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260868000', tag='n260868000')
Linkage_concept.n260869008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260869008', tag='n260869008')
Linkage_concept.n260870009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260870009', tag='n260870009')
Linkage_concept.n260871008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260871008', tag='n260871008')
Linkage_concept.n260872001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260872001', tag='n260872001')
Linkage_concept.n260873006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260873006', tag='n260873006')
Linkage_concept.n260874000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260874000', tag='n260874000')
Linkage_concept.n260875004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260875004', tag='n260875004')
Linkage_concept.n260876003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260876003', tag='n260876003')
Linkage_concept.n260878002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260878002', tag='n260878002')
Linkage_concept.n260879005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260879005', tag='n260879005')
Linkage_concept.n260880008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260880008', tag='n260880008')
Linkage_concept.n260881007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260881007', tag='n260881007')
Linkage_concept.n260882000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260882000', tag='n260882000')
Linkage_concept.n260883005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260883005', tag='n260883005')
Linkage_concept.n260884004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260884004', tag='n260884004')
Linkage_concept.n260885003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260885003', tag='n260885003')
Linkage_concept.n260886002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260886002', tag='n260886002')
Linkage_concept.n260887006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260887006', tag='n260887006')
Linkage_concept.n260888001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260888001', tag='n260888001')
Linkage_concept.n260890000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260890000', tag='n260890000')
Linkage_concept.n260891001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260891001', tag='n260891001')
Linkage_concept.n260892008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260892008', tag='n260892008')
Linkage_concept.n260893003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260893003', tag='n260893003')
Linkage_concept.n260894009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260894009', tag='n260894009')
Linkage_concept.n260895005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260895005', tag='n260895005')
Linkage_concept.n260896006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260896006', tag='n260896006')
Linkage_concept.n260897002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260897002', tag='n260897002')
Linkage_concept.n260898007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260898007', tag='n260898007')
Linkage_concept.n260899004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260899004', tag='n260899004')
Linkage_concept.n260900009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260900009', tag='n260900009')
Linkage_concept.n260902001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260902001', tag='n260902001')
Linkage_concept.n260903006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260903006', tag='n260903006')
Linkage_concept.n260904000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260904000', tag='n260904000')
Linkage_concept.n260905004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260905004', tag='n260905004')
Linkage_concept.n260906003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260906003', tag='n260906003')
Linkage_concept.n260907007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260907007', tag='n260907007')
Linkage_concept.n260909005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260909005', tag='n260909005')
Linkage_concept.n260910000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260910000', tag='n260910000')
Linkage_concept.n260911001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260911001', tag='n260911001')
Linkage_concept.n260913003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260913003', tag='n260913003')
Linkage_concept.n260914009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260914009', tag='n260914009')
Linkage_concept.n260915005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260915005', tag='n260915005')
Linkage_concept.n260916006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260916006', tag='n260916006')
Linkage_concept.n260917002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260917002', tag='n260917002')
Linkage_concept.n260918007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260918007', tag='n260918007')
Linkage_concept.n260919004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260919004', tag='n260919004')
Linkage_concept.n260920005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260920005', tag='n260920005')
Linkage_concept.n260921009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260921009', tag='n260921009')
Linkage_concept.n260922002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260922002', tag='n260922002')
Linkage_concept.n260923007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260923007', tag='n260923007')
Linkage_concept.n260924001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260924001', tag='n260924001')
Linkage_concept.n260925000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260925000', tag='n260925000')
Linkage_concept.n260926004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260926004', tag='n260926004')
Linkage_concept.n260928003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260928003', tag='n260928003')
Linkage_concept.n260929006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260929006', tag='n260929006')
Linkage_concept.n260930001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260930001', tag='n260930001')
Linkage_concept.n260932009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260932009', tag='n260932009')
Linkage_concept.n260933004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260933004', tag='n260933004')
Linkage_concept.n260934005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260934005', tag='n260934005')
Linkage_concept.n260935006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260935006', tag='n260935006')
Linkage_concept.n260936007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260936007', tag='n260936007')
Linkage_concept.n260937003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260937003', tag='n260937003')
Linkage_concept.n260938008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260938008', tag='n260938008')
Linkage_concept.n260939000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260939000', tag='n260939000')
Linkage_concept.n260940003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260940003', tag='n260940003')
Linkage_concept.n260941004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260941004', tag='n260941004')
Linkage_concept.n260942006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260942006', tag='n260942006')
Linkage_concept.n260944007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260944007', tag='n260944007')
Linkage_concept.n260945008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260945008', tag='n260945008')
Linkage_concept.n260946009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260946009', tag='n260946009')
Linkage_concept.n260947000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260947000', tag='n260947000')
Linkage_concept.n260949002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260949002', tag='n260949002')
Linkage_concept.n260950002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260950002', tag='n260950002')
Linkage_concept.n260973005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260973005', tag='n260973005')
Linkage_concept.n260974004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260974004', tag='n260974004')
Linkage_concept.n260977006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260977006', tag='n260977006')
Linkage_concept.n260978001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260978001', tag='n260978001')
Linkage_concept.n260979009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='260979009', tag='n260979009')
Linkage_concept.n261217004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='261217004', tag='n261217004')
Linkage_concept.n263485007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263485007', tag='n263485007')
Linkage_concept.n263486008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263486008', tag='n263486008')
Linkage_concept.n263488009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263488009', tag='n263488009')
Linkage_concept.n263490005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263490005', tag='n263490005')
Linkage_concept.n263491009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263491009', tag='n263491009')
Linkage_concept.n263492002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263492002', tag='n263492002')
Linkage_concept.n263493007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263493007', tag='n263493007')
Linkage_concept.n263494001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263494001', tag='n263494001')
Linkage_concept.n263496004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263496004', tag='n263496004')
Linkage_concept.n263497008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263497008', tag='n263497008')
Linkage_concept.n263498003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263498003', tag='n263498003')
Linkage_concept.n263499006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263499006', tag='n263499006')
Linkage_concept.n263502005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263502005', tag='n263502005')
Linkage_concept.n263503000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263503000', tag='n263503000')
Linkage_concept.n263504006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263504006', tag='n263504006')
Linkage_concept.n263505007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263505007', tag='n263505007')
Linkage_concept.n263506008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263506008', tag='n263506008')
Linkage_concept.n263507004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263507004', tag='n263507004')
Linkage_concept.n263508009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263508009', tag='n263508009')
Linkage_concept.n263509001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263509001', tag='n263509001')
Linkage_concept.n263510006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263510006', tag='n263510006')
Linkage_concept.n263511005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263511005', tag='n263511005')
Linkage_concept.n263514002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263514002', tag='n263514002')
Linkage_concept.n263515001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263515001', tag='n263515001')
Linkage_concept.n263516000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263516000', tag='n263516000')
Linkage_concept.n263517009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263517009', tag='n263517009')
Linkage_concept.n263518004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263518004', tag='n263518004')
Linkage_concept.n263519007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263519007', tag='n263519007')
Linkage_concept.n263520001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263520001', tag='n263520001')
Linkage_concept.n263521002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263521002', tag='n263521002')
Linkage_concept.n263522009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263522009', tag='n263522009')
Linkage_concept.n263523004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263523004', tag='n263523004')
Linkage_concept.n263524005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263524005', tag='n263524005')
Linkage_concept.n263525006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263525006', tag='n263525006')
Linkage_concept.n263526007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263526007', tag='n263526007')
Linkage_concept.n263527003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263527003', tag='n263527003')
Linkage_concept.n263528008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263528008', tag='n263528008')
Linkage_concept.n263529000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263529000', tag='n263529000')
Linkage_concept.n263530005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263530005', tag='n263530005')
Linkage_concept.n263531009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263531009', tag='n263531009')
Linkage_concept.n263532002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263532002', tag='n263532002')
Linkage_concept.n263533007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263533007', tag='n263533007')
Linkage_concept.n263534001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263534001', tag='n263534001')
Linkage_concept.n263535000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263535000', tag='n263535000')
Linkage_concept.n263536004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263536004', tag='n263536004')
Linkage_concept.n263538003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263538003', tag='n263538003')
Linkage_concept.n263539006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263539006', tag='n263539006')
Linkage_concept.n263540008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263540008', tag='n263540008')
Linkage_concept.n263541007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263541007', tag='n263541007')
Linkage_concept.n263542000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263542000', tag='n263542000')
Linkage_concept.n263543005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263543005', tag='n263543005')
Linkage_concept.n263544004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263544004', tag='n263544004')
Linkage_concept.n263545003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263545003', tag='n263545003')
Linkage_concept.n263546002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263546002', tag='n263546002')
Linkage_concept.n263547006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263547006', tag='n263547006')
Linkage_concept.n263548001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263548001', tag='n263548001')
Linkage_concept.n263549009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263549009', tag='n263549009')
Linkage_concept.n263550009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263550009', tag='n263550009')
Linkage_concept.n263551008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263551008', tag='n263551008')
Linkage_concept.n263552001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263552001', tag='n263552001')
Linkage_concept.n263553006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263553006', tag='n263553006')
Linkage_concept.n263554000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263554000', tag='n263554000')
Linkage_concept.n263555004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263555004', tag='n263555004')
Linkage_concept.n263556003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263556003', tag='n263556003')
Linkage_concept.n263557007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263557007', tag='n263557007')
Linkage_concept.n263558002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263558002', tag='n263558002')
Linkage_concept.n263559005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263559005', tag='n263559005')
Linkage_concept.n263560000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263560000', tag='n263560000')
Linkage_concept.n263561001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263561001', tag='n263561001')
Linkage_concept.n263562008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263562008', tag='n263562008')
Linkage_concept.n263563003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263563003', tag='n263563003')
Linkage_concept.n263564009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263564009', tag='n263564009')
Linkage_concept.n263565005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263565005', tag='n263565005')
Linkage_concept.n263566006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263566006', tag='n263566006')
Linkage_concept.n263567002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263567002', tag='n263567002')
Linkage_concept.n263568007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263568007', tag='n263568007')
Linkage_concept.n263569004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263569004', tag='n263569004')
Linkage_concept.n263570003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263570003', tag='n263570003')
Linkage_concept.n263571004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263571004', tag='n263571004')
Linkage_concept.n263572006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263572006', tag='n263572006')
Linkage_concept.n263573001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263573001', tag='n263573001')
Linkage_concept.n263574007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263574007', tag='n263574007')
Linkage_concept.n263575008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263575008', tag='n263575008')
Linkage_concept.n263576009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263576009', tag='n263576009')
Linkage_concept.n263577000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263577000', tag='n263577000')
Linkage_concept.n263578005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263578005', tag='n263578005')
Linkage_concept.n263579002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263579002', tag='n263579002')
Linkage_concept.n263580004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263580004', tag='n263580004')
Linkage_concept.n263581000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263581000', tag='n263581000')
Linkage_concept.n263582007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263582007', tag='n263582007')
Linkage_concept.n263583002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263583002', tag='n263583002')
Linkage_concept.n263584008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263584008', tag='n263584008')
Linkage_concept.n263585009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263585009', tag='n263585009')
Linkage_concept.n263586005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263586005', tag='n263586005')
Linkage_concept.n263587001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263587001', tag='n263587001')
Linkage_concept.n263588006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263588006', tag='n263588006')
Linkage_concept.n263589003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263589003', tag='n263589003')
Linkage_concept.n263590007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263590007', tag='n263590007')
Linkage_concept.n263591006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263591006', tag='n263591006')
Linkage_concept.n263592004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263592004', tag='n263592004')
Linkage_concept.n263593009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263593009', tag='n263593009')
Linkage_concept.n263594003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263594003', tag='n263594003')
Linkage_concept.n263595002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263595002', tag='n263595002')
Linkage_concept.n263596001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263596001', tag='n263596001')
Linkage_concept.n263597005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263597005', tag='n263597005')
Linkage_concept.n263598000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263598000', tag='n263598000')
Linkage_concept.n263599008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263599008', tag='n263599008')
Linkage_concept.n263600006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263600006', tag='n263600006')
Linkage_concept.n263601005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263601005', tag='n263601005')
Linkage_concept.n263602003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263602003', tag='n263602003')
Linkage_concept.n263603008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263603008', tag='n263603008')
Linkage_concept.n263606000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263606000', tag='n263606000')
Linkage_concept.n263607009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263607009', tag='n263607009')
Linkage_concept.n263608004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263608004', tag='n263608004')
Linkage_concept.n263609007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263609007', tag='n263609007')
Linkage_concept.n263610002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263610002', tag='n263610002')
Linkage_concept.n263619001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263619001', tag='n263619001')
Linkage_concept.n263620007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263620007', tag='n263620007')
Linkage_concept.n263621006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263621006', tag='n263621006')
Linkage_concept.n263622004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263622004', tag='n263622004')
Linkage_concept.n263623009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263623009', tag='n263623009')
Linkage_concept.n263624003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263624003', tag='n263624003')
Linkage_concept.n263625002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263625002', tag='n263625002')
Linkage_concept.n263628000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263628000', tag='n263628000')
Linkage_concept.n263629008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263629008', tag='n263629008')
Linkage_concept.n263630003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263630003', tag='n263630003')
Linkage_concept.n263631004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263631004', tag='n263631004')
Linkage_concept.n263632006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263632006', tag='n263632006')
Linkage_concept.n263633001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263633001', tag='n263633001')
Linkage_concept.n263635008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263635008', tag='n263635008')
Linkage_concept.n263636009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263636009', tag='n263636009')
Linkage_concept.n263637000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263637000', tag='n263637000')
Linkage_concept.n263639002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263639002', tag='n263639002')
Linkage_concept.n263640000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263640000', tag='n263640000')
Linkage_concept.n263641001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263641001', tag='n263641001')
Linkage_concept.n263642008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263642008', tag='n263642008')
Linkage_concept.n263643003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263643003', tag='n263643003')
Linkage_concept.n263644009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263644009', tag='n263644009')
Linkage_concept.n263645005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263645005', tag='n263645005')
Linkage_concept.n263646006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263646006', tag='n263646006')
Linkage_concept.n263647002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263647002', tag='n263647002')
Linkage_concept.n263648007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263648007', tag='n263648007')
Linkage_concept.n263649004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263649004', tag='n263649004')
Linkage_concept.n263718001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='263718001', tag='n263718001')
Linkage_concept.n264921002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='264921002', tag='n264921002')
Linkage_concept.n272732008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272732008', tag='n272732008')
Linkage_concept.n272733003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272733003', tag='n272733003')
Linkage_concept.n272734009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272734009', tag='n272734009')
Linkage_concept.n272735005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272735005', tag='n272735005')
Linkage_concept.n272736006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272736006', tag='n272736006')
Linkage_concept.n272737002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272737002', tag='n272737002')
Linkage_concept.n272739004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272739004', tag='n272739004')
Linkage_concept.n272741003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272741003', tag='n272741003')
Linkage_concept.n272742005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='272742005', tag='n272742005')
Linkage_concept.n273248003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='273248003', tag='n273248003')
Linkage_concept.n276131009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276131009', tag='n276131009')
Linkage_concept.n276132002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276132002', tag='n276132002')
Linkage_concept.n276133007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276133007', tag='n276133007')
Linkage_concept.n276134001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276134001', tag='n276134001')
Linkage_concept.n276625007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276625007', tag='n276625007')
Linkage_concept.n276626008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276626008', tag='n276626008')
Linkage_concept.n276731003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276731003', tag='n276731003')
Linkage_concept.n276820004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276820004', tag='n276820004')
Linkage_concept.n276823002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276823002', tag='n276823002')
Linkage_concept.n276824008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276824008', tag='n276824008')
Linkage_concept.n276989002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='276989002', tag='n276989002')
Linkage_concept.n277035007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277035007', tag='n277035007')
Linkage_concept.n277037004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277037004', tag='n277037004')
Linkage_concept.n277038009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277038009', tag='n277038009')
Linkage_concept.n277039001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277039001', tag='n277039001')
Linkage_concept.n277040004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277040004', tag='n277040004')
Linkage_concept.n277041000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277041000', tag='n277041000')
Linkage_concept.n277042007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277042007', tag='n277042007')
Linkage_concept.n277043002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277043002', tag='n277043002')
Linkage_concept.n277044008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277044008', tag='n277044008')
Linkage_concept.n277045009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277045009', tag='n277045009')
Linkage_concept.n277046005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277046005', tag='n277046005')
Linkage_concept.n277047001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277047001', tag='n277047001')
Linkage_concept.n277052006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277052006', tag='n277052006')
Linkage_concept.n277053001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277053001', tag='n277053001')
Linkage_concept.n277054007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277054007', tag='n277054007')
Linkage_concept.n277055008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277055008', tag='n277055008')
Linkage_concept.n277058005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277058005', tag='n277058005')
Linkage_concept.n277059002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277059002', tag='n277059002')
Linkage_concept.n277060007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277060007', tag='n277060007')
Linkage_concept.n277061006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277061006', tag='n277061006')
Linkage_concept.n277062004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277062004', tag='n277062004')
Linkage_concept.n277063009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277063009', tag='n277063009')
Linkage_concept.n277064003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277064003', tag='n277064003')
Linkage_concept.n277097002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277097002', tag='n277097002')
Linkage_concept.n277327002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277327002', tag='n277327002')
Linkage_concept.n277334000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277334000', tag='n277334000')
Linkage_concept.n277335004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277335004', tag='n277335004')
Linkage_concept.n277405005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277405005', tag='n277405005')
Linkage_concept.n277640000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277640000', tag='n277640000')
Linkage_concept.n277655009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277655009', tag='n277655009')
Linkage_concept.n277795004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277795004', tag='n277795004')
Linkage_concept.n277889008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='277889008', tag='n277889008')
Linkage_concept.n278109006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278109006', tag='n278109006')
Linkage_concept.n278111002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278111002', tag='n278111002')
Linkage_concept.n278112009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278112009', tag='n278112009')
Linkage_concept.n278114005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278114005', tag='n278114005')
Linkage_concept.n278115006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278115006', tag='n278115006')
Linkage_concept.n278144008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278144008', tag='n278144008')
Linkage_concept.n278155008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278155008', tag='n278155008')
Linkage_concept.n278156009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278156009', tag='n278156009')
Linkage_concept.n278157000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278157000', tag='n278157000')
Linkage_concept.n278158005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278158005', tag='n278158005')
Linkage_concept.n278174000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278174000', tag='n278174000')
Linkage_concept.n278176003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278176003', tag='n278176003')
Linkage_concept.n278200001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278200001', tag='n278200001')
Linkage_concept.n278201002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278201002', tag='n278201002')
Linkage_concept.n278230009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278230009', tag='n278230009')
Linkage_concept.n278269003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278269003', tag='n278269003')
Linkage_concept.n278483003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278483003', tag='n278483003')
Linkage_concept.n278863006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278863006', tag='n278863006')
Linkage_concept.n278924003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='278924003', tag='n278924003')
Linkage_concept.n279114001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='279114001', tag='n279114001')
Linkage_concept.n279116004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='279116004', tag='n279116004')
Linkage_concept.n279229007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='279229007', tag='n279229007')
Linkage_concept.n279230002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='279230002', tag='n279230002')
Linkage_concept.n280145001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='280145001', tag='n280145001')
Linkage_concept.n280147009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='280147009', tag='n280147009')
Linkage_concept.n280452008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='280452008', tag='n280452008')
Linkage_concept.n280942002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='280942002', tag='n280942002')
Linkage_concept.n281041004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281041004', tag='n281041004')
Linkage_concept.n281256003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281256003', tag='n281256003')
Linkage_concept.n281308007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281308007', tag='n281308007')
Linkage_concept.n281343008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281343008', tag='n281343008')
Linkage_concept.n281355002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281355002', tag='n281355002')
Linkage_concept.n281403002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281403002', tag='n281403002')
Linkage_concept.n281407001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281407001', tag='n281407001')
Linkage_concept.n281947003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281947003', tag='n281947003')
Linkage_concept.n281948008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='281948008', tag='n281948008')
Linkage_concept.n282006001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='282006001', tag='n282006001')
Linkage_concept.n282079007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='282079007', tag='n282079007')
Linkage_concept.n284663008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='284663008', tag='n284663008')
Linkage_concept.n285705001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='285705001', tag='n285705001')
Linkage_concept.n288508002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='288508002', tag='n288508002')
Linkage_concept.n288556008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='288556008', tag='n288556008')
Linkage_concept.n288829000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='288829000', tag='n288829000')
Linkage_concept.n288830005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='288830005', tag='n288830005')
Linkage_concept.n297203006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='297203006', tag='n297203006')
Linkage_concept.n297939008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='297939008', tag='n297939008')
Linkage_concept.n300591002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300591002', tag='n300591002')
Linkage_concept.n300592009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300592009', tag='n300592009')
Linkage_concept.n300594005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300594005', tag='n300594005')
Linkage_concept.n300596007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300596007', tag='n300596007')
Linkage_concept.n300819009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300819009', tag='n300819009')
Linkage_concept.n300842002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='300842002', tag='n300842002')
Linkage_concept.n303221006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='303221006', tag='n303221006')
Linkage_concept.n306987005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='306987005', tag='n306987005')
Linkage_concept.n309824003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='309824003', tag='n309824003')
Linkage_concept.n311788003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='311788003', tag='n311788003')
Linkage_concept.n313044005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='313044005', tag='n313044005')
Linkage_concept.n313067007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='313067007', tag='n313067007')
Linkage_concept.n313136007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='313136007', tag='n313136007')
Linkage_concept.n363589002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363589002', tag='n363589002')
Linkage_concept.n363698007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363698007', tag='n363698007')
Linkage_concept.n363699004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363699004', tag='n363699004')
Linkage_concept.n363700003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363700003', tag='n363700003')
Linkage_concept.n363701004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363701004', tag='n363701004')
Linkage_concept.n363702006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363702006', tag='n363702006')
Linkage_concept.n363703001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363703001', tag='n363703001')
Linkage_concept.n363704007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363704007', tag='n363704007')
Linkage_concept.n363705008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363705008', tag='n363705008')
Linkage_concept.n363706009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363706009', tag='n363706009')
Linkage_concept.n363707000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363707000', tag='n363707000')
Linkage_concept.n363708005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363708005', tag='n363708005')
Linkage_concept.n363709002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363709002', tag='n363709002')
Linkage_concept.n363710007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363710007', tag='n363710007')
Linkage_concept.n363711006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363711006', tag='n363711006')
Linkage_concept.n363712004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363712004', tag='n363712004')
Linkage_concept.n363713009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363713009', tag='n363713009')
Linkage_concept.n363714003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363714003', tag='n363714003')
Linkage_concept.n363715002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='363715002', tag='n363715002')
Linkage_concept.n367324007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367324007', tag='n367324007')
Linkage_concept.n367326009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367326009', tag='n367326009')
Linkage_concept.n367327000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367327000', tag='n367327000')
Linkage_concept.n367346004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367346004', tag='n367346004')
Linkage_concept.n367409002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367409002', tag='n367409002')
Linkage_concept.n367565008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='367565008', tag='n367565008')
Linkage_concept.n370124000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370124000', tag='n370124000')
Linkage_concept.n370125004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370125004', tag='n370125004')
Linkage_concept.n370128002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370128002', tag='n370128002')
Linkage_concept.n370129005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370129005', tag='n370129005')
Linkage_concept.n370130000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370130000', tag='n370130000')
Linkage_concept.n370131001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370131001', tag='n370131001')
Linkage_concept.n370132008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370132008', tag='n370132008')
Linkage_concept.n370133003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370133003', tag='n370133003')
Linkage_concept.n370134009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370134009', tag='n370134009')
Linkage_concept.n370135005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='370135005', tag='n370135005')
Linkage_concept.n371881003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='371881003', tag='n371881003')
Linkage_concept.n371882005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='371882005', tag='n371882005')
Linkage_concept.n384598002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='384598002', tag='n384598002')
Linkage_concept.n385438008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385438008', tag='n385438008')
Linkage_concept.n385641008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385641008', tag='n385641008')
Linkage_concept.n385665006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385665006', tag='n385665006')
Linkage_concept.n385668008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385668008', tag='n385668008')
Linkage_concept.n385675009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385675009', tag='n385675009')
Linkage_concept.n385676005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='385676005', tag='n385676005')
Linkage_concept.n394736001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='394736001', tag='n394736001')
Linkage_concept.n394850002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='394850002', tag='n394850002')
Linkage_concept.n394851003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='394851003', tag='n394851003')
Linkage_concept.n394852005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='394852005', tag='n394852005')
Linkage_concept.n394853000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='394853000', tag='n394853000')
Linkage_concept.n397764000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='397764000', tag='n397764000')
Linkage_concept.n397987002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='397987002', tag='n397987002')
Linkage_concept.n398008005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398008005', tag='n398008005')
Linkage_concept.n398009002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398009002', tag='n398009002')
Linkage_concept.n398039007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398039007', tag='n398039007')
Linkage_concept.n398092000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398092000', tag='n398092000')
Linkage_concept.n398101002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398101002', tag='n398101002')
Linkage_concept.n398282000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398282000', tag='n398282000')
Linkage_concept.n398297002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='398297002', tag='n398297002')
Linkage_concept.n404651003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='404651003', tag='n404651003')
Linkage_concept.n404652005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='404652005', tag='n404652005')
Linkage_concept.n405662005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405662005', tag='n405662005')
Linkage_concept.n405671001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405671001', tag='n405671001')
Linkage_concept.n405683004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405683004', tag='n405683004')
Linkage_concept.n405813007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405813007', tag='n405813007')
Linkage_concept.n405814001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405814001', tag='n405814001')
Linkage_concept.n405815000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405815000', tag='n405815000')
Linkage_concept.n405816004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='405816004', tag='n405816004')
Linkage_concept.n406142009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='406142009', tag='n406142009')
Linkage_concept.n406524005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='406524005', tag='n406524005')
Linkage_concept.n408729009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='408729009', tag='n408729009')
Linkage_concept.n408730004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='408730004', tag='n408730004')
Linkage_concept.n408731000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='408731000', tag='n408731000')
Linkage_concept.n408732007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='408732007', tag='n408732007')
Linkage_concept.n408739003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='408739003', tag='n408739003')
Linkage_concept.n410608001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410608001', tag='n410608001')
Linkage_concept.n410610004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410610004', tag='n410610004')
Linkage_concept.n410612007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410612007', tag='n410612007')
Linkage_concept.n410615009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410615009', tag='n410615009')
Linkage_concept.n410616005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410616005', tag='n410616005')
Linkage_concept.n410618006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410618006', tag='n410618006')
Linkage_concept.n410653004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410653004', tag='n410653004')
Linkage_concept.n410654005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410654005', tag='n410654005')
Linkage_concept.n410657003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410657003', tag='n410657003')
Linkage_concept.n410658008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410658008', tag='n410658008')
Linkage_concept.n410660005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410660005', tag='n410660005')
Linkage_concept.n410662002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410662002', tag='n410662002')
Linkage_concept.n410663007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410663007', tag='n410663007')
Linkage_concept.n410665000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410665000', tag='n410665000')
Linkage_concept.n410666004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410666004', tag='n410666004')
Linkage_concept.n410667008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410667008', tag='n410667008')
Linkage_concept.n410670007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410670007', tag='n410670007')
Linkage_concept.n410671006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410671006', tag='n410671006')
Linkage_concept.n410673009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410673009', tag='n410673009')
Linkage_concept.n410675002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410675002', tag='n410675002')
Linkage_concept.n410677005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410677005', tag='n410677005')
Linkage_concept.n410678000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410678000', tag='n410678000')
Linkage_concept.n410680006 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='410680006', tag='n410680006')
Linkage_concept.n411116001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='411116001', tag='n411116001')
Linkage_concept.n411117005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='411117005', tag='n411117005')
Linkage_concept.n414679000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='414679000', tag='n414679000')
Linkage_concept.n414680002 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='414680002', tag='n414680002')
Linkage_concept.n416083004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='416083004', tag='n416083004')
Linkage_concept.n416271009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='416271009', tag='n416271009')
Linkage_concept.n416586004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='416586004', tag='n416586004')
Linkage_concept.n416698001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='416698001', tag='n416698001')
Linkage_concept.n416872009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='416872009', tag='n416872009')
Linkage_concept.n417151001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='417151001', tag='n417151001')
Linkage_concept.n417318003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='417318003', tag='n417318003')
Linkage_concept.n417569004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='417569004', tag='n417569004')
Linkage_concept.n418775008 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='418775008', tag='n418775008')
Linkage_concept.n419066007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='419066007', tag='n419066007')
Linkage_concept.n422702001 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='422702001', tag='n422702001')
Linkage_concept.n422809003 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='422809003', tag='n422809003')
Linkage_concept.n424226004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424226004', tag='n424226004')
Linkage_concept.n424244007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424244007', tag='n424244007')
Linkage_concept.n424337000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424337000', tag='n424337000')
Linkage_concept.n424361007 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424361007', tag='n424361007')
Linkage_concept.n424528004 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424528004', tag='n424528004')
Linkage_concept.n424697009 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424697009', tag='n424697009')
Linkage_concept.n424876005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='424876005', tag='n424876005')
Linkage_concept.n425391005 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='425391005', tag='n425391005')
Linkage_concept.n609096000 = Linkage_concept._CF_enumeration.addEnumeration(unicode_value='609096000', tag='n609096000')
Linkage_concept._InitializeFacetMap(Linkage_concept._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Linkage_concept', Linkage_concept)

# Atomic simple type: {http://snomed.info/schema/rf2}Characteristic_type
class Characteristic_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Characteristic_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 5994, 4)
    _Documentation = '\n                \n            '
Characteristic_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Characteristic_type, enum_prefix=None)
Characteristic_type.n900000000000006009 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value='900000000000006009', tag='n900000000000006009')
Characteristic_type.n900000000000010007 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value='900000000000010007', tag='n900000000000010007')
Characteristic_type.n900000000000011006 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value='900000000000011006', tag='n900000000000011006')
Characteristic_type.n900000000000225001 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value='900000000000225001', tag='n900000000000225001')
Characteristic_type.n900000000000227009 = Characteristic_type._CF_enumeration.addEnumeration(unicode_value='900000000000227009', tag='n900000000000227009')
Characteristic_type._InitializeFacetMap(Characteristic_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Characteristic_type', Characteristic_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Modifier
class Modifier (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Modifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 6042, 4)
    _Documentation = '\n                \n            '
Modifier._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Modifier, enum_prefix=None)
Modifier.n900000000000451002 = Modifier._CF_enumeration.addEnumeration(unicode_value='900000000000451002', tag='n900000000000451002')
Modifier.n900000000000452009 = Modifier._CF_enumeration.addEnumeration(unicode_value='900000000000452009', tag='n900000000000452009')
Modifier._InitializeFacetMap(Modifier._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Modifier', Modifier)

# Atomic simple type: {http://snomed.info/schema/rf2}Identifier_scheme
class Identifier_scheme (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Identifier_scheme')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 6075, 4)
    _Documentation = '\n                \n            '
Identifier_scheme._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Identifier_scheme, enum_prefix=None)
Identifier_scheme.n900000000000002006 = Identifier_scheme._CF_enumeration.addEnumeration(unicode_value='900000000000002006', tag='n900000000000002006')
Identifier_scheme.n900000000000294009 = Identifier_scheme._CF_enumeration.addEnumeration(unicode_value='900000000000294009', tag='n900000000000294009')
Identifier_scheme._InitializeFacetMap(Identifier_scheme._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Identifier_scheme', Identifier_scheme)

# Atomic simple type: {http://snomed.info/schema/rf2}Reference_set
class Reference_set (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Reference_set')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 6108, 4)
    _Documentation = '\n                \n            '
Reference_set._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Reference_set, enum_prefix=None)
Reference_set.n446608001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='446608001', tag='n446608001')
Reference_set.n446609009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='446609009', tag='n446609009')
Reference_set.n447250001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447250001', tag='n447250001')
Reference_set.n447258008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447258008', tag='n447258008')
Reference_set.n447562003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447562003', tag='n447562003')
Reference_set.n447563008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447563008', tag='n447563008')
Reference_set.n447565001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447565001', tag='n447565001')
Reference_set.n447566000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447566000', tag='n447566000')
Reference_set.n447567009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447567009', tag='n447567009')
Reference_set.n447568004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447568004', tag='n447568004')
Reference_set.n447569007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447569007', tag='n447569007')
Reference_set.n447570008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='447570008', tag='n447570008')
Reference_set.n448879004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='448879004', tag='n448879004')
Reference_set.n450970008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450970008', tag='n450970008')
Reference_set.n450971007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450971007', tag='n450971007')
Reference_set.n450973005 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450973005', tag='n450973005')
Reference_set.n450974004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450974004', tag='n450974004')
Reference_set.n450976002 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450976002', tag='n450976002')
Reference_set.n450977006 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450977006', tag='n450977006')
Reference_set.n450978001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450978001', tag='n450978001')
Reference_set.n450980007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450980007', tag='n450980007')
Reference_set.n450981006 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450981006', tag='n450981006')
Reference_set.n450982004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450982004', tag='n450982004')
Reference_set.n450983009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450983009', tag='n450983009')
Reference_set.n450984003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450984003', tag='n450984003')
Reference_set.n450985002 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450985002', tag='n450985002')
Reference_set.n450986001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450986001', tag='n450986001')
Reference_set.n450988000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450988000', tag='n450988000')
Reference_set.n450989008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450989008', tag='n450989008')
Reference_set.n450990004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450990004', tag='n450990004')
Reference_set.n450991000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450991000', tag='n450991000')
Reference_set.n450992007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450992007', tag='n450992007')
Reference_set.n450993002 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450993002', tag='n450993002')
Reference_set.n450994008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='450994008', tag='n450994008')
Reference_set.n609331003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='609331003', tag='n609331003')
Reference_set.n609430003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='609430003', tag='n609430003')
Reference_set.n700043003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='700043003', tag='n700043003')
Reference_set.n6011000124106 = Reference_set._CF_enumeration.addEnumeration(unicode_value='6011000124106', tag='n6011000124106')
Reference_set.n900000000000456007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000456007', tag='n900000000000456007')
Reference_set.n900000000000480006 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000480006', tag='n900000000000480006')
Reference_set.n900000000000488004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000488004', tag='n900000000000488004')
Reference_set.n900000000000489007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000489007', tag='n900000000000489007')
Reference_set.n900000000000490003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000490003', tag='n900000000000490003')
Reference_set.n900000000000496009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000496009', tag='n900000000000496009')
Reference_set.n900000000000497000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000497000', tag='n900000000000497000')
Reference_set.n900000000000498005 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000498005', tag='n900000000000498005')
Reference_set.n900000000000506000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000506000', tag='n900000000000506000')
Reference_set.n900000000000507009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000507009', tag='n900000000000507009')
Reference_set.n900000000000508004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000508004', tag='n900000000000508004')
Reference_set.n900000000000509007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000509007', tag='n900000000000509007')
Reference_set.n900000000000512005 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000512005', tag='n900000000000512005')
Reference_set.n900000000000513000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000513000', tag='n900000000000513000')
Reference_set.n900000000000516008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000516008', tag='n900000000000516008')
Reference_set.n900000000000517004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000517004', tag='n900000000000517004')
Reference_set.n900000000000521006 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000521006', tag='n900000000000521006')
Reference_set.n900000000000522004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000522004', tag='n900000000000522004')
Reference_set.n900000000000523009 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000523009', tag='n900000000000523009')
Reference_set.n900000000000524003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000524003', tag='n900000000000524003')
Reference_set.n900000000000525002 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000525002', tag='n900000000000525002')
Reference_set.n900000000000526001 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000526001', tag='n900000000000526001')
Reference_set.n900000000000527005 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000527005', tag='n900000000000527005')
Reference_set.n900000000000528000 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000528000', tag='n900000000000528000')
Reference_set.n900000000000529008 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000529008', tag='n900000000000529008')
Reference_set.n900000000000530003 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000530003', tag='n900000000000530003')
Reference_set.n900000000000531004 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000531004', tag='n900000000000531004')
Reference_set.n900000000000534007 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000534007', tag='n900000000000534007')
Reference_set.n900000000000538005 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000538005', tag='n900000000000538005')
Reference_set.n900000000000547002 = Reference_set._CF_enumeration.addEnumeration(unicode_value='900000000000547002', tag='n900000000000547002')
Reference_set._InitializeFacetMap(Reference_set._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Reference_set', Reference_set)

# Atomic simple type: {http://snomed.info/schema/rf2}Reference_set_attribute
class Reference_set_attribute (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Reference_set_attribute')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 6543, 4)
    _Documentation = '\n                \n            '
Reference_set_attribute._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Reference_set_attribute, enum_prefix=None)
Reference_set_attribute.n447247004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447247004', tag='n447247004')
Reference_set_attribute.n447255006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447255006', tag='n447255006')
Reference_set_attribute.n447257003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447257003', tag='n447257003')
Reference_set_attribute.n447556008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447556008', tag='n447556008')
Reference_set_attribute.n447557004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447557004', tag='n447557004')
Reference_set_attribute.n447558009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447558009', tag='n447558009')
Reference_set_attribute.n447559001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447559001', tag='n447559001')
Reference_set_attribute.n447560006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447560006', tag='n447560006')
Reference_set_attribute.n447561005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447561005', tag='n447561005')
Reference_set_attribute.n447634004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447634004', tag='n447634004')
Reference_set_attribute.n447635003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447635003', tag='n447635003')
Reference_set_attribute.n447636002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447636002', tag='n447636002')
Reference_set_attribute.n447637006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447637006', tag='n447637006')
Reference_set_attribute.n447638001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447638001', tag='n447638001')
Reference_set_attribute.n447639009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447639009', tag='n447639009')
Reference_set_attribute.n447640006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447640006', tag='n447640006')
Reference_set_attribute.n447641005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447641005', tag='n447641005')
Reference_set_attribute.n447642003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='447642003', tag='n447642003')
Reference_set_attribute.n449608002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='449608002', tag='n449608002')
Reference_set_attribute.n450995009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='450995009', tag='n450995009')
Reference_set_attribute.n450996005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='450996005', tag='n450996005')
Reference_set_attribute.n450997001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='450997001', tag='n450997001')
Reference_set_attribute.n450998006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='450998006', tag='n450998006')
Reference_set_attribute.n450999003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='450999003', tag='n450999003')
Reference_set_attribute.n451000004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='451000004', tag='n451000004')
Reference_set_attribute.n451001000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='451001000', tag='n451001000')
Reference_set_attribute.n451002007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='451002007', tag='n451002007')
Reference_set_attribute.n451003002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='451003002', tag='n451003002')
Reference_set_attribute.n609330002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='609330002', tag='n609330002')
Reference_set_attribute.n609431004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='609431004', tag='n609431004')
Reference_set_attribute.n609432006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='609432006', tag='n609432006')
Reference_set_attribute.n609642003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='609642003', tag='n609642003')
Reference_set_attribute.n900000000000007000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000007000', tag='n900000000000007000')
Reference_set_attribute.n900000000000216007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000216007', tag='n900000000000216007')
Reference_set_attribute.n900000000000218008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000218008', tag='n900000000000218008')
Reference_set_attribute.n900000000000226000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000226000', tag='n900000000000226000')
Reference_set_attribute.n900000000000458008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000458008', tag='n900000000000458008')
Reference_set_attribute.n900000000000459000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000459000', tag='n900000000000459000')
Reference_set_attribute.n900000000000460005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000460005', tag='n900000000000460005')
Reference_set_attribute.n900000000000461009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000461009', tag='n900000000000461009')
Reference_set_attribute.n900000000000462002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000462002', tag='n900000000000462002')
Reference_set_attribute.n900000000000463007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000463007', tag='n900000000000463007')
Reference_set_attribute.n900000000000464001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000464001', tag='n900000000000464001')
Reference_set_attribute.n900000000000465000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000465000', tag='n900000000000465000')
Reference_set_attribute.n900000000000466004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000466004', tag='n900000000000466004')
Reference_set_attribute.n900000000000467008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000467008', tag='n900000000000467008')
Reference_set_attribute.n900000000000468003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000468003', tag='n900000000000468003')
Reference_set_attribute.n900000000000469006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000469006', tag='n900000000000469006')
Reference_set_attribute.n900000000000470007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000470007', tag='n900000000000470007')
Reference_set_attribute.n900000000000471006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000471006', tag='n900000000000471006')
Reference_set_attribute.n900000000000472004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000472004', tag='n900000000000472004')
Reference_set_attribute.n900000000000473009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000473009', tag='n900000000000473009')
Reference_set_attribute.n900000000000474003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000474003', tag='n900000000000474003')
Reference_set_attribute.n900000000000475002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000475002', tag='n900000000000475002')
Reference_set_attribute.n900000000000476001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000476001', tag='n900000000000476001')
Reference_set_attribute.n900000000000477005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000477005', tag='n900000000000477005')
Reference_set_attribute.n900000000000478000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000478000', tag='n900000000000478000')
Reference_set_attribute.n900000000000479008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000479008', tag='n900000000000479008')
Reference_set_attribute.n900000000000481005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000481005', tag='n900000000000481005')
Reference_set_attribute.n900000000000482003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000482003', tag='n900000000000482003')
Reference_set_attribute.n900000000000483008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000483008', tag='n900000000000483008')
Reference_set_attribute.n900000000000484002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000484002', tag='n900000000000484002')
Reference_set_attribute.n900000000000485001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000485001', tag='n900000000000485001')
Reference_set_attribute.n900000000000486000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000486000', tag='n900000000000486000')
Reference_set_attribute.n900000000000487009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000487009', tag='n900000000000487009')
Reference_set_attribute.n900000000000491004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000491004', tag='n900000000000491004')
Reference_set_attribute.n900000000000492006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000492006', tag='n900000000000492006')
Reference_set_attribute.n900000000000493001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000493001', tag='n900000000000493001')
Reference_set_attribute.n900000000000494007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000494007', tag='n900000000000494007')
Reference_set_attribute.n900000000000495008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000495008', tag='n900000000000495008')
Reference_set_attribute.n900000000000499002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000499002', tag='n900000000000499002')
Reference_set_attribute.n900000000000500006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000500006', tag='n900000000000500006')
Reference_set_attribute.n900000000000501005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000501005', tag='n900000000000501005')
Reference_set_attribute.n900000000000502003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000502003', tag='n900000000000502003')
Reference_set_attribute.n900000000000503008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000503008', tag='n900000000000503008')
Reference_set_attribute.n900000000000504002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000504002', tag='n900000000000504002')
Reference_set_attribute.n900000000000505001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000505001', tag='n900000000000505001')
Reference_set_attribute.n900000000000510002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000510002', tag='n900000000000510002')
Reference_set_attribute.n900000000000511003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000511003', tag='n900000000000511003')
Reference_set_attribute.n900000000000514006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000514006', tag='n900000000000514006')
Reference_set_attribute.n900000000000515007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000515007', tag='n900000000000515007')
Reference_set_attribute.n900000000000518009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000518009', tag='n900000000000518009')
Reference_set_attribute.n900000000000519001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000519001', tag='n900000000000519001')
Reference_set_attribute.n900000000000520007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000520007', tag='n900000000000520007')
Reference_set_attribute.n900000000000532006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000532006', tag='n900000000000532006')
Reference_set_attribute.n900000000000533001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000533001', tag='n900000000000533001')
Reference_set_attribute.n900000000000535008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000535008', tag='n900000000000535008')
Reference_set_attribute.n900000000000536009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000536009', tag='n900000000000536009')
Reference_set_attribute.n900000000000537000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000537000', tag='n900000000000537000')
Reference_set_attribute.n900000000000539002 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000539002', tag='n900000000000539002')
Reference_set_attribute.n900000000000540000 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000540000', tag='n900000000000540000')
Reference_set_attribute.n900000000000541001 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000541001', tag='n900000000000541001')
Reference_set_attribute.n900000000000542008 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000542008', tag='n900000000000542008')
Reference_set_attribute.n900000000000543003 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000543003', tag='n900000000000543003')
Reference_set_attribute.n900000000000544009 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000544009', tag='n900000000000544009')
Reference_set_attribute.n900000000000545005 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000545005', tag='n900000000000545005')
Reference_set_attribute.n900000000000546006 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000546006', tag='n900000000000546006')
Reference_set_attribute.n900000000000548007 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000548007', tag='n900000000000548007')
Reference_set_attribute.n900000000000549004 = Reference_set_attribute._CF_enumeration.addEnumeration(unicode_value='900000000000549004', tag='n900000000000549004')
Reference_set_attribute._InitializeFacetMap(Reference_set_attribute._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Reference_set_attribute', Reference_set_attribute)

# Atomic simple type: {http://snomed.info/schema/rf2}Attribute_type
class Attribute_type (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Attribute_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7108, 4)
    _Documentation = '\n                \n            '
Attribute_type._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Attribute_type, enum_prefix=None)
Attribute_type.n900000000000460005 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000460005', tag='n900000000000460005')
Attribute_type.n900000000000461009 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000461009', tag='n900000000000461009')
Attribute_type.n900000000000462002 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000462002', tag='n900000000000462002')
Attribute_type.n900000000000463007 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000463007', tag='n900000000000463007')
Attribute_type.n900000000000464001 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000464001', tag='n900000000000464001')
Attribute_type.n900000000000465000 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000465000', tag='n900000000000465000')
Attribute_type.n900000000000466004 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000466004', tag='n900000000000466004')
Attribute_type.n900000000000467008 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000467008', tag='n900000000000467008')
Attribute_type.n900000000000468003 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000468003', tag='n900000000000468003')
Attribute_type.n900000000000469006 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000469006', tag='n900000000000469006')
Attribute_type.n900000000000470007 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000470007', tag='n900000000000470007')
Attribute_type.n900000000000471006 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000471006', tag='n900000000000471006')
Attribute_type.n900000000000472004 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000472004', tag='n900000000000472004')
Attribute_type.n900000000000473009 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000473009', tag='n900000000000473009')
Attribute_type.n900000000000474003 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000474003', tag='n900000000000474003')
Attribute_type.n900000000000475002 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000475002', tag='n900000000000475002')
Attribute_type.n900000000000476001 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000476001', tag='n900000000000476001')
Attribute_type.n900000000000477005 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000477005', tag='n900000000000477005')
Attribute_type.n900000000000478000 = Attribute_type._CF_enumeration.addEnumeration(unicode_value='900000000000478000', tag='n900000000000478000')
Attribute_type._InitializeFacetMap(Attribute_type._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Attribute_type', Attribute_type)

# Atomic simple type: {http://snomed.info/schema/rf2}Attribute_value
class Attribute_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Attribute_value')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7230, 4)
    _Documentation = '\n                \n            '
Attribute_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Attribute_value, enum_prefix=None)
Attribute_value.n450995009 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='450995009', tag='n450995009')
Attribute_value.n450996005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='450996005', tag='n450996005')
Attribute_value.n450997001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='450997001', tag='n450997001')
Attribute_value.n450998006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='450998006', tag='n450998006')
Attribute_value.n450999003 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='450999003', tag='n450999003')
Attribute_value.n451000004 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='451000004', tag='n451000004')
Attribute_value.n451001000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='451001000', tag='n451001000')
Attribute_value.n451002007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='451002007', tag='n451002007')
Attribute_value.n451003002 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='451003002', tag='n451003002')
Attribute_value.n900000000000007000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000007000', tag='n900000000000007000')
Attribute_value.n900000000000216007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000216007', tag='n900000000000216007')
Attribute_value.n900000000000218008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000218008', tag='n900000000000218008')
Attribute_value.n900000000000226000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000226000', tag='n900000000000226000')
Attribute_value.n900000000000481005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000481005', tag='n900000000000481005')
Attribute_value.n900000000000482003 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000482003', tag='n900000000000482003')
Attribute_value.n900000000000483008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000483008', tag='n900000000000483008')
Attribute_value.n900000000000484002 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000484002', tag='n900000000000484002')
Attribute_value.n900000000000485001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000485001', tag='n900000000000485001')
Attribute_value.n900000000000486000 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000486000', tag='n900000000000486000')
Attribute_value.n900000000000487009 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000487009', tag='n900000000000487009')
Attribute_value.n900000000000492006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000492006', tag='n900000000000492006')
Attribute_value.n900000000000493001 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000493001', tag='n900000000000493001')
Attribute_value.n900000000000494007 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000494007', tag='n900000000000494007')
Attribute_value.n900000000000495008 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000495008', tag='n900000000000495008')
Attribute_value.n900000000000545005 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000545005', tag='n900000000000545005')
Attribute_value.n900000000000546006 = Attribute_value._CF_enumeration.addEnumeration(unicode_value='900000000000546006', tag='n900000000000546006')
Attribute_value._InitializeFacetMap(Attribute_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Attribute_value', Attribute_value)

# Atomic simple type: {http://snomed.info/schema/rf2}SNOMED_CT_source_code_to_target_map_code_correlation_value
class SNOMED_CT_source_code_to_target_map_code_correlation_value (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SNOMED_CT_source_code_to_target_map_code_correlation_value')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7397, 4)
    _Documentation = '\n                \n            '
SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SNOMED_CT_source_code_to_target_map_code_correlation_value, enum_prefix=None)
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447556008 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447556008', tag='n447556008')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447557004 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447557004', tag='n447557004')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447558009 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447558009', tag='n447558009')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447559001 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447559001', tag='n447559001')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447560006 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447560006', tag='n447560006')
SNOMED_CT_source_code_to_target_map_code_correlation_value.n447561005 = SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration.addEnumeration(unicode_value='447561005', tag='n447561005')
SNOMED_CT_source_code_to_target_map_code_correlation_value._InitializeFacetMap(SNOMED_CT_source_code_to_target_map_code_correlation_value._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SNOMED_CT_source_code_to_target_map_code_correlation_value', SNOMED_CT_source_code_to_target_map_code_correlation_value)

# Atomic simple type: {http://snomed.info/schema/rf2}Acceptability
class Acceptability (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Acceptability')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7464, 4)
    _Documentation = '\n                \n            '
Acceptability._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Acceptability, enum_prefix=None)
Acceptability.n900000000000548007 = Acceptability._CF_enumeration.addEnumeration(unicode_value='900000000000548007', tag='n900000000000548007')
Acceptability.n900000000000549004 = Acceptability._CF_enumeration.addEnumeration(unicode_value='900000000000549004', tag='n900000000000549004')
Acceptability._InitializeFacetMap(Acceptability._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Acceptability', Acceptability)

# Atomic simple type: {http://snomed.info/schema/rf2}Description_format
class Description_format (SCTID, pyxb.binding.basis.enumeration_mixin):

    """
                
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Description_format')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7497, 4)
    _Documentation = '\n                \n            '
Description_format._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Description_format, enum_prefix=None)
Description_format.n900000000000540000 = Description_format._CF_enumeration.addEnumeration(unicode_value='900000000000540000', tag='n900000000000540000')
Description_format.n900000000000541001 = Description_format._CF_enumeration.addEnumeration(unicode_value='900000000000541001', tag='n900000000000541001')
Description_format.n900000000000542008 = Description_format._CF_enumeration.addEnumeration(unicode_value='900000000000542008', tag='n900000000000542008')
Description_format.n900000000000543003 = Description_format._CF_enumeration.addEnumeration(unicode_value='900000000000543003', tag='n900000000000543003')
Description_format._InitializeFacetMap(Description_format._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Description_format', Description_format)

# Atomic simple type: [anonymous]
class STD_ANON (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7791, 24)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.int(0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive)

# Atomic simple type: [anonymous]
class STD_ANON_ (Integer):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7838, 24)
    _Documentation = None
STD_ANON_._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_, value=pyxb.binding.datatypes.int(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_minInclusive)

# Complex type {http://snomed.info/schema/rf2}SCTIDorUUID with content type ELEMENT_ONLY
class SCTIDorUUID (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}SCTIDorUUID with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SCTIDorUUID')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}sctid uses Python identifier sctid
    __sctid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sctid'), 'sctid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2sctid', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 55, 12), )

    
    sctid = property(__sctid.value, __sctid.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uuid'), 'uuid', '__httpsnomed_infoschemarf2_SCTIDorUUID_httpsnomed_infoschemarf2uuid', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 56, 12), )

    
    uuid = property(__uuid.value, __uuid.set, None, None)

    _ElementMap.update({
        __sctid.name() : __sctid,
        __uuid.name() : __uuid
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SCTIDorUUID', SCTIDorUUID)


# Complex type {http://snomed.info/schema/rf2}Base with content type ELEMENT_ONLY
class Base (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Base with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Base')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7622, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'active'), 'active', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}changeset uses Python identifier changeset
    __changeset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'changeset'), 'changeset', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2changeset', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12), )

    
    changeset = property(__changeset.value, __changeset.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}locked uses Python identifier locked
    __locked = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locked'), 'locked', '__httpsnomed_infoschemarf2_Base_httpsnomed_infoschemarf2locked', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12), )

    
    locked = property(__locked.value, __locked.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active,
        __moduleId.name() : __moduleId,
        __changeset.name() : __changeset,
        __locked.name() : __locked
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Base', Base)


# Complex type {http://snomed.info/schema/rf2}Identifier with content type ELEMENT_ONLY
class Identifier_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Identifier with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Identifier')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7714, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}identifierSchemeId uses Python identifier identifierSchemeId
    __identifierSchemeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'identifierSchemeId'), 'identifierSchemeId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2identifierSchemeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7716, 12), )

    
    identifierSchemeId = property(__identifierSchemeId.value, __identifierSchemeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}alternateIdentifier uses Python identifier alternateIdentifier
    __alternateIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alternateIdentifier'), 'alternateIdentifier', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2alternateIdentifier', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7717, 12), )

    
    alternateIdentifier = property(__alternateIdentifier.value, __alternateIdentifier.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7718, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'active'), 'active', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7719, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7720, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referenceComponentId uses Python identifier referenceComponentId
    __referenceComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referenceComponentId'), 'referenceComponentId', '__httpsnomed_infoschemarf2_Identifier__httpsnomed_infoschemarf2referenceComponentId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7721, 12), )

    
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
Namespace.addCategoryObject('typeBinding', 'Identifier', Identifier_)


# Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistory with content type ELEMENT_ONLY
class TransitiveClosureHistory_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistory with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransitiveClosureHistory')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7738, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}subtypeId uses Python identifier subtypeId
    __subtypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subtypeId'), 'subtypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2subtypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7740, 12), )

    
    subtypeId = property(__subtypeId.value, __subtypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}supertypeId uses Python identifier supertypeId
    __supertypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'supertypeId'), 'supertypeId', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2supertypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7741, 12), )

    
    supertypeId = property(__supertypeId.value, __supertypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7742, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'active'), 'active', '__httpsnomed_infoschemarf2_TransitiveClosureHistory__httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7743, 12), )

    
    active = property(__active.value, __active.set, None, None)

    _ElementMap.update({
        __subtypeId.name() : __subtypeId,
        __supertypeId.name() : __supertypeId,
        __effectiveTime.name() : __effectiveTime,
        __active.name() : __active
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'TransitiveClosureHistory', TransitiveClosureHistory_)


# Complex type {http://snomed.info/schema/rf2}RefsetBase with content type ELEMENT_ONLY
class RefsetBase (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}RefsetBase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RefsetBase')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7763, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://snomed.info/schema/rf2}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2id', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}effectiveTime uses Python identifier effectiveTime
    __effectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), 'effectiveTime', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2effectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12), )

    
    effectiveTime = property(__effectiveTime.value, __effectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'active'), 'active', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2active', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12), )

    
    active = property(__active.value, __active.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleId uses Python identifier moduleId
    __moduleId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), 'moduleId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2moduleId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12), )

    
    moduleId = property(__moduleId.value, __moduleId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}refsetId uses Python identifier refsetId
    __refsetId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'refsetId'), 'refsetId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2refsetId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12), )

    
    refsetId = property(__refsetId.value, __refsetId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}referencedComponentId uses Python identifier referencedComponentId
    __referencedComponentId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId'), 'referencedComponentId', '__httpsnomed_infoschemarf2_RefsetBase_httpsnomed_infoschemarf2referencedComponentId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12), )

    
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
Namespace.addCategoryObject('typeBinding', 'RefsetBase', RefsetBase)


# Complex type {http://snomed.info/schema/rf2}Iterator with content type EMPTY
class Iterator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://snomed.info/schema/rf2}Iterator with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Iterator')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7586, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute complete uses Python identifier complete
    __complete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'complete'), 'complete', '__httpsnomed_infoschemarf2_Iterator_complete', CompleteDirectory, required=True)
    __complete._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7587, 8)
    __complete._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7587, 8)
    
    complete = property(__complete.value, __complete.set, None, 'an indicator that states whether the complete directory listing is included in\n                    \n                    or whether additional retrievals are needed to get the full listing.\n                ')

    
    # Attribute numEntries uses Python identifier numEntries
    __numEntries = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numEntries'), 'numEntries', '__httpsnomed_infoschemarf2_Iterator_numEntries', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __numEntries._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7595, 8)
    __numEntries._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7595, 8)
    
    numEntries = property(__numEntries.value, __numEntries.set, None, 'the number of entries in this directory segment. Note that this is\n                    \n                    the total number of entries in the complete directory listing - just the number of entries in this\n                    segment.\n                ')

    
    # Attribute prev uses Python identifier prev
    __prev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prev'), 'prev', '__httpsnomed_infoschemarf2_Iterator_prev', pyxb.binding.datatypes.anyURI)
    __prev._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7604, 8)
    __prev._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7604, 8)
    
    prev = property(__prev.value, __prev.set, None, 'a URI that, when de-referenced, produces the preceding set of entries in the\n                    directory.\n                ')

    
    # Attribute next uses Python identifier next
    __next = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'next'), 'next', '__httpsnomed_infoschemarf2_Iterator_next', pyxb.binding.datatypes.anyURI)
    __next._DeclarationLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7611, 8)
    __next._UseLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7611, 8)
    
    next = property(__next.value, __next.set, None, 'a URI that, when de-referenced, produces the next set of entries in the directory.\n                ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __complete.name() : __complete,
        __numEntries.name() : __numEntries,
        __prev.name() : __prev,
        __next.name() : __next
    })
Namespace.addCategoryObject('typeBinding', 'Iterator', Iterator)


# Complex type {http://snomed.info/schema/rf2}Concept with content type ELEMENT_ONLY
class Concept_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Concept with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Concept')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7636, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element changeset ({http://snomed.info/schema/rf2}changeset) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element locked ({http://snomed.info/schema/rf2}locked) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}definitionStatusId uses Python identifier definitionStatusId
    __definitionStatusId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definitionStatusId'), 'definitionStatusId', '__httpsnomed_infoschemarf2_Concept__httpsnomed_infoschemarf2definitionStatusId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7640, 20), )

    
    definitionStatusId = property(__definitionStatusId.value, __definitionStatusId.set, None, None)

    _ElementMap.update({
        __definitionStatusId.name() : __definitionStatusId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Concept', Concept_)


# Complex type {http://snomed.info/schema/rf2}Description with content type ELEMENT_ONLY
class Description_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Description with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Description')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7659, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element changeset ({http://snomed.info/schema/rf2}changeset) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element locked ({http://snomed.info/schema/rf2}locked) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}conceptId uses Python identifier conceptId
    __conceptId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conceptId'), 'conceptId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2conceptId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7663, 20), )

    
    conceptId = property(__conceptId.value, __conceptId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}languageCode uses Python identifier languageCode
    __languageCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'languageCode'), 'languageCode', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2languageCode', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7664, 20), )

    
    languageCode = property(__languageCode.value, __languageCode.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7665, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'term'), 'term', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2term', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7666, 20), )

    
    term = property(__term.value, __term.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}caseSignificanceId uses Python identifier caseSignificanceId
    __caseSignificanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseSignificanceId'), 'caseSignificanceId', '__httpsnomed_infoschemarf2_Description__httpsnomed_infoschemarf2caseSignificanceId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7667, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'Description', Description_)


# Complex type {http://snomed.info/schema/rf2}Relationship with content type ELEMENT_ONLY
class Relationship_ (Base):
    """Complex type {http://snomed.info/schema/rf2}Relationship with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Relationship')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7686, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element changeset ({http://snomed.info/schema/rf2}changeset) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element locked ({http://snomed.info/schema/rf2}locked) inherited from {http://snomed.info/schema/rf2}Base
    
    # Element {http://snomed.info/schema/rf2}sourceId uses Python identifier sourceId
    __sourceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceId'), 'sourceId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2sourceId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7690, 20), )

    
    sourceId = property(__sourceId.value, __sourceId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}destinationId uses Python identifier destinationId
    __destinationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'destinationId'), 'destinationId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2destinationId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7691, 20), )

    
    destinationId = property(__destinationId.value, __destinationId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}relationshipGroup uses Python identifier relationshipGroup
    __relationshipGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relationshipGroup'), 'relationshipGroup', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2relationshipGroup', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7692, 20), )

    
    relationshipGroup = property(__relationshipGroup.value, __relationshipGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}typeId uses Python identifier typeId
    __typeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'typeId'), 'typeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2typeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7693, 20), )

    
    typeId = property(__typeId.value, __typeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}characteristicTypeId uses Python identifier characteristicTypeId
    __characteristicTypeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'characteristicTypeId'), 'characteristicTypeId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2characteristicTypeId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7694, 20), )

    
    characteristicTypeId = property(__characteristicTypeId.value, __characteristicTypeId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}modifierId uses Python identifier modifierId
    __modifierId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modifierId'), 'modifierId', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2modifierId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7695, 20), )

    
    modifierId = property(__modifierId.value, __modifierId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}isCanonical uses Python identifier isCanonical
    __isCanonical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isCanonical'), 'isCanonical', '__httpsnomed_infoschemarf2_Relationship__httpsnomed_infoschemarf2isCanonical', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7696, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'Relationship', Relationship_)


# Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSetEntry with content type ELEMENT_ONLY
class DescriptorReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptorReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7777, 4)
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
    __attributeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeDescription'), 'attributeDescription', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeDescription', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7788, 20), )

    
    attributeDescription = property(__attributeDescription.value, __attributeDescription.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeType'), 'attributeType', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeType', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7789, 20), )

    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}attributeOrder uses Python identifier attributeOrder
    __attributeOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'attributeOrder'), 'attributeOrder', '__httpsnomed_infoschemarf2_DescriptorReferenceSetEntry__httpsnomed_infoschemarf2attributeOrder', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7790, 20), )

    
    attributeOrder = property(__attributeOrder.value, __attributeOrder.set, None, None)

    _ElementMap.update({
        __attributeDescription.name() : __attributeDescription,
        __attributeType.name() : __attributeType,
        __attributeOrder.name() : __attributeOrder
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DescriptorReferenceSetEntry', DescriptorReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}SimpleReferenceSetEntry with content type ELEMENT_ONLY
class SimpleReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}SimpleReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7815, 4)
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
Namespace.addCategoryObject('typeBinding', 'SimpleReferenceSetEntry', SimpleReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}OrderedReferenceSetEntry with content type ELEMENT_ONLY
class OrderedReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}OrderedReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderedReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7833, 4)
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
    __order = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'order'), 'order', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2order', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7837, 20), )

    
    order = property(__order.value, __order.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}linkedTo uses Python identifier linkedTo
    __linkedTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'linkedTo'), 'linkedTo', '__httpsnomed_infoschemarf2_OrderedReferenceSetEntry__httpsnomed_infoschemarf2linkedTo', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7844, 20), )

    
    linkedTo = property(__linkedTo.value, __linkedTo.set, None, None)

    _ElementMap.update({
        __order.name() : __order,
        __linkedTo.name() : __linkedTo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OrderedReferenceSetEntry', OrderedReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSetEntry with content type ELEMENT_ONLY
class AttributeValueReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AttributeValueReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7863, 4)
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
    __valueId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valueId'), 'valueId', '__httpsnomed_infoschemarf2_AttributeValueReferenceSetEntry__httpsnomed_infoschemarf2valueId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7867, 20), )

    
    valueId = property(__valueId.value, __valueId.set, None, None)

    _ElementMap.update({
        __valueId.name() : __valueId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AttributeValueReferenceSetEntry', AttributeValueReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSetEntry with content type ELEMENT_ONLY
class SimpleMapReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleMapReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7886, 4)
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
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_SimpleMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7890, 20), )

    
    mapTarget = property(__mapTarget.value, __mapTarget.set, None, None)

    _ElementMap.update({
        __mapTarget.name() : __mapTarget
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SimpleMapReferenceSetEntry', SimpleMapReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSetEntry with content type ELEMENT_ONLY
class ComplexMapReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexMapReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7909, 4)
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
    __mapGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapGroup'), 'mapGroup', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapGroup', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7913, 20), )

    
    mapGroup = property(__mapGroup.value, __mapGroup.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapPriority uses Python identifier mapPriority
    __mapPriority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapPriority'), 'mapPriority', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapPriority', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7914, 20), )

    
    mapPriority = property(__mapPriority.value, __mapPriority.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapRule uses Python identifier mapRule
    __mapRule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapRule'), 'mapRule', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapRule', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7915, 20), )

    
    mapRule = property(__mapRule.value, __mapRule.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapAdvice uses Python identifier mapAdvice
    __mapAdvice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapAdvice'), 'mapAdvice', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapAdvice', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7916, 20), )

    
    mapAdvice = property(__mapAdvice.value, __mapAdvice.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapTarget uses Python identifier mapTarget
    __mapTarget = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapTarget'), 'mapTarget', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapTarget', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7917, 20), )

    
    mapTarget = property(__mapTarget.value, __mapTarget.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}correlationId uses Python identifier correlationId
    __correlationId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'correlationId'), 'correlationId', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2correlationId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7918, 20), )

    
    correlationId = property(__correlationId.value, __correlationId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}mapCategoryId uses Python identifier mapCategoryId
    __mapCategoryId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mapCategoryId'), 'mapCategoryId', '__httpsnomed_infoschemarf2_ComplexMapReferenceSetEntry__httpsnomed_infoschemarf2mapCategoryId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7919, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'ComplexMapReferenceSetEntry', ComplexMapReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}LanguageReferenceSetEntry with content type ELEMENT_ONLY
class LanguageReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}LanguageReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7937, 4)
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
    __acceptabilityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptabilityId'), 'acceptabilityId', '__httpsnomed_infoschemarf2_LanguageReferenceSetEntry__httpsnomed_infoschemarf2acceptabilityId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7941, 20), )

    
    acceptabilityId = property(__acceptabilityId.value, __acceptabilityId.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}conceptId uses Python identifier conceptId
    __conceptId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conceptId'), 'conceptId', '__httpsnomed_infoschemarf2_LanguageReferenceSetEntry__httpsnomed_infoschemarf2conceptId', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7943, 20), )

    
    conceptId = property(__conceptId.value, __conceptId.set, None, None)

    _ElementMap.update({
        __acceptabilityId.name() : __acceptabilityId,
        __conceptId.name() : __conceptId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LanguageReferenceSetEntry', LanguageReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSetEntry with content type ELEMENT_ONLY
class QuerySpecificationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuerySpecificationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7961, 4)
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
    __query = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'query'), 'query', '__httpsnomed_infoschemarf2_QuerySpecificationReferenceSetEntry__httpsnomed_infoschemarf2query', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7965, 20), )

    
    query = property(__query.value, __query.set, None, None)

    _ElementMap.update({
        __query.name() : __query
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'QuerySpecificationReferenceSetEntry', QuerySpecificationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSetEntry with content type ELEMENT_ONLY
class AnnotationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnotationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7984, 4)
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
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annotation'), 'annotation', '__httpsnomed_infoschemarf2_AnnotationReferenceSetEntry__httpsnomed_infoschemarf2annotation', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7988, 20), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    _ElementMap.update({
        __annotation.name() : __annotation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AnnotationReferenceSetEntry', AnnotationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}AssociationReferenceSetEntry with content type ELEMENT_ONLY
class AssociationReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}AssociationReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssociationReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8006, 4)
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
    __targetComponent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'targetComponent'), 'targetComponent', '__httpsnomed_infoschemarf2_AssociationReferenceSetEntry__httpsnomed_infoschemarf2targetComponent', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8010, 20), )

    
    targetComponent = property(__targetComponent.value, __targetComponent.set, None, None)

    _ElementMap.update({
        __targetComponent.name() : __targetComponent
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AssociationReferenceSetEntry', AssociationReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ModuleDependencyReferenceSetEntry with content type ELEMENT_ONLY
class ModuleDependencyReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}ModuleDependencyReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModuleDependencyReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8029, 4)
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
    __sourceEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sourceEffectiveTime'), 'sourceEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2sourceEffectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8033, 20), )

    
    sourceEffectiveTime = property(__sourceEffectiveTime.value, __sourceEffectiveTime.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}targetEffectiveTime uses Python identifier targetEffectiveTime
    __targetEffectiveTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'targetEffectiveTime'), 'targetEffectiveTime', '__httpsnomed_infoschemarf2_ModuleDependencyReferenceSetEntry__httpsnomed_infoschemarf2targetEffectiveTime', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8034, 20), )

    
    targetEffectiveTime = property(__targetEffectiveTime.value, __targetEffectiveTime.set, None, None)

    _ElementMap.update({
        __sourceEffectiveTime.name() : __sourceEffectiveTime,
        __targetEffectiveTime.name() : __targetEffectiveTime
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ModuleDependencyReferenceSetEntry', ModuleDependencyReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSetEntry with content type ELEMENT_ONLY
class DescriptionFormatReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionFormatReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8053, 4)
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
    __descriptionFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptionFormat'), 'descriptionFormat', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionFormat', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8057, 20), )

    
    descriptionFormat = property(__descriptionFormat.value, __descriptionFormat.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}descriptionLength uses Python identifier descriptionLength
    __descriptionLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descriptionLength'), 'descriptionLength', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSetEntry__httpsnomed_infoschemarf2descriptionLength', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8058, 20), )

    
    descriptionLength = property(__descriptionLength.value, __descriptionLength.set, None, None)

    _ElementMap.update({
        __descriptionFormat.name() : __descriptionFormat,
        __descriptionLength.name() : __descriptionLength
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DescriptionFormatReferenceSetEntry', DescriptionFormatReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry with content type ELEMENT_ONLY
class ChangeSetReferenceSetEntry_ (RefsetBase):
    """Complex type {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChangeSetReferenceSetEntry')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8077, 4)
    _ElementMap = RefsetBase._ElementMap.copy()
    _AttributeMap = RefsetBase._AttributeMap.copy()
    # Base type is RefsetBase
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element {http://snomed.info/schema/rf2}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpsnomed_infoschemarf2_ChangeSetReferenceSetEntry__httpsnomed_infoschemarf2name', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8081, 20), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}owner uses Python identifier owner
    __owner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'owner'), 'owner', '__httpsnomed_infoschemarf2_ChangeSetReferenceSetEntry__httpsnomed_infoschemarf2owner', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20), )

    
    owner = property(__owner.value, __owner.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}changeDescription uses Python identifier changeDescription
    __changeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'changeDescription'), 'changeDescription', '__httpsnomed_infoschemarf2_ChangeSetReferenceSetEntry__httpsnomed_infoschemarf2changeDescription', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20), )

    
    changeDescription = property(__changeDescription.value, __changeDescription.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}isFinal uses Python identifier isFinal
    __isFinal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'isFinal'), 'isFinal', '__httpsnomed_infoschemarf2_ChangeSetReferenceSetEntry__httpsnomed_infoschemarf2isFinal', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8084, 20), )

    
    isFinal = property(__isFinal.value, __isFinal.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}inRelease uses Python identifier inRelease
    __inRelease = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inRelease'), 'inRelease', '__httpsnomed_infoschemarf2_ChangeSetReferenceSetEntry__httpsnomed_infoschemarf2inRelease', False, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20), )

    
    inRelease = property(__inRelease.value, __inRelease.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __owner.name() : __owner,
        __changeDescription.name() : __changeDescription,
        __isFinal.name() : __isFinal,
        __inRelease.name() : __inRelease
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ChangeSetReferenceSetEntry', ChangeSetReferenceSetEntry_)


# Complex type {http://snomed.info/schema/rf2}ConceptList with content type ELEMENT_ONLY
class ConceptList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ConceptList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ConceptList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7647, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_ConceptList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7651, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'ConceptList', ConceptList_)


# Complex type {http://snomed.info/schema/rf2}DescriptionList with content type ELEMENT_ONLY
class DescriptionList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptionList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7675, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptionList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7679, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'DescriptionList', DescriptionList_)


# Complex type {http://snomed.info/schema/rf2}RelationshipList with content type ELEMENT_ONLY
class RelationshipList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}RelationshipList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RelationshipList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7703, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_RelationshipList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7707, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'RelationshipList', RelationshipList_)


# Complex type {http://snomed.info/schema/rf2}IdentifierList with content type ELEMENT_ONLY
class IdentifierList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}IdentifierList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IdentifierList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7726, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_IdentifierList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7730, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'IdentifierList', IdentifierList_)


# Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistoryList with content type ELEMENT_ONLY
class TransitiveClosureHistoryList_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}TransitiveClosureHistoryList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransitiveClosureHistoryList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7749, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_TransitiveClosureHistoryList__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7753, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'TransitiveClosureHistoryList', TransitiveClosureHistoryList_)


# Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSet with content type ELEMENT_ONLY
class DescriptorReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptorReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptorReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7803, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptorReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7807, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'DescriptorReferenceSet', DescriptorReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}SimpleReferenceSet with content type ELEMENT_ONLY
class SimpleReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}SimpleReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7822, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_SimpleReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7826, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'SimpleReferenceSet', SimpleReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}OrderedReferenceSet with content type ELEMENT_ONLY
class OrderedReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}OrderedReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrderedReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7851, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_OrderedReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7855, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'OrderedReferenceSet', OrderedReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSet with content type ELEMENT_ONLY
class AttributeValueReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AttributeValueReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AttributeValueReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7873, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_AttributeValueReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7877, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'AttributeValueReferenceSet', AttributeValueReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSet with content type ELEMENT_ONLY
class SimpleMapReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}SimpleMapReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SimpleMapReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7897, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_SimpleMapReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7901, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'SimpleMapReferenceSet', SimpleMapReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSet with content type ELEMENT_ONLY
class ComplexMapReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ComplexMapReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ComplexMapReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7925, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_ComplexMapReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7929, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'ComplexMapReferenceSet', ComplexMapReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}LanguageReferenceSet with content type ELEMENT_ONLY
class LanguageReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}LanguageReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LanguageReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7949, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_LanguageReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7953, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'LanguageReferenceSet', LanguageReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSet with content type ELEMENT_ONLY
class QuerySpecificationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}QuerySpecificationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'QuerySpecificationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7971, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_QuerySpecificationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7975, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'QuerySpecificationReferenceSet', QuerySpecificationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSet with content type ELEMENT_ONLY
class AnnotationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AnnotationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnnotationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7994, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_AnnotationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7998, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'AnnotationReferenceSet', AnnotationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}AssociationReferenceSet with content type ELEMENT_ONLY
class AssociationReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}AssociationReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssociationReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8016, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_AssociationReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8020, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'AssociationReferenceSet', AssociationReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ModuleDepencencyReferenceSet with content type ELEMENT_ONLY
class ModuleDepencencyReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ModuleDepencencyReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ModuleDepencencyReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8041, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_ModuleDepencencyReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8045, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'ModuleDepencencyReferenceSet', ModuleDepencencyReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSet with content type ELEMENT_ONLY
class DescriptionFormatReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}DescriptionFormatReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DescriptionFormatReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8064, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_DescriptionFormatReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8068, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'DescriptionFormatReferenceSet', DescriptionFormatReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ChangeSetReferenceSet with content type ELEMENT_ONLY
class ChangeSetReferenceSet_ (Iterator):
    """Complex type {http://snomed.info/schema/rf2}ChangeSetReferenceSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChangeSetReferenceSet')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8091, 4)
    _ElementMap = Iterator._ElementMap.copy()
    _AttributeMap = Iterator._AttributeMap.copy()
    # Base type is Iterator
    
    # Element {http://snomed.info/schema/rf2}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__httpsnomed_infoschemarf2_ChangeSetReferenceSet__httpsnomed_infoschemarf2entry', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8095, 20), )

    
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
Namespace.addCategoryObject('typeBinding', 'ChangeSetReferenceSet', ChangeSetReferenceSet_)


# Complex type {http://snomed.info/schema/rf2}ChangeSetDetails with content type ELEMENT_ONLY
class ChangeSetDetails_ (ChangeSetReferenceSetEntry_):
    """Complex type {http://snomed.info/schema/rf2}ChangeSetDetails with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ChangeSetDetails')
    _XSDLocation = pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8102, 4)
    _ElementMap = ChangeSetReferenceSetEntry_._ElementMap.copy()
    _AttributeMap = ChangeSetReferenceSetEntry_._AttributeMap.copy()
    # Base type is ChangeSetReferenceSetEntry_
    
    # Element id ({http://snomed.info/schema/rf2}id) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element effectiveTime ({http://snomed.info/schema/rf2}effectiveTime) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element active ({http://snomed.info/schema/rf2}active) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element moduleId ({http://snomed.info/schema/rf2}moduleId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element refsetId ({http://snomed.info/schema/rf2}refsetId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element referencedComponentId ({http://snomed.info/schema/rf2}referencedComponentId) inherited from {http://snomed.info/schema/rf2}RefsetBase
    
    # Element name ({http://snomed.info/schema/rf2}name) inherited from {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry
    
    # Element owner ({http://snomed.info/schema/rf2}owner) inherited from {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry
    
    # Element changeDescription ({http://snomed.info/schema/rf2}changeDescription) inherited from {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry
    
    # Element isFinal ({http://snomed.info/schema/rf2}isFinal) inherited from {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry
    
    # Element inRelease ({http://snomed.info/schema/rf2}inRelease) inherited from {http://snomed.info/schema/rf2}ChangeSetReferenceSetEntry
    
    # Element {http://snomed.info/schema/rf2}concept uses Python identifier concept
    __concept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'concept'), 'concept', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2concept', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8106, 20), )

    
    concept = property(__concept.value, __concept.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2description', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8107, 20), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}relationship uses Python identifier relationship
    __relationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relationship'), 'relationship', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2relationship', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8108, 20), )

    
    relationship = property(__relationship.value, __relationship.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}statedRelationship uses Python identifier statedRelationship
    __statedRelationship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'statedRelationship'), 'statedRelationship', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2statedRelationship', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8109, 20), )

    
    statedRelationship = property(__statedRelationship.value, __statedRelationship.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}definition uses Python identifier definition
    __definition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'definition'), 'definition', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2definition', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8110, 20), )

    
    definition = property(__definition.value, __definition.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'language'), 'language', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2language', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8111, 20), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}simplerefset uses Python identifier simplerefset
    __simplerefset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'simplerefset'), 'simplerefset', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2simplerefset', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8112, 20), )

    
    simplerefset = property(__simplerefset.value, __simplerefset.set, None, None)

    
    # Element {http://snomed.info/schema/rf2}moduleDependency uses Python identifier moduleDependency
    __moduleDependency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'moduleDependency'), 'moduleDependency', '__httpsnomed_infoschemarf2_ChangeSetDetails__httpsnomed_infoschemarf2moduleDependency', True, pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8113, 20), )

    
    moduleDependency = property(__moduleDependency.value, __moduleDependency.set, None, None)

    _ElementMap.update({
        __concept.name() : __concept,
        __description.name() : __description,
        __relationship.name() : __relationship,
        __statedRelationship.name() : __statedRelationship,
        __definition.name() : __definition,
        __language.name() : __language,
        __simplerefset.name() : __simplerefset,
        __moduleDependency.name() : __moduleDependency
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ChangeSetDetails', ChangeSetDetails_)


Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7713, 4))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

TransitiveClosureHistory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransitiveClosureHistory'), TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7737, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistory.name().localName(), TransitiveClosureHistory)

Concept = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Concept'), Concept_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7635, 4))
Namespace.addCategoryObject('elementBinding', Concept.name().localName(), Concept)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7658, 4))
Namespace.addCategoryObject('elementBinding', Description.name().localName(), Description)

Relationship = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Relationship'), Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7685, 4))
Namespace.addCategoryObject('elementBinding', Relationship.name().localName(), Relationship)

DescriptorReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescriptorReferenceSetEntry'), DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7776, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSetEntry.name().localName(), DescriptorReferenceSetEntry)

SimpleReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleReferenceSetEntry'), SimpleReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7814, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSetEntry.name().localName(), SimpleReferenceSetEntry)

OrderedReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrderedReferenceSetEntry'), OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7832, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSetEntry.name().localName(), OrderedReferenceSetEntry)

AttributeValueReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeValueReferenceSetEntry'), AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7862, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSetEntry.name().localName(), AttributeValueReferenceSetEntry)

SimpleMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleMapReferenceSetEntry'), SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7885, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSetEntry.name().localName(), SimpleMapReferenceSetEntry)

ComplexMapReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexMapReferenceSetEntry'), ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7908, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSetEntry.name().localName(), ComplexMapReferenceSetEntry)

LanguageReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LanguageReferenceSetEntry'), LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7936, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSetEntry.name().localName(), LanguageReferenceSetEntry)

QuerySpecificationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QuerySpecificationReferenceSetEntry'), QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7960, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSetEntry.name().localName(), QuerySpecificationReferenceSetEntry)

AnnotationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnnotationReferenceSetEntry'), AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7983, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSetEntry.name().localName(), AnnotationReferenceSetEntry)

AssociationReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssociationReferenceSetEntry'), AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8005, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSetEntry.name().localName(), AssociationReferenceSetEntry)

ModuleDependencyReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModuleDependencyReferenceSetEntry'), ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8028, 4))
Namespace.addCategoryObject('elementBinding', ModuleDependencyReferenceSetEntry.name().localName(), ModuleDependencyReferenceSetEntry)

DescriptionFormatReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescriptionFormatReferenceSetEntry'), DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8052, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSetEntry.name().localName(), DescriptionFormatReferenceSetEntry)

ChangeSetReferenceSetEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChangeSetReferenceSetEntry'), ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8076, 4))
Namespace.addCategoryObject('elementBinding', ChangeSetReferenceSetEntry.name().localName(), ChangeSetReferenceSetEntry)

ConceptList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConceptList'), ConceptList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7646, 4))
Namespace.addCategoryObject('elementBinding', ConceptList.name().localName(), ConceptList)

DescriptionList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescriptionList'), DescriptionList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7674, 4))
Namespace.addCategoryObject('elementBinding', DescriptionList.name().localName(), DescriptionList)

RelationshipList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelationshipList'), RelationshipList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7702, 4))
Namespace.addCategoryObject('elementBinding', RelationshipList.name().localName(), RelationshipList)

IdentifierList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IdentifierList'), IdentifierList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7725, 4))
Namespace.addCategoryObject('elementBinding', IdentifierList.name().localName(), IdentifierList)

TransitiveClosureHistoryList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransitiveClosureHistoryList'), TransitiveClosureHistoryList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7748, 4))
Namespace.addCategoryObject('elementBinding', TransitiveClosureHistoryList.name().localName(), TransitiveClosureHistoryList)

DescriptorReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescriptorReferenceSet'), DescriptorReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7802, 4))
Namespace.addCategoryObject('elementBinding', DescriptorReferenceSet.name().localName(), DescriptorReferenceSet)

SimpleReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleReferenceSet'), SimpleReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7821, 4))
Namespace.addCategoryObject('elementBinding', SimpleReferenceSet.name().localName(), SimpleReferenceSet)

OrderedReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrderedReferenceSet'), OrderedReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7850, 4))
Namespace.addCategoryObject('elementBinding', OrderedReferenceSet.name().localName(), OrderedReferenceSet)

AttributeValueReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AttributeValueReferenceSet'), AttributeValueReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7872, 4))
Namespace.addCategoryObject('elementBinding', AttributeValueReferenceSet.name().localName(), AttributeValueReferenceSet)

SimpleMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SimpleMapReferenceSet'), SimpleMapReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7896, 4))
Namespace.addCategoryObject('elementBinding', SimpleMapReferenceSet.name().localName(), SimpleMapReferenceSet)

ComplexMapReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexMapReferenceSet'), ComplexMapReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7924, 4))
Namespace.addCategoryObject('elementBinding', ComplexMapReferenceSet.name().localName(), ComplexMapReferenceSet)

LanguageReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LanguageReferenceSet'), LanguageReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7948, 4))
Namespace.addCategoryObject('elementBinding', LanguageReferenceSet.name().localName(), LanguageReferenceSet)

QuerySpecificationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QuerySpecificationReferenceSet'), QuerySpecificationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7970, 4))
Namespace.addCategoryObject('elementBinding', QuerySpecificationReferenceSet.name().localName(), QuerySpecificationReferenceSet)

AnnotationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AnnotationReferenceSet'), AnnotationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7993, 4))
Namespace.addCategoryObject('elementBinding', AnnotationReferenceSet.name().localName(), AnnotationReferenceSet)

AssociationReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssociationReferenceSet'), AssociationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8015, 4))
Namespace.addCategoryObject('elementBinding', AssociationReferenceSet.name().localName(), AssociationReferenceSet)

ModuleDepencencyReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModuleDepencencyReferenceSet'), ModuleDepencencyReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8040, 4))
Namespace.addCategoryObject('elementBinding', ModuleDepencencyReferenceSet.name().localName(), ModuleDepencencyReferenceSet)

DescriptionFormatReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DescriptionFormatReferenceSet'), DescriptionFormatReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8063, 4))
Namespace.addCategoryObject('elementBinding', DescriptionFormatReferenceSet.name().localName(), DescriptionFormatReferenceSet)

ChangeSetReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChangeSetReferenceSet'), ChangeSetReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8090, 4))
Namespace.addCategoryObject('elementBinding', ChangeSetReferenceSet.name().localName(), ChangeSetReferenceSet)

ChangeSetDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChangeSetDetails'), ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8101, 4))
Namespace.addCategoryObject('elementBinding', ChangeSetDetails.name().localName(), ChangeSetDetails)



SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sctid'), SCTID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 55, 12)))

SCTIDorUUID._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uuid'), UUID, scope=SCTIDorUUID, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 56, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sctid')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 55, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SCTIDorUUID._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uuid')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 56, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SCTIDorUUID._Automaton = _BuildAutomaton()




Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), SCTID, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), Time, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'active'), Boolean, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), SCTID, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'changeset'), UUID, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12)))

Base._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locked'), Boolean, scope=Base, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeset')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Base._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locked')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Base._Automaton = _BuildAutomaton_()




Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'identifierSchemeId'), Identifier_scheme, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7716, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alternateIdentifier'), String, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7717, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), Time, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7718, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'active'), Boolean, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7719, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), Module, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7720, 12)))

Identifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referenceComponentId'), SCTID, scope=Identifier_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7721, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'identifierSchemeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7716, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alternateIdentifier')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7717, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7718, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7719, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7720, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Identifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referenceComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7721, 12))
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




TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7740, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'supertypeId'), SCTID, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7741, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), Time, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7742, 12)))

TransitiveClosureHistory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'active'), Boolean, scope=TransitiveClosureHistory_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7743, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subtypeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7740, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'supertypeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7741, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7742, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7743, 12))
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




RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), UUID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime'), Time, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'active'), Boolean, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleId'), SCTID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'refsetId'), SCTID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12)))

RefsetBase._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId'), SCTIDorUUID, scope=RefsetBase, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RefsetBase._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
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




Concept_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitionStatusId'), Definition_status, scope=Concept_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7640, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeset')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locked')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Concept_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definitionStatusId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7640, 20))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Concept_._Automaton = _BuildAutomaton_5()




Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conceptId'), SCTID, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7663, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'languageCode'), String, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7664, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typeId'), Description_type, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7665, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'term'), String, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7666, 20)))

Description_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseSignificanceId'), Case_significance, scope=Description_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7667, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeset')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locked')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conceptId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7663, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'languageCode')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7664, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'typeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7665, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'term')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7666, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Description_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseSignificanceId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7667, 20))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
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
Description_._Automaton = _BuildAutomaton_6()




Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7690, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'destinationId'), SCTID, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7691, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relationshipGroup'), Integer, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7692, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typeId'), Linkage_concept, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7693, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'characteristicTypeId'), Characteristic_type, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7694, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modifierId'), Modifier, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7695, 20)))

Relationship_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isCanonical'), Boolean, scope=Relationship_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7696, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7624, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7625, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7626, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7628, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeset')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7629, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locked')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7630, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7690, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'destinationId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7691, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relationshipGroup')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7692, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'typeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7693, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'characteristicTypeId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7694, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modifierId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7695, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Relationship_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isCanonical')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7696, 20))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Relationship_._Automaton = _BuildAutomaton_7()




DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeDescription'), Reference_set_attribute, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7788, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeType'), Attribute_type, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7789, 20)))

DescriptorReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'attributeOrder'), STD_ANON, scope=DescriptorReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7790, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeDescription')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7788, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeType')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7789, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'attributeOrder')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7790, 20))
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
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
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




OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'order'), STD_ANON_, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7837, 20)))

OrderedReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'linkedTo'), SCTID, scope=OrderedReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7844, 20)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7844, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'order')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7837, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'linkedTo')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7844, 20))
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




AttributeValueReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valueId'), Attribute_value, scope=AttributeValueReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7867, 20)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valueId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7867, 20))
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




SimpleMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapTarget'), String, scope=SimpleMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7890, 20)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapTarget')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7890, 20))
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




ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapGroup'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7913, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapPriority'), Integer, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7914, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapRule'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7915, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapAdvice'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7916, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapTarget'), String, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7917, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'correlationId'), SNOMED_CT_source_code_to_target_map_code_correlation_value, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7918, 20)))

ComplexMapReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mapCategoryId'), ICD_10_map_category_value, scope=ComplexMapReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7919, 20)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7915, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7916, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7917, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7918, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7919, 20))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapGroup')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7913, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapPriority')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7914, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapRule')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7915, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapAdvice')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7916, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapTarget')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7917, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'correlationId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7918, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mapCategoryId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7919, 20))
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




LanguageReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptabilityId'), Acceptability, scope=LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7941, 20)))

LanguageReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conceptId'), SCTID, scope=LanguageReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7943, 20)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7943, 20))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptabilityId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7941, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conceptId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7943, 20))
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




QuerySpecificationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'query'), String, scope=QuerySpecificationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7965, 20)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'query')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7965, 20))
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




AnnotationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annotation'), String, scope=AnnotationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7988, 20)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annotation')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7988, 20))
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




AssociationReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'targetComponent'), SCTID, scope=AssociationReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8010, 20)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'targetComponent')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8010, 20))
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




ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sourceEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8033, 20)))

ModuleDependencyReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'targetEffectiveTime'), Time, scope=ModuleDependencyReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8034, 20)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sourceEffectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8033, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ModuleDependencyReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'targetEffectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8034, 20))
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




DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptionFormat'), Description_format, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8057, 20)))

DescriptionFormatReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descriptionLength'), Integer, scope=DescriptionFormatReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8058, 20)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptionFormat')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8057, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descriptionLength')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8058, 20))
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




ChangeSetReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), String, scope=ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8081, 20)))

ChangeSetReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'owner'), String, scope=ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20)))

ChangeSetReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'changeDescription'), String, scope=ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20)))

ChangeSetReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'isFinal'), Boolean, scope=ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8084, 20)))

ChangeSetReferenceSetEntry_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inRelease'), Time, scope=ChangeSetReferenceSetEntry_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8081, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeDescription')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isFinal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8084, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSetEntry_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inRelease')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20))
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChangeSetReferenceSetEntry_._Automaton = _BuildAutomaton_20()




ConceptList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Concept_, scope=ConceptList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7651, 20)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7651, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConceptList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7651, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConceptList_._Automaton = _BuildAutomaton_21()




DescriptionList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Description_, scope=DescriptionList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7679, 20)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7679, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7679, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptionList_._Automaton = _BuildAutomaton_22()




RelationshipList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Relationship_, scope=RelationshipList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7707, 20)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7707, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RelationshipList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7707, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelationshipList_._Automaton = _BuildAutomaton_23()




IdentifierList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), Identifier_, scope=IdentifierList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7730, 20)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7730, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentifierList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7730, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentifierList_._Automaton = _BuildAutomaton_24()




TransitiveClosureHistoryList_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), TransitiveClosureHistory_, scope=TransitiveClosureHistoryList_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7753, 20)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7753, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TransitiveClosureHistoryList_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7753, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TransitiveClosureHistoryList_._Automaton = _BuildAutomaton_25()




DescriptorReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), DescriptorReferenceSetEntry_, scope=DescriptorReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7807, 20)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7807, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptorReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7807, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptorReferenceSet_._Automaton = _BuildAutomaton_26()




SimpleReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), SimpleReferenceSetEntry_, scope=SimpleReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7826, 20)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7826, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7826, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleReferenceSet_._Automaton = _BuildAutomaton_27()




OrderedReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), OrderedReferenceSetEntry_, scope=OrderedReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7855, 20)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7855, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OrderedReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7855, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OrderedReferenceSet_._Automaton = _BuildAutomaton_28()




AttributeValueReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), AttributeValueReferenceSetEntry_, scope=AttributeValueReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7877, 20)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7877, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttributeValueReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7877, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AttributeValueReferenceSet_._Automaton = _BuildAutomaton_29()




SimpleMapReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), SimpleMapReferenceSetEntry_, scope=SimpleMapReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7901, 20)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7901, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SimpleMapReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7901, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SimpleMapReferenceSet_._Automaton = _BuildAutomaton_30()




ComplexMapReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), ComplexMapReferenceSetEntry_, scope=ComplexMapReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7929, 20)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7929, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ComplexMapReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7929, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ComplexMapReferenceSet_._Automaton = _BuildAutomaton_31()




LanguageReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), LanguageReferenceSetEntry_, scope=LanguageReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7953, 20)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7953, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LanguageReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7953, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LanguageReferenceSet_._Automaton = _BuildAutomaton_32()




QuerySpecificationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), QuerySpecificationReferenceSetEntry_, scope=QuerySpecificationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7975, 20)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7975, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(QuerySpecificationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7975, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
QuerySpecificationReferenceSet_._Automaton = _BuildAutomaton_33()




AnnotationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), AnnotationReferenceSetEntry_, scope=AnnotationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7998, 20)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7998, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnnotationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7998, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnnotationReferenceSet_._Automaton = _BuildAutomaton_34()




AssociationReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), AssociationReferenceSetEntry_, scope=AssociationReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8020, 20)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8020, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AssociationReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8020, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AssociationReferenceSet_._Automaton = _BuildAutomaton_35()




ModuleDepencencyReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), ModuleDependencyReferenceSetEntry_, scope=ModuleDepencencyReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8045, 20)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8045, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModuleDepencencyReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8045, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ModuleDepencencyReferenceSet_._Automaton = _BuildAutomaton_36()




DescriptionFormatReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), DescriptionFormatReferenceSetEntry_, scope=DescriptionFormatReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8068, 20)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8068, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DescriptionFormatReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8068, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DescriptionFormatReferenceSet_._Automaton = _BuildAutomaton_37()




ChangeSetReferenceSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), ChangeSetReferenceSetEntry_, scope=ChangeSetReferenceSet_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8095, 20)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8095, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetReferenceSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8095, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ChangeSetReferenceSet_._Automaton = _BuildAutomaton_38()




ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'concept'), Concept_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8106, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), Description_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8107, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relationship'), Relationship_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8108, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'statedRelationship'), Relationship_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8109, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definition'), Description_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8110, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'language'), LanguageReferenceSetEntry_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8111, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'simplerefset'), SimpleReferenceSetEntry_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8112, 20)))

ChangeSetDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'moduleDependency'), ModuleDependencyReferenceSetEntry_, scope=ChangeSetDetails_, location=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8113, 20)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8106, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8107, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8108, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8109, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8110, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8111, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8112, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8113, 20))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7765, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'effectiveTime')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7766, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'active')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7767, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7769, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'refsetId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7771, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencedComponentId')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 7772, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8081, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'owner')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8082, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'changeDescription')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8083, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'isFinal')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8084, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inRelease')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8085, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'concept')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8106, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8107, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relationship')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8108, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'statedRelationship')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8109, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'definition')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8110, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'language')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8111, 20))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'simplerefset')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8112, 20))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ChangeSetDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'moduleDependency')), pyxb.utils.utility.Location('/Users/mrf7578/Development/git/CTS2/rf2service/static/xsd/rf2.xsd', 8113, 20))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
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
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ChangeSetDetails_._Automaton = _BuildAutomaton_39()

