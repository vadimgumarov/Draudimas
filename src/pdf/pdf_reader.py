# src/pdf/pdf_reader.py
from pathlib import Path
import fitz
import shutil
from datetime import datetime

class PDFHandler:
    @staticmethod
    def create_crop_list_copies(template_path: Path, case_folder: Path, count: int) -> bool:
        """Create multiple copies of the crop list template with sequential numbering."""
        try:
            # Template name components
            base_name = "Pasėlių sąrašas 2025"
            extension = ".pdf"
            
            print(f"\nDebug: Creating {count} copies of crop list")
            print(f"Debug: Template path: {template_path}")
            print(f"Debug: Case folder: {case_folder}")
            
            # The filled copy will become copy #1
            filled_copy = case_folder / f"{base_name}{extension}"
            first_copy = case_folder / f"{base_name} Nr_1{extension}"
            
            # Rename the filled copy if it exists
            if filled_copy.exists():
                print(f"Debug: Renaming filled copy to Nr_1")
                if first_copy.exists():
                    first_copy.unlink()  # Remove existing Nr_1 if it exists
                filled_copy.rename(first_copy)
                print(f"Debug: Successfully renamed to {first_copy.name}")
            
            # Create additional copies from Nr_1
            if count > 1:
                for i in range(2, count + 1):
                    new_filename = f"{base_name} Nr_{i}{extension}"
                    output_path = case_folder / new_filename
                    
                    print(f"Debug: Creating copy {i}: {new_filename}")
                    
                    # Copy from the first (filled) copy
                    shutil.copy2(str(first_copy), str(output_path))
                    print(f"Debug: Successfully created copy {i}")
            
            return True
            
        except Exception as e:
            print(f"Debug: Error creating crop list copies: {str(e)}")
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

    @staticmethod
    def add_text_to_pdf(template_path: Path, case_folder: Path, text: str, page_number: int, x: float, y: float) -> bool:
        """Add text to PDF at specified coordinates."""
        try:
            # Debug text encoding and character info
            print(f"\nDebug: Text encoding analysis:")
            print(f"Debug: Original text: {text}")
            print(f"Debug: Text bytes (UTF-8): {text.encode('utf-8')}")
            print(f"Debug: Character codes: {[ord(c) for c in text]}")
            
            # For the crop list template, always name the output with Nr_1
            if template_path.name == "Pasėlių sąrašas 2025.pdf":
                output_path = case_folder / "Pasėlių sąrašas 2025 Nr_1.pdf"
            else:
                output_path = case_folder / template_path.name
                
            print(f"\nDebug: Processing template: {template_path.name}")
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

                try:
                    # Create text writer with Unicode support
                    tw = fitz.TextWriter(page.rect)
                    
                    # Load a Unicode font
                    font = fitz.Font("helv")
                    
                    # Add text to the writer
                    tw.append((x, y), text, font=font, fontsize=11)
                    
                    # Write the text to the page
                    tw.write_text(page)
                    
                    print("Debug: Text written successfully")
                    
                except Exception as e:
                    print(f"Debug: Text writing failed: {str(e)}")
                    raise

                print("\nDebug: Text inserted, attempting to save")
                pdf_document.save(str(output_path), incremental=True, encryption=0)
                print("Debug: PDF saved successfully")
                
                # Verify the saved content
                with fitz.open(str(output_path)) as verify_doc:
                    verify_page = verify_doc[page_number]
                    text_instances = verify_page.get_text("text")
                    print(f"\nDebug: Verification - Text found in PDF: {text_instances}")
            
            return True
            
        except Exception as e:
            print(f"\nDebug: Exception type: {type(e).__name__}")
            print(f"Debug: Exception message: {str(e)}")
            print(f"Debug: Current path exists: {output_path.exists() if 'output_path' in locals() else 'Not created'}")
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