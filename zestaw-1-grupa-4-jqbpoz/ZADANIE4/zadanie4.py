import time

def pasek_postepu(dlugosc_paska):
    resolution = 50
    current = round(resolution * dlugosc_paska / 100);
    loaded_str = "|".ljust(current + 1, "=")
    left_str = "|".rjust(resolution - current + 1, '-')
    print(loaded_str + left_str + f" {dlugosc_paska}%")
    pass

if __name__ == "__main__":
    dlugosc_paska = 50  # długość paska %
    pasek_postepu(dlugosc_paska)
