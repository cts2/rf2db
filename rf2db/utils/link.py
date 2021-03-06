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

def rf2link(pyxbElement, pyxbType, addlFields=None, addlSctids=None, linefilter=None):
    """ This implements the following pattern:

    def <impl_class>(line, sep="\t"):
        return <pyxbElement>().load(<impl_class name>, line, sep)

class <impl_class>(<pyxbType>, RF2Base):
    _fieldNames  = RF2Base._baseFields + addlFields
    _nFields     = len(_fieldNames)
    _baseClass   = rf2.Description_

    ...

rf2.Description_._SetSupersedingClass(_RF2Description)

    """

    def impl_link(impl_class):
        def constructor(line, sep="\t"):
            return pyxbElement().load(impl_class.__name__, linefilter(line) if linefilter else line, sep)


        # This will cause the constructor and __init__ methods to be called in the original class
        pyxbType._SetSupersedingClass(impl_class)
        impl_class._baseClass = pyxbType
        impl_class._fieldNames = impl_class._baseFields + (addlFields if addlFields else [])
        impl_class._sctidFields = impl_class._sctidFieldNames + (addlSctids if addlSctids else [])
        impl_class._nFields = len(impl_class._fieldNames)
        return constructor

    return impl_link

