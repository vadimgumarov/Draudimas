# src/pdf/pdf_reader.py
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
            # Debug text encoding and character info
            print(f"\nDebug: Text encoding analysis:")
            print(f"Debug: Original text: {text}")
            print(f"Debug: Text bytes (UTF-8): {text.encode('utf-8')}")
            print(f"Debug: Character codes: {[ord(c) for c in text]}")
            
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