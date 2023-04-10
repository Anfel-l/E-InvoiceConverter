from model.model import XmlToXlsxConverter


class XmlToXlsxController:
    def __init__(self, view):
        self.view = view

    def convert_xml_to_xlsx(self, xml_file_path, tags_list, output_path):
        converter = XmlToXlsxConverter(xml_file_path, tags_list)
        converter.convert(output_path)