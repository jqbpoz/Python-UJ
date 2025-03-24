from ZADANIE2.main import filtruj_litery

def test_standard_input():
    """Test dla pełnego zakresu liter A-Z oraz a-z."""
    kody_ascii = list(range(65, 91)) + list(range(97, 123))  # Kody ASCII dla A-Z i a-z
    wynik = filtruj_litery(kody_ascii)
    assert wynik == ['O', 'Q', 'S', 'U', 'W', 'Y'], "Niepoprawny wynik dla standardowego wejścia"

def test_empty_input():
    """Test dla pustej listy."""
    kody_ascii = []
    wynik = filtruj_litery(kody_ascii)
    assert wynik == [], "Niepoprawny wynik dla pustej listy"

def test_only_lowercase():
    """Test dla małych liter (a-z)."""
    kody_ascii = list(range(97, 123))  # Kody ASCII dla a-z
    wynik = filtruj_litery(kody_ascii)
    assert wynik == [], "Niepoprawny wynik dla małych liter"

def test_mixed_input():
    """Test dla mieszanych kodów ASCII, w tym niewielkich liter."""
    kody_ascii = [65, 78, 109, 90, 120]  # 'A', 'N', 'm', 'Z', 'x'
    wynik = filtruj_litery(kody_ascii)
    assert wynik == [], "Niepoprawny wynik dla mieszanych kodów ASCII"

def test_only_uppercase():
    """Test dla wielkich liter (A-Z), ale tylko wybranych."""
    kody_ascii = [65, 78, 80, 77, 88]  # 'A', 'N', 'P', 'M', 'X'
    wynik = filtruj_litery(kody_ascii)
    assert wynik == ['P', 'X'], "Niepoprawny wynik dla wielkich liter"
