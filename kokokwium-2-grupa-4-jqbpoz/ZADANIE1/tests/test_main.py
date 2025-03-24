from ZADANIE1.main import transform_texts


def test_transform_simple():
    """Test dla podstawowej listy napisów."""
    input_data = ["hello", "world"]
    expected = ["OLLEH", "DLROW"]
    assert transform_texts(input_data) == expected


def test_transform_empty_strings():
    """Test, gdy wśród napisów są puste ciągi i białe znaki."""
    input_data = ["", "  ", "test"]
    expected = ["TSET"]
    assert transform_texts(input_data) == expected


def test_transform_various_chars():
    """Test, gdy występują różne rodzaje znaków (litery, cyfry, wykrzyknik)."""
    input_data = ["a", "Ab!", "123"]
    expected = ["A", "!BA", "321"]
    assert transform_texts(input_data) == expected


def test_transform_empty_list():
    """Test dla pustej listy."""
    input_data = []
    expected = []
    assert transform_texts(input_data) == expected


def test_transform_polish_chars():
    """Test z wykorzystaniem polskich znaków."""
    input_data = ["źle", "gęś"]
    expected = ["ELŹ", "ŚĘG"]
    assert transform_texts(input_data) == expected


def test_transform_only_spaces():
    """Test dla listy z elementami zawierającymi tylko spacje/białe znaki."""
    input_data = ["   ", "  \t  "]
    expected = []
    assert transform_texts(input_data) == expected


def test_no_side_effects():
    """
    Sprawdzamy, czy oryginalna lista nie jest modyfikowana w miejscu.
    """
    original = ["hello", "  ", "world"]
    copy_for_test = original[:]  # kopiujemy na potrzeby testu
    _ = transform_texts(copy_for_test)
    assert copy_for_test == original, "Funkcja nie powinna modyfikować listy wejściowej!"
