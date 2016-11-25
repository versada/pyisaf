# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import io
import unittest
import xml.etree.ElementTree

from pyisaf import ISAF1_2Builder, schema_v1_2
from pyisaf.builder.base import DATE_FORMAT

from .data import isaf_data


class TestISAF12Builder(unittest.TestCase):

    def setUp(self):
        super(TestISAF12Builder, self).setUp()
        self.start_date = datetime.datetime(2016, 10, 1)
        self.end_date = datetime.datetime(2016, 10, 31)
        self.isaf = schema_v1_2.validate(isaf_data)
        self.builder = ISAF1_2Builder(self.isaf)

    def assertTagText(self, element, xpath, text, msg=None):
        try:
            tag = element.findall(xpath)[0]
        except IndexError:
            self.fail('Tag not found at xpath: {}'.format(xpath))
        self.assertEqual(tag.text, text, msg=msg)

    def test_build_header_sets_file_version(self):
        header = self.builder._build_header()
        self.assertTagText(
            header, './FileDescription/FileVersion', 'iSAF1.2')

    def test_build_header_sets_file_date_created(self):
        header = self.builder._build_header()
        self.assertTagText(
            header, './FileDescription/FileDateCreated', '2016-11-02T12:31:59')

    def test_build_header_sets_data_type(self):
        header = self.builder._build_header()
        self.assertTagText(header, './FileDescription/DataType', 'F')

    def test_build_header_sets_software_company_name(self):
        header = self.builder._build_header()
        self.assertTagText(
            header, './FileDescription/SoftwareCompanyName', 'UAB "Imone"')

    def test_build_header_sets_software_name(self):
        header = self.builder._build_header()
        self.assertTagText(
            header, './FileDescription/SoftwareName', 'Imone')

    def test_build_header_sets_software_version(self):
        header = self.builder._build_header()
        self.assertTagText(
            header, './FileDescription/SoftwareVersion', '1.2')

    def test_build_header_sets_selection_start_date(self):
        header = self.builder._build_header()
        self.assertTagText(
            header,
            './FileDescription/SelectionCriteria/SelectionStartDate',
            self.start_date.strftime(DATE_FORMAT),
        )

    def test_build_header_sets_selection_end_date(self):
        header = self.builder._build_header()
        self.assertTagText(
            header,
            './FileDescription/SelectionCriteria/SelectionEndDate',
            self.end_date.strftime(DATE_FORMAT),
        )

    def test_builder_master_adds_two_customers(self):
        master = self.builder._build_master_files()
        self.assertEqual(len(master.findall('./Customers/Customer')), 2)

    def test_builder_master_adds_one_supplier(self):
        master = self.builder._build_master_files()
        self.assertEqual(len(master.findall('./Suppliers/Supplier')), 1)

    def test_builder_master_supplier_data_is_correct(self):
        master = self.builder._build_master_files()
        self.assertTagText(
            master, './Suppliers/Supplier[1]/SupplierID', '1015')
        self.assertTagText(
            master,
            './Suppliers/Supplier[1]/VATRegistrationNumber',
            'LT100004466111',
        )
        self.assertTagText(
            master, './Suppliers/Supplier[1]/RegistrationNumber', '302222220',
        )
        self.assertTagText(master, './Suppliers/Supplier[1]/Country', 'LT')
        self.assertTagText(
            master, './Suppliers/Supplier[1]/Name', 'UAB "Įmonė"')

    def test_builder_source_docs_adds_two_purchase_invoices(self):
        source_docs = self.builder._build_source_documents()
        self.assertEqual(
            len(source_docs.findall('./PurchaseInvoices/Invoice')), 2)

    def test_builder_source_docs_adds_two_sales_invoices(self):
        source_docs = self.builder._build_source_documents()
        self.assertEqual(
            len(source_docs.findall('./SalesInvoices/Invoice')), 2)

    def test_builder_source_docs_adds_two_settlements_and_payments(self):
        source_docs = self.builder._build_source_documents()
        self.assertEqual(
            len(source_docs.findall(
                './SettlementsAndPayments/SettlementAndPayment')),
            2)

    def test_dump_returns_correct_xml(self):
        buf = io.BytesIO()
        self.builder.dump(buf)
        buf.seek(0)
        isaf_xml = xml.etree.ElementTree.parse(buf)

        # FIXME: improve namespace handling somehow
        ns_url = self.builder.namespaces.get('')

        def xpath(v):
            return v % ns_url

        self.assertEqual(len(isaf_xml.findall(xpath('./{%s}Header'))), 1)
        self.assertEqual(len(isaf_xml.findall(xpath('./{%s}MasterFiles'))), 1)
        self.assertEqual(
            len(isaf_xml.findall(xpath('./{%s}SourceDocuments'))), 1)
