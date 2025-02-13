# src/fields_config.py

# Common fields and their display names
FIELD_NAMES = {
    "data": "Data",
    "nario_nr": "Nario Nr.",
    "valdos_nr": "Valdos Nr.",
    "valdos_nr_juridinis": "Juridinio Asmens Valdos Nr.",
    "teisine_forma": "Teisinė Forma (Ūkininkas / Ūkininkė)",
    "ukio_pavadinimas": "Ūkio Pavadinimas",
    "ukio_registracijos_rajonas": "Ūkio Registracijos Rajonas",
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
    "swift_bic": "Banko kodas - SWIFT / BIC",
    "asmens_kodas": "Asmens Kodas",
    "imones_kodas": "Įmonės Kodas",
    "vardas": "Vardas",
    "pavarde": "Pavardė",
    "imone": "Įmonės Pavadinimas",
    "gimimo_data": "Gimimo Data",
    "vieta": "Vieta",
    "igalioto_asmens_vardas_pavarde": "Įgalioto asmens vardas, pavardė",
    "igalioto_asmens_pareigos": "Įgalioto asmens pareigos",
    "igalioto_asmens_tel_nr": "Įgalioto asmens tel. nr.",
    "igalioto_asmens_el_pastas": "Įgalioto asmens el. paštas"
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
        "pavarde": [
            {"page": 1, "x": 40, "y": 205},
            {"page": 2, "x": 40, "y": 50}
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
        "data": {"page": 1, "x": 40, "y": 576}
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
        "data": {"table": 2, "row": 0, "col": 0},
        "vieta": {"table": 2, "row": 2, "col": 0},
        "savivaldybe": {"table": 3, "row": 1, "col": 0},
        "seniunija": {"table": 3, "row": 2, "col": 0},
        "vietove": {"table": 3, "row": 3, "col": 0},
        "gatves_pavadinimas": {"table": 3, "row": 4, "col": 0},
        "namo_nr": {"table": 3, "row": 5, "col": 0},        
        "butas": {"table": 3, "row": 6, "col": 0},
        "pasto_kodas": {"table": 3, "row": 7, "col": 0},
        "tel_nr": {"table": 3, "row": 8, "col": 0},
        "faksas": {"table": 3, "row": 9, "col": 0},
        "el_pastas": {"table": 3, "row": 10, "col": 0},
        "bankas": {"table": 3, "row": 13, "col": 0},
        "swift_bic": {"table": 3, "row": 15, "col": 0},
        "saskaitos_nr": {"table": 3, "row": 17, "col": 0},
        "valdos_nr": {"table": 4, "row": 1, "col": 1},
        "asmens_kodas": {"table": 4, "row": 2, "col": 1},
        "valdos_nr_juridinis": {"table": 4, "row": 4, "col": 1}, 
        "imones_kodas": {"table": 4, "row": 5, "col": 1},
        "vardas": {"table": 10, "row": 0, "col": 4},   
        "pavarde": {"table": 10, "row": 0, "col": 4},
        "teesine_forma": {"table": 10, "row": 0, "col": 0},
        "igalioto_asmens_vardas_pavarde": [
            {"table": 5, "row": 4, "col": 2},
            {"table": 10, "row": 0, "col": 4}
        ],
        "igalioto_asmens_pareigos": [
            {"table": 5, "row": 6, "col": 2},
            {"table": 10, "row": 0, "col": 0}
        ],
        "igalioto_asmens_tel_nr": {"table": 5, "row": 8, "col": 2},
        "igalioto_asmens_el_pastas": {"table": 5, "row": 10, "col": 2}
    },

    "NAC paraiška 2025.docx": {
        "valdos_nr": {"table": 0, "row": 0, "col": 1},
        "teisine_forma": [
            {"table": 0, "row": 1, "col": 1},
            {"table": 8, "row": 0, "col": 0}
        ],
        "asmens_kodas": {"table": 0, "row": 2, "col": 1},
        "vardas": [
            {"table": 0, "row": 3, "col": 1},
            {"table": 8, "row": 0, "col": 4}
        ],    
        "pavarde": [
            {"table": 0, "row": 3, "col": 1},
            {"table": 8, "row": 0, "col": 4},
        ],
        "savivaldybe": {"table": 0, "row": 4, "col": 1},
        "seniunija": {"table": 0, "row": 4, "col": 1},
        "vietove": {"table": 0, "row": 4, "col": 1},
        "gatves_pavadinimas": {"table": 0, "row": 4, "col": 1},
        "namo_nr": {"table": 0, "row": 4, "col": 1},
        "butas": {"table": 0, "row": 4, "col": 1},
        "tel_nr": {"table": 0, "row": 5, "col": 1},
        "el_pastas": {"table": 0, "row": 6, "col": 1},
        "bankas": {"table": 0, "row": 7, "col": 1},
        "swift_bic": {"table": 0, "row": 8, "col": 1},
        "saskaitos_nr": {"table": 0, "row": 9, "col": 1},
        "data": {"table": 8, "row": 2, "col": 4}

    },
    "De minimis nauja paraiska 2025.docx": {
        "valdos_nr": {"table": 0, "row": 0, "col": 1},
        "teisine_forma": [
            {"table": 0, "row": 1, "col": 1},
            {"table": 8, "row": 0, "col": 0}
        ],
        "asmens_kodas": {"table": 0, "row": 2, "col": 1},
        "vardas": [
            {"table": 0, "row": 3, "col": 1},
            {"table": 8, "row": 0, "col": 4}
        ],    
        "pavarde": [
            {"table": 0, "row": 3, "col": 1},
            {"table": 8, "row": 0, "col": 4}
        ],
        "savivaldybe": {"table": 0, "row": 4, "col": 1},
        "seniunija": {"table": 0, "row": 4, "col": 1},
        "vietove": {"table": 0, "row": 4, "col": 1},
        "gatves_pavadinimas": {"table": 0, "row": 4, "col": 1},
        "namo_nr": {"table": 0, "row": 4, "col": 1},
        "butas": {"table": 0, "row": 4, "col": 1},
        "tel_nr": {"table": 0, "row": 5, "col": 1},
        "el_pastas": {"table": 0, "row": 6, "col": 1},
        "bankas": {"table": 0, "row": 7, "col": 1},
        "swift_bic": {"table": 0, "row": 8, "col": 1},
        "saskaitos_nr": {"table": 0, "row": 9, "col": 1},
        "data": {"table": 8, "row": 2, "col": 4}

    },
    "Sutikimas dėl dokumentų siuntimo el. laišku.docx": {
        "vieta": {"table": 0, "row": 0, "col": 1},
        "data": {"table": 0, "row": 0, "col": 1},
        "vardas": {"table": 0, "row": 1, "col": 1},   
        "pavarde": {"table": 0, "row": 1, "col": 1}
    },

    "Sutikimas RINKODAROS BDR 2024.docx": {
        "vardas": {"table": 2, "row": 0, "col": 1},   
        "pavarde": {"table": 2, "row": 0, "col": 1},
        "ukio_pavadinimas": {"table": 2, "row": 1, "col": 1},
        "dydis": {"table": 2, "row": 1, "col": 1},
        "ukio_registracijos_rajonas": {"table": 2, "row": 2, "col": 1},
        "el_pastas": {"table": 2, "row": 3, "col": 1},
        "tel_nr": {"table": 2, "row": 3, "col": 1}
    }
}
