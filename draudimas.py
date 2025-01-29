# draudimas.py
import sys
import tkinter as tk
from src.config import TEMPLATES_DIR, CASES_DIR
from src.fields_config import TEMPLATE_COORDINATES
from src.pdf.reader import PDFHandler
from src.gui.form import DraudimasGUI

def process_form(form_data):
    """Process the submitted form data for all templates."""
    try:
        # Create case folder
        case_folder = PDFHandler.create_case_folder(CASES_DIR, form_data["case_number"])
        
        # Process each template
        for template_name, coordinates in TEMPLATE_COORDINATES.items():
            template_path = TEMPLATES_DIR / template_name
            
            if not template_path.exists():
                print(f"Warning: Template not found: {template_path}")
                continue
            
            # Process each field in the template
            for field_id, coord_info in coordinates.items():
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
        print(f"Error: {str(e)}")
        return False

def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = DraudimasGUI(root, process_form)
    app.run()

if __name__ == "__main__":
    main()