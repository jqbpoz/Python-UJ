import fitz  # pip install pymupdf
import tkinter as tk
from tkinter import filedialog, Menu

okno = tk.Tk()
okno.title("PDF Viewer")
okno.geometry("800x600")

# Create Text widget with some margin
text = tk.Text(okno, wrap='word', padx=10, pady=10)
text.pack(expand=1, fill='both')

# Function to clear the content of Text
def clear_text():
    text.delete(1.0, tk.END)

# Function to open a PDF file
def open_pdf():
    file = filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    if file:
        pdf_file = fitz.open(file)
        text.delete(1.0, tk.END)
        for page in pdf_file:
            content = page.get_text()
            text.insert(tk.END, content)

# Function to quit the application
def quit_app():
    okno.quit()

# Create Menu widget and its structure
menu_bar = Menu(okno)
okno.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_pdf)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

okno.mainloop()