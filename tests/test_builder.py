#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import unittest

from pyisaf import ISAF
from pyisaf.builder.base import DATE_FORMAT
from pyisaf.builder import ISAF12Builder


class TestISAF12Builder(unittest.TestCase):

    def setUp(self):
        super(TestISAF12Builder, self).setUp()
        self.start_date = datetime.datetime(2016, 1, 1)
        self.end_date = datetime.datetime(2016, 12, 31)
        self.isaf = ISAF(
            self.start_date,
            self.end_date,
            software_name='Builder',
            software_company_name='Blah',
            software_version='1.2.3',
        )
        self.builder = ISAF12Builder()

    def assert_tag_text(self, element, xpath, text, msg=None):
        try:
            tag = element.findall(xpath)[0]
        except IndexError:
            self.fail('Tag not found at xpath: {}'.format(xpath))
        self.assertEqual(tag.text, text, msg=msg)

    def test_build_header_sets_file_version(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header, './FileDescription/FileVersion', 'iSAF1.2')

    def test_build_header_sets_data_type(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(header, './FileDescription/DataType', 'F')

    def test_build_header_sets_software_company_name(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header, './FileDescription/SoftwareCompanyName', 'Blah')

    def test_build_header_sets_software_name(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header, './FileDescription/SoftwareName', 'Builder')

    def test_build_header_sets_software_version(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header, './FileDescription/SoftwareVersion', '1.2.3')

    def test_build_header_sets_selection_start_date(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header,
            './FileDescription/SelectionCriteria/SelectionStartDate',
            self.start_date.strftime(DATE_FORMAT),
        )

    def test_build_header_sets_selection_end_date(self):
        header = self.builder._build_header(self.isaf)
        self.assert_tag_text(
            header,
            './FileDescription/SelectionCriteria/SelectionEndDate',
            self.end_date.strftime(DATE_FORMAT),
        )
