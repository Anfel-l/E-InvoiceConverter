from model.model import XmlToXlsxConverter


class XmlToXlsxConverterController:
    def __init__(self, view):
        self.converter = XmlToXlsxConverter()
        self.view = view

    def convert(self, xml_file_path, tags):
        self.converter.set_tags(tags)
        return self.converter.convert(xml_file_path)
