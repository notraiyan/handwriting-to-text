# Sample Images for Testing

This directory contains sample images that you can use to test the Handwritten Text to Digital Text Converter application.

## How to Use Sample Images

1. Launch the application by running `python main.py`
2. Click "Select Image" 
3. Navigate to this `sample_images` folder
4. Choose one of the sample images
5. Try different preprocessing options to see which works best

## Creating Your Own Test Images

### For Best Results:
- **Clear handwriting**: Write legibly with consistent letter formation
- **Good contrast**: Use dark ink on white/light paper
- **Proper lighting**: Ensure even lighting without shadows or glare
- **Stable camera**: Keep the camera steady to avoid blur
- **Straight angle**: Take photos straight-on, not at an angle

### Sample Text Suggestions:

**Simple Text (Good for Testing):**
```
Hello World
This is a test
The quick brown fox jumps over the lazy dog
123456789
```

**Mixed Content:**
```
Shopping List:
1. Apples - $3.50
2. Bread - $2.25
3. Milk - $4.00
Total: $9.75
```

**Technical Text:**
```
Python Code:
def hello():
    print("Hello, World!")
    return True
```

### Camera Capture Tips:

1. **Distance**: Hold the camera 12-18 inches from the paper
2. **Angle**: Keep the camera parallel to the paper
3. **Lighting**: Use natural light or bright indoor lighting
4. **Stability**: Keep the camera steady or use a stand
5. **Focus**: Ensure the text is in focus before capturing

### File Naming Convention:

When saving your own test images, use descriptive names:
- `handwritten_simple.jpg` - Basic handwriting test
- `mixed_numbers_text.png` - Numbers and letters combined
- `cursive_sample.jpg` - Cursive handwriting
- `printed_letters.png` - Print-style handwriting
- `low_quality.jpg` - Testing with poor quality images

## Testing Different Scenarios

### Preprocessing Methods Test:
Try the same image with different preprocessing options:
1. Auto Enhancement
2. Basic Threshold  
3. Adaptive Threshold
4. Morphological Operations
5. Custom Pipeline

### Language Testing:
If you have text in different languages, test the language selection feature:
- English (`eng`)
- English + Arabic (`eng+ara`)
- English + French (`eng+fra`)
- English + German (`eng+deu`)
- English + Spanish (`eng+spa`)

### Quality Testing:
Create or find images with varying quality to test robustness:
- High resolution, clear images
- Low resolution images
- Images with shadows
- Images with poor lighting
- Slightly blurred images
- Images at an angle

## Expected Results

The application should be able to:
- ✅ Recognize clear, well-written text with 80%+ confidence
- ✅ Handle basic punctuation and numbers
- ✅ Process common English words effectively
- ✅ Maintain reasonable accuracy with mixed case text
- ⚠️ May struggle with heavily cursive handwriting
- ⚠️ May have difficulty with very stylized fonts
- ⚠️ Performance depends on image quality

## Troubleshooting Test Results

### If you get poor results:
1. **Check image quality** - Is the text clear and in focus?
2. **Try different preprocessing** - Some methods work better for different image types
3. **Verify language setting** - Make sure it matches your text language
4. **Adjust lighting** - Retake the photo with better lighting
5. **Check text size** - Very small text may be harder to recognize

### If the application crashes:
1. **Check image size** - Very large images may cause memory issues
2. **Verify file format** - Ensure you're using supported formats (PNG, JPG, BMP, TIFF, GIF)
3. **Check Tesseract installation** - Make sure OCR engine is properly installed

---

*Remember: The goal is to test various scenarios to understand how the application performs under different conditions. This helps you learn when and how to use different features for optimal results.*