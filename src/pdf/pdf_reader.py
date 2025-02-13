# src/pdf/pdf_reader.py
from pathlib import Path
import fitz
import shutil
from datetime import datetime

class PDFHandler:
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

    @staticmethod
    def add_text_to_pdf(template_path: Path, case_folder: Path, text: str, page_number: int, x: float, y: float) -> bool:
        """Add text to PDF at specified coordinates."""
        try:
            # For the crop list template, always name the output with Nr_1
            if template_path.name == "Pasėlių sąrašas 2025.pdf":
                output_path = case_folder / "Pasėlių sąrašas 2025 Nr_1.pdf"
            else:
                output_path = case_folder / template_path.name
            
            # If this is the first time adding text to this case, copy the template
            if not output_path.exists():
                case_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(template_path), str(output_path))
            
            # Open PDF and get page
            pdf_document = fitz.open(str(output_path))
            page = pdf_document[page_number]
            
            # Create text writer
            tw = fitz.TextWriter(page.rect)
            font = fitz.Font("helv")
            
            # Add text
            tw.append((x, y), text, font=font, fontsize=11)
            tw.write_text(page)
            
            # Commit changes to this page
            page.clean_contents()
            
            # Save using temporary file
            temp_path = output_path.with_suffix('.tmp.pdf')
            pdf_document.save(str(temp_path))
            pdf_document.close()
            
            # Replace original with temporary file
            shutil.move(str(temp_path), str(output_path))
            
            return True
            
        except Exception as e:
            print(f"Error adding text to PDF: {str(e)}")
            if 'pdf_document' in locals():
                pdf_document.close()
            if 'temp_path' in locals() and temp_path.exists():
                temp_path.unlink()
            return False

    @staticmethod
    def create_crop_list_copies(template_path: Path, case_folder: Path, count: int) -> bool:
        """Create multiple copies of the crop list template with sequential numbering."""
        try:
            # Template name components
            base_name = "Pasėlių sąrašas 2025"
            extension = ".pdf"
            
            # The filled copy will become copy #1
            filled_copy = case_folder / f"{base_name}{extension}"
            first_copy = case_folder / f"{base_name} Nr_1{extension}"
            
            # Rename the filled copy if it exists
            if filled_copy.exists():
                if first_copy.exists():
                    first_copy.unlink()  # Remove existing Nr_1 if it exists
                filled_copy.rename(first_copy)
            
            # Create additional copies from Nr_1
            if count > 1:
                for i in range(2, count + 1):
                    new_filename = f"{base_name} Nr_{i}{extension}"
                    output_path = case_folder / new_filename
                    shutil.copy2(str(first_copy), str(output_path))
            
            return True
            
        except Exception as e:
            print(f"Error creating crop list copies: {str(e)}")
            return False

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