from aspose.pdf import Document
from aspose.pdf import ExcelSaveOptions

class PDFModel:
    def convert_pdf_to_excel(self, pdf_file, excel_file):
        try:
            document = Document(pdf_file)
            excelSaveOptions = ExcelSaveOptions()
            document.save(excel_file, excelSaveOptions)
            return True, "Archivo creado exitosamente"
        except Exception as e:
            return False, f"Error al crear el archivo: {str(e)}"
