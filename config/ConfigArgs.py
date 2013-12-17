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

class ConfigArgs():
    def __init__(self, section, args):
        """ Initialize a collection of configuration arguments
        @param section: The section name for the arguments
        @param args: The list of actual configuration parameters
        """
        self.section = section
        self.args = args

    def addToParser(self, parser, current=None):
        for arg in self.args:
            args = ['--' + arg.argName]
            if arg.argAbbrev:
                args += ['-' + arg.argAbbrev]
            kwargs = {'dest' : arg.argName}
            if arg.argHelp:
                kwargs['help'] = arg.argHelp
            if current and current.section().get(arg.argName):
                kwargs['default'] = current.section().get(arg.argName)
            elif arg.default:
                kwargs['default'] = arg.default
            if arg.action:
                kwargs['action'] = arg.action
            parser.add_argument(*args, **kwargs)

    def values(self):
        return {n.argName : n.default for n in self.args if n.default}

    def keys(self):
        return [n.argName for n in self.args]

class ConfigArg():
    def __init__(self, argName, abbrev=None, help=None, default=None, action=None):
        self.argName = argName
        self.argAbbrev = abbrev
        self.argHelp = help
        self.default = default
        self.action = action

