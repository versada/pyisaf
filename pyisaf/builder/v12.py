from pyisaf.builder.base import DATE_FORMAT, ISAFBuilder

from xml.etree.ElementTree import Element, SubElement


class ISAF12Builder(ISAFBuilder):
    ISAF_VERSION = '1.2'

    def _build_header(self, isaf):
        header = Element('Header')
        file_desc = SubElement(header, 'FileDescription')
        SubElement(file_desc, 'FileVersion').text = 'iSAF{}'.format(
            self.ISAF_VERSION)
        SubElement(file_desc, 'DataType').text = isaf.data_type
        SubElement(file_desc, 'SoftwareCompanyName').text = (
            isaf.software_company_name
        )
        SubElement(file_desc, 'SoftwareName').text = isaf.software_name
        SubElement(file_desc, 'SoftwareVersion').text = isaf.software_version
        period = SubElement(file_desc, 'SelectionCriteria')
        SubElement(period, 'SelectionStartDate').text = (
            isaf.period_start.strftime(DATE_FORMAT)
        )
        SubElement(period, 'SelectionEndDate').text = (
            isaf.period_end.strftime(DATE_FORMAT)
        )
        return header

    def _build_isaf_file(self, isaf):
        isaf_file = Element('iSAFFile')
        header = self._build_header(isaf)
        isaf_file.append(header)
        return isaf_file
