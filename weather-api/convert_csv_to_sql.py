import pandas as pd
import sqlite3

def convert_temperature(temp, unit_from, unit_to):
    """
    Convert temperature between Celsius and Fahrenheit.
    """
    if unit_from == "C" and unit_to == "F":
        return temp * 9/5 + 32
    elif unit_from == "F" and unit_to == "C":
        return (temp - 32) * 5/9
    else:
        return temp

def process_csv_to_sqlite(csv_file_path, database_path, temp_unit="C", new_city_name=""):
    """
    Process a weather data CSV file and store it in an SQLite database.
    Arguments:
    - csv_file_path: Path to the CSV file containing weather data.
    - database_path: Path to the SQLite database file.
    - temp_unit: The unit of temperature in the CSV file ('C' for Celsius, 'F' for Fahrenheit).
    - new_city_name: New name for the city to be used when importing into the database.
    """
    # Read CSV file
    df = pd.read_csv(csv_file_path)
    
    # Convert temperatures if necessary
    if temp_unit != "C":
        temp_columns = ['temp', 'dew_point', 'feels_like', 'temp_min', 'temp_max']
        for col in temp_columns:
            df[col] = df[col].apply(lambda x: convert_temperature(x, temp_unit, "C"))
    
    # Rename city_name if new_city_name is provided
    if new_city_name:
        df['city_name'] = new_city_name
    
    # Connect to SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # Create tables if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                        dt INTEGER,
                        dt_iso TEXT,
                        timezone INTEGER,
                        city_name TEXT,
                        lat REAL,
                        lon REAL,
                        temp REAL,
                        visibility INTEGER,
                        dew_point REAL,
                        feels_like REAL,
                        temp_min REAL,
                        temp_max REAL,
                        pressure INTEGER,
                        sea_level INTEGER,
                        grnd_level INTEGER,
                        humidity INTEGER,
                        wind_speed REAL,
                        wind_deg INTEGER,
                        wind_gust REAL,
                        rain_1h REAL,
                        rain_3h REAL,
                        snow_1h REAL,
                        snow_3h REAL,
                        clouds_all INTEGER,
                        weather_id INTEGER,
                        weather_main TEXT,
                        weather_description TEXT,
                        weather_icon TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT UNIQUE)''')
    
    cursor.execute('''INSERT OR IGNORE INTO locations (city_name) VALUES (?)''', (new_city_name,))
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS data_types (
                        data_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        data_type_name TEXT UNIQUE)''')
    
    data_types = [col for col in df.columns if col not in ['dt', 'dt_iso', 'city_name', 'lat', 'lon']]
    for dtype in data_types:
        cursor.execute('''INSERT OR IGNORE INTO data_types (data_type_name) VALUES (?)''', (dtype,))
    
    # Insert data into the weather_data table
    df.to_sql('weather_data', conn, if_exists='append', index=False)
    
    # Close the database connection
    conn.close()


# The function calls are commented out to avoid execution in this environment.
# Example of function call with the new city name parameter:
process_csv_to_sqlite(csv_file_path="london.csv", database_path="weather_data.db", temp_unit="F", new_city_name="London")
process_csv_to_sqlite(csv_file_path="cambridge.csv", database_path="weather_data.db", temp_unit="C", new_city_name="Cambridge")
