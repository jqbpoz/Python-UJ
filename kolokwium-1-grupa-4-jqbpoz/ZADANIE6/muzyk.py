class Muzyk:
    def __init__(self, imie):
        self.imie = imie

    def gra(self, instrument):
        print(f"{self.imie} zaczyna grać na {instrument}.")
        instrument.graj()