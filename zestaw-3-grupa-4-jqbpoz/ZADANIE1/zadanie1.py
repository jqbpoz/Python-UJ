import json
import re

def process_tram_data(input_file):
    # Wczytaj dane z pliku JSON input_file
    with open(input_file,"r",encoding="utf-8") as read_file:
        data = json.load(read_file)


    # Przekształć dane na format słownikowy
    trams = dict()
    all_stops = set()
    line_stop_counts = list()

    for x in data['tramwaje']:
        key = int(x['linia'])
        values_list = []
        for y in x['przystanek']:
            values_list.append(y['nazwa'][:-3])

        line_stop_counts.append((int(key),len(values_list)))
        all_stops.update(set(values_list))
        trams[key] = tuple(values_list)

    line_stop_counts = sorted(line_stop_counts,key=lambda x:x[1],reverse=True)




    # trams - zawartość do zapisu w pliku 'tramwaje_out.json'
    # line_stop_counts - lista krotek (linia, liczba przystanków)
    # all_stops - set ze wszystkich przystanków
    return trams, line_stop_counts, len(all_stops)

if __name__ == '__main__':
    # Wywołanie funkcji
    trams, line_stop_counts, unique_stop_count = process_tram_data('tramwaje.json')
    # Zapisz dane do nowego pliku JSON 'tramwaje_out.json'

    with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
        json.dump(trams, file, ensure_ascii=False)

    # Wypisz wyniki: linia - liczba przystanków (po tym posortowane od największego)
    print(line_stop_counts)
    # Wypisz wyniki: liczba wszystkich unikanych przystanków
    print(unique_stop_count)
