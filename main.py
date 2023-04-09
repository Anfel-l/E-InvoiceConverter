import dearpygui.dearpygui as dpg
from view.view import XmlToXlsxConverterView


if __name__ == '__main__':
    with dpg.window():
        view = XmlToXlsxConverterView()
    dpg.start_dearpygui()
