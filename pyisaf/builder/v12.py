from pyisaf.builder.base import DATE_FORMAT, ISAFBuilder

from xml.etree.ElementTree import Element, SubElement


class ISAF12Builder(ISAFBuilder):
    ISAF_VERSION = '1.2'

    def _build_header(self):
        h = self.isaf['header']
        fd = h['file_description']
        sc = fd['selection_criteria']

        header = Element('Header')
        file_desc = SubElement(header, 'FileDescription')
        SubElement(file_desc, 'FileVersion').text = fd['file_version']
        SubElement(file_desc, 'FileDateCreated').text = (
            fd['file_date_created'].isoformat()
        )
        SubElement(file_desc, 'DataType').text = fd['data_type']
        SubElement(file_desc, 'SoftwareCompanyName').text = (
            fd['software_company_name']
        )
        SubElement(file_desc, 'SoftwareName').text = fd['software_name']
        SubElement(file_desc, 'SoftwareVersion').text = fd['software_version']
        SubElement(file_desc, 'RegistrationNumber').text = (
            fd['registration_number']
        )
        SubElement(file_desc, 'NumberOfParts').text = fd['number_of_parts']
        SubElement(file_desc, 'PartNumber').text = fd['part_number']

        period = SubElement(file_desc, 'SelectionCriteria')
        SubElement(period, 'SelectionStartDate').text = (
            sc['selection_start_date'].strftime(DATE_FORMAT)
        )
        SubElement(period, 'SelectionEndDate').text = (
            sc['selection_end_date'].strftime(DATE_FORMAT)
        )
        return header

    def _build_master_files(self):

        mf = self.isaf['master_files']
        cs = mf.get('customers', [])
        ss = mf.get('suppliers', [])

        master = Element('MasterFiles')
        customers = SubElement(master, 'Customers')
        for c in cs:
            customers.append(self._build_customer_supplier(
                c, 'Customer', 'CustomerID', 'customer_id')
            )
        suppliers = SubElement(master, 'Suppliers')
        for s in ss:
            suppliers.append(self._build_customer_supplier(
                s, 'Suppliers', 'SupplierID', 'supplier_id')
            )

    def _build_source_documents(self):
        sd = self.isaf['source_documents']
        pi = sd.get('purchase_invoices', [])

        elem = Element('SourceDocuments')
        purchase_invoices = SubElement(elem, 'PurchaseInvoices')
        for i in pi:
            purchase_invoices.append(
                self._build_purchase_invoice(i)
            )

    def _build_purchase_invoice(self, inv):
        elem = Element('Invoice')
        SubElement(elem, 'InvoiceNo').text = inv['invoice_no']
        elem.append(self._build_customer_supplier(
            inv['supplier_info'], 'SupplierInfo', 'SupplierID', 'supplier_id')
        )
        SubElement(elem, 'InvoiceDate').text = inv['invoice_date'].strftime(
            DATE_FORMAT
        )
        SubElement(elem, 'InvoiceType').text = inv['invoice_type']
        SubElement(elem, 'SpecialTaxation').text = inv['special_taxation']

        refs = inv.get('references', [])
        ref_elem = SubElement(elem, 'References')
        for r in refs:
            ref_elem.append(self._build_invoice_reference(r))

        SubElement(elem, 'VATPointDate').text = inv['vat_point_date'].strftime(
            DATE_FORMAT
        )
        SubElement(elem, 'RegistrationAccountDate').text = (
            inv['registration_account_date'].strftime(DATE_FORMAT)
        )
        return elem

    def _build_customer_supplier(self, cs, tag, id_tag, id_field):
        elem = Element(tag)
        SubElement(elem, id_tag).text = cs[id_field]
        SubElement(elem, 'VATRegistrationNumber').text = (
            cs['vat_registration_number'] or ''
        )
        SubElement(elem, 'RegistrationNumber').text = (
            cs['registration_number'] or ''
        )
        SubElement(elem, 'Country').text = cs['country']
        SubElement(elem, 'Name').text = cs['name']
        return elem

    def _build_isaf_file(self):
        isaf_file = Element('iSAFFile')
        header = self._build_header()
        isaf_file.append(header)
        return isaf_file
