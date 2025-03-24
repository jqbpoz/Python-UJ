import sys
from collections import defaultdict


# Funkcja do rozkładania liczby na czynniki pierwsze i formatowania wyniku
def rozklad_na_czynniki(n):

    def prime_factors(number):
        i = 2
        factors = defaultdict(int)
        while i * i <= number:
            if number % i:
                i += 1
            else:
                number //= i
                factors[i] += 1
        if number > 1:
            factors[number] += 1
        return dict(factors)

    def convert_to_string(factors_dict: dict):
        factors = ""
        for key, value in factors_dict.items():
            if int(value) == 1:
                factors += f"{key}*"
                continue
            factors += f"{key}^{value}*"
        return factors[:-1]


    return convert_to_string(prime_factors(int(n)))


# Główna funkcja programu
if __name__ == "__main__":
    argv = sys.argv[1:]  # Pobieranie argumentów zewnętrznych (liczby)

    for arg in argv:
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")
