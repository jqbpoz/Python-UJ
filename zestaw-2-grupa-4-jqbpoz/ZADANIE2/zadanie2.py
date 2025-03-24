import re
def statystyka_lancucha(tekst):
    # dostosu tak, aby instrukcja return była ok

    words = [word for word in re.split(r'\s+|[-.,;:!?"]', tekst) if word]

    count_numbers =0
    count_letters =0
    count_words = 0

    letters_dict = {}
    numbers_dict = {}

    def add_to_dict(my_dict, key):
        if key in my_dict:
            my_dict[key] += 1
        else:
            my_dict[key] = 1

    for word in words:
        if not word.isnumeric() and word.isalpha():
            count_words +=1

        for char in word:
            if char.isdigit():
                count_numbers +=1
                add_to_dict(numbers_dict,char)
            if char.isalpha():
                count_letters +=1
                add_to_dict(letters_dict,str(char).lower())

    sorted_letters = dict(sorted(letters_dict.items(), key=lambda item: item[1]))
    sorted_numbers = dict(sorted(numbers_dict.items(), key=lambda item: item[1]))

    statistics_dict = sorted_letters.copy()
    statistics_dict.update(sorted_numbers)

    print(words)
    return {
        "liczba_slow": count_words, # liczba
        "liczba_liter": count_letters, # liczba
        "liczba_cyfr": count_numbers, # liczba
        "statystyka": statistics_dict # słownik typu 'a': 1, '2': 3
    }


# Przykładowe użycie
if __name__ == "__main__":
    tekst_wejsciowy = '"Ala!" "Czy to kot?" - zapytal Piotr.'
    wynik = statystyka_lancucha(tekst_wejsciowy)

    # Wyświetlanie wyników
    print("Liczba słów:", wynik["liczba_slow"])
    print("Liczba liter:", wynik["liczba_liter"])
    print("Liczba cyfr:", wynik["liczba_cyfr"])
    print("Statystyka częstości występowania:")
    for znak, liczba in wynik["statystyka"].items():
        print(f"'{znak}': {liczba}", end=" ")

