# draudimas.py
import sys
from pathlib import Path
from src.pdf.reader import PDFHandler

def main():
    """Main entry point for the application."""
    template_dir = Path("templates")
    pdf_file = "Dr_paraiska_2025.pdf"
    pdf_path = template_dir / pdf_file
    
    # Initialize PDF handler and try to read the PDF
    success = PDFHandler.read_pdf(pdf_path)
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()