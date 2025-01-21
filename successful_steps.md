# Successful Steps

## Environment Setup
- Installing pymupdf via Homebrew: `brew install pymupdf` ✅
- NOTE: Do not use pip install as macOS uses externally managed environment

## Project Structure
1. Created basic directory structure:
```
project_root/
├── draudimas.py          # Main entry point
├── src/                  # Source code directory
│   ├── __init__.py      
│   └── pdf/             
│       ├── __init__.py  
│       └── reader.py    
├── templates/           
└── templates_lt/        
```

## Git Setup
- Created dev branch: `git checkout -b dev`
- Work being done in dev branch
- Working changes will be merged to main

## Working Features
1. PDF Reading:
   - Successfully opens PDF
   - Reads metadata
   - Gets page count
   - Basic error handling implemented

## Failed Attempts/Issues
1. pip installations fail due to macOS external environment
   - Solution: Use Homebrew instead of pip
2. Virtual environment setup skipped due to system restrictions