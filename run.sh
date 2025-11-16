#!/bin/bash

# Quick run script for Handwritten Text to Digital Text Converter

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run ./install.sh first to set up the project."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "❌ main.py not found!"
    echo "Please ensure you're in the correct directory."
    exit 1
fi

# Run the application
echo "🚀 Starting Handwritten Text to Digital Text Converter..."
python main.py