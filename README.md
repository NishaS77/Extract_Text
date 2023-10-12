
# Text Extraction from Images using Tesseract OCR

This project demonstrates how to extract text from images using the Tesseract OCR library in Python. Tesseract is a powerful open-source tool for recognizing text from images, making it useful for various applications, such as digitizing scanned documents or extracting text from images.

## Prerequisites

Before running the script, you need to set up the following prerequisites:

1. **Tesseract-OCR Installation**:
   - Download and install Tesseract-OCR from the official website: https://github.com/tesseract-ocr/tesseract
   - Set the Tesseract executable path to the location where Tesseract is installed.

2. **Python Dependencies**:
   - You need to install the `Pillow` library for image processing and the `pytesseract` library for interfacing with Tesseract.

   Install the required libraries using pip:

   ```bash
   pip install Pillow pytesseract
   ```

## Usage

1. Clone this repository to your local machine or download the Python script.

2. Set the Tesseract executable path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract_executable'
   ```

3. Specify the path to the image you want to extract text from:
   ```python
   image_path = 'path_to_your_image.png'
   ```

4. Run the Python script:

   ```bash
   ExtractText(image).py
   ```

5. The script will open the specified image, extract text from it using Tesseract OCR, and display the extracted text in the console.

## Customization

You can customize the script to suit your needs. For example, you can change the image path or add additional image processing steps before text extraction.




# Text Extraction from Live Video using Tesseract OCR and OpenCV

This project demonstrates how to extract text from a live video stream using the Tesseract OCR (Optical Character Recognition) library and OpenCV in Python. The script captures video from your webcam, processes the frames, and extracts text from the live video feed.

## Prerequisites

Before running the script, make sure you have the following prerequisites set up:

1. **Tesseract-OCR Installation**:
   - Download and install Tesseract-OCR from the official website: https://github.com/tesseract-ocr/tesseract
   - Set the Tesseract executable path in the script to the location where Tesseract is installed.

2. **Python Dependencies**:
   - You need to install the `pytesseract` library for interfacing with Tesseract and the `OpenCV` library for working with video frames.

   Install the required libraries using pip:

   ```bash
   pip install pytesseract opencv-python
   ```

## Usage

1. Clone this repository to your local machine or download the Python script.

2. Set the Tesseract executable path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract_executable'
   ```

3. Run the Python script:

   ```bash
   ExtractText(vedio).py
   ```

4. The script will open the video feed from your webcam and continuously process frames.
   - It converts each frame to grayscale, enhancing text extraction.
   - It performs OCR on the grayscale frame to extract text.
   - The extracted text is displayed in the console.

5. Press 'q' to exit the live video stream.

## Customization

You can customize the script according to your needs. For instance, you can change the video capture source (e.g., using a different camera) or modify the frame processing steps for better OCR results.
