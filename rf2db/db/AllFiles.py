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
from rf2db.db import RF2ComplexMapFile, RF2ConceptFile, RF2DescriptionFile,  \
    RF2DescriptionTextFile, RF2LanguageFile, RF2ModuleDependencyFile, RF2ModuleVersionsFile, RF2PnAndFSN, \
    RF2RelationshipFile, RF2SimpleMapFile, RF2SimpleReferencesetFile, RF2StatedRelationshipFile
from rf2db.db.RF2DBConnection import RF2DBConnection

# TODO: CannonicalCore not updated
# TODO: RF2ModuleVersionsFile.ModuleVersionsDB, RF2PnAndFSN.PNandFSNDB
# TODO: RF2TransitiveChildren.TransitiveChildrenDB, RF2TransitiveChildrenCanonical.TransitiveChildrenCanonicalDB
# TODO: RF2TransitiveClosureCanonical.TransitiveClosureCanonicalDB,
allfiles = [RF2ComplexMapFile.ComplexMapDB,
            RF2ConceptFile.ConceptDB, RF2DescriptionFile.DescriptionDB,
            RF2DescriptionTextFile.DescriptionTextDB,
            RF2LanguageFile.LanguageDB, RF2ModuleDependencyFile.ModuleDependencyDB,
            RF2RelationshipFile.RelationshipDB, RF2SimpleMapFile.SimpleMapDB,
            RF2SimpleReferencesetFile.SimpleReferencesetDB, RF2StatedRelationshipFile.StatedRelationshipDB,]


def delete(filter_):
    db = RF2DBConnection()
    query = "DELETE FROM %s WHERE %s"
    rval = {}
    for f in allfiles:
        rval[f.fname()] = db.execute_query(query % (f.fname(), filter_))['affected_rows']
        db.commit(disconnect=False)
    # Have to do changeset separately to prevent import loops
    from rf2db.db.RF2ChangeSetFile import ChangeSetDB
    f = ChangeSetDB
    rval[f.fname()] = db.execute_query(query % (f.fname(), filter_))['affected_rows']
    db.commit(disconnect=False)
    return rval


def read_by_changeset(changeset):
    db = RF2DBConnection()
    query = "SELECT * FROM %s WHERE changeset = '" + str(changeset) + "'"
    rval = {}
    for f in allfiles:
        if f.hasrf2rec:
            db.execute(query % f.fname())
            fi = f()
            rval[f.table] = [fi.rf2rec(c) for c in db.ResultsGenerator(db)]
    return rval
