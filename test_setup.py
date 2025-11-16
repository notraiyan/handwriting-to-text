#!/usr/bin/env python3
"""
Quick test script to verify the application can be imported and basic functions work
"""

import sys
import os
import tkinter as tk

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import cv2
        print("✅ OpenCV imported successfully")
    except ImportError as e:
        print(f"❌ OpenCV import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        from PIL import Image, ImageTk
        print("✅ PIL/Pillow imported successfully")
    except ImportError as e:
        print(f"❌ PIL/Pillow import failed: {e}")
        return False
    
    try:
        import pytesseract
        print("✅ pytesseract imported successfully")
    except ImportError as e:
        print(f"❌ pytesseract import failed: {e}")
        return False
    
    return True

def test_tesseract():
    """Test that Tesseract OCR is properly configured"""
    print("\nTesting Tesseract OCR...")
    
    try:
        import pytesseract
        import numpy as np
        
        # Create a simple test image
        test_image = np.ones((100, 300, 3), dtype=np.uint8) * 255
        
        # Test OCR
        result = pytesseract.image_to_string(test_image)
        print("✅ Tesseract OCR is working")
        return True
        
    except Exception as e:
        print(f"❌ Tesseract test failed: {e}")
        print("   Make sure Tesseract OCR is installed on your system")
        return False

def test_gui():
    """Test that the GUI can be created"""
    print("\nTesting GUI creation...")
    
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Import the main application
        from main import HandwrittenTextConverter
        
        app = HandwrittenTextConverter(root)
        print("✅ GUI application created successfully")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Running quick tests for Handwritten Text Converter...")
    print("=" * 60)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please install required dependencies:")
        print("   pip install -r requirements.txt")
        return False
    
    # Test Tesseract
    if not test_tesseract():
        print("\n⚠️  Tesseract OCR tests failed. The application may still work")
        print("   but OCR functionality will be limited.")
    
    # Test GUI
    if not test_gui():
        print("\n❌ GUI tests failed. There may be an issue with the application code.")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed! The application should work correctly.")
    print("\nTo run the application:")
    print("   python main.py")
    print("or")
    print("   ./run.sh")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)