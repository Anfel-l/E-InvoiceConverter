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
