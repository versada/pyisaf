# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import xml.dom.minidom

PY3 = sys.version_info[0] == 3

if PY3:
    ustr = str
    int_types = int
else:  # pragma: no cover
    ustr = unicode  # noqa
    int_types = (int, long)  # noqa


def pretty_print_xml(s, encoding='utf-8'):
    root = xml.dom.minidom.parseString(s)
    return root.toprettyxml(encoding=encoding)


def int_to_digits(number):
    number = abs(number)
    if not isinstance(number, int_types):
        raise TypeError('Only integers are supported')
    if number == 0:
        return [0]
    digits = []
    while number:
        number, digit = divmod(number, 10)
        digits.append(digit)
    return digits[::-1]
