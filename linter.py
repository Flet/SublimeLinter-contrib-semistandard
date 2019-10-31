#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dan Flettre
# Copyright (c) 2015 Dan Flettre
#
# License: MIT
#

"""This module exports the Semistandard plugin class."""

from SublimeLinter.lint import NodeLinter


class Semistandard(NodeLinter):
    """Provides an interface to semistandard."""

    defaults = {
        'selector': 'source.js, source.js.embedded.html, source.javascript, source.javascript.babel'
    }
    cmd = 'semistandard --stdin --verbose'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    selectors = {
        'html': 'source.js.embedded.html'
    }
