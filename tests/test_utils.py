# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from pyisaf.utils import int_to_digits


class TestUtils(unittest.TestCase):

    def test_int_to_digits_1230_returns_1_2_3_0(self):
        self.assertEqual(int_to_digits(1230), [1, 2, 3, 0])

    def test_int_to_digits_negative_123_returns_1_2_3(self):
        self.assertEqual(int_to_digits(-123), [1, 2, 3])

    def test_int_to_digits_0_returns_0(self):
        self.assertEqual(int_to_digits(0), [0])

    def test_int_to_digits_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            int_to_digits(1.23)
