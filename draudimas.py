# draudimas.py
import sys
import tkinter as tk
from src.config import TEMPLATES_DIR, CASES_DIR
from src.fields_config import PDF_FIELDS
from src.pdf.reader import PDFHandler
from src.gui.form import DraudimasGUI

def process_form(form_data):
    """Process the submitted form data."""
    try:
        pdf_file = "Dr_paraiska_2025.pdf"
        template_path = TEMPLATES_DIR / pdf_file
        
        # Verify directories exist
        if not TEMPLATES_DIR.exists():
            raise Exception(f"Templates directory not found: {TEMPLATES_DIR}")
            
        if not template_path.exists():
            raise Exception(f"Template PDF not found: {template_path}")
        
        # Create case folder
        case_folder = PDFHandler.create_case_folder(CASES_DIR, form_data["case_number"])
        
        # Process each field
        for field_id, field_info in PDF_FIELDS.items():
            # Get the corresponding value from form_data
            text = form_data[field_id]
            
            # Add text to PDF
            success = PDFHandler.add_text_to_pdf(
                template_path,
                case_folder,
                text,
                field_info["page"],
                field_info["x"],
                field_info["y"]
            )
            
            if not success:
                raise Exception(f"Failed to process field: {field_info['name']}")
        
        return True
        
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