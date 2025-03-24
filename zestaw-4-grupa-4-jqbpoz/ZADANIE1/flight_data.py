import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from ZADANIE1.database import save_to_db, load_flight_data

def fetch_flight_data(databasefile="flights.db"):
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407
    url = "https://opensky-network.org/api/states/all"
    params = {
        "lamin": lat_min,
        "lomin": lon_min,
        "lamax": lat_max,
        "lomax": lon_max
    }
    response = requests.get(url, params=params)
    data = response.json()
    columns = [
        "icao24", "callsign", "origin_country", "time_position", "last_contact",
        "long", "lat", "baro_altitude", "on_ground", "velocity", "true_track",
        "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"
    ]
    flight_df = pd.DataFrame(data["states"], columns=columns)

    save_to_db(flight_df, databasefile)
    print("Data saved to database successfully!")


def plot_flight_data(databasefile="flights.db", show_plot=True):
    flight_df = load_flight_data(databasefile)
    flight_df = flight_df[flight_df["on_ground"] == False]
    flight_df["velocity_kmh"] = flight_df["velocity"] * 3.6
    flight_df["altitude_km"] = flight_df["baro_altitude"] / 1000

    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=flight_df, x="velocity_kmh", y="altitude_km", hue="icao24", palette="tab20", s=10, legend="full")
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Altitude (km)")
    plt.title("Flight Data")
    plt.legend(title="ICAO24")

    plt.grid(True)
    plt.tight_layout()

    if show_plot:
        plt.show()

