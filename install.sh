#!/bin/bash
python.exe -m pip install  PyQt6
python.exe -m pip install  pandas
python.exe -m pip install openpyxl
python.exe -m pip install pyinstaller
pyinstaller --onefile --windowed --name 'E-Invoice Converter' main.py
