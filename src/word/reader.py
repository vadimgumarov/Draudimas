# src/word/reader.py
from pathlib import Path
import subprocess
import shutil
from datetime import datetime

class WordHandler:
    @staticmethod
    def read_docx(docx_path: Path) -> bool:
        """Read a Word document and verify it can be opened using pandoc."""
        try:
            if not docx_path.exists():
                print(f"Error: File not found: {docx_path}")
                return False
            
            # Try to get document info using pandoc
            result = subprocess.run(['pandoc', '--version'], 
                                 capture_output=True, 
                                 text=True)
            print(f"Using Pandoc version: {result.stdout.split()[1]}")
            
            # Try to read document structure
            result = subprocess.run(['pandoc', '-f', 'docx', '-t', 'plain', str(docx_path)],
                                 capture_output=True,
                                 text=True)
            
            if result.returncode == 0:
                print(f"Successfully opened Word document: {docx_path.name}")
                print(f"Document size: {len(result.stdout)} characters")
                return True
            else:
                print(f"Error reading document: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def create_case_folder(base_dir: Path, case_name: str) -> Path:
        """Create a case folder."""
        try:
            case_folder = base_dir / case_name
            print(f"Debug: Creating case folder: {case_folder}")
            case_folder.mkdir(parents=True, exist_ok=True)
            print(f"Debug: Case folder created/verified successfully")
            return case_folder
        except Exception as e:
            print(f"Debug: Error creating case folder: {str(e)}")
            raise