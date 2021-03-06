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

import xml.parsers.expat
import pyxb, re
from pprint import pprint as pp
from pyxb.utils import domutils

from rf2db.schema import rf2

defaultNS = rf2.Namespace

def prettyxml(pyxb_xml,validate=True, ns=None, xslt=None, toXML=True):
    """ Pretty printer for pyxb object. This differs from the standard minidom's
        toprettyxml because it doesn't touch anything inside a i{value} tag.
        
        @param pyxb_xml: The pyxb node to format
        
        @param validate: Validate when generating flag. 
        @type validate: C{bool}
        
        @param ns: base namespace to use for encoding
        @param xslt: name of xslt module to include in header
        @param toXML: if True, convert to XML otherwise already is in XML
    """
    pyxb.defaultNamespace = ns
    domutils.BindingDOMSupport.SetDefaultNamespace(ns if ns else defaultNS)
    pyxb.RequireValidWhenGenerating(True)
    return prettyxml_(pyxb_xml.toxml(encoding='utf-8') if toXML else pyxb_xml, xslt)

def prettyxml_(rawxml, xslt=None):
    
    def indent(depth, prev):
        return ('\n' + (' ' * 4 * depth)) if prev != 'd' else ""
        
    def args(alist):
        if len(alist):
            return ' ' + ' '.join([k+'="'+v+'"' for (k,v) in alist.items()])
        return ''

    seq = []            
    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler  = lambda name, attrs: seq.append( ('s', name, attrs))
    p.EndElementHandler    = lambda name:        seq.append( ('e', name ))
    p.CharacterDataHandler = lambda data:        seq.append( ('d', data ))
    p.Parse(rawxml,1)

    depth, prev, rval = (0, '', '<?xml version="1.0" encoding="UTF-8"?>' + (xslt if xslt else ""))
    while len(seq):
        e = seq.pop(0)
        if e[0] == 's':
            # shortcut the simple start end tag
            if seq[0][0] == 'e':
                assert e[1] == seq[0][1]
                seq.pop(0)
                rval += indent(depth, prev)
                rval += '<' + e[1] + args(e[2]) + '/>'
                depth -= 1
            else:
                if prev == 's': depth += 1
                rval += indent(depth, prev)
                rval += '<' + e[1] + args(e[2]) + '>'
        elif e[0] == 'e':
            if prev != 'd': depth -= 1
            rval += indent(depth, prev)
            rval += '</' + e[1] + '>'
        else:
            if prev != 'e' or e[0] != 'd' or e[1] != '\n':
                rval += e[1]
        if prev != 'e' or e[0] != 'd' or e[1] != '\n':
            prev = e[0]
    return rval 

def cleanxml(txt):
    if txt:
        return uncleanxml(txt).replace('&','&amp;').replace('<', '&lt;')
    return None

def uncleanxml(txt):
    if txt:
        return txt.replace('&amp;','&').replace('&lt;', '<')

testParms = {"version":"20130731", "serviceURI":"http://localhost:8080/cts2/"}
def testxml(resource, testxml=None, testfile=None, save=False, printdiff=True):
    """ Compare the XML in resource to the supplied string or file
    @param resource - a resource or xml text to test
    @param testxml - xml text to test against
    @param testfile - file name containing xml text
    @param save - if true, write the xml for resource into testfile
    @param printdiff - if true, print out any differences
    @return whether resource and testxml/textfile are the same or not
    """
    assert (testxml or testfile) and not(testxml and testfile)
    if save and testfile:
        open(testfile,'w').write(prettyxml(resource))
        print("SAVED: " + testfile)
        rval = True
    else:
        if not testxml: testxml = open(testfile).read()
        rval = diffxml(resource.toxml() if hasattr(resource, 'toxml') else resource, testxml % testParms, printdiff=printdiff)
    return rval

def diffxml(xml1, xml2, printdiff=True):
    """ XML difference operation.  Compare the contents of two XML strings, ignoring namespaces """

    dateFields = ['accessDate']

    # Fill date fields with dummy values
    def fixDate(seq):
        rval = []
        indate = False
        for e in seq:
            if e[0] == 'd' and indate:
                rval.append( ('d', '2012-04-16T11:03:54Z'))
            else:
                rval.append(e)
            indate = e[0] == 's' and e[1] in dateFields
        return rval


    # White space between elements is tossed
    def tossSpace(seq):
        rval = []
        dbuff = ""
        for e in seq:
            if e[0] == 'd':
                dbuff += e[1]
            else:
                if re.search('\S',dbuff):
                    rval.append( ('d',dbuff.rstrip()))
                dbuff = ""
                rval.append(e)
        return rval

    def cmpElement(e1, e2):
        """
        @param e1: First XML parsed entry (type, key, attributes)
        @param e2: Second XML parsed entry
        @return: True if they match, False otherwise
        """
        # Identical
        if e1 == e2:
            return True

        # Identical type and element - attribute difference
        if e1[0] == e2[0] and e1[1] == e2[1]:
            if e1[2].keys() == e2[2].keys():
                e1attrib = e1[2].copy()
                e2attrib = e2[2].copy()
                if 'href' in e1attrib:
                    e1href = e1attrib.pop('href')
                    e2href = e2attrib.pop('href')
                    if not e1href.endswith(e2href):
                        return False
                if 'assertedInCodeSystemVersion' in e1attrib:
                    e1acsv = e1attrib.pop('assertedInCodeSystemVersion')
                    e2acsv = e2attrib.pop('assertedInCodeSystemVersion')
                    if e1acsv != e2acsv and not ('{v}' in e2acsv or e2acsv.split('{v}')[0] != e1acsv):
                        return False

                if e1[1] in ['version','core:version']:
                    e1v = e1attrib.pop('uri').rsplit('/',1)[0]
                    e2v = e2attrib.pop('uri').rsplit('/',1)[0]
                    if e1v != e2v:
                        return False
                return e1attrib == e2attrib
        if e1[0] == e2[0] and e1[0] == 'd' and '{v}' in e2[1]:
            return e1[1].startswith(e2[1].split('{v}')[0])

        return False

    def handler(seq):
        # We're not overly clever at the moment and simply ignore namespaces
        def nsmap(ename):
            return ename.split(':')[1] if ':' in ename else ename

        # ... and namespace declarations
        def attmap(attrs):
            rval = {}
            for (k,v) in attrs.items():
                if not k.startswith('xmlns'):
                    rval[k] = v
            return rval

        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler  = lambda name, attrs: seq.append( ('s', nsmap(name), attmap(attrs)))
        p.EndElementHandler    = lambda name:        seq.append( ('e', nsmap(name) ) )
        p.CharacterDataHandler = lambda data:        seq.append( ('d', data) )
        return p


    seq1, seq2 = [],[]

    handler(seq1).Parse(xml1,1)
    handler(seq2).Parse(xml2,1)

    seq1 = fixDate(tossSpace(seq1))
    seq2 = fixDate(tossSpace(seq2))

    rval = all([cmpElement(e1, e2) for (e1, e2) in zip(seq1, seq2)])
    if not rval and printdiff:
        while cmpElement(seq1[0], seq2[0]):
            seq1.pop(0), seq2.pop(0)
        print
        print("===== MISMATCH =====")
        print("Source: ")
        pp(seq1.pop(0))
        print("Target: ")
        pp(seq2.pop(0))
    return rval

