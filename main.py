import sys
from PyQt5 import QtWidgets
from model.pdf_model import PDFModel
from view.pdf_view import PDFView
from controller.pdf_controller import PDFController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = PDFModel()
    view = PDFView()
    controller = PDFController(model, view)
    view.show()
    sys.exit(app.exec_())
