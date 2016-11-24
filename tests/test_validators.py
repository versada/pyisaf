# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from pyisaf.validators import (
    decimal,
    max_int_digits,
    max_length,
    min_length,
    non_negative,
)


class TestValidators(unittest.TestCase):

    def test_decimal_total_digits_3_with_four_digits_returns_False(self):
        v = decimal(3, 2)
        self.assertFalse(v('12.34'))

    def test_decimal_total_digits_3_with_3_digits_returns_True(self):
        v = decimal(3, 2)
        self.assertTrue(v('1.23'))

    def test_decimal_total_digits_3_with_3_digits_and_negative_returns_True(
            self):
        v = decimal(3, 2)
        self.assertTrue(v('-1.23'))

    def test_max_int_digits_3_with_four_digits_returns_False(self):
        v = max_int_digits(3)
        self.assertFalse(v(1234))

    def test_max_int_digits_3_with_3_digits_returns_True(self):
        v = max_int_digits(3)
        self.assertTrue(v(123))

    def test_max_int_digits_3_with_3_digits_and_negative_returns_True(self):
        v = max_int_digits(3)
        self.assertTrue(v(-123))

    def test_total_digits_with_float_raises_TypeError(self):
        v = max_int_digits(3)
        with self.assertRaises(TypeError):
            v(1.23)

    def test_max_length_3_with_length_of_2_returns_True(self):
        v = max_length(3)
        self.assertTrue(v('ab'))

    def test_max_length_3_with_length_of_3_returns_True(self):
        v = max_length(3)
        self.assertTrue(v('abc'))

    def test_max_length_3_with_length_of_4_returns_False(self):
        v = max_length(3)
        self.assertFalse(v('abcd'))

    def test_min_length_2_with_length_of_2_returns_True(self):
        v = min_length(2)
        self.assertTrue(v('ab'))

    def test_min_length_2_with_length_of_3_returns_True(self):
        v = min_length(2)
        self.assertTrue(v('abc'))

    def test_min_length_2_with_length_of_1_returns_False(self):
        v = min_length(2)
        self.assertFalse(v('a'))

    def test_non_negative_with_1_returns_True(self):
        self.assertTrue(non_negative(1))

    def test_non_negative_with_0_returns_True(self):
        self.assertTrue(non_negative(0))

    def test_non_negative_with_minus_1_returns_True(self):
        self.assertFalse(non_negative(-1))
