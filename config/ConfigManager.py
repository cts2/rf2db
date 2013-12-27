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
import os

from configparser import ConfigParser

# Default configuration file location
defaultConfigFile = os.path.join(os.path.dirname(__file__),'..', 'settings.cfg')

class ConfigManager(object):
    def __init__(self, parms, cfgfile=defaultConfigFile):
        """ Construct a configuration manager for a given section
        @param parms: configuration arguments
        @type parms: C{ConfigArgs}
        @param cfgfile: name of configuration file
        """
        print "Loading " + cfgfile + " / " + parms.section
        self._configFile = cfgfile
        self._section = parms.section
        self._keys = parms.keys()
        self._config = ConfigParser()
        self._config.optionxform = str
        self._dirty = False

        self._config.setdefault(self._section, {})
        if not os.path.exists(cfgfile):
            self.update(parms.values())
            with open(cfgfile, 'w') as conf:
                self._config.write(conf)
        else:
            self._config.read(cfgfile)



    def __getattr__(self, item):
        if item.startswith('_'):
            return self.__dict__[item]
        else:
            return self._config[self._section].get(item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            self.__dict__[key] = value
        elif self._config[self._section].get(key) != value:
            self._config[self._section][key] = value
            self._dirty = True

    def section(self):
        return dict(self._config[self._section].items())

    def update(self,values):
        """ Update the contents based using the keys that are present in the values dictionary
        """
        for k in self._keys:
            if values.get(k):
                self.__setattr__(k,values.get(k))


    def write(self):
        if not self._dirty:
            return False

        with open(self._configFile, 'w') as conf:
            self._config.write(conf)
            self._dirty = False
        return True


    def __str__(self):
        return "[%s]\n" % self._section + \
            '\n'.join(['%s = %s' % (k,v) for k,v in self._config[self._section].items()])
