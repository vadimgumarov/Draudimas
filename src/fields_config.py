# src/fields_config.py

# Common fields and their display names
FIELD_NAMES = {
    "data": "Data",
    "nario_nr": "Nario Nr.",
    "valdos_nr": "Valdos Nr.",
    "tarpininko_nr": "Tarpininko Nr.",
    "tarpininko_pavarde": "Tarpininko Pavardė",
    "gatves_pavadinimas": "Gatvės Pavadinimas",
    "namo_nr": "Namo Nr.",
    "butas": "Buto Nr.",
    "miestas": "Miestas",
    "savivaldybe": "Savivaldybė",
    "seniunija": "Seniūnija",
    "vietove": "Vietovė (Kaimo Pavadinimas)",
    "pasto_kodas": "Pašto Kodas",   
    "imones_padaliniai": "Įmonės Padaliniai (Gamybos vieta)",
    "adresas_korespondencijai": "Adresas korespondencijai, jei nesutampa su nurodytu buveinės adresu",
    "tel_nr": "Telefono Nr.",
    "faksas": "Fakso Nr.",
    "mobilaus_tel_nr": "Mobilaus Tel. Nr.",
    "el_pastas": "El. pašto adresas",
    "zemes_plotas": "Bendras imonės dirbamų žemių plotas, ha",
    "saskaitos_turetojas": "Sąskaitos turėtojas",
    "bankas": "Bankas",
    "saskaitos_nr": "Sąskaita",
    "swift_bic": "SWIFT/BIC",
    "asmens_kodas": "Asmens Kodas / Įmonės kodas",
    "pavarde_imone": "Pavarde / Įmonės Pavadinimas",
    "vardas": "Vardas",
    "gimimo_data": "Gimimo Data",
    "augalu_grupe": "Augalų grupė",
    "vieta_data": "Vieta/Data"
}

# Coordinates for PDF templates
PDF_COORDINATES = {
    "Dr paraiška 2025.pdf": {
        "nario_nr": {"page": 1, "x": 40, "y": 157},
        "valdos_nr": {"page": 1, "x": 167, "y": 157},
        "tarpininko_nr": {"page": 1, "x": 300, "y": 157},
        "tarpininko_pavarde": {"page": 1, "x": 433, "y": 157},
        "asmens_kodas": [
            {"page": 1, "x": 167, "y": 183},
            {"page": 2, "x": 390, "y": 50}
        ],
        "pavarde_imone": [
            {"page": 1, "x": 40, "y": 205},
            {"page": 2, "x": 35, "y": 50}
        ],
        "vardas": {"page": 1, "x": 40, "y": 232},
        "gimimo_data": {"page": 1, "x": 480, "y": 232},
        "gatves_pavadinimas": {"page": 1, "x": 40, "y": 260},
        "namo_nr": {"page": 1, "x": 208, "y": 260},
        "savivaldybe": {"page": 1, "x": 40, "y": 288},
        "seniunija": {"page": 1, "x": 208, "y": 288},
        "vietove": {"page": 1, "x": 393, "y": 288},
        "pasto_kodas": {"page": 1, "x": 40, "y": 313},
        "imones_padaliniai": {"page": 1, "x": 110, "y": 313},
        "adresas_korespondencijai": {"page": 1, "x": 40, "y": 340},
        "tel_nr": {"page": 1, "x": 40, "y": 370},
        "faksas": {"page": 1, "x": 208, "y": 370},
        "mobilaus_tel_nr": {"page": 1, "x": 40, "y": 395},
        "el_pastas": {"page": 1, "x": 208, "y": 395},
        "zemes_plotas": {"page": 1, "x": 502, "y": 395},
        "saskaitos_turetojas": {"page": 1, "x": 40, "y": 420},
        "bankas": {"page": 1, "x": 208, "y": 420},
        "saskaitos_nr": {"page": 1, "x": 40, "y": 445},
        "swift_bic": {"page": 1, "x": 390, "y": 445},
        "vieta_data": {"page": 1, "x": 40, "y": 576}
    },
    "Pasėlių sąrašas 2025.pdf": {
        "data": {"page": 0, "x": 29, "y": 53},
        "augalu_grupe": {"page": 0, "x": 34, "y": 145},
        "savivaldybe": {"page": 0, "x": 438, "y": 145},
        "asmens_kodas": {"page": 0, "x": 545, "y": 98},
        "pavarde_imone": {"page": 0, "x": 35, "y": 98},
        "vieta_data": {"page": 0, "x": 335, "y": 560}
    }
}

# Coordinates for Word templates (table, row, column)
WORD_COORDINATES = {
    "Europos paramos paraiška KPP.docx": {  
        "savivaldybe": {"table": 2, "row": 1, "col": 0},
        "seniunija": {"table": 2, "row": 2, "col": 0},
        "vietove": {"table": 2, "row": 3, "col": 0},
        "gatves_pavadinimas": {"table": 2, "row": 4, "col": 0},
        "namo_nr": {"table": 2, "row": 5, "col": 0},        
        "butas": {"table": 2, "row": 6, "col": 0},
        "pasto_kodas": {"table": 2, "row": 7, "col": 0},
        "tel_nr": {"table": 2, "row": 8, "col": 0},
        "faksas": {"table": 2, "row": 9, "col": 0},
        "el_pastas": {"table": 2, "row": 10, "col": 0},
        "asmens_kodas": {"table": 3, "row": 2, "col": 1} 
    },
    "NAC paraiška 2025.docx": {
        "asmens_kodas": {"table": 0, "row": 2, "col": 1},
        "vardas": {"table": 0, "row": 3, "col": 1},
        "pavarde_imone": {"table": 0, "row": 3, "col": 1},
        "savivaldybe": {"table": 0, "row": 4, "col": 1},
        "seniunija": {"table": 0, "row": 4, "col": 1},
        "vietove": {"table": 0, "row": 4, "col": 1},
        "gatve_nr": {"table": 0, "row": 4, "col": 1},
        "butas": {"table": 0, "row": 4, "col": 1},
        "tel_nr": {"table": 0, "row": 5, "col": 1},
        "el_pastas": {"table": 0, "row": 6, "col": 1},
        "bankas": {"table": 0, "row": 7, "col": 1},
        "swift_bic": {"table": 0, "row": 8, "col": 1},
        "banko_saskaita": {"table": 0, "row": 9, "col": 1},

    }
}
