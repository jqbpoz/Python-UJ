# Zadanie 4: Aproksymacja liczby π za pomocą metody Monte Carlo

Uwaga: należy doinstalować pip install tqdm

Zadaniem jest zaimplementowanie funkcji `symulacja`, która obliczy przybliżenie liczby π przy użyciu metody Monte Carlo. Program powinien wykorzystywać losowanie punktów w kole wpisanym w kwadrat oraz zliczanie tych, które znajdują się wewnątrz koła.

## Opis działania

1. **Losowanie punktów:**
   - Wykorzystaj funkcję `np.random.uniform(-1, 1, 2)` z biblioteki NumPy do losowania dwóch współrzędnych \(x, y\) z przedziału \([-1, 1]\). 
   - Punkt \((x, y)\) znajduje się w kole o promieniu 1, jeśli \(x^2 + y^2 < 1\).

2. **Zliczanie punktów w kole:**
   - W pętli dla \(N\) powtórzeń generuj punkty i sprawdzaj, czy znajdują się w kole.
   - Skorzystaj z funkcji `np.sum` do obliczenia \(x^2 + y^2\) i porównania wyniku z 1.

3. **Obliczenie π:**
   - Liczba punktów wewnątrz koła podzielona przez całkowitą liczbę losowań \(N\) daje stosunek pola koła do pola kwadratu. Ponieważ \( \pi \) to 4-krotność tego stosunku, wynik można obliczyć jako:
     \[
     \pi \approx 4 \cdot \frac{\text{liczba punktów w kole}}{N}
     \]

4. **Postęp obliczeń:**
   - W pętli `for` opakuj obiekt `range(N)` w `tqdm`, aby wyświetlać pasek postępu podczas działania programu.

## Implementacja

Uzupełnij funkcję `symulacja`, aby działała zgodnie z poniższym wzorem:

```python
import numpy as np
from tqdm import tqdm

def symulacja(N):
    """
    Parametry:
    - N (int): Liczba losowań.
    
    Zwraca:
    - float: Aproksymacja pi.
    """
    return ### tu twój kod, może być dosłownie w jednej linii


if __name__ == "__main__":
    N = 1000000
    print(symulacja(N))
