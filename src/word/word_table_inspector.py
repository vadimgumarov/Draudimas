# word_table_inspector.py
from docx import Document
from pathlib import Path
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Get absolute paths
SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPT_DIR.parent.parent / 'templates'
OUTPUT_FILE = SCRIPT_DIR / 'table_list.md'

logger.info(f"Script directory: {SCRIPT_DIR}")
logger.info(f"Templates directory: {TEMPLATES_DIR}")
logger.info(f"Output file will be saved to: {OUTPUT_FILE}")

class TableInspector:
    """Class to handle Word document table inspection."""
    
    def truncate_text(self, text: str) -> str:
        """Truncate long text keeping first 2 and last 2 words."""
        words = text.split()
        if len(words) > 4:
            return f"{' '.join(words[:2])} ... {' '.join(words[-2:])}"
        return text

    def generate_markdown(self, documents_data: dict) -> str:
        """Generate markdown content for table analysis."""
        md_content = ["# Word Document Table Fields\n"]
        
        for doc_name, tables in documents_data.items():
            md_content.append(f"## {doc_name}\n")
            
            for table_idx, table_data in tables.items():
                rows = table_data['dimensions']['rows']
                cols = table_data['dimensions']['cols']
                md_content.append(f"### Table {table_idx} ||| Total rows: {rows} ||| Total columns: {cols}\n\n")
                
                # Generate table content by rows
                for row in range(rows):
                    row_cells = []
                    for col in range(cols):
                        cell_key = f"{row},{col}"
                        cell_info = table_data['cells'].get(cell_key, {"content": "EMPTY", "coords": f"table: {table_idx}, row: {row}, col: {col}"})
                        # Truncate the content
                        truncated_content = self.truncate_text(cell_info['content'])
                        row_cells.append(f"`{truncated_content} [{cell_info['coords']}]`")
                    
                    # Join cells with proper separator and add to beginning and end
                    md_content.append(f"||| {' ||| '.join(row_cells)} |||\n")
                
                md_content.append("\n")
            
            md_content.append("\n")
            
        return "".join(md_content)

    def inspect_tables(self, file_path: Path) -> dict:
        """Inspect tables in a Word document and return structured data."""
        logger.info(f"\nInspecting document: {file_path.name}")
        
        try:
            doc = Document(file_path)
        except Exception as e:
            logger.error(f"Error opening document {file_path}: {str(e)}")
            return {}

        tables_data = {}
        
        # Loop through all tables
        for table_index, table in enumerate(doc.tables):
            table_data = {
                'dimensions': {
                    'rows': len(table.rows),
                    'cols': len(table.columns)
                },
                'cells': {}
            }
            
            # Track processed cells to handle merged cells
            processed_cells = set()
            
            # Analyze each cell
            for row_index, row in enumerate(table.rows):
                for col_index, cell in enumerate(row.cells):
                    # Skip if this cell was already processed (part of a merged cell)
                    cell_id = (row_index, col_index)
                    if cell_id in processed_cells:
                        continue
                        
                    content = cell.text.strip()
                    content = content if content else "EMPTY"
                    coords = f"table: {table_index}, row: {row_index}, col: {col_index}"
                    
                    # Store cell info with row,col as key
                    cell_key = f"{row_index},{col_index}"
                    table_data['cells'][cell_key] = {
                        "content": content,
                        "coords": coords
                    }
                    
                    # Mark this cell as processed
                    processed_cells.add(cell_id)
            
            tables_data[table_index] = table_data

        return tables_data

def main():
    """Main function to run table inspection on Word documents."""
    inspector = TableInspector()
    all_documents_data = {}
    
    # Process each Word document
    docx_files = sorted(TEMPLATES_DIR.glob("*.docx"))
    if not docx_files:
        logger.warning(f"No Word documents found in templates directory: {TEMPLATES_DIR}")
        return
    
    logger.info(f"Found {len(docx_files)} Word documents")
    
    for file_path in docx_files:
        # Inspect document and store its data
        doc_data = inspector.inspect_tables(file_path)
        if doc_data:
            all_documents_data[file_path.name] = doc_data
    
    # Generate and save markdown
    if all_documents_data:
        markdown_content = inspector.generate_markdown(all_documents_data)
        logger.info(f"Attempting to write to: {OUTPUT_FILE}")
        try:
            # Ensure the directory exists
            OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
            # Write the file
            OUTPUT_FILE.write_text(markdown_content, encoding='utf-8')
            logger.info(f"Successfully wrote table analysis to: {OUTPUT_FILE}")
        except Exception as e:
            logger.error(f"Error writing output file: {e}")
    else:
        logger.warning("No table data found to write")

if __name__ == "__main__":
    main()