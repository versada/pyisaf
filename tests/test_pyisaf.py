#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import unittest

from pyisaf import ISAF


class TestISAF(unittest.TestCase):

    def test_init_period_start_not_datetime_raises_value_error(self):
        start, end = '2011-01-01', datetime.datetime(2011, 12, 31)
        with self.assertRaises(ValueError):
            ISAF(start, end)

    def test_init_period_end_not_datetime_raises_value_error(self):
        start, end = datetime.datetime(2011, 1, 1), '2011-12-31'
        with self.assertRaises(ValueError):
            ISAF(start, end)

    def test_unknown_data_type_raises_value_error(self):
        start, end = (
            datetime.datetime(2011, 1, 1), datetime.datetime(2011, 12, 31))
        with self.assertRaisesRegexp(ValueError, '^Unknown data type'):
            ISAF(start, end, data_type='blah')
