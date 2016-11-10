#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyisaf',
    version='0.1.0',
    description='Python library for i.SAF VAT report generation.',
    long_description=readme + '\n\n' + history,
    author='Naglis Jonaitis',
    author_email='naglis@mailbox.org',
    url='https://github.com/naglis/pyisaf',
    packages=[
        'pyisaf',
    ],
    package_dir={'pyisaf':
                 'pyisaf'},
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
    ],
    test_suite='tests',
    tests_require=test_requirements
)
