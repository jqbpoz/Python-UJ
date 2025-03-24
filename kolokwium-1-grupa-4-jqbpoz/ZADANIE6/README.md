# Zadanie 6: Klasy Instrumenty i Muzyk

Napisać w plikach `instrument.py` i `muzyk.py`, klasy reprezentujące instrumenty muzyczne oraz klasę reprezentującą muzyka. Plik `main.py` (dostępny poniżej) korzysta z tych klas i demonstruje ich działanie. 
Celem jest zaimplementowanie brakujących klas tak, aby program działał poprawnie.

## Wymagania

1. **Plik `instrument.py`:**
   - Klasa `Gitara`:
     - Konstruktor przyjmuje argument `nazwa` (domyślnie `"Gitara"`).
     - Metoda `graj(self)` wypisuje komunikat w stylu: `"Szarpię [nazwa] jak profesjonalista!"`.
     - Metoda `__str__(self)` zwraca nazwę instrumentu.
   - Klasa `Skrzypce`:
     - Konstruktor przyjmuje argument `nazwa` (domyślnie `"Skrzypce"`).
     - Metoda `graj(self)` wypisuje komunikat w stylu: `"Gram piękną melodię na [nazwa]!"`.
     - Metoda `__str__(self)` zwraca nazwę instrumentu.

2. **Plik `muzyk.py`:**
   - Klasa `Muzyk`:
     - Konstruktor przyjmuje argument `imie`.
     - Metoda `gra(self, instrument)`:
       - Wypisuje komunikat: `"[imie] zaczyna grać na [instrument]."`.
       - Następnie wywołuje metodę `graj()` obiektu `instrument`.

3. **Plik `main.py`:**
   - Program korzysta z zaimplementowanych klas, tworzy obiekty `Gitara`, `Skrzypce` oraz `Muzyk` i wykonuje operacje zgodnie z podanym kodem.

## Kod `main.py`

```python
from instrument import Gitara, Skrzypce
from muzyk import Muzyk

if __name__ == "__main__":
    
    gitara = Gitara("Fender Stratocaster")
    skrzypce = Skrzypce("Stradivarius")

    jan = Muzyk("Jan")
    anna = Muzyk("Anna")

    jan.gra(gitara)   # Jan zaczyna grać na Fender Stratocaster.
                      # Szarpię Fender Stratocaster jak profesjonalista!

    anna.gra(skrzypce)  # Anna zaczyna grać na Stradivarius.
                        # Gram piękną melodię na Stradivarius!
