import sys
from PyQt5 import QtWidgets
from view.view import XmlToXlsxView
from controller.controller import XmlToXlsxController


app = QtWidgets.QApplication(sys.argv)
view = XmlToXlsxView()
controller = XmlToXlsxController(view)
view.show()
sys.exit(app.exec_())
