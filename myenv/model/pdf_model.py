import aspose.pdf as pdf

class PDFModel:
    def convert_pdf_to_excel(self, pdf_file, excel_file):
        try:
            document = pdf.Document(pdf_file)
            excelSaveOptions = pdf.ExcelSaveOptions()
            document.save(excel_file, excelSaveOptions)
            return True, "Archivo Creado de Manera Exitosa"
        except Exception as e:
            return False, f"Error al crear el archivo: {str(e)}"
