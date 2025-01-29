# src/word/word_reader.py
from pathlib import Path
import subprocess
import shutil
from datetime import datetime

class WordHandler:
    @staticmethod
    def read_docx(docx_path: Path) -> bool:
        """Read a Word document and verify it can be opened."""
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
    def add_text_to_docx(template_path: Path, case_folder: Path, text: str, table: int, row: int, col: int) -> bool:
        """Add text to Word document at specified table cell."""
        try:
            output_path = case_folder / template_path.name
            print(f"Debug: Processing template: {template_path.name}")
            print(f"Debug: Output path: {output_path}")
            
            # If this is the first time adding text to this case, copy the template
            if not output_path.exists():
                print("Debug: Creating new copy of template")
                case_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(template_path), str(output_path))
                print("Debug: Template copied successfully")
            
            # Convert the document to a temporary markdown file
            temp_md = case_folder / f"{template_path.stem}_temp.md"
            result = subprocess.run([
                'pandoc',
                '-f', 'docx',
                '-t', 'markdown',
                str(output_path),
                '-o', str(temp_md)
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                raise Exception(f"Error converting to markdown: {result.stderr}")
            
            # Read the markdown content
            with open(temp_md, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Modify the content (this is where we'll need to implement table cell modification)
            # TODO: Implement table cell modification logic
            # For now, we'll just append the text to verify the process works
            with open(temp_md, 'a', encoding='utf-8') as f:
                f.write(f"\nAdded text: {text}")
            
            # Convert back to docx
            result = subprocess.run([
                'pandoc',
                '-f', 'markdown',
                '-t', 'docx',
                str(temp_md),
                '-o', str(output_path)
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                raise Exception(f"Error converting back to docx: {result.stderr}")
            
            # Clean up temporary file
            temp_md.unlink()
            
            print("Debug: Document modified and saved successfully")
            return True
            
        except Exception as e:
            print(f"Debug: Exception type: {type(e).__name__}")
            print(f"Debug: Exception message: {str(e)}")
            print(f"Debug: Current path exists: {output_path.exists() if 'output_path' in locals() else 'Not created'}")
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