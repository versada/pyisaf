# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import abc
from xml.etree import ElementTree

from pyisaf.utils import pretty_print_xml


DATE_FORMAT = '%Y-%m-%d'


class ISAFBuilder:
    __metaclass__ = abc.ABCMeta
    ISAF_VERSION = None
    namespaces = {}

    def __init__(self, isaf):
        self._isaf = isaf

    @property
    def isaf(self):
        return self._isaf

    def register_namespaces(self):
        for prefix, uri in self.namespaces.items():
            ElementTree.register_namespace(prefix, uri)

    @abc.abstractmethod
    def _build_header(self):
        '''Builds and returns Header element.'''

    @abc.abstractmethod
    def _build_master_files(self):
        '''Builds and returns MasterFiles element.'''

    @abc.abstractmethod
    def _build_source_documents(self):
        '''Builds and returns SourceDocuments element.'''

    def build_isaf_file(self):
        '''Builds and returns the iSAFFile element.'''
        self.register_namespaces()

        header = self._build_header()
        master_files = self._build_master_files()
        source_docs = self._build_source_documents()

        isaf_file = ElementTree.Element('iSAFFile')
        for ns, url in self.namespaces.items():
            isaf_file.set(
                'xmlns{extra}'.format(extra=(':{0}'.format(ns) if ns else '')),
                url
            )

        isaf_file.append(header)
        isaf_file.append(master_files)
        isaf_file.append(source_docs)
        return isaf_file

    def dumps(self, encoding='utf-8', pretty_print=True):
        root = self.build_isaf_file()
        xml_string = ElementTree.tostring(root, encoding=encoding)
        if pretty_print:
            return pretty_print_xml(xml_string, encoding=encoding)
        else:
            return xml_string

    def dump(self, fobj, pretty_print=True, encoding='utf-8'):
        fobj.write(self.dumps(encoding=encoding, pretty_print=pretty_print))
