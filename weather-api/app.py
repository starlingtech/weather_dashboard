from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app

def query_weather_data(database_path, city_name, data_type, start_date, end_date):
    """
    Query weather data from the SQLite database based on parameters.
    """
    conn = sqlite3.connect(database_path)
    query = f"""
        SELECT dt_iso, {data_type} 
        FROM weather_data 
        WHERE city_name = ? AND dt_iso BETWEEN ? AND ?
    """
    df = pd.read_sql_query(query, conn, params=[city_name, start_date, end_date])
    conn.close()
    return df.to_dict(orient='records')

@app.route('/')
def index():
    """
    Index route that provides a brief explanation of the API and its available endpoints, formatted in HTML.
    """
    api_description_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Data API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            p { color: #666; }
            ul { color: #444; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Weather Data API!</h1>
        <p>This API allows you to query weather data for various locations and time periods. Below are the available endpoints:</p>
        <ul>
            <li><strong>/weather</strong>: Fetch weather data based on location, type of weather data, and date range. 
            Required parameters: 'location', 'type', 'start_date', 'end_date'.</li>
            <li><strong>/locations</strong>: Get a list of available locations from which you can query weather data.</li>
            <li><strong>/data_types</strong>: Discover the types of weather data (e.g., temperature, humidity) you can query.</li>
        </ul>
        <p>Please replace the parameter values in your requests according to the data you wish to retrieve.</p>
    </body>
    </html>
    """
    return api_description_html



@app.route('/weather', methods=['GET'])
def get_weather_data():
    """
    API endpoint to fetch weather data based on location, type of weather data, and date range.
    """
    city_name = request.args.get('location')
    data_type = request.args.get('type')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not all([city_name, data_type, start_date, end_date]):
        return jsonify({'error': 'Missing required parameters'}), 400

    data = query_weather_data('weather_data.db', city_name, data_type, start_date, end_date)
    return jsonify(data)

@app.route('/locations', methods=['GET'])
def get_locations():
    """
    API endpoint to fetch a list of available locations from the weather_data table.
    """
    conn = sqlite3.connect('weather_data.db')
    query = "SELECT DISTINCT city_name FROM weather_data"
    df = pd.read_sql_query(query, conn)
    conn.close()
    locations = df['city_name'].tolist()
    return jsonify(locations)

@app.route('/data_types', methods=['GET'])
def get_data_types():
    """
    API endpoint to dynamically fetch a list of available data types from the data_types table in the database.
    """
    conn = sqlite3.connect('weather_data.db')
    query = "SELECT data_type_name FROM data_types"
    df = pd.read_sql_query(query, conn)
    conn.close()
    data_types = df['data_type_name'].tolist()
    return jsonify(data_types)

if __name__ == '__main__':
    app.run(debug=True)
