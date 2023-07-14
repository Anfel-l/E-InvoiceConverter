from model.pdf_model import PDFModel
from model.xml_model import XMLModel

class Controller:
    def __init__(self):
        self.pdf_model = PDFModel()
        self.xml_model = XMLModel()

    def convert_pdf_to_excel(self, pdf_file, excel_file):
        return self.pdf_model.convert_pdf_to_excel(pdf_file, excel_file)

    def convert_xml_to_excel(self, directory, excel_file):
        return self.xml_model.convert_xml_to_excel(directory, excel_file)
