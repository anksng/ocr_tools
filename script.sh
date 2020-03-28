#!/bin/sh
echo Installing virtual environment package
echo "Creating virtual environment"
python3 -m venv ENV
echo "Activating environment"
source  ENV/bin/activate
# detect os, linux vs mac, make requiremed changes
# create virtual env
# activate virtual env
tput setaf 2; echo "Installing dependencies"
pip install -r requirements.txt
tput setaf 2; echo "Please enter the path to an image of a document in your computer!!"
tput setaf 2; echo "To discontinue anytime please press control + z in mac and ctrl + z in linux/windows!!"

tput setaf 2; echo "HINT - drag the Image to the terminal (this will paste its path), then press enter"
read -p "Path to document image : " path_to_main_dir
echo "Processing the image"
python main.py  --path $path_to_main_dir 


