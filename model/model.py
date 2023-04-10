import pandas as pd
import xml.etree.ElementTree as ET

class XmlToXlsxConverter:
    def __init__(self, xml_file_path, tags_list):
        self.xml_file_path = xml_file_path
        self.tags_list = tags_list

    def _extract_data(self):
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        data = []
        for child in root:
            row = {}
            for tag in self.tags_list:
                element = child.find(tag)
                if element is not None:
                    row[tag] = element.text
                else:
                    row[tag] = ""
            data.append(row)
        return data

    def convert(self, output_path):
        data = self._extract_data()
        df = pd.DataFrame(data)
        df.to_excel(output_path, index=False)
