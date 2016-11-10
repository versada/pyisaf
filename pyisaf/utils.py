# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def assert_isinstance(obj, classinfo):
    msg = 'Assertion failed, exptected type: %s' % (
        ', '.join(classinfo) if isinstance(classinfo, tuple) else classinfo
    )
    if not isinstance(obj, classinfo):
        raise ValueError(msg)
