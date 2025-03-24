import random

def funkcja(wejscie):
    sorted_input = sorted(wejscie, reverse=True)
    for i in range(len(sorted_input)):
        sorted_input[i] = chr(sorted_input[i]).upper()
    return ''.join(sorted_input)
    """Przekształca listę kodów ASCII w ciąg znaków w odwrotnej kolejności (z -> a) i zamienia je na wielkie litery."""
    # twój kod


if __name__ == "__main__":
    # Generowanie losowej permutacji kodów ASCII dla liter a-z
    wejscie = random.sample(range(97, 123), 26)
    
    # Przetwarzanie wejścia przez funkcję
    wyjscie = funkcja(wejscie)
    
    # Wyświetlenie wyniku
    print(wyjscie)
