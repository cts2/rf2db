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


class ConfigManager(object):
    _configfile = None
    _loader_queue = []
    _dirty = False
    _config_parser = ConfigParser()
    _config_parser.optionxform = str

    @classmethod
    @property
    def configfile(cls):
        return cls._configfile

    @classmethod
    def set_configfile(cls, cfgfile, override=False):
        """ Establish the location of the configuration file.  This method should be called once from the
        main portion of the executing program
        @param cfgfile: name of configuration file.
        @param override: True means move to a ndw configuration file
        """
        assert override or not cls._configfile or cls._configfile == cfgfile, \
            "Configuration file location (%s) cannot be changed" % cls._configfile
        if override:
            cls._dirty = False
            cls._config_parser = ConfigParser()
        if override or not cls._configfile:
            cls._configfile = cfgfile
            if os.path.exists(cfgfile):
                cls._config_parser.read(cfgfile)

            for obj, parms in cls._loader_queue:
                obj._load_section(parms)

        cls.flush()

    @classmethod
    def flush(cls):
        assert cls._configfile, "Configuration file name has not been set"
        if cls._dirty:
            with open(cls._configfile, 'w') as conf:
                cls._config_parser.write(conf)
            cls._dirty = False
            return True
        return False


    def __init__(self, parms):
        """ Construct a configuration manager for a given section.
        @param parms: configuration arguments
        @type parms: C{ConfigArgs}
        """
        self._section = parms.section
        self._keys = parms.keys()
        self._dirty = False
        self._loader_queue.append((self, parms))
        if self._configfile:
            self._load_section(parms)


    def _load_section(self, parms):
        # print "Loading " + self._configfile + "[" + parms.section + "]"
        if self._section not in self._config_parser.sections():
            self._config_parser.setdefault(self._section, {})
            self.update(parms.values())

    def __getattr__(self, item):
        if item.startswith('_'):
            return self.__dict__[item]
        else:
            return self._config_parser[self._section].get(item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            self.__dict__[key] = value
        elif self._config_parser[self._section].get(key) != value:
            self._config_parser[self._section][key] = value
            self._dirty = True

    def asdict(self):
        """ Return the configuration variables as a dictionary """
        return dict(self._config_parser[self._section].items())

    def update(self, values):
        """ Update the contents based using the keys that are present in the values dictionary
        """
        for k in self._keys:
            if values.get(k):
                self.__setattr__(k, values.get(k))

    def __str__(self):
        return "[%s]\n" % self._section + \
               '\n'.join(['%s = %s' % (k, v) for k, v in self._config_parser[self._section].items()])
