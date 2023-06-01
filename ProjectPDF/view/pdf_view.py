from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox, QVBoxLayout, QDialog, QPushButton, QProgressBar, QGridLayout

class PDFView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Business Laboratory: PDF to Excel")
        self.setFixedSize(500, 250)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#F4F5F0"))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor("#E6DFD7"))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor("#424953"))

        self.setPalette(palette)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.button_select_pdf = QtWidgets.QPushButton("Seleccionar Factura (PDF)")
        self.button_select_pdf.clicked.connect(self.select_pdf_file)
        self.button_select_pdf.setFixedHeight(40)

        self.button_save_excel = QtWidgets.QPushButton("Guardar Excel")
        self.button_save_excel.clicked.connect(self.save_excel_file)
        self.button_save_excel.setEnabled(False)
        self.button_save_excel.setFixedHeight(40)

        self.button_exit = QtWidgets.QPushButton("Salir")
        self.button_exit.clicked.connect(self.exit_application)
        self.button_exit.setFixedHeight(40)

        self.button_info = QtWidgets.QPushButton("Información")
        self.button_info.clicked.connect(self.show_information)
        self.button_info.setFixedHeight(40)
        
        self.label_pdf_file = QLabel()
        self.label_pdf_file.setStyleSheet("border: 1px solid black")
        self.label_pdf_file.setFixedHeight(40)

        self.label_excel_file = QLabel()
        self.label_excel_file.setStyleSheet("border: 1px solid black")
        self.label_excel_file.setFixedHeight(40)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setStyleSheet("QProgressBar { background-color: #C4C9CD; }")

        grid_layout.addWidget(self.button_select_pdf, 0, 0)
        grid_layout.addWidget(self.label_pdf_file, 0, 1, 1, 3)
        grid_layout.addWidget(self.button_save_excel, 1, 0)
        grid_layout.addWidget(self.label_excel_file, 1, 1, 1, 3)
        grid_layout.addWidget(self.button_info, 2, 3)
        grid_layout.addWidget(self.button_exit, 2, 0)
        grid_layout.addWidget(self.progress_bar, 3, 0, 1, 4)

        self.file_path = ""
        self.output_path = ""

        self.show_instructions_dialog()

    def show_instructions_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Instrucciones")
        dialog.setFixedSize(400, 200)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#F4F5F0"))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor("#E6DFD7"))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor("#424953"))

        dialog.setPalette(palette)

        layout = QVBoxLayout()
        label = QLabel("Instrucciones:\n\n1. Haz clic en 'Seleccionar PDF' para elegir un archivo PDF.\n2. Haz clic en 'Guardar Excel' para elegir la ubicación y el nombre del archivo Excel de salida.\n3. Haz clic en 'Convertir' para realizar la conversión.\n\nNota: El archivo Excel de salida se guardará en la misma ubicación que el archivo PDF de entrada.")
        layout.addWidget(label)

        button_ok = QPushButton("OK", dialog)
        button_ok.clicked.connect(dialog.close)
        button_ok.setFixedHeight(40)

        layout.addWidget(button_ok)
        dialog.setLayout(layout)

        dialog.exec_()

    def select_pdf_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar la factura en formato PDF", "", "PDF Files (*.pdf)", options=options)

        if file_path:
            self.file_path = file_path
            self.output_path = ""
            self.label_pdf_file.setText(file_path)
            self.button_save_excel.setEnabled(True)

    def save_excel_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Excel Files (*.xlsx)", options=options)

        if file_path:
            self.output_path = file_path
            self.label_excel_file.setText(file_path)
            self.button_save_excel.setEnabled(False)
            self.convert_pdf_to_excel()

    def convert_pdf_to_excel(self):
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        # Simulating the conversion process
        total_steps = 1000
        for step in range(total_steps):
            QtCore.QCoreApplication.processEvents()
            progress = int((step / total_steps) * 100)
            self.progress_bar.setValue(progress)

        self.progress_bar.setVisible(False)

        success, message = self.controller.convert_pdf_to_excel(self.file_path, self.output_path)
        self.display_message(message)

        if success:
            reply = QMessageBox.question(self, "Convertir", "¿Quieres realizar otra conversión?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.button_save_excel.setEnabled(True)
                self.file_path = ""
                self.output_path = ""
                self.label_pdf_file.setText("")
                self.label_excel_file.setText("")
            else:
                self.exit_application()

    def exit_application(self):
        reply = QMessageBox.question(self, "Salir", "¿Deseas Cerrar el Programa?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QtWidgets.qApp.quit()

    def show_information(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Información")
        dialog.setFixedSize(300, 150)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#F4F5F0"))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor("#E6DFD7"))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor("#424953"))

        dialog.setPalette(palette)

        layout = QVBoxLayout()
        label = QLabel("Este es un programa para convertir archivos PDF a Excel.")
        layout.addWidget(label)

        button_close = QPushButton("Cerrar", dialog)
        button_close.clicked.connect(dialog.close)
        button_close.setFixedHeight(40)

        layout.addWidget(button_close)
        dialog.setLayout(layout)

        dialog.exec_()

    def display_message(self, message):
        QMessageBox.information(self, "Information", message)
