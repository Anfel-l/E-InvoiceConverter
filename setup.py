from setuptools import setup, find_packages

setup(
    name='e-invoice-converter',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt6',
        'pandas',
        'openpyxl',
        # lista todas tus dependencias aquí
    ],
    entry_points='''
        [console_scripts]
        e-invoice-converter=main:main
    ''',
)
