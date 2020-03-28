#!/bin/bash

echo Installing virtual environment package
echo "Creating virtual environment"
python3 -m venv ENV
echo "Activating environment"
source  ENV/bin/activate
echo "Upgrading pip"
python3 -m pip install --upgrade pip

# detect os, linux vs mac, make requiremed changes
# create virtual env
# activate virtual env
tput setaf 2; echo "Installing dependencies"
pip install -r requirements.txt
tput setaf 2; echo "Please enter the path an image!!"

python3 main.py  --path $path_to_main_dir 


