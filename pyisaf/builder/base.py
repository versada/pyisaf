import abc

from xml.etree import ElementTree


DATE_FORMAT = '%Y-%m-%d'


class ISAFBuilder:
    __metaclass__ = abc.ABCMeta
    ISAF_VERSION = None

    def register_namespaces(self):
        namespaces = {
            '': 'http://www.vmi.lt/cms/imas/isaf',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        }
        for prefix, uri in namespaces.items():
            ElementTree.register_namespace(prefix, uri)

    @abc.abstractmethod
    def _build_header(self, isaf):
        '''Builds and returns Header element.'''

    @abc.abstractmethod
    def _build_isaf_file(self, isaf):
        '''Builds and returns the iSAFFile element.'''
