import os
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image
from pdf2image import convert_from_path

# Configure the path to Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the folder containing PDFs
folder_path = r'C:\Users\USER\Documents\prerna'

# Initialize variables
readable_pdf_count = 0
total_pdf_count = 0
skipped_files = []  # List to track skipped files

# Function to check PDF readability
def check_pdf_readability(pdf_path):
    try:
        print(f"Checking readability for: {pdf_path}")
        
        # Extract text from PDF using PyPDF2
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text = page.extract_text()
            if text and text.strip():
                print(f"Text found in {pdf_path} using PyPDF2.")
                return True
        
        # If no text is found, try OCR on images
        print(f"No text found with PyPDF2, attempting OCR on {pdf_path}...")
        images = convert_from_path(pdf_path)
        for image in images:
            text = pytesseract.image_to_string(image)
            if text.strip():
                print(f"Text found in {pdf_path} using OCR.")
                return True

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        skipped_files.append(pdf_path)  # Add problematic file to skipped list
    return False

# Recursive search for PDFs in the folder and subfolders
def search_pdfs_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):  # Walk through directories and files
        for filename in files:
            if filename.lower().endswith(".pdf"):  # Case-insensitive check for '.pdf'
                pdf_path = os.path.join(root, filename)
                yield pdf_path  # Return the full file path of each PDF

# Process PDFs
if os.path.exists(folder_path):
    for pdf_path in search_pdfs_in_folder(folder_path):
        total_pdf_count += 1
        if check_pdf_readability(pdf_path):
            readable_pdf_count += 1

    # Output results
    if total_pdf_count > 0:
        readability_percentage = (readable_pdf_count / total_pdf_count) * 100
        print(f"\nReadable PDFs: {readable_pdf_count}/{total_pdf_count}")
        print(f"Readability Percentage: {readability_percentage:.2f}%")
    else:
        print("No PDFs found in the folder.")

    # Output skipped files
    if skipped_files:
        print("\nSkipped files (could not process):")
        for skipped_file in skipped_files:
            print(f" - {skipped_file}")
