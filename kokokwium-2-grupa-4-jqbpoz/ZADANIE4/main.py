import numpy as np
import pandas as pd

def create_and_filter_data():
    """
    1) Wygeneruj tablicę numpy z losowymi liczbami całkowitymi.
    2) Umieść je w DataFrame (np. kolumny ['A', 'B']).
    3) Odfiltruj wiersze, w których kolumna 'A' spełnia pewien warunek (np. > 50).
    4) Zwróć przefiltrowany DataFrame.
    """
    # ustaw ziarno losowości np. np.random.seed(123)
    np.random.seed(312)
    # np.random.randint(...) - stwórz losową tablicę (rozmiar i zakres do wyboru)
    # arr = ...
    arr = np.random.randint(1, 100, size=(40, 2))

    # df = 
    df = pd.DataFrame(arr, columns=['A', 'B'])

    # filtered_df = ...  
    filtered_df = df[df['A'] > 50]
    # return ...
    return filtered_df

if __name__ == '__main__':
    # Przykładowe wywołanie
    result_df = create_and_filter_data()
    print("Otrzymany DataFrame (A > 50):")
    print(result_df)
