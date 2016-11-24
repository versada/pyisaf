# -*- coding: utf-8 -*-

import unittest

from pyisaf import schema_v1_2

from .data import isaf_data


class TestSchemaV1_2(unittest.TestCase):

    def test_simple(self):
        schema_v1_2.validate(isaf_data)
