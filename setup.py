#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall(r'__([a-z]+)__ = \'([^\']+)\'', fh.read()))
        return metadata['version']


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'schema>=0.6.5,<0.7.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyisaf',
    version=get_version('pyisaf/__init__.py'),
    description='Python library for i.SAF VAT report generation.',
    long_description=readme + '\n\n' + history,
    author='Naglis Jonaitis',
    author_email='naglis@mailbox.org',
    url='https://github.com/naglis/pyisaf',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    license='BSD license',
    zip_safe=False,
    keywords='pyisaf',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
