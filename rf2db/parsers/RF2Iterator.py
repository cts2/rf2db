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
from rf2db.schema import rf2
from rf2db.parameterparser.ParmParser import ParameterDefinitionList, enumparam, intparam, computedparam

""" Iteration Parameters

    - B{C{order}} - sort order of returned values. The specific sort keys depend on the type of resource
    accessed.  Possible values are I{asc} for ascending and I{desc} for descending.  Default: "asc"
    - B{C{maxtoreturn}} - maximum values to return in a list. 0 we're just doing a count. Default: 100
    - B{C{page}} - starting page number.  Return begins at entry C{page * maxtoreturn}.  Default: 0

"""
iter_parms = ParameterDefinitionList()
iter_parms.order = enumparam(['asc','desc'], default='asc')
iter_parms.page = intparam(default=0)
iter_parms.maxtoreturn = intparam(default=100)
iter_parms.start = computedparam(lambda p: p.page * p.maxtoreturn)

class RF2Iterator(rf2.Iterator, object):
    def setup(self, parmlist, autoSkip=False):
        """ Create a directory listing. This can be used in a number of ways, including:

        @param autoSkip: if True, append will skip the leading entries.  If false, the client does the skipping
        @type autoSkip: C{bool}

        """
        self._parmlist = parmlist
        self._skip =  parmlist.page * parmlist.maxtoreturn if autoSkip else 0
        # This is deliberately left off because it forces callers to invoke finish
        # self.complete = complete
        self.numEntries = 0
        self.at_end = False
        return self


    def append(self, entry, **kw):
        """ Append the entry to the directory.  If the skip count is positive, the entry will be skipped.  The general
        pattern that can be used in this call is:
            for e in list:
                if not rval.append(e):
                    rval.finish(True)
                    return rval
            rval.finish(False)

        @param entry: The entry to append
        @type entry: C{DirectoryEntry}

        @return: True if appending should continue, False if no more should be added
        """
        # TODO: this signature collides with one in the pyxb space.  We need to change it to something different,
        # but this will bake a fairly careful code review.  For the time being, we just pass it on if we have
        # unrecognized content
        if len(kw):
            return super(rf2.Iterator,self).append(entry, **kw)
        if self._skip > 0:
            self._skip -= 1
            return True
        if self.numEntries < self._parmlist.maxtoreturn:
            self.entry.append(entry)
            self.numEntries += 1
        self.at_end = self.numEntries >= self._parmlist.maxtoreturn
        return not self.at_end

    def finish(self, moreToCome=False, total=0):
        """ Finalize an appending process, setting COMPLETE, next and prev
            Returns the resource for convenience
        """
        if not(self._parmlist.maxtoreturn):
            self.numEntries = total
            self.complete = rf2.CompleteDirectory.COMPLETE
        else:
            if self.numEntries >= self._parmlist.maxtoreturn and moreToCome:
                self.next = "next"
                # self.next = URLUtil.forxml(URLUtil.append_params(URLUtil.strip_control_params(self.heading.resourceURI),
                #                                                            {'page':str(self._page+1), 'maxtoreturn':str(self._maxtoreturn)}))
            if self._parmlist.page > 0:
                # self.prev = URLUtil.forxml(URLUtil.append_params(URLUtil.strip_control_params(self.heading.resourceURI),
                #                                                            {'page':str(self._page-1), 'maxtoreturn':str(self._maxtoreturn)}))
                self.prev = "prev"
            self.complete = rf2.CompleteDirectory.COMPLETE if not (self.next or self.prev) else rf2.CompleteDirectory.PARTIAL
        return self


def rf2iterlink(pyxbElement, pyxbType):

    def impl_link(impl_class):
        def constructor(parmlist, autoSkip=False):
            return pyxbElement().setup(parmlist, autoSkip=autoSkip)

        pyxbType._SetSupersedingClass(impl_class)
        return constructor

    return impl_link


@rf2iterlink(rf2.ConceptList,rf2.ConceptList_)
class RF2ConceptList(rf2.ConceptList_, RF2Iterator):
    pass

@rf2iterlink(rf2.DescriptionList,rf2.DescriptionList_)
class RF2DescriptionList(rf2.DescriptionList_, RF2Iterator):
    pass

@rf2iterlink(rf2.RelationshipList,rf2.RelationshipList_)
class RF2RelationshipList(rf2.RelationshipList_, RF2Iterator):
    pass

@rf2iterlink(rf2.ConceptList,rf2.ConceptList_)
class RF2ConceptList(rf2.ConceptList_, RF2Iterator):
    pass

@rf2iterlink(rf2.IdentifierList,rf2.IdentifierList_)
class RF2IdentifierList(rf2.IdentifierList_, RF2Iterator):
    pass

@rf2iterlink(rf2.TransitiveClosureHistoryList,rf2.TransitiveClosureHistoryList_)
class RF2TransitiveClosureHistoryList(rf2.TransitiveClosureHistoryList_, RF2Iterator):
    pass

@rf2iterlink(rf2.DescriptorReferenceSet,rf2.DescriptorReferenceSet_)
class RF2DescriptorReferenceSet(rf2.DescriptorReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.OrderedReferenceSet,rf2.OrderedReferenceSet_)
class RF2OrderedReferenceSet(rf2.OrderedReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.AttributeValueReferenceSet,rf2.AttributeValueReferenceSet_)
class RF2AttributeValueReferenceSet(rf2.AttributeValueReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.SimpleMapReferenceSet,rf2.SimpleMapReferenceSet_)
class RF2SimpleMapReferenceSet(rf2.SimpleMapReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.ComplexMapReferenceSet,rf2.ComplexMapReferenceSet_)
class RF2ComplexMapReferenceSet(rf2.ComplexMapReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.LanguageReferenceSet,rf2.LanguageReferenceSet_)
class RF2LanguageReferenceSet(rf2.LanguageReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.QuerySpecificationReferenceSet,rf2.QuerySpecificationReferenceSet_)
class RF2QuerySpecificationReferenceSet(rf2.QuerySpecificationReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.AnnotationReferenceSet,rf2.AnnotationReferenceSet_)
class RF2AnnotationReferenceSet(rf2.AnnotationReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.AssociationReferenceSet,rf2.AssociationReferenceSet_)
class RF2AssociationReferenceSet(rf2.AssociationReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.ModuleDepencencyReferenceSet,rf2.ModuleDepencencyReferenceSet_)
class RF2ModuleDepencencyReferenceSet(rf2.ModuleDepencencyReferenceSet_, RF2Iterator):
    pass

@rf2iterlink(rf2.DescriptionFormatReferenceSet,rf2.DescriptionFormatReferenceSet_)
class RF2DescriptionFormatReferenceSet(rf2.DescriptionFormatReferenceSet_, RF2Iterator):
    pass