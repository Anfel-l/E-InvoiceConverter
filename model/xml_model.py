import os
import re
import pandas as pd
from openpyxl import load_workbook

class XMLModel:
    def find_invoice_number(self, xml):
        parent_doc_id_start = xml.find("<cbc:ParentDocumentID>")
        if parent_doc_id_start != -1:
            parent_doc_id_end = xml.find("</cbc:ParentDocumentID>", parent_doc_id_start)
            return xml[parent_doc_id_start+len("<cbc:ParentDocumentID>"):parent_doc_id_end].strip()

        prefix_start = xml.find("<sts:AuthorizedInvoices>")
        if prefix_start != -1:
            prefix_end = xml.find("</sts:AuthorizedInvoices>", prefix_start)
            prefix_section = xml[prefix_start:prefix_end]
            prefix_start = prefix_section.find("<sts:Prefix>")
            prefix_end = prefix_section.find("</sts:Prefix>", prefix_start)
            prefix = prefix_section[prefix_start+len("<sts:Prefix>"):prefix_end].strip()
            match = re.search(f"{prefix}[0-9]+", xml)
            if match:
                return match.group()

        return "No encontrado"

    def find_invoice_date(self, xml):
        date_start = xml.find("<xades:SigningTime>")
        if date_start != -1:
            date_end = xml.find("</xades:SigningTime>", date_start)
            return xml[date_start+len("<xades:SigningTime>"):date_end].strip()
        return "No encontrado"

    def find_client_info(self, xml):
        client_info_start = xml.find("<cac:PartyLegalEntity>")
        if client_info_start != -1:
            client_info_end = xml.find("</cac:PartyLegalEntity>", client_info_start)
            client_info_section = xml[client_info_start:client_info_end]
            name_start = client_info_section.find("<cbc:RegistrationName>")
            name_end = client_info_section.find("</cbc:RegistrationName>", name_start)
            nit_start = client_info_section.find("<cbc:CompanyID ")
            nit_end = client_info_section.find("</cbc:CompanyID>", nit_start)
            name = client_info_section[name_start+len("<cbc:RegistrationName>"):name_end].strip()
            nit = client_info_section[nit_start+len("<cbc:CompanyID "):nit_end].split('>')[1].strip()
            return name, nit
        return "No encontrado", "No encontrado"

    def find_total_and_iva(self, xml):
        iva_start = xml.find("<cac:TaxTotal>")
        if iva_start != -1:
            iva_end = xml.find("</cac:TaxTotal>", iva_start)
            iva_section = xml[iva_start:iva_end]
            iva_amount_start = iva_section.find("<cbc:TaxAmount ")
            iva_amount_end = iva_section.find("</cbc:TaxAmount>", iva_amount_start)
            iva_amount = iva_section[iva_amount_start+len("<cbc:TaxAmount "):iva_amount_end].split('>')[1].strip()

        total_start = xml.find("<cac:LegalMonetaryTotal>")
        if total_start != -1:
            total_end = xml.find("</cac:LegalMonetaryTotal>", total_start)
            total_section = xml[total_start:total_end]
            total_amount_start = total_section.find("<cbc:PayableAmount ")
            total_amount_end = total_section.find("</cbc:PayableAmount>", total_amount_start)
            total_amount = total_section[total_amount_start+len("<cbc:PayableAmount "):total_amount_end].split('>')[1].strip()

        return iva_amount if 'iva_amount' in locals() else "0", total_amount if 'total_amount' in locals() else "No encontrado"


    def process_xml_files(self, directory):
        results = []

        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.xml'):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        xml_content = file.read()

                    invoice_number = self.find_invoice_number(xml_content)
                    invoice_date = self.find_invoice_date(xml_content)
                    client_name, client_nit = self.find_client_info(xml_content)
                    iva, total = self.find_total_and_iva(xml_content)

                    if any(x == "No encontrado" for x in [invoice_number, invoice_date, client_name, client_nit, iva, total]):
                        error_info = f"Error en archivo: {filename}"
                    else:
                        error_info = "OK"

                    results.append({
                        "File Name": filename,
                        "Invoice Number": invoice_number,
                        "Invoice Date": invoice_date,
                        "Client Name": client_name,
                        "Client NIT": client_nit,
                        "IVA": iva,
                        "Total": total,
                        "Status": error_info
                    })

        df = pd.DataFrame(results)
        return df
    
    def adjust_column_width(self, filename):
        workbook = load_workbook(filename)
        worksheet = workbook.active

        for column in worksheet.columns:
            max_length = 0
            column = [cell for cell in column if cell.value]
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

        workbook.save(filename)

    def convert_xml_to_excel(self, directory, excel_file):
        df = self.process_xml_files(directory)
        df.to_excel(excel_file, index=False)

        self.adjust_column_width(excel_file)

        return True, f"DataFrame guardado en {excel_file}"