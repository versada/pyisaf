# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyisaf.builder.base import DATE_FORMAT, ISAFBuilder

from xml.etree.ElementTree import Element, SubElement


def date_or_empty(v):
    return '' if v is None else v.strftime(DATE_FORMAT)


def int_or_empty(v):
    return '%d' % v if v else ''


def str_or_empty(v):
    return '' if v is None else v


def date_or_nil(elem, value):
    if value is None:
        elem.set('xsi:nil', 'true')
    else:
        elem.text = value.strftime(DATE_FORMAT)


def int_or_nil(elem, value):
    if value is None:
        elem.set('xsi:nil', 'true')
    else:
        elem.text = '%d' % value


def str_or_nil(elem, value):
    if value is None:
        elem.set('xsi:nil', 'true')
    else:
        elem.text = value


class ISAF1_2Builder(ISAFBuilder):
    ISAF_VERSION = '1.2'

    namespaces = {
        '': 'http://www.vmi.lt/cms/imas/isaf',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    }

    def _build_header(self):
        h = self.isaf['header']
        fd = h['file_description']
        sc = fd['selection_criteria']

        header = Element('Header')
        file_desc = SubElement(header, 'FileDescription')
        SubElement(file_desc, 'FileVersion').text = fd['file_version']
        SubElement(file_desc, 'FileDateCreated').text = (
            fd['file_date_created'].replace(microsecond=0).isoformat()
        )
        SubElement(file_desc, 'DataType').text = fd['data_type']
        SubElement(file_desc, 'SoftwareCompanyName').text = (
            fd['software_company_name']
        )
        SubElement(file_desc, 'SoftwareName').text = fd['software_name']
        SubElement(file_desc, 'SoftwareVersion').text = fd['software_version']
        SubElement(file_desc, 'RegistrationNumber').text = (
            int_or_empty(fd['registration_number'])
        )
        int_or_nil(
            SubElement(file_desc, 'NumberOfParts'), fd.get('number_of_parts'))
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

        elem = Element('MasterFiles')

        if cs:
            customers = SubElement(elem, 'Customers')
            for c in cs:
                customers.append(self._build_customer_supplier(
                    c, 'Customer', 'CustomerID', 'customer_id')
                )
        if ss:
            suppliers = SubElement(elem, 'Suppliers')
            for s in ss:
                suppliers.append(self._build_customer_supplier(
                    s, 'Supplier', 'SupplierID', 'supplier_id')
                )
        return elem

    def _build_source_documents(self):
        sd = self.isaf['source_documents']
        pis = sd.get('purchase_invoices', [])
        sis = sd.get('sales_invoices', [])
        sps = sd.get('settlements_and_payments', [])

        elem = Element('SourceDocuments')
        if pis:
            pis_elem = SubElement(elem, 'PurchaseInvoices')
            for pi in pis:
                pis_elem.append(self._build_purchase_invoice(pi))

        if sis:
            sis_elem = SubElement(elem, 'SalesInvoices')
            for si in sis:
                sis_elem.append(self._build_sales_invoice(si))

        if sps:
            sps_elem = SubElement(elem, 'SettlementsAndPayments')
            for sp in sps:
                sps_elem.append(self._build_settlement_and_payment(sp))

        return elem

    def _build_settlement_and_payment(self, sp):
        elem = Element('SettlementAndPayment')
        SubElement(elem, 'SettlementType').text = sp['settlement_type']
        SubElement(elem, 'SettlementRefNo').text = sp['settlement_ref_no']
        SubElement(elem, 'SettlementDate').text = (
            sp['settlement_date'].strftime(DATE_FORMAT)
        )
        elem.append(self._build_payment(sp['payment']))
        inv_ref_elem = SubElement(elem, 'ReferencesToInvoice')
        for inv_ref in sp.get('references_to_invoice', []):
            inv_ref_elem.append(self._build_payment_invoice_reference(inv_ref))
        return elem

    def _build_payment(self, p):
        elem = Element('Payment')
        sc_id = SubElement(elem, 'SupplierCustomerID')
        if p.get('supplier_customer_id'):
            sc_id.text = p['supplier_customer_id']
        SubElement(elem, 'vat_registration_number').text = (
            p['vat_registration_number'])
        rn = SubElement(elem, 'RegistrationNumber')
        if p.get('registration_number'):
            rn.text = p['registration_number']
        str_or_nil(SubElement(elem, 'Country'), p.get('country'))
        SubElement(elem, 'Name').text = str_or_empty(p.get('name'))
        return elem

    def _build_payment_invoice_reference(self, inv_ref):
        elem = Element('ReferenceToInvoice')
        SubElement(elem, 'InvoiceNo').text = inv_ref['invoice_no']
        SubElement(elem, 'InvoiceDate').text = (
            inv_ref['invoice_date'].strftime(DATE_FORMAT)
        )
        SubElement(elem, 'Amount').text = inv_ref['amount']
        SubElement(elem, 'VATAmount').text = inv_ref['vat_amount']
        return elem

    def _build_invoice_reference(self, ref):
        elem = Element('Reference')
        SubElement(elem, 'ReferenceNo').text = ref['reference_no']
        SubElement(elem, 'ReferenceDate').text = (
            ref['reference_date'].strftime(DATE_FORMAT)
        )
        return elem

    def _build_purchase_invoice_total(self, t):
        elem = Element('DocumentTotal')
        SubElement(elem, 'TaxableValue').text = t['taxable_value']
        str_or_nil(SubElement(elem, 'TaxCode'), t.get('tax_code'))
        str_or_nil(SubElement(elem, 'TaxPercentage'), t.get('tax_percentage'))
        str_or_nil(SubElement(elem, 'Amount'), t.get('amount'))
        return elem

    def _build_sales_invoice_total(self, t):
        elem = Element('DocumentTotal')
        SubElement(elem, 'TaxableValue').text = t['taxable_value']
        str_or_nil(SubElement(elem, 'TaxCode'), t.get('tax_code'))
        str_or_nil(SubElement(elem, 'TaxPercentage'), t.get('tax_percentage'))
        str_or_nil(SubElement(elem, 'Amount'), t.get('amount'))
        date_or_nil(
            SubElement(elem, 'VATPointDate2'), t.get('vat_point_date2'))
        return elem

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

        vat_point_date_elem = SubElement(elem, 'VATPointDate')
        date_or_nil(vat_point_date_elem, inv.get('vat_point_date'))

        registration_account_date_elem = SubElement(
            elem, 'RegistrationAccountDate')
        date_or_nil(
            registration_account_date_elem,
            inv.get('registration_account_date'),
        )

        totals = SubElement(elem, 'DocumentTotals')
        for t in inv.get('document_totals', []):
            totals.append(self._build_purchase_invoice_total(t))
        return elem

    def _build_sales_invoice(self, inv):
        elem = Element('Invoice')
        SubElement(elem, 'InvoiceNo').text = inv['invoice_no']
        elem.append(self._build_customer_supplier(
            inv['customer_info'], 'CustomerInfo', 'CustomerID', 'customer_id')
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

        vat_point_date_elem = SubElement(elem, 'VATPointDate')
        date_or_nil(vat_point_date_elem, inv.get('vat_point_date'))

        totals = SubElement(elem, 'DocumentTotals')
        for t in inv.get('document_totals', []):
            totals.append(self._build_sales_invoice_total(t))
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
        str_or_nil(SubElement(elem, 'Country'), cs.get('country'))
        SubElement(elem, 'Name').text = cs['name']
        return elem
