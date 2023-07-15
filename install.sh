#!/bin/bash

# Nombre del archivo de script: install.sh

# Verificar si PyInstaller está instalado
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller no está instalado. Instalando PyInstaller..."
    pip install pyinstaller
fi

# Ejecutar el comando de instalación de PyInstaller
pyinstaller --name="Business Laboratory Conversion App" --hiddenimport=aspose.pydrawing --noconsole --hiddenimport=aspose.pygc --collect-binaries=aspose main.py

# Verificar si el comando de instalación fue exitoso
if [ $? -eq 0 ]; then
    echo "La instalación se completó exitosamente."
else
    echo "Ocurrió un error durante la instalación."
fi
