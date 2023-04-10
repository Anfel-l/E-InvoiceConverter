from PyQt5 import QtWidgets

class XmlToXlsxView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.xml_file_path = None
        self.tags_list = []
        self.output_path = None

        self.xml_file_label = QtWidgets.QLabel("Select an XML file:")
        self.xml_file_button = QtWidgets.QPushButton("Select")
        self.xml_file_button.clicked.connect(self.select_xml_file)

        self.tags_label = QtWidgets.QLabel("Tags:")
        self.tags_listbox = QtWidgets.QListWidget()
        self.add_tag_button = QtWidgets.QPushButton("Add")
        self.add_tag_button.clicked.connect(self.add_tag)
        self.clear_tags_button = QtWidgets.QPushButton("Clear")
        self.clear_tags_button.clicked.connect(self.clear_tags)

        self.output_label = QtWidgets.QLabel("Output file:")
        self.output_lineedit = QtWidgets.QLineEdit()
        self.output_button = QtWidgets.QPushButton("Select")
        self.output_button.clicked.connect(self.select_output_path)

        self.convert_button = QtWidgets.QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_xml_to_xlsx)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.xml_file_label)
        layout.addWidget(self.xml_file_button)
        layout.addWidget(self.tags_label)
        layout.addWidget(self.tags_listbox)
        layout.addWidget(self.add_tag_button)
        layout.addWidget(self.clear_tags_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_lineedit)
        layout.addWidget(self.output_button)
        layout.addWidget(self.convert_button)
        self.setLayout(layout)

    def select_xml_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select XML File", "", "XML Files (*.xml)", options=options)
        if file_path:
            self.xml_file_path = file_path

    def add_tag(self):
        tag, ok = QtWidgets.QInputDialog.getText(self, "Add Tag", "Tag name:")
        if ok and tag:
            self.tags_list.append(tag)
            self.tags_listbox.addItem(tag)

    def clear_tags(self):
        self.tags_list = []
        self.tags_listbox.clear()

    def select_output_path(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save XLSX File", "", "XLSX Files (*.xlsx)", options=options)
        if file_path:
            self.output_path = file_path
            self.output_lineedit.setText(file_path)

    def convert_xml_to_xlsx(self):
        if not self.xml_file_path or not self.tags_list or not self.output_path:
            QtWidgets.QMessageBox.warning(self, "Error", "Please .fill in all required fields.")
        return self.controller.convert_xml_to_xlsx(self.xml_file_path, self.tags_list, self.output_path)
        #sQtWidgets.QMessageBox.information(self, "Success", "XML to XLSX conversion completed successfully.")

