# src/word/word_reader.py
from pathlib import Path
from docx import Document
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
                
            doc = Document(docx_path)
            print(f"Successfully opened Word document: {docx_path.name}")
            print(f"Number of tables: {len(doc.tables)}")
            return True
                
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
            
            # Open and modify the document
            print("Debug: Opening Word document for modification")
            doc = Document(output_path)
            print(f"Debug: Document opened, found {len(doc.tables)} tables")
            
            # Verify table exists
            if table >= len(doc.tables):
                raise Exception(f"Table index {table} out of range (document has {len(doc.tables)} tables)")
            
            table_obj = doc.tables[table]
            
            # Verify row exists
            if row >= len(table_obj.rows):
                raise Exception(f"Row {row} out of range (table has {len(table_obj.rows)} rows)")
            
            # Verify column exists
            if col >= len(table_obj.rows[row].cells):
                raise Exception(f"Column {col} out of range (row has {len(table_obj.rows[row].cells)} cells)")
            
            # Add text to specified cell while preserving existing content
            cell = table_obj.rows[row].cells[col]
            existing_text = cell.text.strip()
            print(f"Debug: Current cell content: '{existing_text}'")
            
            # Add a space between existing text and new text if there is existing text
            if existing_text:
                new_text = f"{existing_text} {text}"
            else:
                new_text = text
                
            cell.text = new_text
            print(f"Debug: Updated cell content: '{cell.text}'")
            
            # Save the document
            print("Debug: Saving modified document")
            doc.save(str(output_path))
            print("Debug: Document saved successfully")
            
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