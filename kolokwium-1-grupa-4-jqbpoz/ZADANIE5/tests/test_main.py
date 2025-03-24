import time
from ZADANIE5.main import funkcja

def test_funkcja_single_argument(capsys):
    """
    Test funkcji z jednym argumentem.
    """
    czas = funkcja("Hello", delay=0.1)
    captured = capsys.readouterr()  # Przechwyć wyjście stdout
    assert captured.out.strip() == "Hello", "Funkcja powinna wydrukować tylko 'Hello'."
    assert 0.1 <= czas < 0.2, f"Nieprawidłowy czas wykonania: {czas:.4f} sekundy."

def test_funkcja_multiple_arguments(capsys):
    """
    Test funkcji z wieloma argumentami.
    """
    czas = funkcja("Hello", "World", delay=0.1)
    captured = capsys.readouterr()
    expected_output = "Hello\nWorld"
    assert captured.out.strip() == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{captured.out.strip()}'."
    assert 0.2 <= czas < 0.3, f"Nieprawidłowy czas wykonania: {czas:.4f} sekundy."

def test_funkcja_no_arguments():
    """
    Test funkcji bez żadnych argumentów.
    """
    czas = funkcja(delay=0.1)
    assert czas < 0.1, f"Funkcja bez argumentów powinna wykonać się szybko, otrzymano: {czas:.4f} sekundy."

def test_funkcja_delay(capsys):
    """
    Test funkcji z opóźnieniem.
    """
    czas = funkcja("Hello", "World", delay=0.5)
    captured = capsys.readouterr()
    elapsed_time = czas
    assert captured.out.strip() == "Hello\nWorld", "Niepoprawne wyjście funkcji."
    assert 0.9 <= elapsed_time <= 1.1, f"Oczekiwano czasu około 1 sekundy, otrzymano {elapsed_time:.4f} sekundy."

def test_funkcja_non_string_arguments(capsys):
    """
    Test funkcji z argumentami, które nie są stringami.
    """
    czas = funkcja(42, 3.14, True, delay=0.1)
    captured = capsys.readouterr()
    expected_output = "42\n3.14\nTrue"
    assert captured.out.strip() == expected_output, f"Oczekiwano: '{expected_output}', otrzymano: '{captured.out.strip()}'."
    assert 0.3 <= czas < 0.4, f"Nieprawidłowy czas wykonania: {czas:.4f} sekundy."
