# draudimas.py
import sys
from src.config import TEMPLATES_DIR, CASES_DIR, FIELDS
from src.pdf.reader import PDFHandler

def get_user_input(prompt: str) -> str:
    """Get input from user with proper error handling."""
    while True:
        value = input(f"{prompt}: ").strip()
        if value:  # Basic validation - ensure not empty
            return value
        print("Error: Input cannot be empty. Please try again.")

def main():
    """Main entry point for the application."""
    pdf_file = "Dr_paraiska_2025.pdf"
    template_path = TEMPLATES_DIR / pdf_file
    
    # Verify directories exist
    if not TEMPLATES_DIR.exists():
        print(f"Error: Templates directory not found: {TEMPLATES_DIR}")
        return sys.exit(1)
        
    if not template_path.exists():
        print(f"Error: Template PDF not found: {template_path}")
        return sys.exit(1)
    
    # Get case name from user
    case_name = get_user_input("\nCase Number")
    
    # Create case folder
    case_folder = PDFHandler.create_case_folder(CASES_DIR, case_name)
    output_path = case_folder / pdf_file
    
    # Process each field
    for field_name, field_info in FIELDS.items():
        # Get text input for field
        text = get_user_input(f"\n{field_info['prompt']}")
        
        # Add text to PDF
        success = PDFHandler.add_text_to_pdf(
            template_path,
            output_path,
            text,
            field_info['page'],
            field_info['x'],
            field_info['y']
        )
        
        if not success:
            print(f"Failed to process field: {field_name}")
            return sys.exit(1)
    
    print(f"\nSuccessfully created case: {case_folder}")
    return sys.exit(0)

if __name__ == "__main__":
    main()