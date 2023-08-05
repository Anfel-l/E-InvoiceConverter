import os
import re
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


class XMLModel:
    def convert_xml_to_excel(self, directory, excel_file):
        workbook = Workbook()
        sheet = workbook.active

        columnas = {
            "NumFac": "B",
            "NroFactura": "B",
            "NitFac": "C",
            "NitFacturador": "C",
            "FecFac": "D",
            "FechaFactura": "D",
            "HorFac": "E",
            "HoraFactura": "E",
            "ValFac": "F",
            "ValorFactura": "F",
            "ValIva": "G",
            "ValorIVA": "G",
            "ValOtroIm": "H",
            "ValorOtrosImpuestos": "H",
            "ValTolFac": "I",
            "ValorTotalFactura": "I",
            "NitAdquiriente": "J/K",
            "DocAdq": "J/K"
        }

        nombres_columnas = [
            "NumFac/NroFactura", "NitFac/NitFacturador", "FecFac/FechaFactura",
            "HorFac/HoraFactura", "ValFac/ValorFactura", "ValIva/ValorIVA",
            "ValOtroIm/ValorOtrosImpuestos", "ValTolFac/ValorTotalFactura",
            "NitAdquiriente/DocAdq"
        ]

        for i, nombre_columna in enumerate(nombres_columnas, start=1):
            sheet.cell(row=1, column=i, value=nombre_columna).font = sheet.cell(row=1, column=i).font.copy(bold=True)

        archivos_xml = [archivo for archivo in os.listdir(directory) if archivo.endswith(".xml")]
        archivos_omitidos = []

        for archivo_xml in archivos_xml:
            valores_archivo = []

            with open(os.path.join(directory, archivo_xml), "r", encoding="utf-8") as file:
                contenido = file.read()

            etiqueta = re.search(r"<sts:QRCode>(.*?)</sts:QRCode>", contenido)

            if etiqueta:
                contenido_etiqueta = etiqueta.group(1)
                etiquetas = re.findall(r'(\w+)=(\S+)', contenido_etiqueta)
                etiquetas = [(clave, valor) for clave, valor in etiquetas if "CUFE" not in valor and "QRCode" not in valor]

                nit_adquiriente = next((valor for clave, valor in etiquetas if clave in ["NitAdquiriente", "DocAdq"]), "")
                doc_adq = next((valor for clave, valor in etiquetas if clave in ["NitAdquiriente", "DocAdq"]), "")

                for columna in columnas.values():
                    valor = next((valor for clave, valor in etiquetas if columnas.get(clave) == columna), "")

                    if valor not in valores_archivo:
                        valores_archivo.append(valor)

            if any(valores_archivo):
                sheet.append(valores_archivo)
            else:
                archivos_omitidos.append(archivo_xml)

        for columna in sheet.columns:
            max_length = 0
            column_letter = get_column_letter(columna[0].column)
            for celda in columna:
                if celda.value:
                    try:
                        if len(str(celda.value)) > max_length:
                            max_length = len(str(celda.value))
                    except:
                        pass
            adjusted_width = (max_length + 2) * 1.2  # Aumentar el ancho ajustado en un factor de 1.2
            sheet.column_dimensions[column_letter].width = adjusted_width

        # Agregar los nombres de los archivos omitidos en una columna al final, dos columnas después de la última con información
        columna_omitidos = get_column_letter(13)  # Columna M
        sheet.column_dimensions[columna_omitidos].width = 20  # Ajustar el ancho de la columna
        sheet.cell(row=1, column=13, value="Archivos no convertidos").font = sheet.cell(row=1, column=13).font.copy(bold=True)
        for i, archivo_omitido in enumerate(archivos_omitidos, start=2):
            sheet.cell(row=i, column=13, value=archivo_omitido)

        workbook.save(excel_file)
        return True, "Archivos XML convertidos a Excel"
