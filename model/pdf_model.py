import os
from aspose.pdf import Document, ExcelSaveOptions

class PDFModel:
    def convert_pdfs_to_excel(self, input_dir, excel_file):
        try:
            # Obtener la lista de archivos PDF en el directorio de entrada
            pdf_files = [file for file in os.listdir(input_dir) if file.lower().endswith(".pdf")]

            # Crear un objeto de tipo ExcelWorkbook
            workbook = Document()

            for pdf_file in pdf_files:
                pdf_path = os.path.join(input_dir, pdf_file)

                # Crear un objeto de tipo Document para el archivo PDF actual
                doc = Document(pdf_path)

                # Agregar páginas del PDF actual al archivo de Excel
                for page in doc.pages:
                    workbook.pages.add(page)

            # Guardar el archivo de Excel con todas las páginas de los PDF
            excelSaveOptions = ExcelSaveOptions()
            workbook.save(excel_file, excelSaveOptions)

            return True, "Archivos creados exitosamente"
        except Exception as e:
            print(e)
            return False, f"Error al crear los archivos: {str(e)}"
