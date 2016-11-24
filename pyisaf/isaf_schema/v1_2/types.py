# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from schema import And, Or, Regex, Schema, Use

from .const import DATA_TYPES, INVOICE_TYPES, SETTLEMENT_TYPES
from pyisaf.utils import ustr
from pyisaf.validators import (
    decimal,
    max_int_digits,
    max_length,
    min_length,
    non_negative,
)

'''
Custom data types defined in the i.SAF v1.2 XSD:
http://www.vmi.lt/cms/documents/10162/9117564/isaf_1.2.xsd/02cadf68-5fe0-4684-bbeb-16feddbf1fdc
'''

ISAFDataType = Schema(Or(*DATA_TYPES))
ISAFlongtextType = Schema(And(ustr, max_length(256)))
ISAFlongtextTypeNotEmpty = Schema(And(ISAFlongtextType, min_length(1)))
ISAFmiddletextType = Schema(And(ustr, max_length(24)))
ISAFmiddle1textType = Schema(And(ustr, max_length(35)))
ISAFmiddle1textTypeNotEmpty = Schema(And(ISAFmiddle1textType, min_length(1)))
ISAFmiddle2textType = Schema(And(ustr, max_length(70)))
ISAFmiddle2textTypeNotEmpty = Schema(And(ISAFmiddle2textType, min_length(1)))
ISAFRegistrationNumberType = Schema(
    And(Use(int), non_negative, max_int_digits(11)))
ISAFPartNumberType = Schema(
    And(ustr, Regex(r'[A-Z0-9_]*'), max_length(20), min_length(1)))
ISAFCountryCodeISO = Schema(And(ustr, max_length(2)))
ISAFshorttext1Type = Schema(Or(*SETTLEMENT_TYPES))
ISAFshorttext2Type = Schema(Or(*(list(INVOICE_TYPES) + [''])))
ISAFSpecialTaxationType = Schema(Or('T', ''))
ISAFDateType2 = Schema(And(
    datetime.date,
    lambda v: datetime.date(1990, 1, 1) <= v <= datetime.date(2100, 1, 1)
))
ISAFDateType3 = Schema(And(
    datetime.date,
    lambda v: datetime.date(2016, 7, 1) <= v <= datetime.date(2100, 1, 1)
))
ISAFDateType4 = Schema(And(
    datetime.date,
    lambda v: datetime.date(2011, 1, 1) <= v <= datetime.date(2100, 1, 1)
))
ISAFmonetaryType = Schema(And(ustr, decimal(18)))
ISAFTaxCodeType = Schema(
    And(
        ustr,
        min_length(4),
        max_length(6),
        Regex(r'^PVM([0-9])*'),
    )
)
ISAFquantityType = Schema(And(ustr, decimal(5)))
