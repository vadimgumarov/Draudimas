# test_word.py
from pathlib import Path
from src.word.word_reader import WordHandler
from src.config import TEMPLATES_LT_DIR

def main():
    """Test Word document handling."""
    # Try to open each .docx file in templates_lt
    for file_path in TEMPLATES_LT_DIR.glob('*.docx'):
        print(f"\nTesting document: {file_path.name}")
        WordHandler.read_docx(file_path)

if __name__ == "__main__":
    main()