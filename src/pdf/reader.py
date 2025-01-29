# src/pdf/reader.py
import sys
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
                
            with fitz.open(str(pdf_path)) as pdf_document:
                page_count = len(pdf_document)
                print(f"Successfully opened PDF: {pdf_path.name}")
                print(f"Number of pages: {page_count}")
                return True
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def add_text_to_pdf(template_path: Path, case_folder: Path, text: str, page_number: int, x: float, y: float) -> bool:
        """Add text to PDF at specified coordinates."""
        try:
            output_path = case_folder / template_path.name
            print(f"Debug: Processing template: {template_path.name}")
            print(f"Debug: Output path: {output_path}")
            
            # If this is the first time adding text to this case, copy the template
            if not output_path.exists():
                print("Debug: Creating new copy of template")
                case_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(template_path), str(output_path))
                print("Debug: Template copied successfully")
            
            # Open and modify the PDF
            print("Debug: Opening PDF for modification")
            with fitz.open(str(output_path)) as pdf_document:
                print(f"Debug: Successfully opened PDF, pages: {len(pdf_document)}")
                page = pdf_document[page_number]
                print("Debug: Adding text to page")
                
                # Create text using insert_text
                rc = page.insert_text(
                    point=(x, y),
                    text=text,
                    fontsize=11,
                    fontname="helv",
                    rotate=0
                )
                
                if not rc:  # text insertion failed
                    raise Exception("Text insertion failed")
                    
                print("Debug: Text inserted, attempting to save")
                pdf_document.save(str(output_path), incremental=True, encryption=0)
                print("Debug: PDF saved successfully")
            
            return True
            
        except Exception as e:
            print(f"Debug: Exception type: {type(e).__name__}")
            print(f"Debug: Exception message: {str(e)}")
            print(f"Debug: Current path exists: {output_path.exists()}")
            return False

    @staticmethod
    def create_case_folder(base_dir: Path, case_name: str) -> Path:
        """Create a case folder."""
        try:
            case_folder = base_dir / case_name
            print(f"Debug: Creating case folder: {case_folder}")
            case_folder.mkdir(parents=True, exist_ok=True)
            print(f"Debug: Case folder created/verified successfully")
            return case_folder
        except Exception as e:
            print(f"Debug: Error creating case folder: {str(e)}")
            raise