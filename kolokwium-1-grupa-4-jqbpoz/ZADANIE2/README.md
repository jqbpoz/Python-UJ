# Zadanie 2: Filtracja liter ASCII

Napisać funkcję w Pythonie, która przefiltruje zestaw kodów ASCII liter (małych i wielkich) według określonych kryteriów.

## Specyfikacja funkcji

Funkcja powinna mieć następującą sygnaturę:
```python
def filtruj_litery(kody_ascii):
    """
    Filtruje zestaw kodów ASCII i zwraca listę wielkich liter alfabetu angielskiego,
    które spełniają poniższe kryteria:
    1. Litera musi znajdować się na pozycji nieparzystej w liście wejściowej (indeksy liczone od 1).
    2. Litera musi być większa niż 'M' (kod ASCII większy niż 77).
    
    Parametry:
    - kody_ascii (list[int]): Lista liczb całkowitych reprezentujących kody ASCII.

    Zwraca:
    - list[str]: Lista liter spełniających powyższe warunki, w kolejności występowania.
    """
