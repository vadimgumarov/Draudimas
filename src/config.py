# src/config.py
from pathlib import Path

# Directory paths
PROJECT_DIR = Path("/Users/vadim/Desktop/Projects/Draudimas")
TEMPLATES_DIR = PROJECT_DIR / "templates"
TEMPLATES_LT_DIR = PROJECT_DIR / "templates_lt"
CASES_DIR = PROJECT_DIR / "cases"

# Field definitions
FIELDS = {
    "person_code": {
        "prompt": "Enter Person Code",
        "page": 0,
        "x": 100,
        "y": 100
    }
    # Add more fields as needed
}