from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QMainWindow, QProgressBar)
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon
from model.xml_model import XMLModel


class ConversionWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.progress_label = QLabel(self)
        self.progress_label.setText("Procesando...")
        self.progress_label.setGeometry(20, 20, 360, 30)
        self.progress_label.setStyleSheet("font-size: 16px; color: #000000;")

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 50, 360, 30)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

class DirectoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleccionar directorio")
        self.setFixedSize(400, 250)
        self.setWindowIcon(QIcon("icon.png"))

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
        options = QFileDialog.Option.ReadOnly | QFileDialog.Option.DontUseNativeDialog
        directory = QFileDialog.getExistingDirectory(self, "Seleccionar directorio", "", options=options)
        if directory:
            self.directory_label.setText(directory)
            self.process_button.setEnabled(True)

        return directory
    
    def process_directory(self):
        directory = self.directory_label.text()
        if directory:
            self.parent().process_xml_directory(directory)
        self.close()

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Business Laboratory: Conversion App")
        self.setFixedSize(400, 210)
        self.setWindowIcon(QIcon("icon.png"))

        self.controller = controller

        self.label = QLabel(self)
        self.label.setGeometry(20, 20, 360, 30)
        self.label.setText("Seleccione la acción que desea realizar:")
        self.label.setStyleSheet("font-size: 16px; color: #000000;")

        self.xml_button = QPushButton(self)
        self.xml_button.setGeometry(20, 70, 360, 50)
        self.xml_button.setText("Convertir XML a Excel")
        self.xml_button.setStyleSheet("""
            font-size: 16px;
            height: 50px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """)
        self.xml_button.clicked.connect(self.convert_xml)

        self.info_button = QPushButton(self)
        self.info_button.setGeometry(20, 140, 160, 40)
        self.info_button.setText("Información")
        self.info_button.setStyleSheet("""
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """)
        self.info_button.clicked.connect(self.show_info)

        self.exit_button = QPushButton(self)
        self.exit_button.setGeometry(220, 140, 160, 40)
        self.exit_button.setText("Salir")
        self.exit_button.setStyleSheet("""
            font-size: 14px;
            height: 40px;
            background-color: #4b8da0;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            """)
        self.exit_button.clicked.connect(self.close)

    def show_info(self):
        QMessageBox.information(self, "Información",
                                "Bienvenido a Business Laboratory: Conversion App\n\n"
                                "Esta aplicación le permite convertir archivos XML a formato Excel.\n\n"
                                "Para convertir un directorio de archivos XML, haga clic en 'Convertir XML a Excel' y seleccione el directorio.\n\n"
                                "Una vez seleccionado el directorio, haga clic en 'Procesar' para iniciar la conversión.\n\n"
                                "Para mayor información contacte con: anfellr11@gmail.com",
                                QMessageBox.StandardButton.Ok) 

    def convert_xml(self):
        self.directory_dialog = DirectoryDialog(self)
        self.directory_dialog.exec()

    def process_xml_directory(self, directory):
        if directory:
            destination, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos Excel (*.xlsx)")
            if destination:
                success, message = self.controller.convert_xml_to_excel(directory, destination)
                if success:
                    QMessageBox.information(self, "Proceso completado", "La conversión de XML se ha completado con éxito.")
                else:
                    QMessageBox.critical(self, "Error", f"Error al convertir los archivos XML: {message}")

    def set_theme(self):
        if self.dark_mode:
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

    def set_directory(self, directory):
    
        if directory:
            destination, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos Excel (*.xlsx)")
            if destination:
                success, message = self.controller.convert_xml_to_excel(directory, destination)
                if success:
                    QMessageBox.information(self, "Proceso completado", "La conversión de XML se ha completado con éxito.")
                else:
                    QMessageBox.critical(self, "Error", f"Error al convertir los archivos XML: {message}")
                    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
            
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Cerrar", "¿Estás seguro de que quieres cerrar la aplicación?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
