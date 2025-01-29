# src/fields_config.py

# Common fields and their display names
FIELD_NAMES = {
    "asmens_kodas": "Asmens Kodas / Imones kodas",
    "pavarde_imone": "Pavarde / Imones Pavadinimas",
    "vardas": "Vardas",
    "gimimo_data": "Gimimo Data"
}

# Field coordinates for each template
TEMPLATE_COORDINATES = {
    "Dr_paraiska_2025.pdf": {
        "asmens_kodas": {"page": 1, "x": 167, "y": 183},
        "pavarde_imone": {"page": 1, "x": 40, "y": 205},
        "vardas": {"page": 1, "x": 40, "y": 232},
        "gimimo_data": {"page": 1, "x": 480, "y": 232}
    },
    "Paseliu_sarasas_2025.pdf": {
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98}
        # Add other coordinates as needed
    },
    "Paseliu_sarasas_JAVAI_2025.pdf": {
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98}
        # Add other coordinates as needed
    }
}