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
from rf2db.utils.check_digit import generate_verhoeff
from rf2db.utils.sctid import sctid

MAYO_Namespace = 1000134
CIMI_Namespace = 1000160


class sctid_generator(object):
    class partition(object):
        def __init__(self, id):
            self._id = id

    CONCEPT = partition(00)
    DESCRIPTION = partition(01)
    RELATIONSHIP = partition(02)


    def __init__(self, namespace, partition, start):
        """
        @param namespace: SNOMED Namespace identifier
        @param partition: Partition Identifier
        @param start:
        @return:
        """
        assert isinstance(partition, sctid_generator.partition)
        self._namespace = namespace
        self._partition = partition._id
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        rval = generate_verhoeff(self._start * 10 ** 10 + self._namespace * 10 ** 3 + self._partition * 10)
        self._start += 1
        return sctid(rval)
