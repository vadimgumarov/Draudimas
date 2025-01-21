# src/pdf/reader.py
from pathlib import Path
import fitz
import shutil
from datetime import datetime

class PDFHandler:
    @staticmethod
    def read_pdf(pdf_path: Path) -> bool:
        """Read a PDF file and verify it can be opened."""
        try:
            if not pdf_path.exists():
                print(f"Error: File not found: {pdf_path}")
                return False
                
            with fitz.open(pdf_path) as pdf_document:
                page_count = len(pdf_document)
                print(f"Successfully opened PDF: {pdf_path.name}")
                print(f"Number of pages: {page_count}")
                return True
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def add_text_to_pdf(template_path: Path, output_path: Path, text: str, page_number: int, x: float, y: float) -> bool:
        """Add text to PDF at specified coordinates."""
        try:
            # Copy template to new location
            shutil.copy2(template_path, output_path)
            
            # Open the copied file and add text
            with fitz.open(output_path) as pdf_document:
                page = pdf_document[page_number]
                page.insert_text((x, y), text)
                pdf_document.save(output_path)
            
            print(f"Successfully added text to PDF: {output_path}")
            return True
            
        except Exception as e:
            print(f"Error adding text to PDF: {str(e)}")
            return False

    @staticmethod
    def create_case_folder(base_dir: Path, case_name: str) -> Path:
        """Create a case folder with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        case_folder = base_dir / f"{case_name}_{timestamp}"
        case_folder.mkdir(parents=True, exist_ok=True)
        return case_folder