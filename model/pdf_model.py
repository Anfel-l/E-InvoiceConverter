import os
import re
import pandas as pd
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

class PDFModel:
    def convert_pdf_to_excel(self, pdf_file, excel_file):
        try:
            # Extraer texto del PDF utilizando pdfminer
            text = extract_text(pdf_file, laparams=LAParams())

            # Convertir el texto en una lista de líneas
            lines = text.split('\n')

            # Filtrar las líneas para eliminar líneas vacías y espacios en blanco
            lines = [line.strip() for line in lines if line.strip()]

            # Separar los datos de las facturas
            # Aquí necesitarás implementar una lógica específica para tu caso, ya que cada factura puede tener un formato diferente
            # En este ejemplo, simplemente se dividen las líneas en bloques de 5 líneas cada uno
            data = [lines[i:i+5] for i in range(0, len(lines), 5)]

            # Crear un DataFrame de pandas con los datos extraídos
            df = pd.DataFrame(data, columns=['Columna 1', 'Columna 2', 'Columna 3', 'Columna 4', 'Columna 5'])

            # Guardar el DataFrame en un archivo Excel
            df.to_excel(excel_file, index=False)

            return True, "Archivo creado exitosamente"
        except Exception as e:
            return False, f"Error al crear el archivo: {str(e)}"
