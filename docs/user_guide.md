# User Guide - Handwritten Text to Digital Text Converter

## Getting Started

### First Launch
1. Run the application by executing `python main.py`
2. The main window will open with the title "Handwritten Text to Digital Text Converter"

### Interface Overview

The application interface is divided into two main sections:

#### Left Panel - Image Processing
- **File Selection Buttons**:
  - "Select Image": Choose an image file from your computer
  - "Capture from Camera": Take a photo using your camera
- **Image Display**: Shows the selected image (resized for display)
- **Processing Options**: Various preprocessing and OCR settings
- **Process Button**: Starts the text extraction process
- **Progress Bar**: Shows processing status

#### Right Panel - Text Output
- **Text Area**: Displays the extracted text
- **Control Buttons**: Copy, Save, and Clear functions
- **Confidence Score**: Shows the accuracy of text recognition

## Step-by-Step Usage

### Step 1: Load an Image

**Option A: From File**
1. Click "Select Image"
2. Browse and select an image file (PNG, JPG, BMP, TIFF, GIF)
3. The image will appear in the left panel

**Option B: From Camera**
1. Click "Capture from Camera"
2. A camera preview window will open
3. Position the handwritten text in view
4. Click "Capture" when ready

### Step 2: Configure Processing Options

**Preprocessing Methods:**
- **Auto Enhancement** (Recommended): Automatic noise reduction and enhancement
- **Basic Threshold**: Simple black and white conversion
- **Adaptive Threshold**: Advanced thresholding for varied lighting
- **Morphological Operations**: Shape-based text cleanup
- **Custom Pipeline**: Multi-step enhancement process

**OCR Language:**
- Select the language of the handwritten text
- Options include English, Arabic, French, German, Spanish
- Multi-language options available (e.g., "eng+ara")

### Step 3: Process the Image

1. Click "Process Image"
2. The progress bar will show processing status
3. Processing may take a few seconds depending on image size
4. Results will appear in the right panel

### Step 4: Review Results

**Text Output:**
- Extracted text appears in the scrollable text area
- Text can be edited if needed

**Confidence Score:**
- Green (80%+): High confidence, likely accurate
- Orange (60-79%): Medium confidence, review recommended
- Red (<60%): Low confidence, consider different preprocessing

**Image Comparison:**
- A comparison window may open showing original vs processed image
- This helps understand how preprocessing affected the image

### Step 5: Use the Results

**Copy to Clipboard:**
1. Click "Copy Text"
2. Text is copied and ready to paste elsewhere

**Save to File:**
1. Click "Save to File"
2. Choose location and filename
3. Text is saved as a .txt file

**Clear Results:**
- Click "Clear" to remove current results and start over

## Tips for Better Results

### Image Quality
- **Resolution**: Use high-resolution images when possible
- **Lighting**: Ensure even, bright lighting
- **Focus**: Images should be sharp and in focus
- **Angle**: Take photos straight-on, avoid skewed angles

### Handwriting Style
- **Clarity**: Clear, legible handwriting works best
- **Spacing**: Well-spaced words and lines improve accuracy
- **Size**: Larger text is generally easier to recognize
- **Contrast**: Dark ink on light paper is ideal

### Preprocessing Selection
- **Auto Enhancement**: Good starting point for most images
- **Adaptive Threshold**: Best for images with uneven lighting
- **Custom Pipeline**: Try when auto enhancement doesn't work well
- **Experiment**: Different methods work better for different types of images

### Language Settings
- **Match the Text**: Select the language that matches your handwritten text
- **Multi-language**: Use combined options for mixed-language documents
- **English Default**: When unsure, English often works for basic Latin characters

## Troubleshooting

### Common Issues and Solutions

**Problem**: "No text detected" or empty results
- **Solution**: Try different preprocessing methods
- **Solution**: Ensure image has sufficient contrast
- **Solution**: Check that handwriting is clearly visible

**Problem**: Inaccurate text recognition
- **Solution**: Use "Auto Enhancement" or "Custom Pipeline"
- **Solution**: Verify correct language is selected
- **Solution**: Try taking a clearer photo with better lighting

**Problem**: Camera not working
- **Solution**: Check camera permissions for the application
- **Solution**: Ensure no other applications are using the camera
- **Solution**: Try restarting the application

**Problem**: Application crashes during processing
- **Solution**: Try with a smaller image file
- **Solution**: Check that Tesseract OCR is properly installed
- **Solution**: Restart the application

**Problem**: Low confidence scores
- **Solution**: Improve image quality (lighting, focus, contrast)
- **Solution**: Try different preprocessing options
- **Solution**: Ensure handwriting is clear and well-spaced

### Performance Tips

**For Large Images:**
- Consider resizing very large images before processing
- Close other applications to free up memory
- Use "Basic Threshold" for faster processing

**For Better Accuracy:**
- Take multiple photos and use the best one
- Ensure proper lighting when capturing images
- Keep handwriting neat and well-spaced

## Keyboard Shortcuts

- **Ctrl+O**: Open image file (when available)
- **Ctrl+S**: Save text to file (when text is available)
- **Ctrl+C**: Copy text to clipboard (when text is available)
- **Ctrl+Q**: Quit application

## Advanced Features

### Batch Processing
While the current version processes one image at a time, you can:
1. Process multiple images sequentially
2. Save each result to a separate file
3. Compare results from different preprocessing methods

### Image Comparison Window
- Shows original image alongside processed version
- Helps understand the effect of preprocessing
- Can be used to fine-tune preprocessing settings

### Confidence Analysis
- Confidence scores help assess result reliability
- Low scores indicate potential recognition errors
- Can guide decision to try different settings

## Technical Information

### Supported File Formats
- **Input**: PNG, JPEG, JPG, BMP, TIFF, GIF
- **Output**: Plain text (.txt files)

### System Requirements
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 50MB for application, additional space for images
- **Camera**: Optional, for direct capture feature

### Dependencies
The application uses several machine learning and computer vision libraries:
- OpenCV for image processing
- Tesseract OCR for text recognition
- PIL/Pillow for image handling
- NumPy for numerical operations
- tkinter for the GUI interface

---

For additional help or to report issues, please refer to the project repository or documentation.