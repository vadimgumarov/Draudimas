# draudimas.py
import sys
import tkinter as tk
from pathlib import Path
from src.config import TEMPLATES_DIR, CASES_DIR
from src.fields_config import FIELD_NAMES, PDF_COORDINATES, WORD_COORDINATES
from src.pdf.pdf_reader import PDFHandler
from src.word.word_reader import WordHandler
from src.gui.form import DraudimasGUI

def process_pdf_templates(case_folder: Path, form_data: dict) -> bool:
    """Process all PDF templates with form data."""
    try:
        for template_name, field_coordinates in PDF_COORDINATES.items():
            template_path = TEMPLATES_DIR / template_name
            print(f"\nDebug: Processing PDF template: {template_name}")
            
            if not template_path.exists():
                print(f"Warning: Template not found: {template_path}")
                continue
            
            # Process each field defined for this template
            for field_id, coord_info in field_coordinates.items():
                if field_id in form_data:
                    success = PDFHandler.add_text_to_pdf(
                        template_path,
                        case_folder,
                        form_data[field_id],
                        coord_info["page"],
                        coord_info["x"],
                        coord_info["y"]
                    )
                    
                    if not success:
                        raise Exception(f"Failed to process field {field_id} in {template_name}")
        return True
    except Exception as e:
        print(f"Error in PDF processing: {str(e)}")
        return False

def process_word_templates(case_folder: Path, form_data: dict) -> bool:
    """Process all Word templates with form data."""
    try:
        for template_name, field_coordinates in WORD_COORDINATES.items():
            template_path = TEMPLATES_DIR / template_name
            print(f"\nDebug: Processing Word template: {template_name}")
            
            if not template_path.exists():
                print(f"Warning: Template not found: {template_path}")
                continue
            
            # Process each field defined for this template
            for field_id, coord_info in field_coordinates.items():
                if field_id in form_data:
                    success = WordHandler.add_text_to_docx(
                        template_path,
                        case_folder,
                        form_data[field_id],
                        coord_info["table"],
                        coord_info["row"],
                        coord_info["col"]
                    )
                    
                    if not success:
                        raise Exception(f"Failed to process field {field_id} in {template_name}")
        return True
    except Exception as e:
        print(f"Error in Word processing: {str(e)}")
        return False

def process_form(form_data: dict) -> bool:
    """Process the submitted form data for all templates."""
    try:
        print(f"Debug: Starting process with data: {form_data.keys()}")
        
        # Create case folder
        case_folder = PDFHandler.create_case_folder(CASES_DIR, form_data["case_number"])
        
        # Process all templates
        pdf_success = process_pdf_templates(case_folder, form_data)
        word_success = process_word_templates(case_folder, form_data)
        
        return pdf_success and word_success
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = DraudimasGUI(root, process_form)
    app.run()

if __name__ == "__main__":
    main()