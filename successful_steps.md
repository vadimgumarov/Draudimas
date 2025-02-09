# Technical Implementation Guide

## System Architecture

### Core Components
The system implements a modular architecture with clear separation of concerns:

1. Configuration Layer
   - Environment configuration
   - Field definitions
   - Coordinate mappings
   - Path management

2. Processing Layer
   - PDF document handling
   - Word document processing
   - Template management
   - Output generation

3. Presentation Layer
   - Dynamic form generation
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
src/
    config.py         # Environment configuration
    │                 # Path management
    │                 # Resource location
    │
    fields_config.py  # Field definitions
    │                 # Coordinate mappings
    │                 # Display names
    │
    gui/
    │   form.py       # Dynamic form generation
    │                 # Input handling
    │                 # Validation
    │
    pdf/
    │   pdf_reader.py # PDF processing
    │                 # Text insertion
    │                 # Coordinate mapping
    │
    word/
        word_reader.py # Word processing
        │              # Table handling
        │              # Cell modification
        │
        word_table_inspector.py  # Table inspection
                                # Structure visualization
                                # Field mapping
```

### Technical Specifications

#### PDF Processing
- Framework: PyMuPDF (MuPDF)
- Character Encoding: UTF-8
- Coordinate System: Bottom-left origin
- Text Insertion: Absolute positioning

#### Word Processing
- Framework: python-docx
- Document Structure: Table-based
- Cell Identification: Table/Row/Column indices
- Content Preservation: Existing text maintained
- Table Inspection:
    - Structure visualization in markdown
    - Field location mapping
    - Merged cell detection
    - Cell content analysis
    - Generated reports for field mapping

#### GUI Implementation
- Framework: tkinter
- Layout: Dynamic generation
- Scrolling: Canvas-based implementation
- Validation: Real-time field validation

### Data Structures

#### Field Configuration
```python
FIELD_NAMES = {
    "field_id": "Display Name",
    # Field definitions
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
        "field_id": {"table": int, "row": int, "col": int}
    }
}
```

#### Processing Logic
```python
def process_form(form_data: dict) -> bool:
    """
    Process form data across all templates.
    
    Args:
        form_data: Dictionary of field values
        
    Returns:
        bool: Success status
        
    Processing Flow:
    1. Create case directory
    2. Process PDF templates
    3. Process Word templates
    4. Validate outputs
    """
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
    - Error handling
    """
    
class WordHandler:
    """Word document handler.
    
    Responsibilities:
    - Template management
    - Table navigation
    - Cell modification
    - Content preservation
    """
```

#### GUI Components
```python
class ScrollableFrame:
    """Scrollable container implementation.
    
    Features:
    - Dynamic content
    - Mousewheel support
    - Responsive layout
    - Custom styling
    """
    
class DraudimasGUI:
    """Main application interface.
    
    Components:
    - Dynamic form generation
    - Field validation
    - Event handling
    - User feedback
    """
```

### Cross-Platform Considerations

#### Path Management
```python
def get_executable_dir():
    """Get executable directory for standalone mode.
    
    Handles:
    - Development environment
    - Standalone mode
    - Platform differences
    - Resource location
    """
```

#### Resource Management
```python
class ResourceManager:
    """Resource handling for standalone mode.
    
    Responsibilities:
    - Template location
    - Output management
    - Path resolution
    - State persistence
    """
```

### Error Handling

#### Exception Hierarchy
```python
class DocumentError(Exception):
    """Base class for document processing errors."""
    
class PDFError(DocumentError):
    """PDF-specific processing errors."""
    
class WordError(DocumentError):
    """Word document processing errors."""
```

#### Validation
```python
def validate_field(field_id: str, value: str) -> bool:
    """
    Validate field value.
    
    Checks:
    - Required fields
    - Format validation
    - Character encoding
    - Length constraints
    """
```

### Building Process

#### Development Build
```bash
python3 draudimas.py  # Direct execution
```

#### Standalone Build
```bash
# Clean previous build
rm -rf build dist

# Build application
pyinstaller draudimas.spec

# Prepare distribution
mkdir dist/cases
cp -r templates dist/
```

### Testing Methodology

#### Functional Testing
1. Document Processing
   - Template copying
   - Text insertion
   - Multi-field handling
   - Error cases

2. GUI Testing
   - Form generation
   - Field validation
   - Event handling
   - Error display

#### Integration Testing
1. End-to-End Processing
   - Complete form submission
   - Multiple template processing
   - Output verification
   - Error handling

2. Cross-Platform Testing
   - macOS functionality
   - Windows compatibility
   - Resource handling
   - Path resolution

### Known Issues and Solutions

#### PDF Processing
- Layer warnings in specific templates
  - Non-critical for functionality
  - Can be safely ignored
  - No impact on output

#### GUI Implementation
- Mousewheel scrolling issues
  - Platform-specific behavior
  - Requires custom implementation
  - Event binding modifications

#### Word Processing
- Cell content preservation
  - Table structure complexity
  - Content formatting
  - Multiple field handling

### Future Considerations

#### Performance Optimization
- Batch processing
- Memory management
- GUI responsiveness
- Document handling

#### Security Implementation
- Document integrity
- Access control
- Audit logging
- Data protection

#### Feature Extensions
- Template management
- Data persistence
- Batch processing
- Reporting system