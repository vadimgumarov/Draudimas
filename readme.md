# Document Field Automation

## Project Goals
- Automate filling fields across multiple document types (PDF and Word)
- Support Windows and macOS platforms
- Handle Lithuanian characters and special formatting
- Provide easy-to-use interface for both platforms

## Current Features
- Multi-document processing (PDF and Word)
- Lithuanian character support
- Special filename handling
- Case-based file organization
- GUI for user input

## Platform Support

### macOS
- Terminal-based setup and execution
- GUI interface for document processing
- Virtual environment management
- UTF-8 encoding support

### Windows (Current)
- Batch file automation
- Basic GUI interface
- Virtual environment setup
- Document processing support

### Windows (Planned Development)

#### Phase 1 - Basic Windows Integration
- [x] Batch file automation
- [x] Basic GUI
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

## File Structure
```
/project_folder
├── lauris_application.py    # Main application
├── field_mappings.json     # Field configuration
├── setup.bat              # Windows setup
├── run.bat               # Windows launcher
├── /templates           # Document templates
└── /cases              # Generated cases
```

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

## Troubleshooting

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

## Version History
- 1.0.0: Initial release
- 1.0.1: Added Lithuanian support
- 1.0.2: Basic Windows support
- 1.0.3: Windows batch automation
- 1.1.0: Planned Windows executable

## Contact & Support
For installation assistance and bug reports, please contact support.
