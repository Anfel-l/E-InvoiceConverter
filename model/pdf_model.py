import os
import pandas as pd
import threading
from aspose.pdf import Document, ExcelSaveOptions

class PDFModel:
    def convert_pdfs_to_excel(self, input_dir, output_dir):
        try:
            # Obtener la lista de archivos PDF en el directorio de entrada
            pdf_files = [file for file in os.listdir(input_dir) if file.lower().endswith(".pdf")]

            # Crear la carpeta para los archivos temporales si no existe
            os.makedirs(output_dir, exist_ok=True)

            # Dividir los archivos PDF en grupos de 4
            pdf_groups = [pdf_files[i:i + 4] for i in range(0, len(pdf_files), 4)]

            # Función para procesar un grupo de archivos PDF y guardar el resultado en un archivo de Excel temporal
            def process_group(group):
                workbook = Document()

                for pdf_file in group:
                    pdf_path = os.path.join(input_dir, pdf_file)

                    # Crear un objeto de tipo Document para el archivo PDF actual
                    doc = Document(pdf_path)

                    # Agregar páginas del PDF actual al archivo de Excel
                    for page in doc.pages:
                        workbook.pages.add(page)

                # Guardar el archivo de Excel temporal con todas las páginas de los PDF
                excel_file = os.path.join(output_dir, f"temp_{group[0]}.xlsx")
                excelSaveOptions = ExcelSaveOptions()
                workbook.save(excel_file, excelSaveOptions)

            # Crear y ejecutar un hilo para cada grupo de archivos PDF
            threads = []
            for group in pdf_groups:
                t = threading.Thread(target=process_group, args=(group,))
                threads.append(t)
                t.start()

            # Esperar a que todos los hilos terminen
            for t in threads:
                t.join()

            return True, "Archivos temporales creados exitosamente"
        except Exception as e:
            print(e)
            return False, f"Error al crear los archivos temporales: {str(e)}"

    def combine_temporales_with_pandas(self, temp_dir, excel_file):
        try:
            # Lista para almacenar DataFrames temporales
            dfs = []

            # Leer cada archivo temporal y almacenar su contenido en la lista de DataFrames
            for file in os.listdir(temp_dir):
                if file.lower().endswith(".xlsx"):
                    excel_file_path = os.path.join(temp_dir, file)
                    df = pd.read_excel(excel_file_path)
                    dfs.append(df)

            # Combinar todos los DataFrames en uno solo
            all_data = pd.concat(dfs, ignore_index=True)

            # Guardar el archivo de Excel final
            all_data.to_excel(excel_file, index=False)

            return True, "Archivos temporales combinados y creados exitosamente"
        except Exception as e:
            print(e)
            return False, f"Error al combinar los archivos temporales: {str(e)}"
