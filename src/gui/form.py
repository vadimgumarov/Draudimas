# src/gui/form.py
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from src.fields_config import FIELD_NAMES

class DraudimasGUI:
    def __init__(self, root, on_submit):
        self.root = root
        self.root.title("Draudimas Form")
        self.on_submit = on_submit
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Case Number
        ttk.Label(main_frame, text="Case Number:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.case_number = ttk.Entry(main_frame, width=40)
        self.case_number.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Dictionary to store field entries
        self.field_entries = {}
        
        # Create fields
        for i, (field_id, field_name) in enumerate(FIELD_NAMES.items(), start=1):
            ttk.Label(main_frame, text=field_name+":").grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = ttk.Entry(main_frame, width=40)
            entry.grid(row=i, column=1, sticky=tk.W, pady=5)
            self.field_entries[field_id] = entry
        
        # Submit Button
        submit_btn = ttk.Button(main_frame, text="Submit", command=self.submit)
        submit_btn.grid(row=len(FIELD_NAMES)+1, column=0, columnspan=2, pady=20)

    def submit(self):
        # Basic validation
        case_num = self.case_number.get().strip()
        if not case_num:
            messagebox.showerror("Error", "Case number must be filled")
            return
            
        # Collect form data
        form_data = {"case_number": case_num}
        
        # Validate and collect all field values
        for field_id, entry in self.field_entries.items():
            value = entry.get().strip()
            if not value:
                field_name = FIELD_NAMES[field_id]
                messagebox.showerror("Error", f"{field_name} must be filled")
                return
            form_data[field_id] = value
        
        # Call the callback function with the form data
        success = self.on_submit(form_data)
        
        if success:
            messagebox.showinfo("Success", "Case processed successfully!")
            # Clear the form
            self.case_number.delete(0, tk.END)
            for entry in self.field_entries.values():
                entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to process case")

    def run(self):
        # Configure grid weight for responsive resizing
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.mainloop()