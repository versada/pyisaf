# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .utils import int_to_digits


def decimal(total_digits, fraction_digits=2):

    def validator(v):
        v = v.lstrip('-')
        if '.' in v:
            d, f = v.split('.')
        else:
            d, f = v, ''
        total = len(d) + len(f)
        return total <= total_digits and len(f) <= fraction_digits

    return validator


def max_int_digits(max_digits):

    def validator(v):
        return len(int_to_digits(v)) <= max_digits

    return validator


def max_length(max_len):

    def validator(v):
        return len(v) <= max_len

    return validator


def min_length(min_len):

    def validator(v):
        return len(v) >= min_len

    return validator


def non_negative(v):
    return v >= 0
