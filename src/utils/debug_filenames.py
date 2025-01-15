import json
from pathlib import Path

def debug_filenames():
    # Print actual files in templates folder
    templates_folder = Path("/Users/206753750/Desktop/Lauris/templates")
    print("\nFiles in templates folder:")
    template_files = [f.name for f in templates_folder.iterdir() if f.is_file()]
    for file in template_files:
        print(f"'{file}'")

    # Print files in mappings
    with open('field_mappings.json', 'r', encoding='utf-8') as f:
        mappings = json.load(f)
        print("\nFiles in mappings:")
        for field in mappings['fields']:
            print(f"\nField: {field['name']}")
            for filename in field['locations'].keys():
                print(f"'{filename}'")

if __name__ == "__main__":
    debug_filenames()
