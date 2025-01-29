# src/fields_config.py

# Common fields and their display names
FIELD_NAMES = {
    "asmens_kodas": "Asmens Kodas / Imones kodas",
    "pavarde_imone": "Pavarde / Imones Pavadinimas",
    "vardas": "Vardas",
    "gimimo_data": "Gimimo Data"
}

# Coordinates for PDF templates
PDF_COORDINATES = {
    "Dr_paraiška_2025.pdf": {
        "asmens_kodas": {"page": 1, "x": 167, "y": 183},
        "pavarde_imone": {"page": 1, "x": 40, "y": 205},
        "vardas": {"page": 1, "x": 40, "y": 232},
        "gimimo_data": {"page": 1, "x": 480, "y": 232}
    },
    "Pasėlių_sąrašas_2025.pdf": {
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98}
    },
    "Pasėlių_sąrašas_JAVAI_2025.pdf": {
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98}
    },
    "Pasėlių_sąrašas_ANKŠTINIAI_2025.pdf": {
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98}
    }
}

# Coordinates for Word templates (table, row, column)
WORD_COORDINATES = {
    "Europos_paramos_paraiška_KPP.docx": {
        "asmens_kodas": {"table": 3, "row": 2, "col": 1}
    },
    "NAC paraiška 2025.docx": {
        "asmens_kodas": {"table": 0, "row": 2, "col": 1}
    }
}