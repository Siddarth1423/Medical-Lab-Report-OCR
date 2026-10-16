# Medical Laboratory Report Text Detection and Recognition

A Python OCR pipeline that extracts text from medical laboratory report images using image preprocessing, patch-based processing, and Tesseract OCR.

## Features
- Grayscale conversion and image denoising
- Adaptive thresholding to improve text contrast
- Patch-based processing for tall/high-resolution images
- OCR text extraction
- Saves extracted text to a `.txt` file

## Technology
Python, OpenCV, Tesseract OCR, Pillow, NumPy, pytesseract.

## Requirements
1. Python 3.10 or newer
2. Tesseract OCR installed separately on Windows:
   https://github.com/UB-Mannheim/tesseract/wiki

## Run on Windows / Git Bash

From the project folder:

```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
python app.py samples/medical_report.png
```

The extracted text is saved to `outputs/extracted_text.txt`.

You can choose another output path:

```bash
python app.py samples/medical_report.png --output outputs/report.txt
```

## Project Structure

```text
Medical-Lab-Report-OCR/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── patch_processing.py
│   └── ocr_engine.py
├── samples/
│   └── medical_report.png
└── outputs/
```

## Important accuracy note
This repository is a working OCR pipeline using Tesseract. It does not include custom PyTorch model training and does not claim a verified 92% recognition accuracy. To report an accuracy figure, evaluate against a labelled dataset and document the metric and results.

## Disclaimer
For educational purposes only. OCR can make mistakes. Always verify extracted text against the original document. Use synthetic or de-identified samples; do not publish private patient information.
