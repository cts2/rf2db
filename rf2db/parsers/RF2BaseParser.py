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

""" Convert RF2 Tab seperated values into the equivalent XML format
"""
import sys
from rf2db.schema import rf2

from rf2db.constants import RF2ValueSets
from rf2db.utils.sctid import sctid
from rf2db.utils import xmlutils
from rf2db.utils.link import rf2link

#from dateutil.parser import parse
#self.effectiveTimeISO = parse(flds[1]).isoformat()


class RF2Base(rf2.Base, object):
    _baseFields = ['id', 'effectiveTime', 'active', 'moduleId']
    _sctidFieldNames = ['moduleId']
    _fieldNames = _baseFields
    _sctidFields = _sctidFieldNames
    _nFields = len(_fieldNames)
    _baseClass = rf2.Base


    def load(self, name, line, sep="\t"):
        fields = line.strip().split(sep)
        nFields = len(fields)
        self._name = name
        self.valid = nFields == self._nFields
        if nFields < self._nFields:
            fields += [None] * (self._nFields - nFields)
        self._baseClass.__init__(self, **dict(zip(self._fieldNames, fields)))
        self._changeset, self._locked = fields[len(self._fieldNames):len(self._fieldNames)+2] \
            if len(fields) > len(self._fieldNames) else (None, 0)
        return self

    def __str__(self):
        return self._name + "(" + \
               ', '.join(k + ":" + self.strify(k) for k in self._fieldNames) + ")"

    def __repr__(self):
        return '\t'.join(self.strify(k) for k in self._fieldNames)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.__str__().__hash__()

    def strify(self, key):
        v = getattr(self, key)
        return bytearray.decode(v) if isinstance(v, bytearray) else str(v)

    def issctid(self, key):
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


@rf2link(rf2.Concept, rf2.Concept_, ['definitionStatusId'], ['id', 'definitionStatusId'])
class RF2Concept(rf2.Concept_, RF2Base):
    @property
    def isPrimitive(self):
        return self.definitionStatusId == RF2ValueSets.primitive

    @property
    def isFullyDefined(self):
        return self.definitionStatusId == RF2ValueSets.defined


@rf2link(rf2.Description, rf2.Description_, ['conceptId', 'languageCode', 'typeId', 'term', 'caseSignificanceId'],
         ['conceptId', 'typeId', 'caseSignificanceId'], linefilter=xmlutils.cleanxml)
class RF2Description(rf2.Description_, RF2Base):
    def strify(self, key):
        if sys.version_info.major < 3:
            return getattr(self, key).encode('utf-8') if key == 'term' else RF2Base.strify(self, key)
        else:
            return RF2Base.strify(self, key)

    @property
    def isDefinition(self):
        return self.typeId == RF2ValueSets.definition

    @property
    def isFsn(self):
        return self.typeId == RF2ValueSets.fsn

    @property
    def isSynonym(self):
        return self.typeId == RF2ValueSets.synonym


@rf2link(rf2.Relationship, rf2.Relationship_, ['sourceId', 'destinationId', 'relationshipGroup',
                                               'typeId', 'characteristicTypeId', 'modifierId', 'isCanonical'],
         ['sourceId', 'destinationId', 'typeId', 'characteristicTypeId', 'modifierId'])
class RF2Relationship(rf2.Relationship_, RF2Base):
    @property
    def isAll(self):
        return self.modifierId == RF2ValueSets.all_

    @property
    def isSome(self):
        return self.modifierId == RF2ValueSets.some

    @property
    def isDefining(self):
        return sctid(self.characteristicTypeId) in [RF2ValueSets.definingRelationship,
                                                    RF2ValueSets.inferredRelationship, #inferredRelationship
                                                    RF2ValueSets.statedRelationship] #statedRelationship

    @property
    def isInferred(self):
        return sctid(self.characteristicTypeId) == RF2ValueSets.inferredRelationship

    @property
    def isAdditional(self):
        return sctid(self.characteristicTypeId) == RF2ValueSets.additionalRelationship

    @property
    def isQualifying(self):
        return sctid(self.characteristicTypeId) == RF2ValueSets.qualifyingRelationship


@rf2link(rf2.Identifier, rf2.Identifier_,
         ['identifierSchemeId', 'alternativeIdentifier', 'effectiveTime', 'moduleId', 'referenceComponentId'])
class RF2Identifier(rf2.Identifier_, RF2Base):
    pass


@rf2link(rf2.TransitiveClosureHistory, rf2.TransitiveClosureHistory_,
         ['typeId', 'supertypeId', 'effectiveTime', 'active'], ['typeId', 'supertypeId'])
class _RF2TransitiveClosureHistory(rf2.TransitiveClosureHistory_, RF2Base):
    pass

