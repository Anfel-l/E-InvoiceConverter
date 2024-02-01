#!/bin/bash
python.exe -m pip install pyinstaller
pyinstaller --onefile --windowed --name 'E-Invoice Converter' main.py
