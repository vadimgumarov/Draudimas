# draudimas.py
import sys
import tkinter as tk
from pathlib import Path
from src.config import TEMPLATES_DIR, CASES_DIR
from src.fields_config import FIELD_NAMES, PDF_COORDINATES, WORD_COORDINATES
from src.pdf.pdf_reader import PDFHandler
from src.word.word_reader import WordHandler
from src.gui.form import DraudimasGUI

def process_form(form_data):
    """Process the submitted form data for all templates."""
    try:
        print(f"Debug: Starting process with data: {form_data.keys()}")
        
        # Create case folder
        case_folder = PDFHandler.create_case_folder(CASES_DIR, form_data["case_number"])

        # Debug Word document detection
        print("\nDebug: Looking for Word documents in templates directory...")
        docx_files = list(TEMPLATES_DIR.glob('*.docx'))
        print("Debug: Found Word files:")
        for doc in docx_files:
            print(f"  - {doc.name}")

        print("\nDebug: Word templates configured in WORD_COORDINATES:")
        for template in WORD_COORDINATES.keys():
            print(f"  - {template}")
        
        # Debug PDF files
        print("\nDebug: Found PDF files in templates directory:")
        pdf_files = [f for f in TEMPLATES_DIR.glob('*.pdf')]
        for pdf in pdf_files:
            print(f"  - {pdf.name}")

        print("\nDebug: Templates configured in PDF_COORDINATES:")
        for template in PDF_COORDINATES.keys():
            print(f"  - {template}")

        # Process PDFs
        for template_name, field_coordinates in PDF_COORDINATES.items():
            template_path = TEMPLATES_DIR / template_name
            print(f"\nDebug: Processing PDF template: {template_name}")
            
            if not template_path.exists():
                print(f"Warning: Template not found: {template_path}")
                continue
            
            # Track if any field was processed for this template
            fields_processed = False
            
            # Process each field defined for this template
            for field_id, coordinates_list in field_coordinates.items():
                if field_id in form_data and form_data[field_id].strip():  # Only process non-empty fields
                    print(f"Debug: Starting to process field: {field_id}")
                    print(f"Debug: Full coordinates list: {coordinates_list}")
                    
                    # Convert single coordinate dictionary to list if necessary
                    if isinstance(coordinates_list, dict):
                        coordinates_list = [coordinates_list]
                        print(f"Debug: Converted single coordinate to list: {coordinates_list}")
                    
                    # Process each coordinate set for this field
                    for i, coord_info in enumerate(coordinates_list, 1):
                        print(f"Debug: Processing coordinate set {i} of {len(coordinates_list)}")
                        print(f"Debug: Current coordinates: {coord_info}")
                        
                        success = PDFHandler.add_text_to_pdf(
                            template_path,
                            case_folder,
                            form_data[field_id],
                            coord_info["page"],
                            coord_info["x"],
                            coord_info["y"]
                        )
                        
                        if success:
                            print(f"Debug: Successfully processed coordinate set {i}")
                        else:
                            print(f"Warning: Failed to process field {field_id} at coordinate set {i}: {coord_info}")
                            continue
                            
                    fields_processed = True
            
            if not fields_processed:
                print(f"Debug: No fields to process for {template_name}")

        # Create multiple copies of crop list if count is provided
        crop_list_count = form_data.get("crop_list_count", "").strip()
        if crop_list_count:
            try:
                count = int(crop_list_count)
                if count > 0:
                    crop_list_template = TEMPLATES_DIR / "Pasėlių sąrašas 2025.pdf"
                    if crop_list_template.exists():
                        success = PDFHandler.create_crop_list_copies(
                            crop_list_template,
                            case_folder,
                            count
                        )
                        if not success:
                            print("Warning: Failed to create crop list copies")
                    else:
                        print("Warning: Crop list template not found")
            except ValueError:
                print("Warning: Invalid crop list count value")

        # Process Word documents
        print("\nDebug: Starting Word document processing...")
        try:
            for template_name, field_coordinates in WORD_COORDINATES.items():
                template_path = TEMPLATES_DIR / template_name
                print(f"\nDebug: Attempting to process Word template: {template_name}")
                print(f"Debug: Full path: {template_path}")
                print(f"Debug: File exists: {template_path.exists()}")
                
                if not template_path.exists():
                    print(f"Warning: Word template not found: {template_path}")
                    continue
                
                # Track if any field was processed for this template
                fields_processed = False
                
                # Process each field defined for this template
                for field_id, coord_info in field_coordinates.items():
                    if field_id in form_data and form_data[field_id].strip():  # Only process non-empty fields
                        print(f"Debug: Processing Word field: {field_id}")
                        
                        # Handle both single and multiple coordinates
                        if isinstance(coord_info, list):
                            # Multiple coordinates
                            for location in coord_info:
                                success = WordHandler.add_text_to_docx(
                                    template_path,
                                    case_folder,
                                    form_data[field_id],
                                    location["table"],
                                    location["row"],
                                    location["col"]
                                )
                                if not success:
                                    raise Exception(f"Failed to process field {field_id} in {template_name}")
                        else:
                            # Single coordinate
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
                        
                        fields_processed = True
                
                if not fields_processed:
                    print(f"Debug: No fields to process for {template_name}")
                    
        except Exception as e:
            print(f"Debug: Error in Word processing: {str(e)}")
            raise

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