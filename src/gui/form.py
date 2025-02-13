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
        if fields_dict:
            self.create_fields(fields_dict)

    def create_fields(self, fields_dict):
        for i, (field_id, field_name) in enumerate(fields_dict.items()):
            label = ttk.Label(self, text=f"{field_name}:")
            label.grid(row=i, column=0, sticky=tk.W, pady=2, padx=5)
            
            entry = ttk.Entry(self, width=40)
            entry.grid(row=i, column=1, sticky=tk.W, pady=2, padx=5)
            
            self.fields[field_id] = entry

class DraudimasGUI:
    def __init__(self, root, on_submit):
        self.root = root
        self.root.title("Draudimas Form")
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
        
        # Case Number
        ttk.Label(top_frame, text="Case Number:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.case_number = ttk.Entry(top_frame, width=40)
        self.case_number.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        
        # Crop List Count
        ttk.Label(top_frame, text="Crop List Count:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
        self.crop_list_count = ttk.Entry(top_frame, width=40, validate='key', validatecommand=vcmd)
        self.crop_list_count.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)

        # Create sections with their respective fields
        self.sections = {}
        
        # Define fields for each section
        fiziniai_fields = {
            "asmens_kodas": FIELD_NAMES["asmens_kodas"],
            "vardas": FIELD_NAMES["vardas"],
            "pavarde": FIELD_NAMES["pavarde"],
            "teisine_forma": FIELD_NAMES["teisine_forma"],
            "gimimo_data": FIELD_NAMES["gimimo_data"]
        }
        
        juridiniai_fields = {
            "imones_kodas": FIELD_NAMES["imones_kodas"],
            "imone": FIELD_NAMES["imone"],            
            "valdos_nr_juridinis": FIELD_NAMES["valdos_nr_juridinis"],
            "imones_padaliniai": FIELD_NAMES["imones_padaliniai"]
        }
        
        ukio_fields = {
            "valdos_nr": FIELD_NAMES["valdos_nr"],
            "nario_nr": FIELD_NAMES["nario_nr"],
            "ukio_pavadinimas": FIELD_NAMES["ukio_pavadinimas"],
            "ukio_registracijos_rajonas": FIELD_NAMES["ukio_registracijos_rajonas"],
            "zemes_plotas": FIELD_NAMES["zemes_plotas"]
        }
        
        atstovas_fields = {
            "igalioto_asmens_vardas_pavarde": FIELD_NAMES["igalioto_asmens_vardas_pavarde"],
            "igalioto_asmens_pareigos": FIELD_NAMES["igalioto_asmens_pareigos"],
            "igalioto_asmens_tel_nr": FIELD_NAMES["igalioto_asmens_tel_nr"],
            "igalioto_asmens_el_pastas": FIELD_NAMES["igalioto_asmens_el_pastas"],
            "tarpininko_nr": FIELD_NAMES["tarpininko_nr"],
            "tarpininko_pavarde": FIELD_NAMES["tarpininko_pavarde"]
        }
        
        banko_fields = {
            "saskaitos_turetojas": FIELD_NAMES["saskaitos_turetojas"],
            "bankas": FIELD_NAMES["bankas"],
            "saskaitos_nr": FIELD_NAMES["saskaitos_nr"],
            "swift_bic": FIELD_NAMES["swift_bic"]
        }
        
        kontaktai_fields = {
            "gatves_pavadinimas": FIELD_NAMES["gatves_pavadinimas"],
            "namo_nr": FIELD_NAMES["namo_nr"],
            "butas": FIELD_NAMES["butas"],
            "miestas": FIELD_NAMES["miestas"],
            "savivaldybe": FIELD_NAMES["savivaldybe"],
            "seniunija": FIELD_NAMES["seniunija"],
            "vietove": FIELD_NAMES["vietove"],
            "pasto_kodas": FIELD_NAMES["pasto_kodas"],
            "tel_nr": FIELD_NAMES["tel_nr"],
            "faksas": FIELD_NAMES["faksas"],
            "mobilaus_tel_nr": FIELD_NAMES["mobilaus_tel_nr"],
            "el_pastas": FIELD_NAMES["el_pastas"],
            "adresas_korespondencijai": FIELD_NAMES["adresas_korespondencijai"]
        }

        bendri_fields = {
            "data": FIELD_NAMES["data"],
            "vieta": FIELD_NAMES["vieta"],
        }

        # Create and pack sections
        sections_data = [
            ("Bendri Duomenys", bendri_fields),
            ("Fiziniai Asmenys", fiziniai_fields),
            ("Juridiniai Asmenys", juridiniai_fields),
            ("Ūkio Duomenys", ukio_fields),
            ("Atstovas", atstovas_fields),
            ("Banko Duomenys", banko_fields),
            ("Kontaktai", kontaktai_fields)
        ]

        for title, fields in sections_data:
            section = Section(self.scroll_frame.scrollable_frame, title, fields)
            section.pack(fill=tk.X, pady=5, padx=5)
            self.sections[title] = section
        
        # Create bottom frame for submit button (outside scrollable area)
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=10)
        
        # Submit Button
        submit_btn = ttk.Button(bottom_frame, text="Submit", command=self.submit)
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
            messagebox.showerror("Error", "Case number must be filled")
            return
            
        # Get crop list count (optional)
        crop_count = self.crop_list_count.get().strip()
        if crop_count and not crop_count.isdigit():
            messagebox.showerror("Error", "Crop list count must be a valid number")
            return
            
        # Collect form data
        form_data = {
            "case_number": case_num,
            "crop_list_count": crop_count
        }
        
        # Collect all field values from sections
        for section in self.sections.values():
            for field_id, entry in section.fields.items():
                form_data[field_id] = entry.get().strip()
        
        # Call the callback function with the form data
        success = self.on_submit(form_data)
        
        if success:
            messagebox.showinfo("Success", "Case processed successfully!")
            # Clear the form
            self.case_number.delete(0, tk.END)
            self.crop_list_count.delete(0, tk.END)
            for section in self.sections.values():
                for entry in section.fields.values():
                    entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to process case")

    def run(self):
        """Start the GUI."""
        self.root.mainloop()