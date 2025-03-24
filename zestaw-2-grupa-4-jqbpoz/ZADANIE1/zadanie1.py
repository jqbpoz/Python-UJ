all_paths = []
temp_paths = []
def create_path_recursion(current_iterable, step):
    global deep , max_deep, temp_paths

    if step == "start":
        all_paths.clear()
        temp_paths.clear()

    temp_paths.append(step)
    all_paths.append(temp_paths.copy())

    if isinstance(current_iterable,dict):
        for key , value in current_iterable.items():
            if isinstance(value,(list,dict,tuple)):
                create_path_recursion(current_iterable.get(key), key)
        temp_paths.pop()
        return
    if isinstance(current_iterable,(list,tuple)):
        for index, item in enumerate(current_iterable):
            if isinstance(item,(list,dict,tuple)):
                create_path_recursion(current_iterable[index], index)
        temp_paths.pop()
        return
    temp_paths.pop()

def dodaj_element(wejscie):

    create_path_recursion(wejscie,"start");
    all_paths_sorted = sorted(all_paths,key=len,reverse=True)
    print(f"all_paths_sorted{all_paths_sorted}")
    current_iterable = wejscie
    max_len = len(all_paths_sorted[0])

    added = False;
    for p in all_paths_sorted:
        current_len = len(p)
        if(max_len>current_len and added == True):
            return wejscie

        for i in range(1,len(p)):
            if isinstance(current_iterable,dict):
                current_iterable = current_iterable.get(p[i])
                continue
            current_iterable = current_iterable[p[i]]

        to_adds = [element for element in current_iterable if isinstance(element, int)]
        to_add = max(to_adds) if len(to_adds) != 0 else 0

        if(isinstance(current_iterable,tuple)):
            current_iterable = wejscie
            continue
        if(isinstance(current_iterable,list)):
            added = True
            current_iterable.append(to_add+1)
            max_len = current_len

        current_iterable = wejscie
    return wejscie


if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)

