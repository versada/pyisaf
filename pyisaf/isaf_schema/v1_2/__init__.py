# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from schema import And, Optional, Or, Schema, Use

from pyisaf.validators import (
    non_negative,
)
from .types import (
    ISAFCountryCodeISO,
    ISAFDataType,
    ISAFDateType2,
    ISAFDateType3,
    ISAFDateType4,
    ISAFPartNumberType,
    ISAFRegistrationNumberType,
    ISAFSpecialTaxationType,
    ISAFTaxCodeType,
    ISAFlongtextType,
    ISAFlongtextTypeNotEmpty,
    ISAFmiddle1textType,
    ISAFmiddle1textTypeNotEmpty,
    ISAFmiddle2textType,
    ISAFmiddle2textTypeNotEmpty,
    ISAFmiddletextType,
    ISAFmonetaryType,
    ISAFquantityType,
    ISAFshorttext1Type,
    ISAFshorttext2Type,
)


selection_criteria = Schema({
    'selection_start_date': datetime.date,
    'selection_end_date': datetime.date,
})

file_description = Schema({
    'file_version': Schema('iSAF1.2'),
    'file_date_created': Schema(datetime.datetime),
    'data_type': ISAFDataType,
    'software_company_name': ISAFlongtextType,
    'software_name': ISAFlongtextType,
    'software_version': ISAFmiddletextType,
    'registration_number': ISAFRegistrationNumberType,
    'number_of_parts': Schema(Or(None, And(Use(int), non_negative))),
    'part_number': ISAFPartNumberType,
    'selection_criteria': selection_criteria,
})

reference = Schema({
    'reference_no': ISAFmiddle2textTypeNotEmpty,
    'reference_date': ISAFDateType2,
})

customer = Schema({
    'customer_id': ISAFmiddle2textTypeNotEmpty,
    'vat_registration_number': ISAFmiddle1textTypeNotEmpty,
    'registration_number': ISAFmiddle1textType,
    'country': Schema(Or(None, ISAFCountryCodeISO)),
    'name': ISAFlongtextTypeNotEmpty,
})

supplier = Schema({
    'supplier_id': ISAFmiddle2textTypeNotEmpty,
    'vat_registration_number': ISAFmiddle1textTypeNotEmpty,
    'registration_number': ISAFmiddle1textType,
    'country': Schema(Or(None, ISAFCountryCodeISO)),
    'name': ISAFlongtextTypeNotEmpty,
})

supplier_info = Schema({
    Optional('supplier_id'): ISAFmiddle2textType,
    'vat_registration_number': ISAFmiddle1textType,
    Optional('registration_number'): ISAFmiddle1textType,
    'country': Schema(Or(None, ISAFCountryCodeISO)),
    'name': ISAFlongtextType,
})

customer_info = Schema({
    Optional('customer_id'): ISAFmiddle2textType,
    'vat_registration_number': ISAFmiddle1textType,
    Optional('registration_number'): ISAFmiddle1textType,
    'country': Schema(Or(None, ISAFCountryCodeISO)),
    'name': ISAFlongtextType,
})

master_file = Schema({
    Optional('customers'): Schema([customer]),
    Optional('suppliers'): Schema([supplier]),
})

purchase_document_total = Schema({
    'taxable_value': ISAFmonetaryType,
    'tax_code': Schema(Or(None, ISAFTaxCodeType)),
    'tax_percentage': Schema(Or(None, ISAFquantityType)),
    'amount': Schema(Or(None, ISAFmonetaryType)),
})

sales_document_total = Schema({
    'taxable_value': ISAFmonetaryType,
    'tax_code': Schema(Or(None, ISAFTaxCodeType)),
    'tax_percentage': Schema(Or(None, ISAFquantityType)),
    'amount': Schema(Or(None, ISAFmonetaryType)),
    'vat_point_date2': Schema(Or(None, ISAFDateType3)),
})

purchase_invoice = Schema({
    'invoice_no': ISAFmiddle2textTypeNotEmpty,
    'supplier_info': supplier_info,
    'invoice_date': Schema(datetime.date),
    'invoice_type': ISAFshorttext2Type,
    'special_taxation': ISAFSpecialTaxationType,
    'references': Schema([reference]),
    'vat_point_date': Schema(Or(None, ISAFDateType3)),
    'registration_account_date': Schema(Or(None, ISAFDateType3)),
    'document_totals': Schema([purchase_document_total]),
})

sales_invoice = Schema({
    'invoice_no': ISAFmiddle2textTypeNotEmpty,
    'customer_info': customer_info,
    'invoice_date': ISAFDateType3,
    'invoice_type': ISAFshorttext2Type,
    'special_taxation': ISAFSpecialTaxationType,
    'references': Schema([reference]),
    'vat_point_date': Schema(Or(None, ISAFDateType3)),
    'document_totals': Schema([sales_document_total]),
})

payment = Schema({
    Optional('supplier_customer_id'): ISAFmiddle2textType,
    'vat_registration_number': ISAFmiddle1textType,
    Optional('registration_number'): ISAFmiddle1textType,
    'country': Schema(Or(None, ISAFCountryCodeISO)),
    'name': ISAFlongtextType,
})

reference_to_invoice = Schema({
    'invoice_no': ISAFmiddle2textTypeNotEmpty,
    'invoice_date': ISAFDateType4,
    'amount': ISAFmonetaryType,
    'vat_amount': ISAFmonetaryType,
})

settlement_and_payment = Schema({
    'settlement_type': ISAFshorttext1Type,
    'settlement_ref_no': ISAFmiddle2textType,
    'settlement_date': ISAFDateType3,
    'payment': payment,
    'references_to_invoice': Schema([reference_to_invoice]),
})
source_documents = Schema({
    Optional('purchase_invoices'): Schema([purchase_invoice]),
    Optional('sales_invoices'): Schema([sales_invoice]),
    Optional('settlements_and_payments'): Schema([settlement_and_payment]),
})

customers = Schema([customer])
suppliers = Schema([supplier])
header = Schema({'file_description': Schema(file_description)})
schema_v1_2 = Schema({
    'header': header,
    'master_files': Schema({
        Optional('customers'): customers,
        Optional('suppliers'): suppliers,
    }),
    'source_documents': source_documents,

})
