#!/bin/bash

# Nombre del archivo de script: install.sh

# Verificar si cx_Freeze está instalado
if ! command -v cxfreeze &> /dev/null; then
    echo "cx_Freeze no está instalado. Instalando cx_Freeze..."
    pip install cx-Freeze
fi

# Instalar los paquetes requeridos
pip install pandas PyQt6 openpyxl aspose.pdf

# Crear un archivo de configuración para cx_Freeze
cat <<EOF > setup.py
from cx_Freeze import setup, Executable

# Agregar aquí tus dependencias y otros detalles necesarios para el empaquetado
# por ejemplo, includes, excludes, packages, etc.

base = None

executables = [Executable("main.py", base=base)]

setup(
    name="Business Laboratory Conversion App",
    version="1.0",
    description="Descripción de tu aplicación",
    options={"build_exe": {"packages": ["os"], "excludes": []}},
    executables=executables
)
EOF

# Ejecutar el comando de empaquetado de cx_Freeze
cxfreeze --target-dir dist main.py

# Verificar si el comando de empaquetado fue exitoso
if [ $? -eq 0 ]; then
    echo "El empaquetado se completó exitosamente."
else
    echo "Ocurrió un error durante el empaquetado."
fi
