import pytest
from ZADANIE3.main import dekompozycja  

@pytest.mark.parametrize("input_text, expected", [
    ("abc 1.23 123 True", ['abc', 1.23, 123, True]),  # Test podstawowy
    ("hello 42 3.14 False", ['hello', 42, 3.14, False]),  # Test z innymi wartościami
    ("42 1 3.1415 true false", [42, 1, 3.1415, True, False]),  # Test mieszanych liczb i logiki
    ("", []),  # Test pustego ciągu
    ("text_with_underscores 100", ['text_with_underscores', 100])  # Test tekstu z podkreślnikiem
])
def test_typow(input_text, expected):
    assert dekompozycja(input_text) == expected
