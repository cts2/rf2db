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
from rf2db.utils.SCTID import SCTID


# This source contains the various metadata constants that are used in the construction
# of the SNOMED CT model.  It also carries the maps from module identifiers to Edition
# and Extension identifiers

# The root concept for all things SNOMED CT
sctRoot         = SCTID(138875005)

# The root concept for all predicates
linkage_concept = SCTID(106237007)

# sct_concept.definitionStatusId
primitive = SCTID(900000000000074008)
defined   = SCTID(900000000000073002)


# sct_description.typeId
definition = SCTID(900000000000550004)
fsn        = SCTID(900000000000003001)
synonym    = SCTID(900000000000013009)


# sct_language.acceptabilityId
preferred  = SCTID(900000000000548007)
acceptable = SCTID(900000000000549004)

# sct_language.refsetId
us_english = SCTID(900000000000509007)
gb_english = SCTID(900000000000508004)
spanish    = SCTID(450828004)

# sct_relationship.characteristicTypeId
some       = SCTID(900000000000451002)
all_       = SCTID(900000000000452009)

# sct subsumption relationship
is_a       = SCTID(116680003)

# Root of all modules
module     = SCTID(900000000000443000)

# Extension identifiers - there is no SNOMED CT concept code for these
snomedCTInternational   = SCTID(900000000000207008)
snomedCTSpanishEdition  = SCTID(450829007)
snomedCTUSExtension     = SCTID(731000124108)

# Descendants of the model component module (900000000000443000)

snomedCTtoICD9CMequivalencyMappingModule    = SCTID(449079008)
snomedCTtoICD10ruleBasedmappingModule       = SCTID(449080006)
ihtsdoMaintainedModule                      = SCTID(900000000000445007)
snomedCTSpanishEditionModule                = SCTID(449081005)
moduloDeLaExtensionDeLaLenguaCastellanaParaLatinoameric = SCTID(450829007)
usNationalLibraryOfMedicineMaintainedModule = SCTID(731000124108)
snomedCTcore                                = SCTID(900000000000207008)
snomedCTtoICD10CMruleBasedMappingModule     =  SCTID(5991000124107)
snomedCTmodelComponent                      = SCTID(900000000000012004)

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
characteristicType      = SCTID(900000000000449001)
definingRelationship    = SCTID(900000000000412007)   # (superclass - not actually used)
inferredRelationship    = SCTID(900000000000011006)   # in relationships file
statedRelationship      = SCTID(900000000000010007)   # in stated relationships file
additionalRelationship  = SCTID(900000000000412007)   # (No examples)
qualifyingRelationship  = SCTID(900000000000409009)   # in relationships file