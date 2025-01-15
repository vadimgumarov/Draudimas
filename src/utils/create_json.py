import json

mapping = {
    "fields": [
        {
            "name": "asmens_imones_kodas",
            "display_name": "Asmens/Imones kodas",
            "locations": {
                "Dr. paraiška 2025.pdf": [[1, 166, 182]],
                "Pasėlių sąrašas 2025.pdf": [[0, 545, 98]],
                "Pasėlių sąrašas JAVAI 2025.pdf": [[0, 545, 98]],
                "Pasėlių sąrašas ANKŠTINIAI 2025.pdf": [[0, 545, 98]],
                "Europos paramos paraiška KPP.docx": [[1, 210, 389]],
                "NAC paraiška 2025.docx": [[0, 322, 328]]
            }
        },
        {
            "name": "pavarde_imone",
            "display_name": "Pavarde / Imone",
            "locations": {
                "Dr. paraiška 2025.pdf": [[1, 39, 207]],
                "Pasėlių sąrašas 2025.pdf": [[0, 32, 100]],
                "Pasėlių sąrašas JAVAI 2025.pdf": [[0, 32, 100]],
                "Pasėlių sąrašas ANKŠTINIAI 2025.pdf": [[0, 32, 100]],
                "Europos paramos paraiška KPP.docx": [[4, 465, 445]],
                "NAC paraiška 2025.docx": [[0, 420, 347], [7, 420, 715]]
            }
        },
        # ... rest of the fields remain the same structure but with updated filenames
    ]
}

# Ensure UTF-8 encoding when writing the file
with open('field_mappings.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=4)

print("field_mappings.json has been created successfully")
