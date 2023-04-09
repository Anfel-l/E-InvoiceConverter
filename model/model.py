import pandas as pd
from xml.etree import ElementTree as et

class XmlToXlsxConverter:
    def __init__(self):
        self.tags = []

    def set_tags(self, tags):
        self.tags = tags
    
    def convert(self,xml_file_path):
        data = []
        root = et.parse(xml_file_path).getroot()

        for item in root.findall('.//*'):
            if item.tag in self.tags:
                row = [item.tag]

                for child in item:
                    row.append(child.text)

                data.append(row)
        
        df = pd.DataFrame(data)
        xlsx_file_path = xml_file_path.replace('.xml', '.xlsx')
        df.to_excel(xlsx_file_path, index = False, header = False)

        return xlsx_file_path