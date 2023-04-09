from model import XmlToXlsxConverter
from view import XmlToXlsxConverterView

class XmlToXlsxConverterController:

    def __init__(self):
        self.converter = XmlToXlsxConverter()
        self.view = XmlToXlsxConverterView(self)

    def convert(self, xml_file_path, tags):
        self.converter.set_tags(tags)
        return self.converter.convert(xml_file_path)

