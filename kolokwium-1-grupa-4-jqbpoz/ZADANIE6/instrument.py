class Gitara:
    def __init__(self, nazwa="Gitara"):
        self.nazwa = nazwa

    def graj(self):
        print(f"Szarpię {self.nazwa} jak profesjonalista!")

    def __str__(self):
        return self.nazwa


class Skrzypce:
    def __init__(self, nazwa="Skrzypce"):
        self.nazwa = nazwa

    def graj(self):
        print(f"Gram piękną melodię na {self.nazwa}!")

    def __str__(self):
        return self.nazwa
