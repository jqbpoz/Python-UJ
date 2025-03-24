import pytest
import tkinter as tk
from ZADANIE5.main import create_app

@pytest.fixture
def app():
    """
    Fixture tworząca i zwracająca główne okno aplikacji.
    Po teście niszczymy to okno (root.destroy()),
    by nie blokować kolejnych testów.
    """
    root = create_app()
    yield root
    root.destroy()

def test_create_app_type(app):
    """Sprawdzamy, czy create_app zwraca obiekt klasy Tk."""
    assert isinstance(app, tk.Tk), "Funkcja create_app powinna zwracać instancję tk.Tk."

def test_widgets_present(app):
    """
    Sprawdzamy, czy w oknie są widżety: Label, Entry, Button i inna Label.
    """
    # Pobieramy wszystkie widżety (children)
    children = app.winfo_children()
    labels = [w for w in children if isinstance(w, tk.Label)]
    entries = [w for w in children if isinstance(w, tk.Entry)]
    buttons = [w for w in children if isinstance(w, tk.Button)]

    assert len(labels) >= 2, "Powinny być co najmniej 2 etykiety."
    assert len(entries) >= 1, "Powinno być co najmniej 1 pole Entry."
    assert len(buttons) >= 1, "Powinien być co najmniej 1 przycisk."

def test_button_action(app):
    """
    Symulujemy wpisanie tekstu do Entry i kliknięcie przycisku,
    sprawdzamy, czy Label zmieni swój tekst.
    """
    children = app.winfo_children()
    entry = next((w for w in children if isinstance(w, tk.Entry)), None)
    button = next((w for w in children if isinstance(w, tk.Button)), None)
    label_result = None

    # Zakładamy, że 'label_result' to ta etykieta, która wyświetli wpisany tekst.
    # Rozpoznajemy ją np. po domyślnym tekście: "Tu pojawi się Twój tekst"
    for w in children:
        if isinstance(w, tk.Label) and w.cget("text") == "Tu pojawi się Twój tekst":
            label_result = w
            break

    assert entry is not None, "Nie znaleziono pola Entry."
    assert button is not None, "Nie znaleziono przycisku."
    assert label_result is not None, "Nie znaleziono etykiety wynikowej."

    # Symulujemy wpisanie tekstu
    test_text = "Test123"
    entry.insert(0, test_text)

    # Symulujemy kliknięcie
    button.invoke()

    # Sprawdzamy, czy etykieta została zaktualizowana
    expected_text = f"Wpisałeś: {test_text}"
    assert label_result.cget("text") == expected_text, (
        f"Oczekiwano tekstu '{expected_text}' w etykiecie wynikowej."
    )
