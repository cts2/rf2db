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

import unittest, argparse, os
from config.ConfigArgs import ConfigArgs, ConfigArg
from config.ConfigManager import ConfigManager

config_parms = ConfigArgs( 'dbparms',
                           [ConfigArg('host', help='MySQL DB Host', default='localhost'),
                            ConfigArg('port', help='MySQL DB Port'),
                            ConfigArg('user', abbrev='u', help='MySQL User Id'),
                            ConfigArg('passwd', abbrev='p', help='MySQL Password'),
                            ConfigArg('db', abbrev='db', help='Database', default='rf2'),
                            ConfigArg('charset', help='MySQL Character Set', default='utf8'),
                            ConfigArg('trace', help='Trace SQL Statements')
                            ])


defaultConfigFile = os.path.join(os.path.dirname(__file__),'testdata/settings.cfg')
class ConfigManagerTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(defaultConfigFile):
            os.remove(defaultConfigFile)

    def test_load_args(self):
        cfg = ConfigManager(config_parms,cfgfile=defaultConfigFile)
        self.assertEqual(str(cfg), """[dbparms]
host = localhost
db = rf2
charset = utf8""")

    def test_set_parm(self):
        cfg = ConfigManager(config_parms,cfgfile=defaultConfigFile)
        parser = argparse.ArgumentParser()
        config_parms.add_to_parser(parser, current=cfg)
        parser.add_argument('-show', dest='show', action="store_true", help="show current configuration")
        parser.add_argument('-upd', dest='update', action="store_true", help="update configuration file")
        parser.add_argument('--create', action="store_true", help="create database if it doesn't exist")
        parser.add_argument('--configfile', help="configuration file location (default: %s)" % defaultConfigFile,
                            default=defaultConfigFile)
        opts = parser.parse_args("-db rf2test --host localhost --port 8091 -u root -p rootpw".split())
        cfg.update(vars(opts))
        self.assertEqual(str(cfg),"""[dbparms]
host = localhost
db = rf2test
charset = utf8
port = 8091
user = root
passwd = rootpw""")
        cfg.write()
        cfg = ConfigManager(config_parms,cfgfile=defaultConfigFile)
        self.assertEqual(str(cfg),"""[dbparms]
host = localhost
db = rf2test
charset = utf8
port = 8091
user = root
passwd = rootpw""")


if __name__ == '__main__':
    unittest.main()
