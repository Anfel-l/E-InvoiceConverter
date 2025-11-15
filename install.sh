#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creating env"
    python3 -m venv venv

fi

source venv/bin/activate

echo "Installing dependencies"
python3 -m pip install --upgrade pip
python3 -m pip install PyQt6
python3 -m pip install pandas
python3 -m pip install openpyxl
python3 -m pip install pyinstaller

echo "Creating executable file"
pyinstaller --onefile --windowed --name 'E-Invoice Converter' main.py
echo "Installation complete!"