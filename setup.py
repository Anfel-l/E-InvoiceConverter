from cx_Freeze import setup, Executable

# Agregar aquí tus dependencias y otros detalles necesarios para el empaquetado
# por ejemplo, includes, excludes, packages, etc.

base = None

executables = [Executable("main.py", base=base)]

setup(
    name="Business Laboratory Conversion App",
    version="1.0",
    description="The E-Invoice Converter App is an application that allows you to convert PDF and XML files to Excel format with ease. This tool is useful for processing and analyzing data contained in PDF and XML files and working with it in an Excel spreadsheet.",
    options={"build_exe": {"packages": ["os"], "excludes": []}},
    executables=executables
)
