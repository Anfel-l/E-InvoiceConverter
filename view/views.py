import os
import re
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QAction, QDialog, QVBoxLayout, QHBoxLayout, QProgressBar

class ConversionThread(QThread):
    progress_update = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, controller, source, destination):
        super().__init__()
        self.controller = controller
        self.source = source
        self.destination = destination

    def run(self):
        success, message = self.controller.convert_pdf_to_excel(self.source, self.destination)
        if success:
            self.finished.emit()
        else:
            self.progress_update.emit(-1)  # Emitir un valor negativo para indicar un error
            self.finished.emit()

class DirectoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar directorio")
        self.setFixedSize(400, 250)  # Establecer un tamaño fijo para la ventana
        self.setWindowIcon(QIcon("icon.png"))  # Agregar un icono a la ventana

        self.label = QLabel("Seleccione el directorio:", self)
        self.label.setStyleSheet("font-size: 14px; color: #000000;")

        self.directory_label = QLabel("", self)
        self.directory_label.setStyleSheet(
            """
            background-color: #ffffff;
            border: 1px solid #c0c0c0;
            padding: 5px;
            color: #000000;
            """
        )

        self.directory_button = QPushButton("Seleccionar directorio", self)
        self.directory_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.directory_button.clicked.connect(self.select_directory)

        self.process_button = QPushButton("Procesar", self)
        self.process_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.process_button.clicked.connect(self.process_directory)
        self.process_button.setEnabled(False)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.directory_label)
        layout.addWidget(self.directory_button)
        layout.addWidget(self.process_button)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Seleccionar directorio", "", QFileDialog.ShowDirsOnly)
        if directory:
            self.directory_label.setText(directory)
            self.process_button.setEnabled(True)

    def process_directory(self):
        directory = self.directory_label.text()
        self.parent().set_directory(directory)
        self.close()

class FileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar archivo")
        self.setFixedSize(400, 250)  # Establecer un tamaño fijo para la ventana
        self.setWindowIcon(QIcon("icon.png"))  # Agregar un icono a la ventana

        self.label = QLabel("Seleccione el archivo:", self)
        self.label.setStyleSheet("font-size: 14px; color: #000000;")

        self.file_label = QLabel("", self)
        self.file_label.setStyleSheet(
            """
            background-color: #ffffff;
            border: 1px solid #c0c0c0;
            padding: 5px;
            color: #000000;
            """
        )

        self.file_button = QPushButton("Seleccionar archivo", self)
        self.file_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.file_button.clicked.connect(self.select_file)

        self.process_button = QPushButton("Procesar", self)
        self.process_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.process_button.clicked.connect(self.process_file)
        self.process_button.setEnabled(False)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_button)
        layout.addWidget(self.process_button)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos PDF (*.pdf)")
        if file:
            self.file_label.setText(file)
            self.process_button.setEnabled(True)

    def process_file(self):
        file = self.file_label.text()
        self.parent().set_file(file)
        self.close()

class ConversionWindow(QMainWindow):
    def __init__(self, controller, source, destination):
        super().__init__()
        self.setWindowTitle("Procesando...")
        self.setFixedSize(400, 150)  # Establecer un tamaño fijo para la ventana
        self.setWindowIcon(QIcon("icon.png"))  # Agregar un icono a la ventana

        self.controller = controller
        self.source = source
        self.destination = destination

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 50, 360, 30)
        self.progress_bar.setValue(0)

        self.thread = ConversionThread(self.controller, self.source, self.destination)
        self.thread.progress_update.connect(self.update_progress)
        self.thread.finished.connect(self.process_finished)

        self.thread.start()

    def update_progress(self, value):
        if value >= 0:
            self.progress_bar.setValue(value)
        else:
            self.progress_bar.reset()

    def process_finished(self):
        QMessageBox.information(self, "Proceso completado", "La conversión se ha completado con éxito.")
        self.close()

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Business Laboratory: Conversion App")
        self.setFixedSize(400, 300)  # Establecer un tamaño fijo para la ventana
        self.setWindowIcon(QIcon("icon.png"))  # Agregar un icono a la ventana

        self.controller = controller

        self.label = QLabel(self)
        self.label.setGeometry(20, 20, 360, 30)
        self.label.setText("Seleccione la acción que desea realizar:")
        self.label.setStyleSheet("font-size: 16px; color: #000000;")

        self.pdf_button = QPushButton(self)
        self.pdf_button.setGeometry(20, 70, 360, 50)
        self.pdf_button.setText("Convertir PDF a Excel")
        self.pdf_button.setStyleSheet(
            """
            font-size: 16px;
            height: 50px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.pdf_button.clicked.connect(self.convert_pdf)

        self.xml_button = QPushButton(self)
        self.xml_button.setGeometry(20, 140, 360, 50)
        self.xml_button.setText("Convertir XML a Excel")
        self.xml_button.setStyleSheet(
            """
            font-size: 16px;
            height: 50px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.xml_button.clicked.connect(self.convert_xml)

        self.info_button = QPushButton(self)
        self.info_button.setGeometry(20, 210, 160, 40)
        self.info_button.setText("Información")
        self.info_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.info_button.clicked.connect(self.show_info)

        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(220, 210, 160, 40)
        self.exit_button.setText("Salir")
        self.exit_button.setStyleSheet(
            """
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """
        )
        self.exit_button.clicked.connect(self.close)

        self.dark_mode = False
        self.set_theme()

    def show_info(self):
        info_dialog = QMessageBox()
        info_dialog.setWindowTitle("Información")
        info_dialog.setText(
            "Bienvenido a Business Laboratory: Conversion App\n\n"
            "Esta aplicación le permite convertir archivos PDF y XML a formato Excel.\n\n"
            "Para convertir un archivo PDF, haga clic en 'Convertir PDF a Excel' y seleccione el archivo PDF.\n\n"
            "Para convertir un directorio de archivos XML, haga clic en 'Convertir XML a Excel' y seleccione el directorio.\n\n"
            "Una vez seleccionado el archivo o directorio, haga clic en 'Procesar' para iniciar la conversión.\n\n"
            "El progreso de la conversión se mostrará en la barra de progreso.\n\n"
            "¡Disfrute utilizando Business Laboratory: Conversion App!"
        )
        info_dialog.setIcon(QMessageBox.Information)
        info_dialog.exec_()

    def convert_pdf(self):
        self.file_dialog = FileDialog(self)
        self.file_dialog.exec_()

    def convert_xml(self):
        self.directory_dialog = DirectoryDialog(self)
        self.directory_dialog.exec_()

    def set_file(self, file):
        self.selected_file = file
        if self.selected_file:
            destination, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos Excel (*.xlsx)")
            if destination:
                self.conversion_window = ConversionWindow(self.controller, self.selected_file, destination)
                self.conversion_window.show()

    def set_directory(self, directory):
            self.selected_directory = directory
            if self.selected_directory:
                destination, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos Excel (*.xlsx)")
                if destination:
                    success, message = self.controller.convert_xml_to_excel(self.selected_directory, destination)
                    if success:
                        QMessageBox.information(self, "Proceso completado", "La conversión se ha completado con éxito.")
                    else:
                        QMessageBox.critical(self, "Error", f"Error al convertir los archivos: {message}")

    def set_theme(self):
        if self.dark_mode:
            # Tema oscuro
            self.setStyleSheet(
                """
                QMainWindow {
                    background-color: #303030;
                }
                QLabel {
                    color: #ffffff;
                }
                QPushButton {
                    background-color: #4b8da0;
                    color: #ffffff;
                    border: none;
                    border-radius: 5px;
                }
                """
            )
        else:
            # Tema claro
            self.setStyleSheet(
                """
                QMainWindow {
                    background-color: #f0f0f0;
                }
                QLabel {
                    color: #000000;
                }
                QPushButton {
                    background-color: #4b8da0;
                    color: #ffffff;
                    border: none;
                    border-radius: 5px;
                }
                """
            )

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Cerrar", "¿Estás seguro de que quieres cerrar la aplicación?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
