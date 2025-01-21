# src/pdf/reader.py
from pathlib import Path
import fitz

class PDFHandler:
    """Handle PDF reading and processing operations."""
    
    @staticmethod
    def read_pdf(pdf_path: Path) -> bool:
        """
        Read a PDF file and verify it can be opened.
        
        Args:
            pdf_path (Path): Path to the PDF file
            
        Returns:
            bool: True if file was successfully opened, False otherwise
        """
        try:
            if not pdf_path.exists():
                print(f"Error: File not found: {pdf_path}")
                return False
                
            with fitz.open(pdf_path) as pdf_document:
                page_count = len(pdf_document)
                print(f"Successfully opened PDF: {pdf_path.name}")
                print(f"Number of pages: {page_count}")
                
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