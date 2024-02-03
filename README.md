# E-Invoice Converter

The E-Invoice Converter App is an application that allows you to convert XML using the UBL format files to Excel format efficiently. This tool is useful for processing and analyzing data contained in XML files and working with it in an Excel spreadsheet.

## Features

- **XML Files to Excel Conversion**: You can select a directory containing XML files and convert them into a single Excel file. This is useful when you have multiple XML files with related data that you want to combine into a spreadsheet.
  
- **Formatted Excel Output**: The application not only converts the XML files into an Excel format but also formats the output. The header row will be highlighted, and the rows will have alternating colors for better readability.

- **Intuitive User Interface**: The application has a user-friendly graphical interface (GUI) that allows you to perform the conversions easily and quickly. You simply need to select the directory and click the conversion button.

## Requirements

- Python 3.x
- PyQt6
- pandas
- openpyxl

## Installation

### Windows

1. Install Python 3.x from the [official website](https://www.python.org/downloads/). During installation, make sure to select "Add Python to PATH".
   
2. Download the application source code from this repository.

3. Open a command prompt or PowerShell window in the downloaded directory.

4. Run the installation script:

   install.bat

### Linux/Unix

1. Install Python 3.x using your distribution's package manager or download it from the official website.

2. Download the application source code from this repository.

3. Open a terminal in the downloaded directory.

4. Give execute permission to the installation script:

    chmod +x install.sh

5. Run the installation script:

    ./install.sh

## Usage

After installation, launch the E-Invoice Converter App. The application interface is straightforward:

1. Click on the "Convert XML to Excel" button.
2. Select the directory containing your XML files.
3. Choose where to save the output Excel file.
4. The application will process the files and save the formatted Excel file to your chosen location.

## License

This project is open source and available under the [MIT License](https://opensource.org/license/mit/).

