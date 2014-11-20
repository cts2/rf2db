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

import re

from rf2db.utils.sctid import sctid


class ParameterDefinitionList(object):
    class parms(object):
        """ A Namespace of parameters.
        """

        def __init__(self, casesensitive):
            """ Build a new parsed parameter list
            @param casesensitive: Parameter names are case sensitive.
            @type casesensitive: C{bool}
            """
            self._casesensitive = casesensitive
            self._defaulted = []
            self.remainingargs = {}

        def __getattr__(self, key):
            if key.startswith('_') or self._casesensitive:
                return self.__dict__.get(key)
            else:
                return self.__dict__.get(key.lower())

        def __setattr__(self, key, value):
            if key.startswith('_') or self._casesensitive:
                self.__dict__[key] = value
            else:
                self.__dict__[key.lower()] = value

        def defaulted(self, key):
            """ Determine whether C{key} is defaulted
            @param key: value to check
            @return: C{True} if key has a default value, C{False} if the value was supplied
            """
            return key in self._defaulted


    def __init__(self, base=None, caseSensitive=False):
        """ Set up a collection of parameter parsers
        @param caseSensitive: Collection keys are case sensitive (e.g. 'isActive' is different than 'isactive')
        """
        self._caseSensitive = caseSensitive
        if base:
            self.add(base)

    def __setattr__(self, key, value, ignoredups=False):
        """ Add a new parameter definition or parameter definition list to the list
        @param key: parameter name
        @param value: parameter definition(s)
        @type value: C{ParameterDefinition} or C{ParameterDefinitionList}
        """
        if not key.startswith('_'):
            assert isinstance(value, ParameterDefinition)
            if not self._caseSensitive:
                key = key.lower()
            if not ignoredups:
                assert self.__dict__.get(key) is None, "Parameter %s defined more than once" % key
        self.__dict__[key] = value

    def replace(self, key, value):
        self.__setattr__(key, value, ignoredups=True)

    def add(self, other, ignoredups=False):
        """ Merge another set of definitions with this one
        @param other: Set of definitions to join
        @type other: C{ParameterDefinitionList}
        @param ignoredups: True means don't worry about double definitions
        """
        for k, v in other.definitions():
            self.__setattr__(k, v, ignoredups)

    def definitions(self):
        """ Return the parameter definitions in the list
        @return: key/definition tuples
        """
        return [e for e in self.__dict__.items() if not e[0].startswith('_')]

    def validate(self, **kwargs):
        """ Determine whether C{kwargs} is valid
        @param kwargs: dictionary of arguments to validate
        @return: C{True} if all arguments are valid, C{False} otherwise
        """
        for arg, val in kwargs.items():
            if not (arg.startswith('_')):
                if not self._caseSensitive:
                    arg = arg.lower()
                if isinstance(val, str) and ' ' in val and self._splitable:
                    val = val.split()
                parser = self.__dict__.get(arg)
                if parser and not parser.isValid(val):
                    return False
        return True

    def invalidParms(self, **kwargs):
        """ Return any invalid arguments in C{kwargs}
        @param kwargs: dictionary or arguments to parse
        @return: tuple - (dictionary of invalid arguments, dictionary of valid or unparsed args)
        """
        invalidargs = {}
        remainingargs = {i[0]: i[1] for i in
                         map(lambda i: (i[0] if self._caseSensitive else i[0].lower(), i[1]), kwargs.items())}
        for name, parser in self.definitions():
            v = remainingargs.pop(name, None)
            if v is not None and not parser.isValid(v):
                invalidargs[name] = v
        return invalidargs, remainingargs

    def invalidMessage(self, **kwargs):
        invalidargs, _ = self.invalidParms(**kwargs)
        if len(invalidargs):
            badarg = invalidargs.keys()[0]
            return "Invalid value (%s) for argument %s" % (invalidargs[badarg], badarg)
        return "Unknown argument problem"

    def unparsed(self):
        return self._remainingargs

    def parse(self, **kwargs):
        """ Parse the keywords and return matching parameters plus all unmatched entries
        @param kwargs: dictionary of arguments to parse
        @type kwargs: C{dict}
        @return:  namespace of parsed parameters
        """
        parmdefs = self.parms(self._caseSensitive)
        remainingargs = {i[0]: i[1] for i in
                         map(lambda i: (i[0] if self._caseSensitive else i[0].lower(), i[1]), kwargs.items())}
        for name, parser in self.definitions():
            v = remainingargs.pop(name, None)
            if v is not None and not parser.isFixed():
                parmdefs.__dict__[name] = parser.value(v)
            elif parser.hasDefault() and not parser._computed:
                parmdefs.__dict__[name] = parser.defaultValue()
                parmdefs._defaulted.append(name)

        for name, parser in self.definitions():
            if parser._computed:
                parmdefs.__dict__[name] = parser._computeValue(parmdefs)

        parmdefs.remainingargs = remainingargs
        return parmdefs


""" Parameter definition - define a parameter for subsequent parsing """


class ParameterDefinition(object):
    _computed = False

    def __init__(self, typename, default=None, splitable=True, fixed=False, required=True):
        self._typename = typename
        self._default = default
        self._required = required
        self._splitable = splitable
        self._fixed = fixed


    def _splitmaybe(self, val):
        return val.split() if self._splitable and isinstance(val, str) and ' ' in val else val

    def isValid(self, val):
        if self._computed:
            return True
        val = self._splitmaybe(val)
        if isinstance(val, list):
            return reduce(lambda a, b: a and self._isValid(b), val, True)
        return self._isValid(val)

    def isFixed(self):
        return self._fixed

    def value(self, val):
        if self.isValid(val) and not self._computed:
            val = self._splitmaybe(val)
            if isinstance(val, list):
                return map(self._value, val)
            return self._value(val)
        print("Invalid module id: %s" % val)
        return None

    def hasDefault(self):
        return self._default is not None or not self._required

    def defaultValue(self):
        return self.value(self._default) if self._default is not None else None


class booleanparam(ParameterDefinition):
    true_values = ['y', 'yes', 'true', '1', 'on', 'yup']
    false_values = ['n', 'no', 'false', '0', 'off', 'nope']

    def __init__(self, **args):
        ParameterDefinition.__init__(self, "boolean", **args)
        if self.hasDefault():
            assert self.isValid(self.defaultValue())

    def _isValid(self, val):
        val = str(val).lower()
        return val in self.true_values or val in self.false_values

    def _value(self, val):
        return self.v(val, self._default)

    @staticmethod
    def v(arg, default):
        if arg is None:
            return default
        rval = str(arg).lower()
        if rval in booleanparam.true_values:
            return True
        if rval in booleanparam.false_values:
            return False
        return None


class intparam(ParameterDefinition):
    def __init__(self, **args):
        ParameterDefinition.__init__(self, "integer", **args)

    def _isValid(self, val):
        try:
            int(val)
        except:
            return False
        return True

    def _value(self, val):
        return int(val)


class strparam(ParameterDefinition):
    sql_escapes = [(r'\\', r'\\\\'),
                   (r"'", r"\'"),
                   (r'"', r'\"'),
                   (r'%', r'\%'),
                   (r'_', r'\_'),
                   (r'\x00', r'\\0'),
                   (r'\x08', r'\\b'),
                   (r'\n', r'\\n'),
                   (r'\r', r'\\r'),
                   (r'\t', r'\\t'),
                   (r'\x1a', r'\\Z'),
    ]
    _sanitize = True

    def __init__(self, fixed=False, **args):
        ParameterDefinition.__init__(self, "string", fixed=fixed, **args)

    def _isValid(self, val):
        try:
            str(val)
        except:
            return False
        return len(str(val)) > 0

    def _value(self, val):
        """ Return the string value, sanitized for SQL if sanitize is set to true
        """
        return reduce(lambda s, e: re.sub(e[0], e[1], s, re.DOTALL + re.MULTILINE), self.sql_escapes, str(val))


class sctidparam(ParameterDefinition):
    def __init__(self, **args):
        ParameterDefinition.__init__(self, "sctid", **args)

    def _isValid(self, val):
        return sctid.isValid(val)

    def _value(self, val):
        return sctid(val)


class enumparam(ParameterDefinition):
    def __init__(self, possvalues, casesensitive=False, **args):
        ParameterDefinition.__init__(self, "enum", **args)
        self._possvalues = [str(v) if casesensitive else str(v).lower() for v in possvalues]
        self._casesensitive = casesensitive

    def possibleValues(self):
        return self._possvalues

    def _isValid(self, val):
        _val = str(val) if self._casesensitive else str(val).lower()
        return _val in self._possvalues

    def _value(self, val):
        return str(val) if self._casesensitive else str(val).lower()


class computedparam(ParameterDefinition):
    _computed = True

    def __init__(self, formula):
        """ Formula is an expression that operates on a parameters list.  It is executed after all other parameters
            are parsed.
        """
        ParameterDefinition.__init__(self, "computed", default=formula, fixed=True)

    def _computeValue(self, parms):
        return self._default(parms)


class dateparam(ParameterDefinition):
    def __init__(self, val, **args):
        ParameterDefinition.__init__(self, "date", **args)

    def _isValid(self, val):
        # TODO: Add date time validation and the like
        return True

    def _value(self, val):
        # TODO: add date time conversion
        return val

