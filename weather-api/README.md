# Weather Data API

The Weather Data API provides access to historical weather data for various locations. It allows querying weather information based on location, data type (e.g., temperature, humidity), and date range. This API is designed to serve as a backend service for weather data retrieval.

## Features

- **Data Querying**: Fetch weather data by specifying location, data type, and date range.
- **Dynamic Endpoints**: Discover available locations and data types through dedicated API endpoints.
- **Cross-Origin Requests Enabled**: Supports cross-origin requests, making it suitable for frontend applications to consume the API.

## Prerequisites

Before setting up the API, ensure you have the following installed on your system:

- Python 3.6 or newer
- pip (Python package installer)

## Setup Instructions

Follow these steps to get the API up and running:

1. **Database Initialization**

If the `weather_data.db` SQLite database file does not exist yet, you will need to generate it from a CSV file containing the weather data. Run the `convert_csv_to_sql.py` script provided in the repository:

```
python convert_csv_to_sql.py
```

Ensure your CSV file is correctly formatted and accessible by the script.

2. **Create a Virtual Environment (Optional)**

Navigate to the project directory and create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

3. **Install Dependencies**

With the virtual environment activated, install the required Python packages:

```
pip install -r requirements.txt
```

4. **Running the API**

Start the Flask application:

```
flask run
```

This command starts the API on the default port 5000.

## Accessing the API

Once the API is running, you can access it from your web browser or any HTTP client. Here are the available endpoints:

- `/`: The root endpoint provides a brief description of the API and its usage.
- `/weather`: Fetch weather data by specifying `location`, `type` (data type), `start_date`, and `end_date` as query parameters.
- `/locations`: Get a list of available locations for querying weather data.
- `/data_types`: Discover the types of weather data you can query.

Example query:

```
http://localhost:5000/weather?location=London&type=temperature&start_date=2021-01-01&end_date=2021-01-31
```

