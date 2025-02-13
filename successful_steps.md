# Technical Implementation Guide

## System Architecture

### Core Components
The system implements a modular architecture with clear separation of concerns:

1. Configuration Layer
   - Environment configuration
   - Field definitions
   - Coordinate mappings
   - Path management
   - Section-based organization

2. Processing Layer
   - PDF document handling
   - Word document processing
   - Template management
   - Output generation
   - Multi-coordinate support

3. Presentation Layer
   - Dynamic form generation
   - Section-based organization
   - User input handling
   - Validation
   - Feedback system

### Implementation Details

#### Environment Setup
```bash
# Development Environment
python3 -m venv venv
source venv/bin/activate

# Core Dependencies
brew install pymupdf  # macOS PDF processing
pip install python-docx  # Word processing
pip install pyinstaller  # Standalone builds
```

#### Module Structure
```python
src/
    config.py         # Environment configuration
    │                 # Path management
    │                 # Resource location
    │
    fields_config.py  # Field definitions
    │                 # Coordinate mappings
    │                 # Display names
    │                 # Section organization
    │
    gui/
    │   form.py       # Dynamic form generation
    │                 # Section-based layout
    │                 # Input handling
    │                 # Validation
    │
    pdf/
    │   pdf_reader.py # PDF processing
    │                 # Text insertion
    │                 # Coordinate mapping
    │                 # Multi-page handling
    │
    word/
        word_reader.py # Word processing
        │              # Table handling
        │              # Cell modification
        │              # Multi-coordinate support
        │
        word_table_inspector.py  # Table inspection
                                # Structure visualization
                                # Field mapping
```

### Form Organization

#### Section Structure
```python
class DraudimasGUI:
    """Main application interface with sectioned organization.
    
    Sections:
    - Common Data (Bendri Duomenys)
    - Natural Persons (Fiziniai Asmenys)
    - Legal Entities (Juridiniai Asmenys)
    - Farm Data (Ūkio Duomenys)
    - Representatives (Atstovas)
    - Bank Details (Banko Duomenys)
    - Contacts (Kontaktai)
    """
```

### Document Processing

#### PDF Processing
- Framework: PyMuPDF (MuPDF)
- Character Encoding: UTF-8
- Coordinate System: Bottom-left origin
- Text Insertion: Absolute positioning
- Multi-page support with page-specific handling
- Incremental save management

#### Word Processing
- Framework: python-docx
- Document Structure: Table-based
- Cell Identification: Table/Row/Column indices
- Content Preservation: Existing text maintained
- Multi-coordinate support for repeated fields
- Table Inspection:
    - Structure visualization in markdown
    - Field location mapping
    - Multiple coordinate sets
    - Generated reports for field mapping

#### Template Support
- PDF Templates:
  - Dr paraiška 2025.pdf
  - Pasėlių sąrašas 2025.pdf
- Word Templates:
  - Europos paramos paraiška KPP.docx
  - NAC paraiška 2025.docx
  - De minimis nauja paraiska 2025.docx
  - Sutikimas dėl dokumentų siuntimo el. laišku.docx
  - Sutikimas RINKODAROS BDR 2024.docx

#### GUI Implementation
- Framework: tkinter
- Layout: Section-based organization
- Scrolling: Canvas-based implementation
- Validation: Real-time field validation
- Sections: Logical grouping of related fields

### Data Structures

#### Field Configuration
```python
FIELD_NAMES = {
    "field_id": "Display Name",
    # Field definitions by type
}

PDF_COORDINATES = {
    "template.pdf": {
        "field_id": [
            {"page": int, "x": float, "y": float},
            # Multiple coordinates
        ]
    }
}

WORD_COORDINATES = {
    "template.docx": {
        "field_id": [
            {"table": int, "row": int, "col": int},
            # Multiple coordinates
        ]
    }
}
```

### Implementation Patterns

#### Template Processing
```python
class PDFHandler:
    """PDF document handler.
    
    Responsibilities:
    - Template copying
    - Text insertion
    - Coordinate mapping
    - Multi-page handling
    - Error handling
    """
    
class WordHandler:
    """Word document handler.
    
    Responsibilities:
    - Template management
    - Table navigation
    - Cell modification
    - Content preservation
    - Multi-coordinate support
    """
```

#### GUI Components
```python
class Section:
    """Section container implementation.
    
    Features:
    - Grouped fields
    - Section title
    - Related field organization
    - Dynamic field creation
    """
    
class DraudimasGUI:
    """Main application interface.
    
    Components:
    - Section-based organization
    - Dynamic form generation
    - Field validation
    - Event handling
    - User feedback
    """
```

[Rest of existing content remains the same...]

## Recent Improvements

### GUI Organization
- Implemented section-based form organization
- Added new sections for different entity types
- Improved field grouping and organization
- Enhanced visual layout and spacing

### Document Support
- Added support for new document templates
- Enhanced Word document handling with multiple coordinate support
- Improved PDF text placement reliability
- Added support for various document types

### Field Configuration
- Extended field definitions for comprehensive entity support
- Added new fields for juridical person support
- Improved field naming and organization
- Enhanced coordinate mapping for multi-page documents
- Added support for representative details
- Expanded farm-specific data fields

### Document Processing
- Improved handling of multiple coordinates in Word documents
- Enhanced PDF text placement with better save handling
- Added verification steps for text placement
- Improved error handling and debugging information

[Previous content continues...]