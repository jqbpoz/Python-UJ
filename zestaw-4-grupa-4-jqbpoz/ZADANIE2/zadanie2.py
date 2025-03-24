from abc import ABC, abstractmethod

class Pojazd(ABC):
    def __init__(self, model: str, rok: int):
        self._model = model
        self._rok = rok
        self._predkosc = 0

    # Dokoncz definicje, rowniez setter i deleter
    @property
    def predkosc(self) -> float:
        return self._predkosc
    @predkosc.setter
    def predkosc(self, predkosc: float):
        if(predkosc < 0):
            raise ValueError("Prędkość nie może być ujemna!")
        self._predkosc = predkosc

    @predkosc.deleter
    def predkosc(self):
        self._predkosc = 0

class Samochod(Pojazd):
# w __init__ dodaj skladowa liczba_drzwi
    def __init__(self, model: str, rok: int, liczba_drzwi: int):
        super().__init__(model, rok)
        self._liczba_drzwi = liczba_drzwi

    @property
    def liczba_drzwi(self) -> int:
        return self._liczba_drzwi


class Autobus(Pojazd):
# w __init__ dodaj skladowa liczba_miejsc
    def __init__(self, model:str , rok:int,liczba_miejsc:int):
        super().__init__(model,rok)
        self._liczba_miejsc = liczba_miejsc
    @property
    def liczba_miejsc(self) -> int:
        return self._liczba_miejsc

class FabrykaPojazdow(ABC):

    def __init__(self, nazwa: str):
        self._nazwa = nazwa
        self._liczba_wyprodukowanych = 0

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @abstractmethod
    def stworz_pojazd(self, model: str, rok: int):
        pass

    @classmethod
    def utworz_fabryke(cls,typ: str,fabryka: str):
        if typ == 'samochod' and fabryka.__contains__("Fabryka Samochodów"):
            return FabrykaSamochodow(fabryka)
        if typ == 'autobus' and fabryka.__contains__("Fabryka Autobusów"):
            return FabrykaAutobusow(fabryka)
        else:
            raise ValueError("Nieprawidłowa nazwa fabryki")

    def spawdz_rok(self,rok:int):
        return 1900 < rok < 2025

    def ile_wyprodukowano(self) -> int:
        return self._liczba_wyprodukowanych



class FabrykaSamochodow(FabrykaPojazdow):

    def stworz_pojazd(self, model: str, rok: int, liczba_drzwi: int = 4) -> Samochod:

        if not self.spawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")

        pojazd = Samochod(model,rok,liczba_drzwi)
        self._liczba_wyprodukowanych += 1
        return pojazd


class FabrykaAutobusow(FabrykaPojazdow):
    def stworz_pojazd(self, model: str, rok: int, liczba_miejsc: int = 50) -> Autobus:
        if not self.spawdz_rok(rok):
            raise ValueError("Nieprawidłowy rok produkcji!")

        pojazd = Autobus(model,rok,liczba_miejsc)
        self._liczba_wyprodukowanych += 1
        return pojazd



def main():
    # Utworz fabryki pojazdow (samochodow i autobusow)
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke('samochod', "Fabryka Samochodów Warszawa")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke('autobus', "Fabryka Autobusów Kraków")

    # Utworzone fabryki - demonstracja @property nazwa
    print(f"Nazwa fabryki: {fabryka_samochodow.nazwa}")  
    print(f"Nazwa fabryki: {fabryka_autobusow.nazwa}")  

    # Utworz pojazdy
    samochod = fabryka_samochodow.stworz_pojazd("Fiat", 2023, liczba_drzwi=5)
    autobus = fabryka_autobusow.stworz_pojazd("Solaris", 2023, liczba_miejsc=60)

    # Demonstracja dzialania gettera, settera i deletera
    samochod.predkosc = 50  # uzycie setter
    print(f"Prędkość samochodu: {samochod.predkosc}")  # uzycie getter
    del samochod.predkosc  # uzycie deleter
    print(f"Prędkość po reset: {samochod.predkosc}")

    # Pokazanie ile pojazdow wyprodukowano
    print(f"Wyprodukowano samochodów: {fabryka_samochodow.ile_wyprodukowano()}")
    print(f"Wyprodukowano autobusów: {fabryka_autobusow.ile_wyprodukowano()}")

if __name__ == "__main__":
    main()