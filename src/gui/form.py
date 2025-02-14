# src/gui/form.py
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from src.fields_config import FIELD_NAMES

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self, height=600)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # Create the scrollable frame
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Add the frame to the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack the widgets
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class Section(ttk.LabelFrame):
    def __init__(self, parent, title, fields_dict=None):
        super().__init__(parent, text=title, padding="5")
        self.fields = {}
        # Configure grid column weights
        self.grid_columnconfigure(1, weight=1)
        # Set uniform minimum width for label column
        self.grid_columnconfigure(0, minsize=300)
        
        if fields_dict:
            self.create_fields(fields_dict)

    def create_fields(self, fields_dict):
        for i, (field_id, field_name) in enumerate(fields_dict.items()):
            # Create label with text wrapping
            label = ttk.Label(self, text=f"{field_name}:", wraplength=280, justify="left")
            label.grid(row=i, column=0, sticky=tk.W, pady=5, padx=(5, 10))
            
            # Create frame for entry to ensure consistent height
            entry_frame = ttk.Frame(self)
            entry_frame.grid(row=i, column=1, sticky=tk.EW, pady=5, padx=5)
            
            # Add entry widget with full width
            entry = ttk.Entry(entry_frame)
            entry.pack(fill=tk.X, expand=True)
            
            self.fields[field_id] = entry

class DraudimasGUI:
    def __init__(self, root, on_submit):
        self.root = root
        self.root.title("Draudimo Forma")
        self.on_submit = on_submit
        
        # Set window size and make it resizable
        self.root.geometry("800x800")
        self.root.minsize(600, 600)
        
        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrollable frame
        self.scroll_frame = ScrollableFrame(main_frame)
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        # Validate function for numeric input
        vcmd = (self.root.register(self.validate_numeric), '%P')
        
        # Create top section (uncategorized fields)
        top_frame = ttk.Frame(self.scroll_frame.scrollable_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Configure grid column weights
        top_frame.grid_columnconfigure(1, weight=1)
        # Set uniform minimum width for label column
        top_frame.grid_columnconfigure(0, minsize=300)

        # Case Name
        case_label = ttk.Label(top_frame, text="Bylos pavadinimas:", wraplength=280, justify="left")
        case_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=(5, 10))
        self.case_number = ttk.Entry(top_frame)
        self.case_number.grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)
        
        # Date
        date_label = ttk.Label(top_frame, text="Data:", wraplength=280, justify="left")
        date_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=(5, 10))
        self.date = ttk.Entry(top_frame)
        self.date.grid(row=1, column=1, sticky=tk.EW, pady=5, padx=5)

        # Place
        place_label = ttk.Label(top_frame, text="Vieta:", wraplength=280, justify="left")
        place_label.grid(row=2, column=0, sticky=tk.W, pady=5, padx=(5, 10))
        self.place = ttk.Entry(top_frame)
        self.place.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=5)
        
        # Crop List Count
        crop_label = ttk.Label(top_frame, text="Pasėlių sąrašo kopijų skaičius:", wraplength=280, justify="left")
        crop_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(5, 10))
        self.crop_list_count = ttk.Entry(top_frame, validate='key', validatecommand=vcmd)
        self.crop_list_count.grid(row=3, column=1, sticky=tk.EW, pady=5, padx=5)

        # Create sections with their respective fields
        self.sections = {}
        
        # Define fields for each section
        individual_fields = {
            "vardas": "Vardas",
            "pavarde": "Pavardė",
            "asmens_kodas": "Asmens kodas",
            "gimimo_data": "Gimimo data",
            "teisine_forma": "Teisinė forma (Ūkininkas / Ūkininkė)",
            "nario_nr": "Nario numeris"
        }
        
        legal_entity_fields = {
            "imone": "Įmonės pavadinimas",
            "imones_kodas": "Įmonės kodas",            
            "valdos_nr_juridinis": "Juridinio asmens valdos numeris",
            "imones_padaliniai": "Įmonės padaliniai (Gamybos vieta)"
        }
        
        farm_fields = {
            "valdos_nr": "Valdos numeris",
            "ukio_pavadinimas": "Ūkio pavadinimas",
            "ukio_registracijos_rajonas": "Ūkio registracijos rajonas",
            "zemes_plotas": "Bendras įmonės dirbamų žemių plotas, ha"
        }
        
        representative_fields = {
            "authorized_person_name": "Įgalioto asmens vardas, pavardė",
            "authorized_person_position": "Įgalioto asmens pareigos",
            "authorized_person_phone": "Įgalioto asmens tel. nr.",
            "authorized_person_email": "Įgalioto asmens el. paštas",

        }

        mediator_fields = {           
            "mediator_number": "Tarpininko numeris",
            "mediator_surname": "Tarpininko pavardė"
        }

        bank_fields = {
            "saskaitos_turetojas": "Sąskaitos turėtojas",
            "bankas": "Bankas",
            "saskaitos_nr": "Sąskaitos numeris",
            "swift_bic": "Banko kodas - SWIFT / BIC"
        }
        
        contact_fields = {
            "savivaldybe": "Savivaldybė",
            "seniunija": "Seniūnija",
            "miestas": "Miestas",
            "vietove": "Vietovė (Kaimo pavadinimas)",
            "gatves_pavadinimas_nr": "Gatvės pavadinimas ir namo numeris",
            "butas": "Buto numeris",
            "pasto_kodas": "Pašto kodas",
            "tel_nr": "Telefono numeris",
            "faksas": "Fakso numeris",
            "mobilaus_tel_nr": "Mobilaus tel. numeris",
            "el_pastas": "El. pašto adresas",
            "adresas_korespondencijai": "Adresas korespondencijai, jei nesutampa su nurodytu buveinės adresu"
        }

        # Create and pack sections
        sections_data = [
            ("Fiziniai asmenys", individual_fields),
            ("Juridiniai asmenys", legal_entity_fields),
            ("Ūkio duomenys", farm_fields),
            ("Atstovas", representative_fields),
            ("Tarpininkas", mediator_fields),
            ("Banko duomenys", bank_fields),
            ("Kontaktinė informacija", contact_fields)
        ]

        for title, fields in sections_data:
            section = Section(self.scroll_frame.scrollable_frame, title, fields)
            section.pack(fill=tk.X, pady=5, padx=5)
            self.sections[title] = section
        
        # Create bottom frame for submit button
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=10)
        
        # Submit Button
        submit_btn = ttk.Button(bottom_frame, text="Pateikti", command=self.submit)
        submit_btn.pack(pady=10)

    def validate_numeric(self, P):
        if P == "":
            return True
        try:
            int(P)
            return True
        except ValueError:
            return False

    def submit(self):
        """Handle form submission."""
        # Basic validation
        case_num = self.case_number.get().strip()
        if not case_num:
            messagebox.showerror("Klaida", "Būtina įvesti bylos numerį")
            return
            
        # Get crop list count (optional)
        crop_count = self.crop_list_count.get().strip()
        if crop_count and not crop_count.isdigit():
            messagebox.showerror("Klaida", "Pasėlių sąrašo kopijų skaičius turi būti skaičius")
            return
            
        # Collect form data
        form_data = {
            "case_number": case_num,
            "data": self.date.get().strip(),
            "vieta": self.place.get().strip(),
            "crop_list_count": crop_count
        }
        
        # Collect all field values from sections
        for section in self.sections.values():
            for field_id, entry in section.fields.items():
                form_data[field_id] = entry.get().strip()
        
        # Call the callback function with the form data
        success = self.on_submit(form_data)
        
        if success:
            messagebox.showinfo("Sėkmė", "Byla sėkmingai apdorota!")
            # Clear the form
            self.case_number.delete(0, tk.END)
            self.crop_list_count.delete(0, tk.END)
            for section in self.sections.values():
                for entry in section.fields.values():
                    entry.delete(0, tk.END)
        else:
            messagebox.showerror("Klaida", "Nepavyko apdoroti bylos")

    def run(self):
        """Start the GUI."""
        self.root.mainloop()