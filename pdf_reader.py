import sys
from pathlib import Path
import fitz  # PyMuPDF

def read_pdf(pdf_path):
    """
    Read a PDF file and verify it can be opened.
    
    Args:
        pdf_path (Path): Path to the PDF file
        
    Returns:
        bool: True if file was successfully opened, False otherwise
    """
    try:
        # Check if file exists
        if not pdf_path.exists():
            print(f"Error: File not found: {pdf_path}")
            return False
            
        # Try to open PDF
        with fitz.open(pdf_path) as pdf_document:
            # Get basic document info
            page_count = len(pdf_document)
            print(f"Successfully opened PDF: {pdf_path.name}")
            print(f"Number of pages: {page_count}")
            
            # Basic metadata
            metadata = pdf_document.metadata
            print("\nDocument Information:")
            print(f"Title: {metadata.get('title', 'Not available')}")
            print(f"Author: {metadata.get('author', 'Not available')}")
            print(f"Creation Date: {metadata.get('creationDate', 'Not available')}")
            
            return True
            
    except fitz.FileDataError:
        print(f"Error: Not a valid PDF file: {pdf_path}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return False

def main():
    # Define the template directory and PDF file
    template_dir = Path("templates")
    pdf_file = "Dr_paraiska_2025.pdf"
    pdf_path = template_dir / pdf_file
    
    # Try to read the PDF
    success = read_pdf(pdf_path)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()