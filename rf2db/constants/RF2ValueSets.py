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
from rf2db.utils.sctid import sctid


# This source contains the various metadata constants that are used in the construction
# of the SNOMED CT model.  It also carries the maps from module identifiers to Edition
# and Extension identifiers

# The root concept for all things SNOMED CT
sctRoot = sctid(138875005)

# The root concept for all predicates
linkage_concept = sctid(106237007)

# sct_concept.definitionStatusId
primitive = sctid(900000000000074008)
defined = sctid(900000000000073002)


# sct_description.typeId
definition = sctid(900000000000550004)
fsn = sctid(900000000000003001)
synonym = sctid(900000000000013009)

# sct_description.caseSignificanceId
insensitive = 900000000000448009
sensitive = 900000000000017005
initialChar = 900000000000020002

# sct_language.acceptabilityId
preferred = sctid(900000000000548007)
acceptable = sctid(900000000000549004)

# sct_language.refsetId
us_english = sctid(900000000000509007)
gb_english = sctid(900000000000508004)
spanish = sctid(450828004)

# sct_relationship.characteristicTypeId
some = sctid(900000000000451002)
all_ = sctid(900000000000452009)

# sct subsumption relationship
is_a = sctid(116680003)

# Root of all modules
module = sctid(900000000000443000)

# Module dependency refset
moduleDependencyRefset = sctid(900000000000534007)

# Extension identifiers - there is no SNOMED CT concept code for these
snomedCTInternational = sctid(900000000000207008)
snomedCTSpanishEdition = sctid(450829007)
snomedCTUSExtension = sctid(731000124108)

# Parent of simple type reference sets
simpleReferenceSetRoot = sctid(446609009)

# Simple map refsets from SCT International
icdoSimpleMap = sctid(446608001)
ctv3simplemap = sctid(900000000000497000)
snomedrtSimpleMap = sctid(900000000000498005)

# Descendants of the model component module (900000000000443000)
snomedCTtoICD9CMequivalencyMappingModule = sctid(449079008)
snomedCTtoICD10ruleBasedmappingModule = sctid(449080006)
ihtsdoMaintainedModule = sctid(900000000000445007)
snomedCTSpanishEditionModule = sctid(449081005)
moduloDeLaExtensionDeLaLenguaCastellanaParaLatinoameric = sctid(450829007)
usNationalLibraryOfMedicineMaintainedModule = sctid(731000124108)
snomedCTcore = sctid(900000000000207008)
snomedCTtoICD10CMruleBasedMappingModule = sctid(5991000124107)
snomedCTmodelComponent = sctid(900000000000012004)
cimiModule = sctid(11000160102)
mayoModule = sctid(11000134103)

# Reference set for change sets
changeSetRefSet = sctid(21000160106)

# Map from module to extension identifier
moduleToExtensionMap = {
    snomedCTtoICD9CMequivalencyMappingModule:               snomedCTInternational,
    ihtsdoMaintainedModule:                                 snomedCTInternational,
    snomedCTSpanishEditionModule:                           snomedCTSpanishEdition,
    moduloDeLaExtensionDeLaLenguaCastellanaParaLatinoameric:snomedCTSpanishEdition,
    usNationalLibraryOfMedicineMaintainedModule:            snomedCTUSExtension,
    snomedCTcore:                                           snomedCTInternational,
    snomedCTtoICD10CMruleBasedMappingModule:                snomedCTInternational,
    snomedCTmodelComponent:                                 snomedCTInternational}


# relationship characteristic type
characteristicType = sctid(900000000000449001)
definingRelationship = sctid(900000000000006009)   # (superclass - not actually used)
inferredRelationship = sctid(900000000000011006)   # in relationships file
statedRelationship = sctid(900000000000010007)   # in stated relationships file
additionalRelationship = sctid(900000000000227009)   # (No examples)
qualifyingRelationship = sctid(900000000000225001)   # in relationships file