def rysuj_miarke(dlugosc):
    measure = ["|...." for x in range(0,dlugosc)]
    measure.append("|")
    measure_label = []
    previous = 0
    for item in range(1,dlugosc+2):
        num_str = (str(item))
        spaces = list([" "]*(5-len(num_str)))
        measure_label.extend(list(str(previous)))
        if(item == dlugosc+1):
            break
        measure_label.extend(spaces)
        previous = item
    measure_str = "".join(measure)
    measure_label_str = "".join(measure_label)
    return f"{measure_str}\n{measure_label_str}"

def main():
    dlugosc_miarki = 123  # Możesz zmienić długość miarki
    miarka = rysuj_miarke(dlugosc_miarki)
    print(miarka)

if __name__ == "__main__":
    main()
