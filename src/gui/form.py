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

class DraudimasGUI:
    def __init__(self, root, on_submit):
        self.root = root
        self.root.title("Draudimas Form")
        self.on_submit = on_submit
        
        # Set window size and make it resizable
        self.root.geometry("600x800")
        self.root.minsize(500, 600)
        
        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrollable frame
        self.scroll_frame = ScrollableFrame(main_frame)
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        # Dictionary to store field entries
        self.field_entries = {}
        
        # Create fields
        self._create_fields()
        
        # Create bottom frame for submit button (outside scrollable area)
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=10)
        
        # Submit Button
        submit_btn = ttk.Button(bottom_frame, text="Submit", command=self.submit)
        submit_btn.pack(pady=10)
        
    def _create_fields(self):
        """Create all input fields."""
        # Case Number (always first)
        ttk.Label(self.scroll_frame.scrollable_frame, text="Case Number:").grid(
            row=0, column=0, sticky=tk.W, pady=5, padx=5
        )
        self.case_number = ttk.Entry(self.scroll_frame.scrollable_frame, width=40)
        self.case_number.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        
        # Create fields from FIELD_NAMES
        for i, (field_id, field_name) in enumerate(FIELD_NAMES.items(), start=1):
            ttk.Label(self.scroll_frame.scrollable_frame, text=f"{field_name}:").grid(
                row=i, column=0, sticky=tk.W, pady=5, padx=5
            )
            entry = ttk.Entry(self.scroll_frame.scrollable_frame, width=40)
            entry.grid(row=i, column=1, sticky=tk.W, pady=5, padx=5)
            self.field_entries[field_id] = entry

    def submit(self):
        """Handle form submission."""
        # Basic validation
        case_num = self.case_number.get().strip()
        if not case_num:
            messagebox.showerror("Error", "Case number must be filled")
            return
            
        # Collect form data
        form_data = {"case_number": case_num}
        
        # Collect all field values (allowing empty fields)
        for field_id, entry in self.field_entries.items():
            value = entry.get().strip()
            form_data[field_id] = value  # Store value even if empty
        
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
        """Start the GUI."""
        self.root.mainloop()