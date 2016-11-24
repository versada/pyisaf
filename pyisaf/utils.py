# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import xml.dom.minidom

PY3 = sys.version_info[0] == 3

if PY3:
    ustr = str
else:
    ustr = unicode  # noqa


def pretty_print_xml(s, encoding='utf-8'):
    root = xml.dom.minidom.parseString(s)
    return root.toprettyxml(encoding=encoding)
