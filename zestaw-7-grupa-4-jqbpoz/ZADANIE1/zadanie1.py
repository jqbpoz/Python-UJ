import tkinter as tk
from tkinter import Label, StringVar, Frame
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

window = tk.Tk()
# tytuł, rozmiar, blokada wielkości

# utwórz StringVar()
date_time_var = StringVar()

def update_date_time():
    current_time = datetime.now()
    dt = current_time.strftime('%A, %d %B %Y\n%H:%M:%S')
    date_time_var.set(dt)
    date_time_label.after(1000, update_date_time)

date_time_frame = Frame(window, bg="#ffffff", bd=2, relief="groove")
date_time_frame.pack(pady=1, padx=0, fill="x")

# widget Label ustawiony na StringVar zrobiony na początku, rozmiar, czcionki, tło - wg uznania
date_time_label = Label(
    date_time_frame,
    textvariable=date_time_var,
    font=("Arial", 16, "bold"),
    bg="#ffffff",
    fg="#333333",
    padx=10,
    pady=10
)
date_time_label.pack()

current_time = datetime.now()
day = current_time.strftime('%d')
month = current_time.strftime('%m')
year = current_time.strftime('%Y')

calendar_frame = Frame(window, bg="#e6e9ed", bd=2, relief="groove")
calendar_frame.pack()

# utwórz cal = Calendar(...)
cal = Calendar(
    calendar_frame,
    selectmode='day',
    year=int(year),
    month=int(month),
    day=int(day),
    font=("Arial", 16),
    background="#ffffff",
    foreground="#333333",
    selectbackground="#4CAF50",
    selectforeground="#ffffff"
)
cal.pack(padx=10, pady=10)


update_date_time()

window.mainloop()