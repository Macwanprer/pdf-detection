# PDF Readability Checker

This project contains a Python script designed to check the readability of PDF files in a specified folder. It uses two methods to detect readable content:

1. **Text Extraction** using `PyPDF2` (if the PDF contains directly extractable text).
2. **OCR (Optical Character Recognition)** using `Tesseract` and `pdf2image` (if the PDF contains images or scanned content).

The script will check all `.pdf` files in the folder (including subdirectories) and print a summary with the following results:
- Number of readable PDF files.
- Percentage of readable PDFs.
- List of skipped files (if any errors occurred during processing).

## Requirements

Before running the script, ensure you have the following dependencies installed:
- `pytesseract` (for OCR)
- `PyPDF2` (for PDF text extraction)
- `pdf2image` (for converting PDFs to images)
- `Pillow` (for image handling)

Install these dependencies using `pip`:
```bash
pip install pytesseract PyPDF2 pdf2image Pillow



