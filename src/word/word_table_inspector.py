# src/word/word_table_inspector.py
from docx import Document
from pathlib import Path
from src.config import TEMPLATES_DIR

def inspect_tables(file_path: Path):
    """Inspect tables in a Word document."""
    print(f"\nInspecting document: {file_path.name}")
    doc = Document(file_path)
    
    # Loop through all tables
    for table_index, table in enumerate(doc.tables):
        print(f"\nTable {table_index}:")
        print(f"Dimensions: {len(table.rows)} rows x {len(table.columns)} columns")
        print("----------------------------------------")
        
        # Print content of each cell
        for row_index, row in enumerate(table.rows):
            for col_index, cell in enumerate(row.cells):
                content = cell.text.strip()
                if content:  # Only print non-empty cells
                    print(f"Row {row_index}, Col {col_index}:")
                    print(f"'{content}'")
                    print("----------------------------------------")

def main():
    """Inspect tables in Word templates."""
    # Process each Word document
    docx_files = sorted(TEMPLATES_DIR.glob("*.docx"))
    if not docx_files:
        print("No Word documents found in templates directory")
        return
        
    for file_path in docx_files:
        inspect_tables(file_path)

if __name__ == "__main__":
    main()