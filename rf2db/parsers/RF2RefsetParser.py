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

""" RF2 Reference Set parser module
"""
from rf2db.schema import rf2

from rf2db.constants import RF2ValueSets
from rf2db.utils.sctid import sctid
from rf2db.utils.link import rf2link

#from dateutil.parser import parse
#self.effectiveTimeISO = parse(flds[1]).isoformat()


# ==================
#  Reference Sets
# ==================
class RF2RefsetBase(rf2.RefsetBase, object):
    _baseFields  = ['id', 'effectiveTime', 'active', 'moduleId', 'refsetId', 'referencedComponentId']
    _sctidFieldNames = ['moduleId', 'refsetId',
                        'referencedComponentId']  # be aware that referencedComponentId isn't always a concept id
    _rcididx     = len(_baseFields) - 1
    _fieldNames  = _baseFields
    _sctidFields = _sctidFieldNames
    _nFields     = len(_fieldNames)
    _baseClass   = rf2.RefsetBase
    
    def load(self, name, line, sep="\t"):
        fields = line.strip().split(sep)
        nFields = len(fields)
        self._name = name
        self.valid = nFields == self._nFields
        if nFields < self._nFields:
            fields += [None] * (self._nFields - nFields)
        e = fields[self._rcididx]
        if e:
            fields[self._rcididx] = rf2.SCTIDorUUID(uuid=e) if '-' in e else rf2.SCTIDorUUID(sctid=e)
        vals = filter(lambda f: f[1], zip(self._fieldNames, fields))
        self._baseClass.__init__(self, **dict(self._dropNulls(vals)) )
        self._changeset, self._locked = fields[len(self._fieldNames):len(self._fieldNames)+2] \
            if len(fields) > len(self._fieldNames) else (None, 0)
        return self
                    
    def __str__(self):
        return self._name + "(" + \
               ', '.join(k + ":" + self.strify(k) for k in self._fieldNames) + ")"

    def _dropNulls(self, vals):
        return [v for v in vals if v[0] not in self._sctidFields or v[1] != 'None']

    def __repr__(self):
        return '\t'.join(self.strify(k) for k in self._fieldNames)
                
    def strify(self, key):
        val = getattr(self, key)
        if key == 'referencedComponentId':
            val = val.uuid if val.uuid else val.sctid
        return str(val)

    def issctid(self,key):
        return key in self._sctidFields

    def isActive(self):
        return self.active == 1

    @property
    def locked(self):
        return bool(self._locked)

    @property
    def changeset(self):
        return self._changeset

    @classmethod
    def validateHeader(cls, headerfields):
        return cls._fieldNames == headerfields


@rf2link(rf2.LanguageReferenceSetEntry, rf2.LanguageReferenceSetEntry_, ['acceptabilityId', 'conceptId'],
         ['acceptabilityId', 'conceptId'])
class RF2LanguageRefsetEntry(rf2.LanguageReferenceSetEntry_, RF2RefsetBase):

    @property
    def isPreferred(self):
        return sctid(self.acceptabilityId) == RF2ValueSets.preferred
        
    @property
    def isSynonym(self):
        return sctid(self.acceptabilityId) == RF2ValueSets.acceptable



@rf2link(rf2.DescriptorReferenceSetEntry, rf2.DescriptorReferenceSetEntry_,
         ['attributeDescription', 'attributeType', 'attributeOrder'])
class RF2DescriptorReferenceSetEntry(rf2.DescriptorReferenceSetEntry_, RF2RefsetBase):
    pass
        

@rf2link(rf2.SimpleReferenceSetEntry, rf2.SimpleReferenceSetEntry_)
class RF2SimpleReferenceSetEntry(rf2.SimpleReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.OrderedReferenceSetEntry, rf2.OrderedReferenceSetEntry_, ['order', 'linkedTo'])
class RF2OrderedReferenceSetEntry(rf2.OrderedReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.AttributeValueReferenceSetEntry, rf2.AttributeValueReferenceSetEntry_, ['valueId'])
class RF2AttributeValueReferenceSetEntry(rf2.AttributeValueReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.SimpleMapReferenceSetEntry, rf2.SimpleMapReferenceSetEntry_, ['mapTarget'])
class RF2SimpleMapReferenceSetEntry(rf2.SimpleMapReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.ComplexMapReferenceSetEntry, rf2.ComplexMapReferenceSetEntry_,
         ['mapGroup', 'mapPriority', 'mapRule', 'mapAdvice', 'mapTarget', 'correlationId', 'mapCategoryId'],
         ['correlationId', 'mapCategoryId'])
class RF2ComplexMapReferenceSetEntry(rf2.ComplexMapReferenceSetEntry_, RF2RefsetBase):
    pass

             
@rf2link(rf2.QuerySpecificationReferenceSetEntry, rf2.QuerySpecificationReferenceSetEntry_,['query'])
class RF2QuerySpecificationReferenceSetEntry(rf2.QuerySpecificationReferenceSetEntry_, RF2RefsetBase):
    pass

        
@rf2link(rf2.AnnotationReferenceSetEntry, rf2.AnnotationReferenceSetEntry_, ['annotation'])
class RF2AnnotationReferenceSetEntry(rf2.AnnotationReferenceSetEntry_, RF2RefsetBase):
    pass


@rf2link(rf2.AssociationReferenceSetEntry, rf2.AssociationReferenceSetEntry_, ['targetComponent'])
class RF2AssociationReferenceSetEntry(rf2.AssociationReferenceSetEntry_, RF2RefsetBase):
    pass


@rf2link(rf2.ModuleDependencyReferenceSetEntry, rf2.ModuleDependencyReferenceSetEntry_,
         ['sourceEffectiveTime', 'targetEffectiveTime'])
class RF2ModuleDependencyReferenceSetEntry(rf2.ModuleDependencyReferenceSetEntry_, RF2RefsetBase):
    pass

        
@rf2link(rf2.DescriptionFormatReferenceSetEntry, rf2.DescriptionFormatReferenceSetEntry_,
         ['descriptionFormat', 'descriptionLength'])
class RF2DescriptionFormatReferenceSetEntry(rf2.DescriptionFormatReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.ChangeSetReferenceSetEntry, rf2.ChangeSetReferenceSetEntry_,
        ['name', 'owner', 'changeDescription', 'isFinal', 'inRelease'])
class RF2ChangeSetReferenceSetEntry(rf2.ChangeSetReferenceSetEntry_, RF2RefsetBase):
    pass

@rf2link(rf2.ChangeSetDetails, rf2.ChangeSetDetails_,
         ['name', 'owner', 'changeDescription', 'isFinal', 'inRelease'])
class RF2ChangeSetDetails(rf2.ChangeSetDetails_, RF2RefsetBase):
    pass