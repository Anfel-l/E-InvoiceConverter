from model.xml_model import XMLModel

class Controller:
    def __init__(self):
        self.xml_model = XMLModel()
        
    def convert_xml_to_excel(self, directory, excel_file):
        return self.xml_model.convert_xml_to_excel(directory, excel_file)
