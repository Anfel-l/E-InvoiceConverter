#!/bin/bash

# Dependencies installation and executable generation

pip install -r requirements.txt
pyinstaller --noconsole --onefile  --collect-all "aspose" main.py


