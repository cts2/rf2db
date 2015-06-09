# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
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

from rf2db.utils.sctid_generator import sctid_generator


class DecodedNamespace():
    def __init__(self, sctid):
        sctid = int(sctid)
        self.checkdigit = sctid % 10
        self.partition = (sctid // 10) % 100
        if self.partition // 10:
            self.namespace = (sctid // 1000) % 10000000
            self.item = (sctid // 10000000000)
        else:
            self.namespace = 0
            self.item = sctid // 1000

class RF2Namespace():
    activeNamespaces = {}
    def __init__(self, namespace):
        self._namespace = int(namespace)
        if self._namespace not in self.activeNamespaces:
            self.activeNamespaces[self._namespace] = IDGenerator(self._namespace)

    def nextConceptId(self):
        return self.activeNamespaces[self._namespace].next(sctid_generator.CONCEPT)

    def nextRelationshipId(self):
        return self.activeNamespaces[self._namespace].next(sctid_generator.RELATIONSHIP)

    def nextDescriptionId(self):
        return self.activeNamespaces[self._namespace].next(sctid_generator.DESCRIPTION)



class IDGenerator():
    def __init__(self, namespace):
        from rf2db.db.RF2ConceptFile import ConceptDB
        from rf2db.db.RF2DescriptionFile import DescriptionDB
        from rf2db.db.RF2RelationshipFile import RelationshipDB
        self._generators = {partition : self._generator(int(namespace), partition, db)
                            for partition, db in ((sctid_generator.CONCEPT, ConceptDB),
                                                  (sctid_generator.DESCRIPTION, DescriptionDB),
                                                  (sctid_generator.RELATIONSHIP, RelationshipDB),)
        }



    def _generator(self, namespace, partition, db):
        item = db().getMaxId(namespace).item
        return sctid_generator(namespace, partition, item+1)

    def next(self, partition):
        return next(self._generators[partition])
