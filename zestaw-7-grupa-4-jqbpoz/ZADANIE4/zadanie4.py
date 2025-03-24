from tkinter import Label, StringVar, Button, Entry, filedialog, Canvas, Scrollbar
import tkinter as tk
from PIL import Image, ImageTk


class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("800x600")
        self.root.resizable(True, True)

        # Atrybuty
        self.image_fp = None  # Ścieżka do otwartego pliku obrazu
        self.image = None  # Oryginalny obraz
        self.photo_image = None  # Obraz do wyświetlania na Canvas

        # UI
        self.setup_ui()

    def setup_ui(self):
        """Ustawia interfejs użytkownika"""
        # Panel narzędziowy
        toolbar_frame = tk.Frame(self.root)
        toolbar_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Przyciski i pola tekstowe
        Button(toolbar_frame, text="Open", command=self.open_handler).pack(side=tk.LEFT, padx=5, pady=5)

        Label(toolbar_frame, text="Width:").pack(side=tk.LEFT, padx=5)
        self.width_entry_str = StringVar()
        self.width_entry = Entry(toolbar_frame, textvariable=self.width_entry_str, width=10)
        self.width_entry.pack(side=tk.LEFT, padx=5)
        self.width_entry.bind("<KeyRelease>", self.width_modified)

        Label(toolbar_frame, text="Height:").pack(side=tk.LEFT, padx=5)
        self.height_entry_str = StringVar()
        self.height_entry = Entry(toolbar_frame, textvariable=self.height_entry_str, width=10)
        self.height_entry.pack(side=tk.LEFT, padx=5)
        self.height_entry.bind("<KeyRelease>", self.height_modified)

        # Przyciski Resize i Save
        Button(toolbar_frame, text="Resize", command=self.resize_handler).pack(side=tk.LEFT, padx=5)
        Button(toolbar_frame, text="Save", command=self.save_handler).pack(side=tk.LEFT, padx=5)

        # Canvas do wyświetlania obrazu
        canvas_frame = tk.Frame(self.root)
        canvas_frame.grid(row=1, column=0, sticky="nsew")

        self.canvas = Canvas(canvas_frame, bg="gray")
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Paski przewijania do Canvas
        self.scroll_x = Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scroll_y = Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)

        # Połącz paski przewijania z Canvas
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        # Umieść paski przewijania w siatce (grid)
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        # Dynamiczne skalowanie elementów
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)

    def open_handler(self):
        """Obsługuje otwieranie pliku obrazu"""
        self.image_fp = filedialog.askopenfilename(
            initialdir=".", filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*"))
        )
        if self.image_fp:
            try:
                self.image = Image.open(self.image_fp)
                self.display_image(self.image)
                self.width_entry_str.set(str(self.image.width))
                self.height_entry_str.set(str(self.image.height))
            except Exception as e:
                print(f"Error opening image: {e}")

    def width_modified(self, event):
        """Automatyczne wyliczenie wysokości przy zmianie szerokości"""
        if self.image:
            try:
                w = int(self.width_entry.get())
                height_set_to = int(self.image.height * (w / self.image.width))
                self.height_entry_str.set(str(height_set_to))
            except ValueError:
                pass

    def height_modified(self, event):
        """Automatyczne wyliczenie szerokości przy zmianie wysokości"""
        if self.image:
            try:
                h = int(self.height_entry.get())
                width_set_to = int(self.image.width * (h / self.image.height))
                self.width_entry_str.set(str(width_set_to))
            except ValueError:
                pass

    def resize_handler(self):
        """Zmiana rozmiaru obrazu"""
        if self.image:
            try:
                new_width = int(self.width_entry.get())
                new_height = int(self.height_entry.get())
                resized_image = self.image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                self.display_image(resized_image)
            except ValueError:
                print("Invalid width or height")


    def save_handler(self):
        """Zapisanie zmienionego obrazu"""
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")))
            if file_path:
                try:
                    self.image.save(file_path)
                except Exception as e:
                    print(f"Error saving image: {e}")

    def display_image(self, image):
        """Wyświetla obraz na Canvasie"""
        self.canvas.delete("all")

        # Get the canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Scale the image if it is larger than the canvas
        if image.width > canvas_width or image.height > canvas_height:
            scale = min(canvas_width / image.width, canvas_height / image.height)
            image = image.resize((int(image.width * scale), int(image.height * scale)), Image.ANTIALIAS)

        self.photo_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)
        self.canvas.config(scrollregion=(0, 0, image.width, image.height))


# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()