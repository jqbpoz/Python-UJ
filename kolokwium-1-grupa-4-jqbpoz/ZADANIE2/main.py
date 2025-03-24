def filtruj_litery(kody_ascii):
    """
    Zwraca ciąg wielkich liter alfabetu angielskiego spełniających warunki:
    - Pozycja w sekwencji (licząc od 1) jest nieparzysta, sekwencja zawiera litery wielkie i małe.
    - Litera jest większa niż 'M' (sprawdzane w kolejności zgodnie z ASCII).
    """

    result = []
    for idx, kod in enumerate(kody_ascii, start=1):
        if idx % 2 != 0 and 65 <= kod <= 90 and kod > ord('M'):
            result.append(chr(kod))
    return result

if __name__ == "__main__":
    # Przykładowe dane wejściowe
    kody_ascii = list(range(65, 91)) + list(range(97, 123))  # Kody ASCII dla A-Z i a-z
    wynik = filtruj_litery(kody_ascii)
    print(wynik)
