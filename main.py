import sys
from PyQt6.QtWidgets import QApplication
from controller.controller import Controller
from view.views import MainWindow

'''Main method for execution'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    main_window = MainWindow(controller)
    main_window.show()
    sys.exit(app.exec())
