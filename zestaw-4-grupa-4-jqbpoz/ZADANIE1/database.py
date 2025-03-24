import sqlite3
import pandas as pd

# def create_table(max_repeats, databasefile="flights.db"):
#     import sqlite3

def create_table(max_repeats, databasefile="flights.db"):
    connection = sqlite3.connect(databasefile)
    cursor = connection.cursor()
    if max_repeats > 0:
        cursor.execute("DROP TABLE IF EXISTS airport_atl")
        cursor.execute("""
            CREATE TABLE airport_atl (
                icao24 TEXT,
                callsign TEXT,
                origin_country TEXT,
                time_position REAL,
                last_contact REAL,
                long REAL,
                lat REAL,
                baro_altitude REAL,
                on_ground BOOLEAN,
                velocity REAL,
                true_track REAL,
                vertical_rate REAL,
                sensors TEXT,
                geo_altitude REAL,
                squawk TEXT,
                spi BOOLEAN,
                position_source INTEGER
            )
        """)

    # zamknij polaczenie z baza danych
    connection.commit()
    connection.close()

def save_to_db(flight_df, databasefile="flights.db"):
    # napisz kod zapisania do bazy danych SQLite
    connection = sqlite3.connect(databasefile)
    flight_df.to_sql('flights', connection, if_exists='append', index=False)
    connection.commit()
    connection.close()

def load_flight_data(databasefile="flights.db"):
    # napisz kod odczytania danych z bazy danych SQLite
    connection = sqlite3.connect(databasefile)
    flight_df = pd.read_sql_query("SELECT * FROM flights", connection)
    connection.close()
    return flight_df