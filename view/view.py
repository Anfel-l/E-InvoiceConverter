import dearpygui.dearpygui as dpg

class XmlToXlsxConverterView:

    def __init__(self, controller):
        self.controller = controller

        with dpg.window("Convertidor XML a XLSX"):
            dpg.add_text("Por favor, selecciona el archivo XML:")
            self.xml_file_path = dpg.add_input_text("##Ruta archivo XML", width=500)

            dpg.add_button("Buscar", callback=self.browse_xml_file)

            dpg.add_text("Tags:")
            self.tags = dpg.add_input_text("##Tags", width=500)

            dpg.add_button("Convertir", callback=self.convert_xml_to_xlsx)

            dpg.add_text("Ruta de guardado:")
            self.xlsx_file_path = dpg.add_input_text("##Ruta archivo XLSX", width=500)

            dpg.add_button("Guardar", callback=self.save_xlsx_file)
    
    def browse_xml_file(self):
        file_path = dpg.file_dialog("Selecciona archivo XML", extensions = [".xml"])
        dpg.set_value(self.xml_file_path, file_path)
    
    def convert_xml_to_xlsx(self):
        xml_file_path = dpg.get_value(self.xml_file_path)
        tags = dpg.get_value(self.tags).split(',')

        self.controller.convert(xml_file_path, tags)

        xlsx_file_path = xml_file_path.replace('.xml', '.xlsx')
        dpg.set_value(self.xlsx_file_path, xlsx_file_path)

    def save_xlsx_file(self):
        xlsx_file_path = dpg.get_value(self.xlsx_file_path)
        dpg.file_dialog_save_as("Guardar archivo xlsx", default_filename = xlsx_file_path, extensions = [".xlsx"])
    