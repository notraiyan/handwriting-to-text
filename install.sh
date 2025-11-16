#!/bin/bash

# Installation script for Handwritten Text to Digital Text Converter
# This script sets up the environment and installs dependencies

echo "🚀 Setting up Handwritten Text to Digital Text Converter..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found"

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "✅ Python version $python_version is compatible"
else
    echo "❌ Python version $python_version is too old. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "📈 Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Check if Tesseract is installed
echo "🔍 Checking for Tesseract OCR..."

tesseract_paths=(
    "/usr/bin/tesseract"
    "/usr/local/bin/tesseract" 
    "/opt/homebrew/bin/tesseract"
)

tesseract_found=false
for path in "${tesseract_paths[@]}"; do
    if [ -f "$path" ]; then
        echo "✅ Tesseract OCR found at $path"
        tesseract_found=true
        break
    fi
done

if [ "$tesseract_found" = false ]; then
    echo "⚠️  Tesseract OCR not found!"
    echo "   Please install Tesseract OCR:"
    
    # Detect OS and provide installation instructions
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "   macOS: brew install tesseract"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "   Ubuntu/Debian: sudo apt-get install tesseract-ocr"
        echo "   CentOS/RHEL: sudo yum install tesseract"
    else
        echo "   Please visit: https://github.com/tesseract-ocr/tesseract#installing-tesseract"
    fi
    echo ""
fi

# Create desktop shortcut (optional)
if command -v desktop-file-install &> /dev/null; then
    echo "🖥️  Creating desktop shortcut..."
    cat > handwritten-converter.desktop << EOF
[Desktop Entry]
Name=Handwritten Text Converter
Comment=Convert handwritten text to digital text
Exec=$(pwd)/venv/bin/python $(pwd)/main.py
Icon=applications-graphics
Terminal=false
Type=Application
Categories=Graphics;Photography;
EOF
    
    if desktop-file-install --dir="$HOME/.local/share/applications" handwritten-converter.desktop 2>/dev/null; then
        echo "✅ Desktop shortcut created"
        rm handwritten-converter.desktop
    fi
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To run the application:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the application: python main.py"
echo ""
echo "Or simply run: ./run.sh"
echo ""

if [ "$tesseract_found" = false ]; then
    echo "⚠️  Remember to install Tesseract OCR before using the application!"
    echo ""
fi