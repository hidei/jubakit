# -*- coding: utf-8 -*-

"""
Utilities for CLI classes.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import shlex

from ..compat import *

__all__ = [
  'shell_split',
  'comp_position',
  'filter_candidates',
]

def shell_split(s):
  if isinstance(s, unicode_t) and PYTHON2_6:
    # shlex does not support Unicode on Python 2.6
    return map(lambda x: x.decode(), shlex.split(s.encode()))
  return shlex.split(s)

def comp_position(text, line, begidx, endidx):
  """
  Returns the current completion position of the argument.
  """
  return len(shell_split(line[:begidx])) - 1

def filter_candidates(text, candidates):
  """
  Filters completion candidates by the text being entered.
  """
  return [x for x in candidates if x.startswith(text)]
