# Handwritten Text to Digital Text Converter

A Python application that converts handwritten text images to machine-readable text using computer vision and OCR (Optical Character Recognition) techniques with a user-friendly GUI interface.

## Features

- **Visual Interface**: Easy-to-use tkinter-based GUI
- **Multiple Input Methods**: 
  - Load images from files
  - Capture directly from camera
- **Advanced Image Preprocessing**: 
  - Auto enhancement with noise reduction
  - Basic and adaptive thresholding
  - Morphological operations
  - Custom processing pipelines
- **OCR with Confidence Scoring**: Real-time confidence assessment of text recognition
- **Multi-language Support**: Support for multiple languages (English, Arabic, French, German, Spanish)
- **Text Management**: Copy to clipboard, save to file, clear functions
- **Image Comparison**: Side-by-side view of original vs processed images

## Prerequisites

### Tesseract OCR
This application requires Tesseract OCR to be installed on your system.

#### macOS (using Homebrew)
```bash
brew install tesseract
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr tesseract-ocr-eng
```

#### Windows
1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install and add to your system PATH

### Python Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd handwritten-to-digital-text
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Tesseract OCR is properly installed (see Prerequisites)

## Usage

1. Run the application:
```bash
python main.py
```

2. **Load an Image**:
   - Click "Select Image" to choose an image file
   - Or click "Capture from Camera" to take a photo

3. **Choose Processing Options**:
   - Select preprocessing method (Auto Enhancement recommended)
   - Choose OCR language if needed

4. **Process Image**:
   - Click "Process Image" to extract text
   - View confidence score and results

5. **Manage Results**:
   - Copy text to clipboard
   - Save to text file
   - Clear results

## Supported Image Formats

- PNG
- JPEG/JPG
- BMP
- TIFF
- GIF

## Machine Learning Techniques Used

### Computer Vision Preprocessing
1. **Noise Reduction**: Gaussian blur and Non-local Means denoising
2. **Contrast Enhancement**: CLAHE (Contrast Limited Adaptive Histogram Equalization)
3. **Thresholding**: Adaptive thresholding for binarization
4. **Morphological Operations**: Opening and closing operations for text cleanup

### OCR Technology
- **Tesseract OCR Engine**: Google's open-source OCR engine
- **Page Segmentation**: Automatic page layout analysis
- **Character Recognition**: Pattern matching and feature extraction
- **Confidence Scoring**: Statistical confidence assessment

## Project Structure

```
handwritten-to-digital-text/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── setup.py               # Installation script
├── sample_images/         # Sample images for testing
│   ├── handwritten1.jpg
│   ├── handwritten2.png
│   └── mixed_text.jpg
└── docs/                  # Additional documentation
    └── user_guide.md
```

## Tips for Best Results

1. **Image Quality**: Use high-resolution, well-lit images
2. **Preprocessing**: Try different preprocessing methods for different image types
3. **Language**: Select the appropriate language for better accuracy
4. **Handwriting**: Clear, well-spaced handwriting works best
5. **Background**: Plain, contrasting backgrounds improve recognition

## Technical Details

### Image Preprocessing Pipeline

The application implements several preprocessing techniques:

```python
# Auto Enhancement Pipeline
1. Noise reduction using Non-local Means denoising
2. Contrast enhancement using CLAHE
3. Adaptive thresholding for binarization
4. Optional morphological operations
```

### OCR Configuration

```python
# Tesseract configuration
OEM Mode: 3 (Default, based on availability)
PSM Mode: 6 (Uniform block of text)
Languages: Configurable multi-language support
```

## Future Enhancements

- [ ] Deep learning models for improved accuracy
- [ ] Handwriting style adaptation
- [ ] Batch processing capabilities
- [ ] PDF output support
- [ ] Real-time video processing
- [ ] Custom model training interface

## Troubleshooting

### Common Issues

1. **Tesseract not found**: Ensure Tesseract is installed and in your system PATH
2. **Poor recognition accuracy**: Try different preprocessing options
3. **Camera not working**: Check camera permissions and drivers
4. **Memory issues**: Process smaller images or reduce image resolution

### Error Messages

- `TesseractNotFoundError`: Install Tesseract OCR
- `Camera Error`: Check camera permissions
- `Processing failed`: Try different preprocessing options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Google Tesseract OCR team
- OpenCV community
- PIL/Pillow developers
- Python tkinter framework

## Author

**Raiyan**  
Date: November 16, 2025

---

*This application demonstrates the practical implementation of computer vision and machine learning techniques for real-world text recognition challenges.*