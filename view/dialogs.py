from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import pyqtSignal

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
    directory_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.label = QLabel("Seleccione el directorio:", self)
        self.label.setStyleSheet("font-size: 14px; color: #000000;")

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
        self.process_button.setEnabled(False)

        self.directory_button.clicked.connect(self.select_directory)
        self.process_button.clicked.connect(self.process_directory)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.directory_button)
        layout.addWidget(self.process_button)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Seleccionar directorio", "", QFileDialog.ShowDirsOnly)
        if directory:
            self.directory_selected.emit(directory)

    def process_directory(self):
        directory = self.directory_label.text()
        self.directory_selected.emit(directory)
        self.close()

class FileDialog(QDialog):
    file_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.label = QLabel("Seleccione el archivo:", self)
        self.label.setStyleSheet("font-size: 14px; color: #000000;")

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
        self.process_button.setEnabled(False)

        self.file_button.clicked.connect(self.select_file)
        self.process_button.clicked.connect(self.process_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.file_button)
        layout.addWidget(self.process_button)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos PDF (*.pdf)")
        if file:
            self.file_selected.emit(file)

    def process_file(self):
        file = self.file_label.text()
        self.file_selected.emit(file)
        self.close()
