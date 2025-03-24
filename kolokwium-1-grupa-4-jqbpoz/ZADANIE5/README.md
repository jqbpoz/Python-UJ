# Zadanie 5: dekorator mierzący czas wykonania funkcji

Napisać dekorator, który zmierzy czas wykonania opakowanej funkcji. Dekorator powinien zwracać całkowity czas wykonania funkcji w sekundach jako wynik swojego działania.

## Szczegóły zadania

1. **Dekorator**:
   - Napisz dekorator o nazwie `pomiar_powtorzen`, który przyjmuje jako argument funkcję, mierzy czas jej wykonania i zwraca zmierzony czas w sekundach jako wynik działania.

2. **Funkcja opakowywana**:
   - Dekorator będzie używany do opakowania funkcji, która wykonuje różne operacje, np. drukowanie tekstu i czekanie.

3. **Użycie dekoratora**:
   - Dekorator musi być zgodny z modułem `decorator`, tj. oznaczony jako `@decorator`.

4. **Pomiar czasu**:
   - Zmierz czas pomiędzy początkiem a końcem wykonania opakowanej funkcji za pomocą modułu `time`.

5. **Zwracanie wyniku**:
   - Dekorator powinien zwracać wyłącznie czas wykonania (w sekundach) jako wartość zwróconą przez opakowaną funkcję.

## Przykładowe użycie

Twój dekorator zostanie użyty z poniższą funkcją `funkcja`:

```python
import time
from decorator import decorator

@pomiar_powtorzen
def funkcja(*args, delay=1):
    for arg in args:
        print(arg)
        time.sleep(delay)

if __name__ == "__main__":
    czas = funkcja("Hello", "World", "to", "jest", "test", delay=0.5)
    print(f"Czas wykonania funkcji '{funkcja.__name__}': {czas:.4f} sekundy")
