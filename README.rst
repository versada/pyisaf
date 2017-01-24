=======
pyisaf
=======

.. image:: https://img.shields.io/pypi/v/pyisaf.svg
        :target: https://pypi.python.org/pypi/pyisaf

.. image:: https://img.shields.io/travis/naglis/pyisaf.svg
        :target: https://travis-ci.org/naglis/pyisaf

.. image:: https://codecov.io/gh/naglis/pyisaf/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/naglis/pyisaf

Python library for i.SAF VAT report generation.


* GitHub: https://github.com/naglis/pyisaf
* Free software: BSD license
* Supported Python versions: 2.7, 3.5+

Features
--------

* i.SAF data validation based on XSD
* i.SAF XML builder

Usage
-----

A complete example of i.SAF data dict can be found `in the tests
<https://github.com/naglis/pyisaf/blob/master/tests/data.py>`_.

.. code:: python

    from pyisaf import schema_v1_2 as isaf_schema, ISAF1_2Builder as Builder
    from schema import SchemaError


    # Prepare i.SAF data
    data = {
        'header': {
            'file_description': {
                # ...
            },
        },
        'master_files': {
            'customers': {
                # ...
            },
            'suppliers': {
                # ...
            },
        },
        'source_documents': {
            'purchase_invoices': {
                # ...
            },
            'sales_invoices': {
                # ...
            },
            'settlements_and_payments': {
                # ...
            },
        },
    }
    # Validate data against i.SAF schema
    isaf_data = isaf_schema.validate(data)

    # Build the XML
    builder = Builder(isaf_data)
    isaf_xml = builder.dumps()
