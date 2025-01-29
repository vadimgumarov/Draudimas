# draudimas.py
import sys
import tkinter as tk
from pathlib import Path
from src.config import TEMPLATES_DIR, CASES_DIR
from src.fields_config import FIELD_NAMES, TEMPLATE_COORDINATES
from src.pdf.reader import PDFHandler
from src.gui.form import DraudimasGUI

def process_form(form_data):
    """Process the submitted form data for all templates."""
    try:
        print(f"Debug: Starting process with data: {form_data.keys()}")
        
        # Create case folder
        case_folder = PDFHandler.create_case_folder(CASES_DIR, form_data["case_number"])
        
        # Get all PDF files in templates directory
        pdf_files = [f for f in TEMPLATES_DIR.iterdir() if f.suffix.lower() == '.pdf']
        print(f"\nDebug: Found PDF files in templates directory:")
        for pdf_file in pdf_files:
            print(f"  - {pdf_file.name}")
        
        # List configured templates
        print("\nDebug: Templates configured in TEMPLATE_COORDINATES:")
        for template_name in TEMPLATE_COORDINATES.keys():
            print(f"  - {template_name}")
        
        # Process each template that has coordinates configured
        for template_name, field_coordinates in TEMPLATE_COORDINATES.items():
            template_path = TEMPLATES_DIR / template_name
            print(f"\nDebug: Processing template: {template_name}")
            
            if not template_path.exists():
                print(f"Warning: Template not found: {template_path}")
                continue
            
            # Process each field defined for this template
            for field_id, coord_info in field_coordinates.items():
                print(f"Debug: Processing field: {field_id}")
                if field_id in form_data:
                    try:
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
                    except Exception as e:
                        print(f"Debug: Error processing field {field_id}: {str(e)}")
                        print(f"Debug: Field info: {coord_info}")
                        raise
                else:
                    print(f"Debug: Field {field_id} not found in form_data")
        
        # List any templates that were found but not processed
        print("\nDebug: Templates found but not configured:")
        configured_templates = set(TEMPLATE_COORDINATES.keys())
        for pdf_file in pdf_files:
            if pdf_file.name not in configured_templates:
                print(f"  - {pdf_file.name}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    """Main entry point for the application."""
    # Ensure UTF-8 encoding
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'UTF-8')
    except locale.Error:
        print("Warning: UTF-8 locale not available")
    
    root = tk.Tk()
    app = DraudimasGUI(root, process_form)
    app.run()

if __name__ == "__main__":
    main()