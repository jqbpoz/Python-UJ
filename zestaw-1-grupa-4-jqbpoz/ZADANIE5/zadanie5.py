import os
import time

def wyczysc_ekran():
    # Czyszczenie ekranu w zależności od systemu operacyjnego
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac


def przesun_tekst_w_pionie(tekst, wysokosc_okna, opoznienie=0.1):
    while True:
        for i in range(wysokosc_okna):
            wyczysc_ekran()
            print("\n" * i + tekst)
            time.sleep(opoznienie)
        for i in range(wysokosc_okna, 0, -1):
            wyczysc_ekran()
            print("\n" * i + tekst)
            time.sleep(opoznienie)
        pass


if __name__ == "__main__":
    tekst = "  Hello world!  "  # tekst do przesuwania
    wysokosc_okna = 20  # Wysokość "okna" terminala
    przesun_tekst_w_pionie(tekst, wysokosc_okna)



### CIEKAWOSTKA ŹLE ZROZUMIEŁEM ZADANIE I WYSZŁO COŚ TAKIEGO:

#import time
# direction_x = -1
# direction_y = -1
#
#
# def change_direction_x(row: str, direction: int):
#     global direction_x
#     row_list = list(row)
#     if direction == 1:
#         row_list.insert(0, ".")
#         row_list.pop(-1)
#         if row_list[-1] == "!":
#             direction_x = -1
#         return "".join(row_list)
#
#     if direction == -1:
#         row_list.append(".")
#         row_list.pop(0)
#         if row_list[0] == "H":
#             direction_x = 1
#         return "".join(row_list)
#
#
# def change_direction_y(position: int, row: str, row_list: list, background: str, height: int):
#     global direction_y
#
#     row_list[position] = background
#     position += direction_y
#     if (position == 0):
#         direction_y = 1
#     if (position) == height - 1:
#         direction_y = -1
#     row_list[position] = row
#
#     return row_list, position
#
#
# def window(width: int, height: int):
#     global direction_y
#
#     row = " Hello Word ! ".center(width, ".")
#     background = "".center(width, ".")
#     rows_list = [background for x in range(0, height)]
#     current_y_position = height // 2
#
#     i = 10000000
#     while (i != 0):
#         time.sleep(0.08)
#         row = change_direction_x(row, direction_x)
#
#         rows_list, current_y_position = change_direction_y(current_y_position, row, rows_list, background, height)
#
#         rows_str = "".join(f"{r}\n" for r in rows_list)
#         print(f"\033[F" * (height + 1), end="")
#         print(f"{rows_str}", end="")
#         i -= 1
