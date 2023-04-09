import dearpygui.dearpygui as dpg
from controller.controller import XmlToXlsxConverterController


class XmlToXlsxConverterView:
    def __init__(self):
        self.controller = XmlToXlsxConverterController(self)

        with dpg.window("XML to XLSX Converter"):
            dpg.add_text("Select XML File:")
            self.xml_file_path = dpg.add_input_text("##XML_FILE_PATH", width=500)

            dpg.add_button("Browse", callback=self.browse_xml_file)

            dpg.add_text("Tags:")
            self.tags = dpg.add_input_text("##TAGS", width=500)

            dpg.add_button("Convert", callback=self.convert_xml_to_xlsx)

            dpg.add_text("Output File:")
            self.xlsx_file_path = dpg.add_input_text("##XLSX_FILE_PATH", width=500)

            dpg.add_button("Save", callback=self.save_xlsx_file)

    def browse_xml_file(self):
        file_path = dpg.file_dialog(label="Select XML File", extensions=[".xml"])
        dpg.set_value(self.xml_file_path, file_path)

    def convert_xml_to_xlsx(self):
        xml_file_path = dpg.get_value(self.xml_file_path)
        tags = dpg.get_value(self.tags).split(',')

        self.controller.convert(xml_file_path, tags)

        xlsx_file_path = xml_file_path.replace('.xml', '.xlsx')
        dpg.set_value(self.xlsx_file_path, xlsx_file_path)

    def save_xlsx_file(self):
        xlsx_file_path = dpg.get_value(self.xlsx_file_path)
        dpg.file_dialog(label="Save XLSX File", default_filename=xlsx_file_path, extensions=[".xlsx"])
