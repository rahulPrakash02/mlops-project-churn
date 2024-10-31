#!/bin/bash

#Remove existing venv
rm -rf venv

# Create a virtual environment
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

#Initialize Git
git init

#Initialize DVC
source ./bin/dvc-init.sh

# Optional: Keep the terminal open or indicate completion
echo "Environment setup complete. Virtual environment activated."