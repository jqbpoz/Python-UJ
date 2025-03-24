import numpy as np
import pandas as pd
from ZADANIE4.main import create_and_filter_data

def test_create_and_filter_data_dataframe_type():
    """
    Sprawdzamy, czy zwracany obiekt jest typu pandas.DataFrame.
    """
    df = create_and_filter_data()
    assert isinstance(df, pd.DataFrame), "Funkcja powinna zwracać DataFrame."

def test_create_and_filter_data_columns():
    """
    Sprawdzamy, czy DataFrame ma kolumny 'A' i 'B'.
    """
    df = create_and_filter_data()
    expected_columns = ['A', 'B']
    assert list(df.columns) == expected_columns, "DataFrame powinien mieć kolumny 'A' i 'B'."

def test_create_and_filter_data_condition():
    """
    Sprawdzamy, czy wszystkie wartości w kolumnie 'A' są > 50 (lub czy DataFrame jest pusty).
    """
    df = create_and_filter_data()
    if not df.empty:
        assert (df['A'] > 50).all(), "Wszystkie wartości w kolumnie 'A' powinny być > 50."
    else:
        # Jeżeli DataFrame jest pusty, też jest to dopuszczalne, bo mogło nie być wylosowanych wartości > 50
        pass

def test_fixed_seed_behavior():
    """
    Jeśli w funkcji ustawiłeś np.random.seed(42),
    sprawdzamy powtarzalność wyniku.
    """
    df1 = create_and_filter_data()
    df2 = create_and_filter_data()
    # Przy tym samym seed wyniki powinny być identyczne (ten sam zbiór wierszy).
    pd.testing.assert_frame_equal(df1, df2, check_exact=True)
