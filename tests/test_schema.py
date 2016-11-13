#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import unittest

from pyisaf import schema_v1_2

class TestSchemaV1_2(unittest.TestCase):

    def test_simple(self):
        isaf = {
            'header': {
                'file_description': {
                    'file_version': 'iSAF1.2',
                    'data_type': 'S',
                    'file_date_created': datetime.datetime.today(),
                    'number_of_parts': '123',
                    'software_version': '123',
                    'part_number': 'kaunas',
                    'registration_number': '123',
                    'selection_criteria': {
                        'selection_start_date': datetime.date(2000,1,1),
                        'selection_end_date': datetime.date(2000,1,1),
                    },
                    'software_company_name': 'hbee',
                    'software_name': 'Odoo',
                },
            },
            'master_files': {
            },
            'source_documents': {
                'purchase_invoices': [
                    {
                        'invoice_no': '1',
                        'invoice_type': 'SF',
                        'vat_point_date': datetime.date(2016, 8, 2),
                        'invoice_date': datetime.date(2016, 9, 1),
                        'references': [],
                        'registration_account_date': datetime.date(2016, 10, 1),
                        'special_taxation': '',
                        'document_totals': [
                        ],
                        'supplier_info': {
                            'country': '',
                            'name': '',
                            'vat_registration_number': '',
                        },
                    },
                ],
            },
        }
        schema_v1_2.validate(isaf)

