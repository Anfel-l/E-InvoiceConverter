import aspose.pdf as ap

class PDFModel:
    def convert_pdf_to_excel(self, pdf_file, excel_file):
        try:
            # Crear un objeto de tipo Document
            doc = ap.Document(pdf_file)

            # Crear un objeto de tipo ExcelSaveOptions
            excel_save_options = ap.ExcelSaveOptions()

            # Guardar el archivo PDF como Excel
            doc.save(excel_file, excel_save_options)

            return True, "Archivo creado exitosamente"
        except Exception as e:
            return False, f"Error al crear el archivo: {str(e)}"
