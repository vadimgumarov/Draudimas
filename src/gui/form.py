# src/gui/form.py
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

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
        self.case_number = ttk.Entry(main_frame, width=30)
        self.case_number.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Person Code
        ttk.Label(main_frame, text="Person Code:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.person_code = ttk.Entry(main_frame, width=30)
        self.person_code.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Submit Button
        submit_btn = ttk.Button(main_frame, text="Submit", command=self.submit)
        submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

    def submit(self):
        # Basic validation
        case_num = self.case_number.get().strip()
        person_code = self.person_code.get().strip()
        
        if not case_num or not person_code:
            messagebox.showerror("Error", "All fields must be filled")
            return
            
        # Collect form data
        form_data = {
            "case_number": case_num,
            "person_code": person_code
        }
        
        # Call the callback function with the form data
        success = self.on_submit(form_data)
        
        if success:
            messagebox.showinfo("Success", "Case processed successfully!")
            # Clear the form
            self.case_number.delete(0, tk.END)
            self.person_code.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to process case")

    def run(self):
        self.root.mainloop()