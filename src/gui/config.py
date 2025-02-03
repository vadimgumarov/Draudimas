# src/config.py
import os
import sys
from pathlib import Path

def get_base_path():
    """Get the base path for the application."""
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (standalone)
        return Path(sys._MEIPASS)
    # If run from Python interpreter
    return Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Base paths
BASE_DIR = get_base_path()
TEMPLATES_DIR = BASE_DIR / "templates"
CASES_DIR = BASE_DIR / "cases"