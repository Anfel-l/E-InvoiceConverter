@echo off
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name "E-Invoice Converter" main.py
pause
