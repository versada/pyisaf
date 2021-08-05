import abc
import typing
from xml.etree import ElementTree as ET  # nosec

DATE_FORMAT = "%Y-%m-%d"


class ISAFBuilder(metaclass=abc.ABCMeta):
    ISAF_VERSION: typing.Optional[str] = None
    namespaces: typing.Dict[str, str] = {}

    def __init__(self, isaf):
        self._isaf = isaf

    @property
    def isaf(self):
        return self._isaf

    def register_namespaces(self) -> None:
        for prefix, uri in self.namespaces.items():
            ET.register_namespace(prefix, uri)

    @abc.abstractmethod
    def _build_header(self):
        """Builds and returns Header element."""

    @abc.abstractmethod
    def _build_master_files(self):
        """Builds and returns MasterFiles element."""

    @abc.abstractmethod
    def _build_source_documents(self):
        """Builds and returns SourceDocuments element."""

    def build_isaf_file(self) -> ET.Element:
        """Builds and returns the iSAFFile element."""
        self.register_namespaces()

        header = self._build_header()
        master_files = self._build_master_files()
        source_docs = self._build_source_documents()

        isaf_file = ET.Element("iSAFFile")
        for ns, url in self.namespaces.items():
            isaf_file.set("xmlns{extra}".format(extra=(f":{ns}" if ns else "")), url)

        isaf_file.append(header)
        isaf_file.append(master_files)
        isaf_file.append(source_docs)
        return isaf_file

    def dumps(self, *, pretty_print: bool = True) -> str:
        root = self.build_isaf_file()
        if pretty_print:
            ET.indent(root, space="\t")
        return ET.tostring(root, encoding="unicode")

    def dump(
        self,
        fobj: typing.BinaryIO,
        *,
        encoding: str = "utf-8",
        pretty_print: bool = True,
    ) -> None:
        if encoding == "unicode":
            raise ValueError("Invalid encoding, use `dumps`")
        root = self.build_isaf_file()
        if pretty_print:
            ET.indent(root, space="\t")
        tree = ET.ElementTree(element=root)
        tree.write(fobj, encoding=encoding)
