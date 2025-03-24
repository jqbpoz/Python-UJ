# Zadanie 3: Rozpoznawanie typów wejściowych

## Treść zadania
Napisz program, który:
1. Odbiera od użytkownika jeden ciąg tekstowy składający się z różnych wartości oddzielonych spacją.
2. Rozdziela tekst na poszczególne wartości.
3. Automatycznie rozpoznaje typ każdej wartości (`int`, `float`, `bool`, `str`) i konwertuje je na odpowiedni typ.
4. Zwraca listę zawierającą rozpoznane i skonwertowane wartości.
5. Uwaga: zakładamy, że wśród danych nie ma wartości None ani znaków + lub - przed liczbą.

### Przykład
**Dane wejściowe:**
abc 1.23 123 True

**Oczekiwany wynik:**
['abc', 1.23, 123, True]
