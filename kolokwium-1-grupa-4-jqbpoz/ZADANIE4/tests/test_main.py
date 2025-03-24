import numpy as np
from ZADANIE4.main import symulacja

def błąd_odchylenia(N):
    return 4 * (np.sqrt(2) / np.sqrt(N))

def test_symulacja_N_1000(capsys):
    N = 1000
    # with capsys.disabled():  # Wyłącza przechwytywanie stdout/stderr
    wynik = symulacja(N)  
    błąd = błąd_odchylenia(N)
    assert abs(wynik - np.pi) <= błąd, f"Wynik {wynik} poza zakresem błędu {błąd} dla N={N}"

def test_symulacja_N_1000000(capsys):
    N = 1000000
    # with capsys.disabled():  # Wyłącza przechwytywanie stdout/stderr
    wynik = symulacja(N)  
    błąd = błąd_odchylenia(N)
    assert abs(wynik - np.pi) <= błąd, f"Wynik {wynik} poza zakresem błędu {błąd} dla N={N}"
