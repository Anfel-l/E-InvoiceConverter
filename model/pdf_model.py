import aspose.pdf as pdf

class PDFModel:
    def convert_pdf_to_excel(self, pdf_file, excel_file):
        try:
            document = pdf.Document(pdf_file)
            excelSaveOptions = pdf.ExcelSaveOptions()
            document.save(excel_file, excelSaveOptions)
            return True, "File created successfully"
        except Exception as e:
            return False, f"Error creating file: {str(e)}"
