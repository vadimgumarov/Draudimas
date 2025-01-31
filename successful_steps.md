# Successful Steps

## Project Overview
A document automation application that fills in multiple document types (PDF and Word) with the same input data. The application uses a GUI interface for data entry and handles both PDF and Word documents simultaneously.

## Development Environment Setup (macOS)
1. Package Management:
```bash
# Install required packages via Homebrew
brew install pymupdf     # For PDF handling
brew install pandoc      # For document conversions
```

2. Python Virtual Environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install required Python packages
pip install python-docx  # For Word document handling
```

## Project Structure
```
project_root/
├── draudimas.py         # Main entry point
├── src/
│   ├── __init__.py    
│   ├── config.py       # Path configurations
│   ├── fields_config.py # Field coordinates for documents
│   ├── gui/
│   │   ├── __init__.py
│   │   └── form.py     # GUI implementation
│   ├── pdf/           
│   │   ├── __init__.py
│   │   └── pdf_reader.py   # PDF handling functions
│   └── word/
│       ├── __init__.py
│       ├── word_reader.py  # Word document handling
│       └── word_table_inspector.py  # Utility for finding table coordinates
├── templates/          # Template directory
│   ├── Dr_paraiška_2025.pdf
│   ├── Pasėlių_sąrašas_2025.pdf
│   ├── Pasėlių_sąrašas_JAVAI_2025.pdf
│   └── Pasėlių_sąrašas_ANKŠTINIAI_2025.pdf
└── cases/             # Output directory for processed documents
```

## Git Workflow
1. Main Branch Organization:
   - main: Stable, production-ready code
   - dev: Development branch, base for feature branches
   - feature branches: Individual features (e.g., feature/word-support)

2. Branch Strategy:
```bash
# Create feature branch
git checkout -b feature/name

# After feature completion
git checkout main
git merge feature/name

# Return to dev for new development
git checkout dev
```

## Implemented Features

### 1. PDF Document Handling
- PDF text insertion at specific coordinates
- UTF-8 support for Lithuanian characters
- Template copying to case folders
- Coordinate-based text placement
- Error handling and debugging information

### 2. Word Document Handling
- Table cell modifications
- Preservation of existing cell content
- Automated template copying
- Structural document navigation (tables, rows, cells)
- Debugging tools for locating table coordinates

### 3. GUI Interface
- Dynamic form generation from configuration
- Field validation
- Success/error message handling
- Common input for both PDF and Word documents

### 4. Configuration System
- Separate path configurations (config.py)
- Field coordinates for PDF files
- Table coordinates for Word documents
- Common field definitions

## Document Field Configuration
Located in fields_config.py:
```python
# Common fields
FIELD_NAMES = {
    "asmens_kodas": "Asmens Kodas / Imones kodas",
    "pavarde_imone": "Pavarde / Imones Pavadinimas",
    "vardas": "Vardas",
    "gimimo_data": "Gimimo Data"
}

# PDF coordinates
PDF_COORDINATES = {
    "Dr_paraiška_2025.pdf": {
        "asmens_kodas": {"page": 1, "x": 167, "y": 183},
        # Additional fields...
    }
}

# Word document coordinates
WORD_COORDINATES = {
    "Europos_paramos_paraiška_KPP.docx": {
        "asmens_kodas": {"table": 3, "row": 2, "col": 1}
    }
}
```

## Development Notes
1. File Management:
   - Keep consistent file naming
   - Use absolute paths in configuration
   - Handle UTF-8 filenames properly

2. Code Organization:
   - Separate functionality into modules
   - Keep main file minimal
   - Use consistent naming conventions

3. Error Handling:
   - Comprehensive error checking
   - Detailed debug information
   - User-friendly error messages

## Next Steps
1. Standalone Application Development:
   - PyInstaller setup for macOS
   - Windows compatibility
   - Distribution packaging

## Common Issues and Solutions
1. macOS Package Management:
   - Use Homebrew for system packages
   - Use pip in virtual environment for Python packages
   - Handle externally-managed environment restrictions

2. Document Processing:
   - PDF layer warnings can be ignored if functionality works
   - Word documents require table cell preservation
   - Handle both static (PDF) and dynamic (Word) layouts

## Testing
To verify functionality:
1. Create test case with all field types
2. Check both PDF and Word outputs
3. Verify text placement and formatting
4. Ensure Lithuanian characters display correctly