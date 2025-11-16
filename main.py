"""
Handwritten Text to Digital Text Converter
A GUI application that converts handwritten text images to machine-readable text
using computer vision and OCR techniques.

Author: Raiyan
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import cv2
import numpy as np
import pytesseract
import os
from typing import Optional, Tuple
import threading


class HandwrittenTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Text to Digital Text Converter")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.current_image = None
        self.processed_image = None
        self.extracted_text = ""
        
        # Configure style
        self.setup_styles()
        
        # Create GUI components
        self.create_widgets()
        
        # Try to set tesseract path (adjust based on your system)
        self.setup_tesseract()
    
    def setup_styles(self):
        """Configure custom styles for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Subtitle.TLabel', font=('Arial', 10, 'bold'))
        style.configure('Custom.TButton', padding=(10, 5))
    
    def setup_tesseract(self):
        """Setup tesseract path based on common installation locations"""
        possible_paths = [
            '/usr/bin/tesseract',  # Linux
            '/usr/local/bin/tesseract',  # macOS with Homebrew
            '/opt/homebrew/bin/tesseract',  # macOS with Apple Silicon Homebrew
            r'C:\Program Files\Tesseract-OCR\tesseract.exe',  # Windows
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                pytesseract.pytesseract.tesseract_cmd = path
                break
    
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main title
        title_label = ttk.Label(
            self.root,
            text="Handwritten Text to Digital Text Converter",
            style='Title.TLabel'
        )
        title_label.pack(pady=(10, 20))
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel for image processing
        left_frame = ttk.LabelFrame(main_frame, text="Image Processing", padding=10)
        left_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        
        # Right panel for text output
        right_frame = ttk.LabelFrame(main_frame, text="Extracted Text", padding=10)
        right_frame.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        self.create_left_panel(left_frame)
        self.create_right_panel(right_frame)
    
    def create_left_panel(self, parent):
        """Create the left panel with image processing controls"""
        # File selection frame
        file_frame = ttk.Frame(parent)
        file_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Button(
            file_frame,
            text="Select Image",
            command=self.select_image,
            style='Custom.TButton'
        ).pack(side='left', padx=(0, 10))
        
        ttk.Button(
            file_frame,
            text="Capture from Camera",
            command=self.capture_from_camera,
            style='Custom.TButton'
        ).pack(side='left')
        
        # Image display
        self.image_label = ttk.Label(parent, text="No image selected")
        self.image_label.pack(pady=10)
        
        # Processing controls
        controls_frame = ttk.LabelFrame(parent, text="Processing Options", padding=5)
        controls_frame.pack(fill='x', pady=10)
        
        # Preprocessing options
        self.preprocessing_var = tk.StringVar(value="auto")
        preprocessing_options = [
            ("Auto Enhancement (Best)", "auto"),
            ("Advanced Custom Pipeline", "custom"),
            ("Morphological Operations", "morphology"),
            ("Adaptive Threshold", "adaptive"),
            ("Otsu Threshold", "threshold")
        ]
        
        ttk.Label(controls_frame, text="Preprocessing:").grid(row=0, column=0, sticky='w', pady=2)
        for i, (text, value) in enumerate(preprocessing_options):
            ttk.Radiobutton(
                controls_frame,
                text=text,
                variable=self.preprocessing_var,
                value=value
            ).grid(row=i+1, column=0, sticky='w', padx=10)
        
        # OCR language selection
        self.language_var = tk.StringVar(value="eng")
        ttk.Label(controls_frame, text="OCR Language:").grid(row=0, column=1, sticky='w', padx=(20, 0), pady=2)
        language_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.language_var,
            values=["eng", "eng+ara", "eng+fra", "eng+deu", "eng+spa"],
            state="readonly",
            width=15
        )
        language_combo.grid(row=1, column=1, sticky='w', padx=(20, 0))
        
        # OCR accuracy options
        ttk.Label(controls_frame, text="Accuracy Mode:").grid(row=2, column=1, sticky='w', padx=(20, 0), pady=(10, 2))
        self.accuracy_var = tk.StringVar(value="high")
        accuracy_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.accuracy_var,
            values=["High (Multi-pass)", "Standard", "Fast"],
            state="readonly",
            width=15
        )
        accuracy_combo.grid(row=3, column=1, sticky='w', padx=(20, 0))
        
        # Image enhancement checkbox
        self.enhance_var = tk.BooleanVar(value=True)
        enhance_check = ttk.Checkbutton(
            controls_frame,
            text="Auto-enhance small images",
            variable=self.enhance_var
        )
        enhance_check.grid(row=4, column=1, sticky='w', padx=(20, 0), pady=5)
        
        # Process button
        self.process_button = ttk.Button(
            parent,
            text="Process Image",
            command=self.process_image,
            style='Custom.TButton'
        )
        self.process_button.pack(pady=20)
        self.process_button.configure(state='disabled')
        
        # Progress bar
        self.progress = ttk.Progressbar(parent, mode='indeterminate')
        self.progress.pack(fill='x', pady=5)
    
    def create_right_panel(self, parent):
        """Create the right panel with text output and controls"""
        # Text output area
        self.text_output = scrolledtext.ScrolledText(
            parent,
            wrap=tk.WORD,
            width=40,
            height=20,
            font=('Arial', 11)
        )
        self.text_output.pack(fill='both', expand=True, pady=(0, 10))
        
        # Text controls
        text_controls = ttk.Frame(parent)
        text_controls.pack(fill='x')
        
        ttk.Button(
            text_controls,
            text="Copy Text",
            command=self.copy_text,
            style='Custom.TButton'
        ).pack(side='left', padx=(0, 10))
        
        ttk.Button(
            text_controls,
            text="Save to File",
            command=self.save_text,
            style='Custom.TButton'
        ).pack(side='left', padx=(0, 10))
        
        ttk.Button(
            text_controls,
            text="Clear",
            command=self.clear_text,
            style='Custom.TButton'
        ).pack(side='left')
        
        # Confidence score
        self.confidence_label = ttk.Label(parent, text="")
        self.confidence_label.pack(pady=(10, 0))
    
    def select_image(self):
        """Open file dialog to select an image"""
        file_types = [
            ('Image files', '*.png *.jpg *.jpeg *.bmp *.tiff *.gif'),
            ('All files', '*.*')
        ]
        
        filename = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=file_types
        )
        
        if filename:
            self.load_image(filename)
    
    def capture_from_camera(self):
        """Capture image from camera"""
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                messagebox.showerror("Error", "Could not open camera")
                return
            
            # Create camera preview window
            camera_window = tk.Toplevel(self.root)
            camera_window.title("Camera Preview")
            camera_window.geometry("640x480")
            
            preview_label = ttk.Label(camera_window)
            preview_label.pack()
            
            def update_preview():
                ret, frame = cap.read()
                if ret:
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_pil = Image.fromarray(frame_rgb)
                    frame_pil = frame_pil.resize((600, 400), Image.Resampling.LANCZOS)
                    frame_tk = ImageTk.PhotoImage(frame_pil)
                    
                    preview_label.configure(image=frame_tk)
                    preview_label.image = frame_tk
                
                if camera_window.winfo_exists():
                    camera_window.after(10, update_preview)
            
            def capture_image():
                ret, frame = cap.read()
                if ret:
                    # Save temporary image
                    temp_path = "temp_capture.png"
                    cv2.imwrite(temp_path, frame)
                    self.load_image(temp_path)
                    os.remove(temp_path)
                    
                cap.release()
                camera_window.destroy()
            
            ttk.Button(
                camera_window,
                text="Capture",
                command=capture_image
            ).pack(pady=10)
            
            update_preview()
            
        except Exception as e:
            messagebox.showerror("Camera Error", f"Error accessing camera: {str(e)}")
    
    def load_image(self, filename: str):
        """Load and display an image"""
        try:
            # Load image with OpenCV
            self.current_image = cv2.imread(filename)
            if self.current_image is None:
                messagebox.showerror("Error", "Could not load image")
                return
            
            # Display image in GUI
            self.display_image(self.current_image)
            self.process_button.configure(state='normal')
            
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {str(e)}")
    
    def display_image(self, cv_image: np.ndarray):
        """Display OpenCV image in tkinter label"""
        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        
        # Resize for display
        height, width = image_rgb.shape[:2]
        max_size = 300
        
        if width > height:
            new_width = max_size
            new_height = int((max_size * height) / width)
        else:
            new_height = max_size
            new_width = int((max_size * width) / height)
        
        image_resized = cv2.resize(image_rgb, (new_width, new_height))
        
        # Convert to PIL and then to PhotoImage
        image_pil = Image.fromarray(image_resized)
        image_tk = ImageTk.PhotoImage(image_pil)
        
        # Update label
        self.image_label.configure(image=image_tk, text="")
        self.image_label.image = image_tk
    
    def preprocess_image(self, image: np.ndarray, method: str) -> np.ndarray:
        """Apply advanced preprocessing to the image for optimal OCR accuracy"""
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Resize image for better OCR if too small
        height, width = gray.shape
        if height < 300 or width < 300:
            scale_factor = max(300 / height, 300 / width)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            gray = cv2.resize(gray, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
        
        if method == "threshold":
            # Improved Otsu thresholding
            _, processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        elif method == "adaptive":
            # Enhanced adaptive threshold with preprocessing
            # Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            processed = cv2.adaptiveThreshold(
                blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 8
            )
        
        elif method == "morphology":
            # Advanced morphological processing
            # Apply bilateral filter first to preserve edges while reducing noise
            filtered = cv2.bilateralFilter(gray, 9, 75, 75)
            
            # Otsu thresholding
            _, thresh = cv2.threshold(filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Morphological operations with better kernels
            kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
            
            processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel_close)
            processed = cv2.morphologyEx(processed, cv2.MORPH_OPEN, kernel_open)
        
        elif method == "custom":
            # Advanced custom pipeline with multiple enhancement stages
            # Stage 1: Noise reduction with bilateral filter
            denoised = cv2.bilateralFilter(gray, 11, 17, 17)
            
            # Stage 2: Sharpening to enhance text edges
            kernel_sharpen = np.array([[-1, -1, -1],
                                     [-1, 9, -1],
                                     [-1, -1, -1]])
            sharpened = cv2.filter2D(denoised, -1, kernel_sharpen)
            
            # Stage 3: Contrast enhancement
            clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
            enhanced = clahe.apply(sharpened)
            
            # Stage 4: Advanced adaptive threshold
            processed = cv2.adaptiveThreshold(
                enhanced, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10
            )
            
            # Stage 5: Morphological cleaning
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            processed = cv2.morphologyEx(processed, cv2.MORPH_OPEN, kernel)
            processed = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel)
        
        else:  # auto enhancement - most advanced pipeline
            # Multi-stage automatic enhancement for maximum accuracy
            
            # Stage 1: Noise reduction with Non-local Means
            denoised = cv2.fastNlMeansDenoising(gray, h=10, templateWindowSize=7, searchWindowSize=21)
            
            # Stage 2: Unsharp masking for text sharpening
            gaussian = cv2.GaussianBlur(denoised, (0, 0), 2.0)
            unsharp = cv2.addWeighted(denoised, 1.5, gaussian, -0.5, 0)
            
            # Stage 3: Contrast enhancement with CLAHE
            clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
            enhanced = clahe.apply(unsharp)
            
            # Stage 4: Histogram equalization for better contrast
            equalized = cv2.equalizeHist(enhanced)
            
            # Stage 5: Gamma correction for better text visibility
            gamma = 1.2
            lookupTable = np.empty((1, 256), np.uint8)
            for i in range(256):
                lookupTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
            gamma_corrected = cv2.LUT(equalized, lookupTable)
            
            # Stage 6: Advanced adaptive threshold with optimal parameters
            processed = cv2.adaptiveThreshold(
                gamma_corrected, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 19, 9
            )
            
            # Stage 7: Morphological operations for text cleanup
            kernel_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
            kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            
            # Light erosion to separate touching characters
            processed = cv2.erode(processed, kernel_erode, iterations=1)
            # Dilation to restore character thickness
            processed = cv2.dilate(processed, kernel_dilate, iterations=1)
            
            # Final morphological closing to connect broken characters
            kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
            processed = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel_close)
        
        return processed
    
    def deskew_image(self, image: np.ndarray) -> np.ndarray:
        """Detect and correct text skew for better OCR accuracy"""
        try:
            # Convert to grayscale if needed
            if len(image.shape) == 3:
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                gray = image.copy()
            
            # Apply threshold to get binary image
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Invert colors (black text on white background)
            binary = cv2.bitwise_not(binary)
            
            # Find contours
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filter contours by area to get text regions
            text_contours = [c for c in contours if cv2.contourArea(c) > 50]
            
            if not text_contours:
                return image  # No text found, return original
            
            # Calculate skew angle using minimum area rectangle
            angles = []
            for contour in text_contours:
                rect = cv2.minAreaRect(contour)
                angle = rect[2]
                
                # Normalize angle
                if angle < -45:
                    angle += 90
                elif angle > 45:
                    angle -= 90
                
                angles.append(angle)
            
            # Use median angle to avoid outliers
            if angles:
                skew_angle = np.median(angles)
                
                # Only correct if skew is significant (> 0.5 degrees)
                if abs(skew_angle) > 0.5:
                    # Get image center and create rotation matrix
                    (h, w) = image.shape[:2]
                    center = (w // 2, h // 2)
                    rotation_matrix = cv2.getRotationMatrix2D(center, skew_angle, 1.0)
                    
                    # Apply rotation
                    corrected = cv2.warpAffine(image, rotation_matrix, (w, h), 
                                             flags=cv2.INTER_CUBIC, 
                                             borderMode=cv2.BORDER_REPLICATE)
                    return corrected
            
            return image
            
        except Exception:
            # If deskewing fails, return original image
            return image
    
    def process_image(self):
        """Process the current image and extract text"""
        if self.current_image is None:
            messagebox.showwarning("Warning", "Please select an image first")
            return
        
        # Start processing in a separate thread to avoid GUI freezing
        def process_thread():
            try:
                # Update GUI
                self.root.after(0, lambda: self.progress.start())
                self.root.after(0, lambda: self.process_button.configure(state='disabled'))
                
                # Preprocess image with deskewing
                preprocessing_method = self.preprocessing_var.get()
                
                # Step 1: Deskew the image first
                deskewed_image = self.deskew_image(self.current_image)
                
                # Step 2: Apply selected preprocessing
                processed_image = self.preprocess_image(deskewed_image, preprocessing_method)
                self.processed_image = processed_image
                
                # Advanced OCR configuration with multiple attempts
                language = self.language_var.get()
                accuracy_mode = self.accuracy_var.get()
                enhance_small = self.enhance_var.get()
                
                # Adjust processing based on accuracy mode
                if "High" in accuracy_mode:
                    # Try multiple PSM modes for best results
                    psm_modes = [6, 8, 13, 7, 4]  # More comprehensive modes
                elif "Fast" in accuracy_mode:
                    psm_modes = [6]  # Single mode for speed
                else:  # Standard
                    psm_modes = [6, 8]  # Balanced approach
                
                best_text = ""
                best_confidence = 0
                debug_info = []
                
                for psm in psm_modes:
                    try:
                        # OCR configuration with enhanced parameters
                        ocr_config = f'--oem 1 --psm {psm} -l {language}'
                        
                        # Try direct text extraction first (simpler approach)
                        candidate_text = pytesseract.image_to_string(
                            processed_image,
                            config=ocr_config
                        ).strip()
                        
                        # If we got text, calculate confidence
                        if candidate_text and len(candidate_text) > 0:
                            try:
                                # Get confidence data
                                data = pytesseract.image_to_data(
                                    processed_image,
                                    config=ocr_config,
                                    output_type=pytesseract.Output.DICT
                                )
                                
                                # Calculate confidence
                                confidences = [int(conf) for conf in data['conf'] if int(conf) > 0]
                                words = [word for word, conf in zip(data['text'], data['conf']) if int(conf) > 0 and word.strip()]
                                
                                if confidences:
                                    avg_conf = np.mean(confidences)
                                    text_quality = len([w for w in words if len(w) > 1])  # Prefer longer words
                                    
                                    # Combined score: confidence + text quality
                                    combined_score = avg_conf * (1 + text_quality * 0.1)
                                    
                                    debug_info.append(f"PSM {psm}: '{candidate_text[:50]}...', conf: {avg_conf:.1f}, score: {combined_score:.1f}")
                                    
                                    if combined_score > best_confidence:
                                        best_confidence = combined_score
                                        best_text = candidate_text
                                else:
                                    # No confidence data but we have text
                                    if len(candidate_text) > len(best_text):
                                        best_text = candidate_text
                                        best_confidence = 50  # Default confidence
                            except Exception:
                                # Confidence calculation failed but we have text
                                if len(candidate_text) > len(best_text):
                                    best_text = candidate_text
                                    best_confidence = 40  # Lower default confidence
                    
                    except Exception as e:
                        debug_info.append(f"PSM {psm}: Error - {str(e)}")
                        continue
                
                # Multiple fallback approaches if no good results
                if not best_text or len(best_text.strip()) == 0:
                    debug_info.append("Trying fallback methods...")
                    
                    # Fallback 1: Simple OCR with different OEM
                    fallback_configs = [
                        f'--oem 3 --psm 6 -l {language}',  # Legacy engine
                        f'--oem 2 --psm 8 -l {language}',  # Cube + Tesseract
                        f'--oem 1 --psm 13 -l {language}', # Raw line. Treat the image as a single text line
                        '--oem 1 --psm 8',  # Single word, no language
                    ]
                    
                    for config in fallback_configs:
                        try:
                            fallback_text = pytesseract.image_to_string(
                                processed_image,
                                config=config
                            ).strip()
                            
                            if fallback_text and len(fallback_text) > 0:
                                best_text = fallback_text
                                best_confidence = 35  # Fallback confidence
                                debug_info.append(f"Fallback success with: {config}")
                                break
                        except Exception as e:
                            debug_info.append(f"Fallback failed for {config}: {str(e)}")
                            continue
                
                # Final fallback: Try with inverted image
                if not best_text or len(best_text.strip()) == 0:
                    try:
                        inverted_image = cv2.bitwise_not(processed_image)
                        final_text = pytesseract.image_to_string(
                            inverted_image,
                            config=f'--oem 1 --psm 6 -l {language}'
                        ).strip()
                        
                        if final_text and len(final_text) > 0:
                            best_text = final_text
                            best_confidence = 30
                            debug_info.append("Success with inverted image")
                    except Exception:
                        pass
                
                # If still no text, provide helpful message
                if not best_text or len(best_text.strip()) == 0:
                    best_text = "[No text detected. Try a different preprocessing method or check image quality.]"
                    best_confidence = 0
                    debug_info.append("No text found with any method")
                
                # Post-process text for better readability
                extracted_text = self.post_process_text(best_text)
                avg_confidence = best_confidence
                
                # Create debug summary
                debug_summary = "\n".join(debug_info[-3:])  # Show last 3 debug messages
                
                # Update GUI in main thread
                self.root.after(0, lambda: self.update_results(extracted_text, avg_confidence, debug_summary))
                
            except Exception as e:
                error_msg = f"Processing failed: {str(e)}"
                self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
                self.root.after(0, lambda: self.update_results(f"[Error: {error_msg}]", 0, ""))
            finally:
                self.root.after(0, lambda: self.progress.stop())
                self.root.after(0, lambda: self.process_button.configure(state='normal'))
        
        threading.Thread(target=process_thread, daemon=True).start()
    
    def update_results(self, text: str, confidence: float, debug_info: str = ""):
        """Update the results in the GUI"""
        self.extracted_text = text
        
        # Clear and update text output
        self.text_output.delete(1.0, tk.END)
        if text.startswith("[No text detected"):
            self.text_output.insert(1.0, text)
        else:
            self.text_output.insert(1.0, text)
            if debug_info:
                self.text_output.insert(tk.END, f"\n\n--- Debug Info ---\n{debug_info}")
        
        # Update confidence label
        confidence_text = f"Average Confidence: {confidence:.1f}%"
        if confidence >= 80:
            confidence_color = "green"
        elif confidence >= 60:
            confidence_color = "orange"
        else:
            confidence_color = "red"
        
        self.confidence_label.configure(
            text=confidence_text,
            foreground=confidence_color
        )
        
        # Display processed image
        if self.processed_image is not None:
            # Create a side-by-side comparison
            self.show_comparison()
    
    def post_process_text(self, text: str) -> str:
        """Post-process extracted text for better accuracy and readability"""
        if not text or text.startswith("[No text detected") or text.startswith("[Error:"):
            return text
        
        # Remove excessive whitespace
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove excessive spaces
            cleaned_line = ' '.join(line.split())
            
            # Skip very short lines that are likely OCR artifacts
            if len(cleaned_line.strip()) > 0:
                cleaned_lines.append(cleaned_line)
        
        # Join lines with proper spacing
        result = '\n'.join(cleaned_lines)
        
        # Common OCR error corrections
        corrections = {
            '0': 'O',  # Zero to O in words
            '1': 'I',  # One to I in words
            '5': 'S',  # Five to S in words
            '8': 'B',  # Eight to B in words
            'rn': 'm',  # Common OCR error
            'ii': 'll', # Common OCR error
            '|': 'I',   # Pipe to I
        }
        
        # Apply corrections only to alphabetic words
        import re
        words = result.split()
        corrected_words = []
        
        for word in words:
            if word.isalpha() or any(c.isalpha() for c in word):
                corrected_word = word
                # Apply corrections more intelligently
                for wrong, correct in corrections.items():
                    if wrong in word and not word.isdigit():
                        # Only correct if it makes sense in context
                        if wrong in ['0', '1', '5', '8'] and any(c.isalpha() for c in word):
                            corrected_word = corrected_word.replace(wrong, correct)
                        elif wrong in ['rn', 'ii', '|']:
                            corrected_word = corrected_word.replace(wrong, correct)
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words)
    
    def show_comparison(self):
        """Show original vs processed image comparison"""
        if self.current_image is None or self.processed_image is None:
            return
        
        # Create comparison window
        comp_window = tk.Toplevel(self.root)
        comp_window.title("Image Comparison")
        comp_window.geometry("800x400")
        
        # Original image
        orig_frame = ttk.LabelFrame(comp_window, text="Original", padding=5)
        orig_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Processed image
        proc_frame = ttk.LabelFrame(comp_window, text="Processed", padding=5)
        proc_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        # Display images
        self._display_comparison_image(self.current_image, orig_frame)
        self._display_comparison_image(self.processed_image, proc_frame)
    
    def _display_comparison_image(self, cv_image: np.ndarray, parent: ttk.Frame):
        """Display image in comparison frame"""
        # Convert and resize
        if len(cv_image.shape) == 3:
            image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        else:
            image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2RGB)
        
        height, width = image_rgb.shape[:2]
        max_size = 350
        
        if width > height:
            new_width = max_size
            new_height = int((max_size * height) / width)
        else:
            new_height = max_size
            new_width = int((max_size * width) / height)
        
        image_resized = cv2.resize(image_rgb, (new_width, new_height))
        image_pil = Image.fromarray(image_resized)
        image_tk = ImageTk.PhotoImage(image_pil)
        
        label = ttk.Label(parent, image=image_tk)
        label.image = image_tk
        label.pack()
    
    def copy_text(self):
        """Copy extracted text to clipboard"""
        if self.extracted_text:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.extracted_text)
            messagebox.showinfo("Copied", "Text copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No text to copy")
    
    def save_text(self):
        """Save extracted text to file"""
        if not self.extracted_text:
            messagebox.showwarning("Warning", "No text to save")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.extracted_text)
                messagebox.showinfo("Saved", f"Text saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {str(e)}")
    
    def clear_text(self):
        """Clear the text output"""
        self.text_output.delete(1.0, tk.END)
        self.extracted_text = ""
        self.confidence_label.configure(text="")


def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = HandwrittenTextConverter(root)
    
    # Add menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open Image", command=app.select_image)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(
        label="About",
        command=lambda: messagebox.showinfo(
            "About",
            "Handwritten Text to Digital Text Converter\n\n"
            "This application uses computer vision and OCR techniques\n"
            "to convert handwritten text images to machine-readable text.\n\n"
            "Features:\n"
            "• Multiple preprocessing options\n"
            "• Real-time camera capture\n"
            "• Confidence scoring\n"
            "• Multiple language support\n\n"
            "Author: Raiyan\n"
        )
    )
    
    root.mainloop()


if __name__ == "__main__":
    main()