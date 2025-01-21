# src/pdf/inspector/coordinates.py
import tkinter as tk
from tkinter import ttk
import fitz
from PIL import Image, ImageTk

class PDFCoordinateInspector:
    def __init__(self, pdf_path):
        self.window = tk.Tk()
        self.window.title("PDF Coordinate Inspector")
        
        # Load PDF
        self.pdf_document = fitz.open(pdf_path)
        self.current_page = 0
        self.zoom = 2  # Zoom factor for better visibility
        
        # Create main frame
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas for PDF display
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create info label for coordinates
        self.info_label = ttk.Label(self.window, text="Click anywhere to get coordinates")
        self.info_label.pack(pady=5)
        
        # Create page navigation
        self.nav_frame = ttk.Frame(self.window)
        self.nav_frame.pack(pady=5)
        
        self.prev_btn = ttk.Button(self.nav_frame, text="Previous", command=self.prev_page)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.page_label = ttk.Label(self.nav_frame, text=f"Page {self.current_page + 1}/{len(self.pdf_document)}")
        self.page_label.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = ttk.Button(self.nav_frame, text="Next", command=self.next_page)
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.get_coordinates)
        
        # Display first page
        self.display_page()

    def display_page(self):
        # Get page
        page = self.pdf_document[self.current_page]
        
        # Convert PDF page to image
        pix = page.get_pixmap(matrix=fitz.Matrix(self.zoom, self.zoom))
        
        # Convert to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Convert to PhotoImage
        self.photo = ImageTk.PhotoImage(img)
        
        # Update canvas
        self.canvas.config(width=pix.width, height=pix.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        # Update page label
        self.page_label.config(text=f"Page {self.current_page + 1}/{len(self.pdf_document)}")
        
        # Update button states
        self.prev_btn.state(['!disabled'] if self.current_page > 0 else ['disabled'])
        self.next_btn.state(['!disabled'] if self.current_page < len(self.pdf_document) - 1 else ['disabled'])

    def get_coordinates(self, event):
        # Convert screen coordinates to PDF coordinates (considering zoom)
        pdf_x = event.x / self.zoom
        pdf_y = event.y / self.zoom
        
        # Get page dimensions
        page = self.pdf_document[self.current_page]
        
        # Update info label
        self.info_label.config(text=f"Coordinates - X: {pdf_x:.1f}, Y: {pdf_y:.1f}")

    def next_page(self):
        if self.current_page < len(self.pdf_document) - 1:
            self.current_page += 1
            self.display_page()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page()

    def run(self):
        self.window.mainloop()

    def __del__(self):
        if hasattr(self, 'pdf_document'):
            self.pdf_document.close()