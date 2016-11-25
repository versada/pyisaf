# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

'''
The test data is prepared based on the example i.SAF XML, provided by VMI:
https://www.vmi.lt/cms/documents/10162/9052063/isaf_xml_pavyzdys_20160922.xml
'''

header = {
    'file_description': {
        'file_version': 'iSAF1.2',
        'file_date_created': datetime.datetime(2016, 11, 2, 12, 31, 59),
        'data_type': 'F',
        'software_company_name': 'UAB "Imone"',
        'software_name': 'Imone',
        'software_version': '1.2',
        'registration_number': '12345678912',
        'number_of_parts': '1',
        'part_number': 'Vilnius',
        'selection_criteria': {
            'selection_start_date': datetime.date(2016, 10, 1),
            'selection_end_date': datetime.date(2016, 10, 31),
        },
    },
}

customers = [
    {
        'customer_id': '12500',
        'vat_registration_number': 'LT119500000',
        'registration_number': '211123456',
        'country': 'LT',
        'name': 'UAB "Bendrovė"',
    },
    {
        'customer_id': '2222',
        'vat_registration_number': 'LT122222220',
        'registration_number': '222222222',
        'country': 'LT',
        'name': 'UAB "Kooperatyvas"',
    },
]

suppliers = [
    {
        'supplier_id': '1015',
        'vat_registration_number': 'LT100004466111',
        'registration_number': '302222220',
        'country': 'LT',
        'name': 'UAB "Įmonė"',
    },
]

purchase_invoices = [
    {
        'invoice_no': 'IM0011',
        'supplier_info': {
            'supplier_id': '1015',
            'vat_registration_number': 'LT100004466111',
            'registration_number': '302222220',
            'country': 'LT',
            'name': 'UAB "Įmonė"',
        },
        'invoice_date': datetime.date(2016, 10, 13),
        'invoice_type': 'SF',
        'special_taxation': 'T',
        'references': [],
        'vat_point_date': datetime.date(2016, 10, 13),
        'registration_account_date': datetime.date(2016, 10, 13),
        'document_totals': [
            {
                'taxable_value': '420',
                'tax_code': 'PVM1',
                'tax_percentage': '21',
                'amount': '88.2',
            },
            {
                'taxable_value': '250',
                'tax_code': 'PVM2',
                'tax_percentage': '9',
                'amount': '22.5',
            },
        ],
    },
    {
        'invoice_no': 'IM0012',
        'supplier_info': {
            'supplier_id': '1015',
            'vat_registration_number': 'LT100004466111',
            'registration_number': '302222220',
            'country': 'LT',
            'name': 'UAB "Įmonė"',
        },
        'invoice_date': datetime.date(2016, 10, 14),
        'invoice_type': 'DS',
        'special_taxation': '',
        'references': [
            {
                'reference_no': 'IM001',
                'reference_date': datetime.date(2016, 10, 1),
            },
            {
                'reference_no': 'INS002',
                'reference_date': datetime.date(2016, 10, 6),
            },
            {
                'reference_no': 'INS003',
                'reference_date': datetime.date(2016, 10, 7),
            },
        ],
        'vat_point_date': datetime.date(2016, 10, 14),
        'registration_account_date': datetime.date(2016, 10, 15),
        'document_totals': [
            {
                'taxable_value': '1005',
                'tax_code': 'PVM1',
                'tax_percentage': '21',
                'amount': '211.05',
            },
            {
                'taxable_value': '250',
                'tax_code': 'PVM2',
                'tax_percentage': '9',
                'amount': '22.5',
            }
        ],
    },
]

sales_invoices = [
    {
        'invoice_no': 'VM105',
        'customer_info': {
            'customer_id': '12500',
            'vat_registration_number': 'LT119500000',
            'registration_number': '211123456',
            'country': 'LT',
            'name': 'UAB "Bendrovė"',

        },
        'invoice_date': datetime.date(2016, 10, 1),
        'invoice_type': 'KS',
        'special_taxation': '',
        'references': [
            {
                'reference_no': 'VM100',
                'reference_date': datetime.date(2016, 9, 24),
            },
        ],
        'vat_point_date': datetime.date(2016, 9, 5),
        'document_totals': [
            {
                'taxable_value': '1065',
                'tax_code': 'PVM45',
                'tax_percentage': '5',
                'amount': '53.25',
                'vat_point_date2': datetime.date(2016, 9, 23),
            },
        ],
    },
    {
        'invoice_no': 'VM106',
        'customer_info': {
            'customer_id': '2222',
            'vat_registration_number': 'LT122222220',
            'registration_number': '222222222',
            'country': 'LT',
            'name': 'UAB "Kooperatyvas"',
        },
        'invoice_date': datetime.date(2016, 10, 1),
        'invoice_type': 'SF',
        'special_taxation': '',
        'references': [],
        'vat_point_date': datetime.date(2016, 10, 1),
        'document_totals': [
            {
                'taxable_value': '1065',
                'tax_code': 'PVM1',
                'tax_percentage': '21',
                'amount': '223.65',
                'vat_point_date2': datetime.date(2016, 10, 2),
            },
        ],
    },
]

settlements_and_payments = [
    {
        'settlement_type': 'V',
        'settlement_ref_no': 'ND',
        'settlement_date': datetime.date(2016, 10, 25),
        'payment': {
            'supplier_customer_id': '1015',
            'vat_registration_number': 'LT100004466111',
            'registration_number': '302222220',
            'country': 'LT',
            'name': 'UAB "Įmonė"',

        },
        'references_to_invoice': [
            {
                'invoice_no': 'IM0011',
                'invoice_date': datetime.date(2016, 10, 13),
                'amount': '670',
                'vat_amount': '110.70',
            },
        ],
    },
    {
        'settlement_type': 'G',
        'settlement_ref_no': '1145',
        'settlement_date': datetime.date(2016, 10, 25),
        'payment': {
            'supplier_customer_id': '1015',
            'vat_registration_number': 'LT100004466111',
            'registration_number': '302222220',
            'country': 'LT',
            'name': 'UAB "Įmonė"',
        },
        'references_to_invoice': [
            {
                'invoice_no': 'IM0001',
                'invoice_date': datetime.date(2016, 8, 13),
                'amount': '100',
                'vat_amount': '21',
            },
        ],
    },
]

isaf_data = {
    'header': header,
    'master_files': {
        'customers': customers,
        'suppliers': suppliers,
    },
    'source_documents': {
        'purchase_invoices': purchase_invoices,
        'sales_invoices': sales_invoices,
        'settlements_and_payments': settlements_and_payments,
    },
}
