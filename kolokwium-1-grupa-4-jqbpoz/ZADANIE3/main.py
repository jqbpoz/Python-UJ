
# def dedukcja_typu(value: str):
#     """Rozpoznaj typ danej wejściowej i rzutuj na odpowiedni typ."""
#     # Sprawdź, czy to jest liczba całkowita (bez + i -)
#     # Spróbuj przekonwertować na liczbę zmiennoprzecinkową
#     # Sprawdź, czy to jest wartość logiczna
#     # Domyślnie traktuj jako string
#     # twój kod tutaj
#
#
# def dekompozycja(text: str):

def dedukcja_typu(value: str):

    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value

def dekompozycja(text: str):
    if not text.strip():
        return []
    return [dedukcja_typu(value) for value in text.split()]



    
if __name__ == "__main__":
    # Pobierz dane wejściowe
    tekst = input("Podaj ciąg tekstowy: ")
    
    # Rzutowanie i dekompozycja
    wynik = dekompozycja(tekst)
    
    # Wyświetl wynik
    print("Rozpoznane i skonwertowane elementy:", wynik)
