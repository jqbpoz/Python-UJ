from ZADANIE6.instrument import Gitara, Skrzypce
from ZADANIE6.muzyk import Muzyk

def test_gra_na_gitarze(capsys):
    """
    Test sprawdzający tekst drukowany przez Muzyk.gra() dla instrumentu Gitara.
    """
    gitara = Gitara("Fender Stratocaster")
    jan = Muzyk("Jan")

    jan.gra(gitara)  # Wywołanie metody gra
    captured = capsys.readouterr()  # Przechwycenie wyjścia
    expected_output = (
        "Jan zaczyna grać na Fender Stratocaster.\n"
        "Szarpię Fender Stratocaster jak profesjonalista!\n"
    )
    assert captured.out == expected_output, f"Otrzymano: {captured.out}"

def test_gra_na_skrzypcach(capsys):
    """
    Test sprawdzający tekst drukowany przez Muzyk.gra() dla instrumentu Skrzypce.
    """
    skrzypce = Skrzypce("Stradivarius")
    anna = Muzyk("Anna")

    anna.gra(skrzypce)  # Wywołanie metody gra
    captured = capsys.readouterr()  # Przechwycenie wyjścia
    expected_output = (
        "Anna zaczyna grać na Stradivarius.\n"
        "Gram piękną melodię na Stradivarius!\n"
    )
    assert captured.out == expected_output, f"Otrzymano: {captured.out}"
