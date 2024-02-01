@echo off
python -m pip install  PyQt6
python -m pip install  pandas
python -m pip install openpyxl
python -m pip install pyinstaller
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name "E-Invoice Converter" main.py
pause
