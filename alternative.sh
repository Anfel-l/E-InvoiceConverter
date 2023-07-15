#!/bin/bash

# Verificar si PyInstaller está instalado
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller no está instalado. Instalando..."
    pip install pyinstaller
fi

# Actualizar pip
echo "Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar la aplicación
echo "Ejecutando la aplicación..."
python main.py
