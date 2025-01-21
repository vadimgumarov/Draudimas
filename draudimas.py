# draudimas.py
import sys
from pathlib import Path
from src.pdf.reader import PDFHandler
from src.pdf.inspector.coordinates import PDFCoordinateInspector

def main():
    """Main entry point for the application."""
    template_dir = Path("templates")
    pdf_file = "Dr_paraiska_2025.pdf"
    pdf_path = template_dir / pdf_file
    
    # Verify PDF is readable
    if not PDFHandler.read_pdf(pdf_path):
        return sys.exit(1)
        
    # Launch coordinate inspector
    inspector = PDFCoordinateInspector(pdf_path)
    inspector.run()
    
    return sys.exit(0)

if __name__ == "__main__":
    main()