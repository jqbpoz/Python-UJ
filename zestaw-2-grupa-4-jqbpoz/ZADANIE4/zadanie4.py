def fun(n):
    print(list(bin(n)))
    bit_list = list(bin(n))
    gaps =[]
    current_gap = 0
    for bit in bit_list[2:]:
        if(int(bit) == 0):
            current_gap +=1
        else:
            gaps.append(current_gap)
            current_gap =0
    return max(gaps)



if __name__ == "__main__":
    N = 529 # przykladowa wartosc, oczekiwany wynik 4
    wynik = fun(N)
    print(f"Reprezentacja binarna {N}: {bin(N)}")
    print(f"fun({N}): {wynik}")

