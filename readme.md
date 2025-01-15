# Document Field Automation

## Project Goals
Automate the process of filling in text fields across multiple document types:
- Unified form input for all documents
- Support Windows and macOS platforms
- Handle Lithuanian characters and special formatting
- Provide easy-to-use interface for both platforms


## Main Features
- Process multiple document formats (PDF and Word)
- Special filename handling
- Handle special characters and spaces in filenames
- Support landscape and portrait PDF orientations
- Create timestamped case folders for each submission
- GUI for user input with multiple fields
- Option to process multiple cases in succession


## MacOS Support

- Terminal-based setup and execution
- GUI interface for document processing
- Virtual environment management
- UTF-8 encoding support

## Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install PyMuPDF  # For PDF handling
pip install python-docx  # For Word documents
pip install reportlab  # For PDF text overlay
```
## Technical Documentation

### PDF Processing
```python
def add_text_to_pdf(self, input_path, output_path, text, page_number, x, y):
    # Handles text addition to PDFs with coordinates
    # x, y: coordinates from bottom-left of page
    # page_number: 0-based page index
```

### Word Document Processing
```python
def fill_word(self, input_path, output_path, text_replacements, table_locations):
    # Handles table cell updates in Word documents
    # table_locations: list of {table_index, row, column}
```

## Development Roadmap

### Phase 1 - Completed
- [x] Basic PDF text insertion
- [x] GUI form creation
- [x] Case folder management

### Phase 2 - Current
- [ ] Improved error handling
- [ ] Better debug information
- [ ] File validation checks
- [ ] Input validation


### Phase 3 - Planned
- [ ] Support for more document types
- [ ] Word document table handling
- [ ] Batch processing capabilities
- [ ] Configuration GUI
- [ ] Template management interface

### Phase 4 - Future
- [ ] Automated testing
- [ ] PDF preview
- [ ] Coordinate picker tool
- [ ] Multi-language support

## File Structure
```
project_root/
├── src/                    # Source code directory
│   ├── utils/             # Utility scripts
│   │   ├── debug_filenames.py
│   │   └── analyze_word.py
│   └── lauris_application.py
├── config/                # Configuration files
│   └── field_mappings.json
├── scripts/               # Setup and run scripts
│   ├── setup.bat
│   └── get-pip.py
├── templates/             # Template documents
├── cases/                # Generated cases
└── README.md
```
### Field Mapping Structure
```python
field_mappings = {
    "fields": [
        {
            "name": "field_internal_name",
            "display_name": "Field Label in GUI",
            "locations": {
                "document1.pdf": [[page, x, y]],
                "document2.docx": {
                    "table_locations": [
                        {"table_index": 0, "row": 1, "column": 1}
                    ]
                }
            }
        }
    ]
}
```

## Example Configuration
```json
{
    "fields": [
        {
            "name": "asmens_imones_kodas",
            "display_name": "Asmens/Imones kodas",
            "locations": {
                "Dr. paraiška 2025.pdf": [[1, 166, 182]],
                "Pasėlių sąrašas 2025.pdf": [[0, 545, 98]],
                "Europos paramos paraiška KPP.docx": {
                    "table_locations": [
                        {"table_index": 3, "row": 2, "column": 1}
                    ]
                }
            }
        }
    ]
}
```

## Troubleshooting Guide for MacOS

### Common Issues and Solutions

1. Files Not Being Modified
   - Verify filenames match exactly in field_mappings.json
   - Check file permissions in templates folder
   - Ensure coordinates are within page boundaries

2. Text Not Appearing in PDFs
   - Verify page numbers (0-based indexing)
   - Check coordinate system orientation
   - Confirm PDF isn't protected/encrypted

3. Word Document Issues
   - Verify table indices are correct
   - Check cell accessibility
   - Ensure proper table structure

4. Character Encoding Problems
   - Use UTF-8 encoding for field_mappings.json
   - Verify document compatibility
   - Check system locale settings

### Debug Steps
1. Run debug_filenames.py to verify file matching
2. Check console output for processing details
3. Inspect generated files in case folder
4. Verify coordinate system with test inputs



## Usage
1. Place template documents in templates folder
2. Configure field_mappings.json with coordinates
3. Run application:
```bash
python lauris_application.py
```
4. Enter case details and field values
5. Choose to process another case or exit

## Known Limitations
- PDF coordinates are page-specific
- Word documents require proper table structure
- Limited font customization
- Single-session processing

## Notes
- Maintain exact filenames as specified in field_mappings.json
- Ensure proper encoding for Lithuanian characters
- Test coordinates before production use
- Regular backups of template documents recommended


## Windows Support (Planned)

#### Phase 1 - Basic Windows Integration
- [ ] Batch file automation
- [ ] Basic GUI
- [ ] Virtual environment setup
- [ ] Document processing support
- [ ] Windows installer script
- [ ] System path handling

#### Phase 2 - Enhanced Windows Support
- [ ] Standalone executable (.exe)
- [ ] Custom installer
- [ ] Windows registry integration
- [ ] File association support
- [ ] Desktop shortcut creation

#### Phase 3 - Advanced Windows Features
- [ ] System tray integration
- [ ] Auto-start capability
- [ ] Windows notification support
- [ ] Multi-user support
- [ ] Admin and user mode

#### Phase 4 - Windows Enterprise Features
- [ ] Network deployment support
- [ ] Active Directory integration
- [ ] Group Policy support
- [ ] Remote configuration
- [ ] Automated updates

## Future Windows Development Details

### Executable Creation
```python
# PlannedExe.py
import PyInstaller.__main__

PyInstaller.__main__.run([
    'lauris_application.py',
    '--onefile',
    '--windowed',
    '--icon=app_icon.ico',
    '--add-data=templates;templates',
    '--name=DocumentAutomation',
    '--version-file=version.txt',
    '--uac-admin'  # For admin privileges
])
```

### Windows Installer Features
- Silent installation option
- Custom installation path
- Dependencies check
- System requirements verification
- Registry entries creation
- File associations setup
- Recovery and repair options

### System Integration
- Windows context menu integration
- File type associations
- Auto-update mechanism
- System tray functionality
- Windows security compliance

### Enterprise Features
- Group Policy templates
- Network deployment scripts
- User access control
- Logging and monitoring
- Remote administration

## Troubleshooting Guide for Windows

### Windows-Specific
1. Installation Issues
   - Admin rights verification
   - System requirements check
   - .NET Framework verification
   - Path environment variables

2. Runtime Issues
   - File permissions
   - Network access
   - Registry permissions
   - User account control

### Development Notes
- Use Windows-specific path handling
- Implement proper registry access
- Handle Windows security features
- Support Windows character encoding
- Maintain cross-platform compatibility

______________________________________________________

## Installation

### macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install PyMuPDF python-docx reportlab
```

### Windows
1. Run `setup.bat` for initial setup
2. Use `run.bat` to launch application
3. (Future) Use Windows installer

## Dependencies
- Python 3.x
- PyMuPDF
- python-docx
- reportlab
- (Future Windows) .NET Framework 4.5+


## Version History - In progress
- 1.0.0: Initial release 


## Contact & Support

For installation assistance and bug reports, please contact support.






