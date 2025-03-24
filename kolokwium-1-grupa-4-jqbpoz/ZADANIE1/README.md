# Zadanie 1: Sortowanie i przekształcanie liter

## Treść zadania
Napisać program, który zaczynając od listy losowo wymieszanych kodów ASCII odpowiadających literom `a`-`z` (zakres kodów ASCII: 97-122), przekształci ją w ciąg znaków `ZYXWVUTSRQPONMLKJIHGFEDCBA` w jednej linii kodu.

### Szczegóły:
1. Użyj funkcji `random.sample(range(97, 123), 26)` do wygenerowania losowej permutacji liczb w zakresie kodów ASCII dla liter małych `a`-`z`.
2. Posortuj te litery w odwrotnej kolejności (`z-a`).
3. Zamień je na wielkie litery (`A-Z`).
4. Wszystkie kroki mają zostać zrealizowane w **jednej linii kodu**.

### Przykład
**Dane wejściowe:**
```python
random.sample(range(97, 123), 26)

