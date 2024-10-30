#!/bin/bash

# setup_environment.sh
# Script to set up the development environment for the project.

echo "Setting up the development environment..."

# Update package lists
sudo apt-get update

# Install Python and pip if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing..."
    sudo apt-get install python3 python3-pip -y
else
    echo "Python3 is already installed."
fi

# Install required Python packages
pip3 install numpy pandas

# Check if virtualenv is installed, if not, install it
if ! pip3 show virtualenv &> /dev/null; then
    echo "Installing virtualenv..."
    pip3 install virtualenv
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating a virtual environment..."
    virtualenv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install project-specific dependencies
pip install -r requirements.txt

echo "Development environment setup complete."
