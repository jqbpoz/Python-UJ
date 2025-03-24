from ZADANIE2.main import Animal, LandAnimal, WaterAnimal, Amphibian

def test_land_animal_sound():
    """Test sprawdza, czy LandAnimal zwraca poprawny dźwięk."""
    la = LandAnimal()
    assert la.make_sound() == "LandAnimal sound", "LandAnimal powinien zwracać 'LandAnimal sound'."


def test_water_animal_sound():
    """Test sprawdza, czy WaterAnimal zwraca poprawny dźwięk."""
    wa = WaterAnimal()
    assert wa.make_sound() == "WaterAnimal sound", "WaterAnimal powinien zwracać 'WaterAnimal sound'."


def test_amphibian_sound():
    """
    Test sprawdza, czy Amphibian zwraca połączony dźwięk LandAnimal i WaterAnimal.
    Zakładamy: "LandAnimal sound & WaterAnimal sound".
    """
    frog = Amphibian()
    expected_sound = "LandAnimal sound & WaterAnimal sound"
    assert frog.make_sound() == expected_sound, f"Oczekiwano '{expected_sound}'."


def test_animal_cannot_be_instantiated():
    """
    Test sprawdza, czy klasa abstrakcyjna Animal nie może być instancjonowana.
    Powinien zostać rzucony TypeError (ponieważ Animal ma metody abstrakcyjne).
    """
    with pytest.raises(TypeError):
        Animal()


def test_mro_amphibian():
    """
    Test sprawdza kolejność dziedziczenia (MRO) dla klasy Amphibian.
    MRO: Amphibian -> LandAnimal -> WaterAnimal -> Animal -> ABC -> object
    """
    mro = Amphibian.mro()
    # Sprawdzamy, czy kolejność jest taka, jak oczekujemy
    assert mro[0] == Amphibian
    assert mro[1] == LandAnimal
    assert mro[2] == WaterAnimal
    assert Animal in mro
    # (Nie musimy sprawdzać każdej pozycji, wystarczy zarys; lub ewentualnie dopasować do potrzeb.)
