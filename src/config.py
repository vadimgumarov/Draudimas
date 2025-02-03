# src/config.py
import os
import sys
import platform
from pathlib import Path

def get_executable_dir():
    """Get the directory where the executable is located.
    Works in both development and standalone modes, on both Windows and macOS.
    """
    if getattr(sys, 'frozen', False):
        # Running as compiled (standalone) executable
        if platform.system() == 'Windows':
            return Path(os.path.dirname(sys.executable))
        else:  # macOS
            return Path(os.path.dirname(sys.executable))
    else:
        # Running in development mode
        return Path(os.path.dirname(os.path.dirname(__file__)))

def init_directories():
    """Initialize directories based on platform and mode (dev/standalone)."""
    base_dir = get_executable_dir()
    
    # Print debug info
    print(f"Debug: Operating System: {platform.system()}")
    print(f"Debug: Executable Directory: {base_dir}")
    print(f"Debug: Running in {'standalone' if getattr(sys, 'frozen', False) else 'development'} mode")
    
    return {
        'BASE_DIR': base_dir,
        'TEMPLATES_DIR': base_dir / 'templates',
        'CASES_DIR': base_dir / 'cases'
    }

# Initialize all directory paths
dirs = init_directories()

# Export directory paths
BASE_DIR = dirs['BASE_DIR']
TEMPLATES_DIR = dirs['TEMPLATES_DIR']
CASES_DIR = dirs['CASES_DIR']

# Create necessary directories if they don't exist
def ensure_directories():
    """Ensure all required directories exist."""
    try:
        TEMPLATES_DIR.mkdir(exist_ok=True)
        CASES_DIR.mkdir(exist_ok=True)
        print("Debug: Directories initialized successfully")
    except Exception as e:
        print(f"Error creating directories: {str(e)}")

# Create directories when module is imported
ensure_directories()