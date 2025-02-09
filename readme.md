# Document Field Automation System

## Project Overview
A sophisticated document automation system designed to handle concurrent field population across multiple document types (PDF and Word) through a unified interface. The system implements a configuration-driven architecture that maintains separation between field definitions, coordinate mappings, and processing logic.

## Core Functionality
- Unified data entry interface for multiple document types
- Simultaneous processing of PDF and Word documents
- Support for multiple field occurrences within documents
- Dynamic form generation from configuration
- Cross-platform compatibility (macOS, Windows planned)
- Word document table inspection and field mapping
- Automatic crop list copy generation with sequential numbering
  - User-defined number of copies
  - Automatic naming (Nr_1, Nr_2, etc.)
  - Copies maintain all filled data from first document
  - Intelligent copy management system

## Technical Architecture

### Component Structure
```
project_root/
├── draudimas.py          # Application entry point
├── draudimas.spec        # PyInstaller configuration
├── src/                  # Source code directory
│   ├── config.py        # Environment configuration
│   ├── fields_config.py # Field definitions and mappings
│   ├── gui/            # User interface components
│   ├── pdf/            # PDF processing modules
│   └── word/           # Word document processing modules
│       ├── word_reader.py  # Word document handling
│       └── word_table_inspector.py  # Table inspection tool
├── templates/           # Document templates
└── cases/              # Processed output
```

### Key Components

#### Configuration System
- Path management for development and production environments
- Field definitions with display names
- Coordinate mappings for PDF documents
- Table cell mappings for Word documents
- Support for multiple field occurrences

#### Document Processing
- PDF processing using PyMuPDF (MuPDF)
- Word document processing using python-docx
    - Table structure inspection and visualization
    - Field location identification
    - Merged cell detection
    - Generated markdown reports for table structure
- UTF-8 support for Lithuanian characters
- Template copying with state preservation
- Coordinate-based text placement
- Table-based cell modifications

#### User Interface
- Dynamic form generation from configuration
- Scrollable interface supporting numerous fields
- Optional field input capabilities
- Validation and error handling
- Success/error feedback system

## Development Environment

### Prerequisites
- Python 3.x
- Virtual Environment
- Git for version control

### Required Packages
- PyMuPDF for PDF processing
- python-docx for Word documents
- PyInstaller for standalone builds
- tkinter for GUI (included with Python)

### Installation
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install core dependencies
brew install pymupdf  # macOS
pip install python-docx
pip install pyinstaller
```

## Version Control Strategy

### Branch Structure
- main: Production-ready code
- dev: Development integration
- feature/*: Feature-specific branches

### Branch Naming Convention
- feature/standalone-mac: macOS standalone support
- feature/standalone-win: Windows standalone support
- feature/improvements: Ongoing enhancements

## Building and Distribution

### Development Build
```bash
python3 draudimas.py
```

### Standalone Build
```bash
pyinstaller draudimas.spec
```

### Distribution Structure
```
dist/
├── draudimas     # Main executable
├── templates/    # Required templates
└── cases/       # Output directory
```

## Current Status
- ✓ Basic PDF processing implemented
- ✓ Basic Word document processing implemented
- ✓ GUI implementation complete
- ✓ macOS standalone support
- ✓ Windows standalone support 
- ⋯ Field mapping expansion ongoing
- ⋯ GUI improvements planned

## Contributing
Development follows a feature-branch workflow:
1. Create feature branch from dev
2. Implement and test changes
3. Merge to dev when complete
4. Regular dev to main merges for releases

## Known Issues
- PDF layer warnings (non-critical)
- Mousewheel scrolling in GUI
- Word document cell preservation complexities

## Future Development
See dev_phases.md for detailed development roadmap and phase information.

## Project Documentation
- README.md: This file
- successful_steps.md: Detailed technical implementation guide
- dev_phases.md: Development phases and roadmap