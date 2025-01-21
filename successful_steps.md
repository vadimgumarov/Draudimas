# Successful Steps

## Step 1: Environment Setup (macOS)
1. Install required packages via Homebrew:
```bash
brew install pymupdf
```
NOTE: Do not use pip install as macOS uses externally managed environment

## Step 2: Project Structure
1. Create project directories:
```
project_root/
├── draudimas.py        # Main entry point
├── src/
│   ├── __init__.py    
│   ├── config.py      # Global settings
│   └── pdf/           
│       ├── __init__.py
│       └── reader.py  
├── templates/         # English templates
└── templates_lt/      # Lithuanian templates
```

## Step 3: Git Setup
1. Initialize repository:
```bash
git init
```
2. Create dev branch:
```bash
git checkout -b dev
```

## Step 4: Create Initial Files
1. Create config.py with global paths:
```python
# src/config.py
from pathlib import Path

PROJECT_DIR = Path("/Users/vadim/Desktop/Projects/Draudimas")
TEMPLATES_DIR = PROJECT_DIR / "templates"
TEMPLATES_LT_DIR = PROJECT_DIR / "templates_lt"
```

2. Create PDF reader with basic functionality:
```python
# src/pdf/reader.py
from pathlib import Path
import fitz

class PDFHandler:
    @staticmethod
    def read_pdf(pdf_path: Path) -> bool:
        # Basic PDF reading functionality
        ...
```

## Working Features
1. PDF Reading:
   - Opens PDF successfully
   - Reads metadata
   - Gets page count
   - Basic error handling

## Failed Attempts/Issues
1. pip installations fail due to macOS external environment
   - Solution: Use Homebrew instead

## Next Steps
1. Add coordinate mapping for form fields
2. Implement text insertion capability
3. Add configuration for field positions

## Git Usage
- Work in dev branch
- Commit after each working change
- Merge to main only after feature is fully tested