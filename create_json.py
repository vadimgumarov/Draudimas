import json

mapping = {
    "fields": [
        {
            "name": "asmens_imones_kodas",
            "display_name": "Asmens/Imones kodas",
            "locations": {
                "Forma_1.pdf": [[1, 166, 182]],
                "Forma_2.pdf": [[0, 545, 98]],
                "Forma_3.pdf": [[0, 545, 98]],
                "Forma_4.pdf": [[0, 545, 98]],
                "Europos_paramos_KPP.pdf": [[1, 210, 389]],
                "NAC_2025.pdf": [[0, 322, 328]]
            }
        },
        {
            "name": "pavarde_imone",
            "display_name": "Pavarde / Imone",
            "locations": {
                "Forma_1.pdf": [[1, 39, 207]],
                "Forma_2.pdf": [[0, 32, 100]],
                "Forma_3.pdf": [[0, 32, 100]],
                "Forma_4.pdf": [[0, 32, 100]],
                "Europos_paramos_KPP.pdf": [[4, 465, 445]],
                "NAC_2025.pdf": [[0, 420, 347], [7, 420, 715]]
            }
        },
        {
            "name": "vardas",
            "display_name": "Vardas",
            "locations": {
                "Forma_1.pdf": [[1, 39, 34]],
                "Forma_2.pdf": [[0, 158, 100]],
                "Forma_3.pdf": [[0, 158, 100]],
                "Forma_4.pdf": [[0, 158, 100]],
                "Europos_paramos_KPP.pdf": [[4, 465, 425]],
                "NAC_2025.pdf": [[0, 320, 347], [7, 420, 695]]
            }
        },
        {
            "name": "savilvaldybe",
            "display_name": "Savivaldybe",
            "locations": {
                "Forma_1.pdf": [[1, 39, 289]],
                "Forma_2.pdf": [[0, 435, 145]],
                "Forma_3.pdf": [[0, 435, 145]],
                "Forma_4.pdf": [[0, 435, 145]]
            }
        },
        {
            "name": "data",
            "display_name": "Pasirasimo Data",
            "locations": {
                "Forma_1.pdf": [[1, 39, 289]],
                "Forma_2.pdf": [[0, 435, 560]],
                "Forma_3.pdf": [[0, 435, 560]],
                "Forma_4.pdf": [[0, 435, 560]],
                "Europos_paramos_KPP.pdf": [[0, 300, 495]],
                "NAC_2025.pdf": [[7, 415, 750]]
            }
        },
        {
            "name": "vieta",
            "display_name": "Pasirasmo Vieta",
            "locations": {
                "Forma_1.pdf": [[1, 39, 289]],
                "Forma_2.pdf": [[0, 335, 560]],
                "Forma_3.pdf": [[0, 335, 560]],
                "Forma_4.pdf": [[0, 335, 560]],
                "Europos_paramos_KPP.pdf": [[0, 295, 520]]
            }
        }
    ]
}

with open('field_mappings.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=4)

print("field_mappings.json has been created successfully")
