# test_word.py
from pathlib import Path
from src.word.word_reader import WordHandler
from src.config import TEMPLATES_DIR

def main():
    """Test Word document handling."""
    # Search for Word documents in templates directory
    for file_path in TEMPLATES_DIR.glob('*.docx'):
        print(f"\nTesting document: {file_path.name}")
        WordHandler.read_docx(file_path)

if __name__ == "__main__":
    main()