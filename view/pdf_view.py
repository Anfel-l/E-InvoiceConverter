from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox

class PDFView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PDF to Excel Converter")
        self.setGeometry(100, 100, 800, 600)

        self.button_select_pdf = QtWidgets.QPushButton("Select PDF", self)
        self.button_select_pdf.setGeometry(20, 20, 120, 40)
        self.button_select_pdf.clicked.connect(self.select_pdf_file)

        self.button_save_excel = QtWidgets.QPushButton("Save Excel", self)
        self.button_save_excel.setGeometry(20, 80, 120, 40)
        self.button_save_excel.clicked.connect(self.save_excel_file)
        self.button_save_excel.setEnabled(False)

        self.button_exit = QtWidgets.QPushButton("Exit", self)
        self.button_exit.setGeometry(20, 140, 120, 40)
        self.button_exit.clicked.connect(self.exit_application)

        self.label_pdf_file = QLabel("Selected PDF: None", self)
        self.label_pdf_file.setGeometry(150, 20, 400, 40)

        self.label_excel_file = QLabel("Output Excel: None", self)
        self.label_excel_file.setGeometry(150, 80, 400, 40)

        self.file_path = ""
        self.output_path = ""

    def select_pdf_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)", options=options)

        if file_path:
            self.file_path = file_path
            self.output_path = ""
            self.label_pdf_file.setText(f"Selected PDF: {file_path}")
            self.button_save_excel.setEnabled(True)

    def save_excel_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Excel File", "", "Excel Files (*.xlsx)", options=options)

        if file_path:
            self.output_path = file_path
            self.label_excel_file.setText(f"Output Excel: {file_path}")
            self.button_save_excel.setEnabled(False)
            self.convert_pdf_to_excel()

    def convert_pdf_to_excel(self):
        success, message = self.controller.convert_pdf_to_excel(self.file_path, self.output_path)
        self.display_message(message)

        if success:
            reply = QMessageBox.question(self, "Convert Another", "Do you want to convert another PDF?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.button_save_excel.setEnabled(True)
                self.file_path = ""
                self.output_path = ""
                self.label_pdf_file.setText("Selected PDF: None")
                self.label_excel_file.setText("Output Excel: None")
            else:
                self.exit_application()

    def exit_application(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.qApp.quit()

    def display_message(self, message):
        QMessageBox.information(self, "Information", message)
