# src/config.py
import os
import sys
from pathlib import Path

def get_executable_dir():
    """Get the directory where the executable is located."""
    if getattr(sys, 'frozen', False):
        # We're running in a bundle (standalone executable)
        return Path(os.path.dirname(sys.executable))
    # We're running in a normal Python environment
    return Path(os.path.dirname(os.path.dirname(__file__)))

# Get executable directory
EXECUTABLE_DIR = get_executable_dir()

# Define all paths relative to executable directory
TEMPLATES_DIR = EXECUTABLE_DIR / "templates"
CASES_DIR = EXECUTABLE_DIR / "cases"

print(f"Debug: Executable directory: {EXECUTABLE_DIR}")
print(f"Debug: Templates directory: {TEMPLATES_DIR}")
print(f"Debug: Cases directory: {CASES_DIR}")