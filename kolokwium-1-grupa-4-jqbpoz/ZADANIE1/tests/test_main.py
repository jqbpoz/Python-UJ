import pytest
import random
from ZADANIE1.main import funkcja

def test_full_alphabet():
    """Test dla pełnego alfabetu a-z."""
    wejscie = list(range(97, 123))  # Kody ASCII dla 'a'-'z'
    expected_output = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    assert funkcja(wejscie) == expected_output

def test_partial_alphabet():
    """Test dla ograniczonego zestawu kodów ASCII."""
    wejscie = [113, 97, 115, 98, 120, 121, 122]  # Losowe litery
    expected_output = "ZYXSQBA"  # Wynik po sortowaniu tych liter
    assert funkcja(wejscie) == expected_output

def test_shuffled_alphabet():
    """Test dla losowej permutacji pełnego alfabetu."""
    wejscie = list(range(97, 123))  # Kody ASCII dla 'a'-'z'
    random.shuffle(wejscie)  # Losowa kolejność
    expected_output = "ZYXWVUTSRQPONMLKJIHGFEDCBA"  # Wynik zawsze powinien być taki sam
    assert funkcja(wejscie) == expected_output
