import tkinter as tk

# Napisz funkcję create_app(), która:
# Tworzy główne okno Tkinter,
# Dodaje etykietę (label) z jakimś wstępnym tekstem (np. "Wpisz coś:"),
# Dodaje pole tekstowe (Entry), w którym użytkownik może coś wpisać,
# Dodaje przycisk (Button), po którego kliknięciu tekst z pola Entry zostanie wyświetlony w drugiej etykiecie (np. "Wpisałeś: <tekst>").


def create_app():
    """
    Tworzy i zwraca główne okno Tkinter z prostym interfejsem.
    1) Etykieta: "Wpisz coś:"
    2) Pole Entry
    3) Przycisk "Pokaż", który wyświetli wpisany tekst w innej etykiecie
    """
    # title - "Prosta aplikacja Tkinter"
    root = tk.Tk()
    root.title("Prosta aplikacja Tkinter")
    root.geometry("400x300")
    # label_instruct = umocuj przez pack
    label_instruct = tk.Label(root, text="Wpisz coś:")
    label_instruct.pack()
    # entry_text =
    entry_text = tk.Entry(root)
    entry_text.pack()
    # label_result = tk.Label(...
    label_result = tk.Label(root, text="Wpisałeś:")
    label_result.pack()

    # zdefiniuj funkcję show_text() pobierającą wpisany tekst i wyświetlającą w label_result
    # def show_text():
    #     ...
    #     label_result.config(...)

    def show_text():
        input_text = entry_text.get()
        label_result.config(text=f"Wpisałeś: {input_text}")

    # button_show = 
    # button_show.pack()
    button_show = tk.Button(root, text="Pokaż", command=show_text)
    button_show.pack()

    return root
    pass

if __name__ == '__main__':
    # TODO: app = create_app()
    # TODO: app.mainloop()
    app = create_app()
    app.mainloop()
    pass
