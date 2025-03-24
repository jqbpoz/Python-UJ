import yfinance as yf
import pandas as pd
import numpy as np

tickets = ['BTC-USD']
data = yf.download(tickers=tickets, start='2024-01-01')


def find_crossovers():
    """
    Pobiera dane BTC-USD od 2024-01-01, oblicza 50-dniową i 200-dniową średnią kroczącą,
    identyfikuje punkty przecięcia i zwraca listę dat tych przecięć.

    Returns:
        list: Lista dat przecięć w formacie 'YYYY-MM-DD'.
    """
    btc_data = yf.download('BTC-USD', start='2024-01-01')

    # Oblicz 50-dniową i 200-dniową średnią kroczącą
    btc_data['50-day MA'] = btc_data['Close'].rolling(window=50).mean()
    btc_data['200-day MA'] = btc_data['Close'].rolling(window=200).mean()

    btc_data['Difference'] = btc_data['50-day MA'] - btc_data['200-day MA']
    crossovers = btc_data[(btc_data['Difference'] > 0) & (btc_data['Difference'].shift(1) <= 0)]
    return crossovers.index.strftime('%Y-%m-%d').tolist()
    




def calculate_total_btc_traded():
    """
    Pobiera dane BTC-USD z całego 2024 roku, oblicza ilość BTC handlowanych w każdym dniu
    oraz zwraca łączną ilość BTC dla dnia z najwyższym wolumenem.
    
    Returns:
        int: Łączna ilość BTC handlowanych w dniu z najwyższym wolumenem.
    """
    btc_data = yf.download('BTC-USD', start='2024-01-01', end='2024-12-31')
    max_volume_day = btc_data['Volume'].idxmax()
    total_btc_traded = btc_data.loc[max_volume_day, 'Volume']
    return int(total_btc_traded['BTC-USD'].sum())


if __name__ == '__main__':
    # Wywołanie funkcji i uzyskanie wyników
    crossover_dates = find_crossovers()
    total_traded = calculate_total_btc_traded()
    
    # Drukowanie wyników w żądanym formacie
    print(" ".join(crossover_dates))
    print(total_traded)
