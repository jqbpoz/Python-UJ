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
