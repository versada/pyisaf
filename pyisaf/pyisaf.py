# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from .utils import assert_isinstance

DATA_TYPES = {
    'F': 'Full',
    'P': 'Received',
    'S': 'Issued',
}
DEFAULT_DATATYPE = 'F'

__version__ = '0.1.0'


class ISAF(object):
    '''Only holds i.SAF data, knows nothing about building XML.'''

    def __init__(
            self, period_start, period_end,
            data_type=DEFAULT_DATATYPE,
            software_company_name='Naglis Jonaitis',
            software_name='pyisaf', software_version=__version__):

        assert_isinstance(period_start, datetime.datetime)
        assert_isinstance(period_end, datetime.datetime)

        if data_type not in DATA_TYPES:
            raise ValueError('Unknown data type: {}'.format(data_type))

        self.period_start = period_start
        self.period_end = period_end
        self.data_type = data_type
        self.software_company_name = software_company_name
        self.software_name = software_name
        self.software_version = software_version
