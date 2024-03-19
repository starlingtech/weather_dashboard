# Weather Data Frontend Application

This Flask application provides a user-friendly interface for querying weather data from a specified Weather API. The interface allows users to input a location, data type, start date, and end date to fetch weather data, which is then displayed in raw JSON format.

## Prerequisites

Before you can run this application, you'll need to have the following installed on your system:

- Python 3.6 or newer
- pip (Python package installer)

## Installation

Follow these steps to get the frontend application up and running:

1. **Create a Virtual Environment (Optional but Recommended)**

Create a virtual environment by running:

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

2. **Install Required Python Packages**

With the virtual environment activated, install the required Python packages by running:

```
pip install -r requirements.txt
```

3. **Running the Frontend Application**

Start the Flask application by running:

```
flask run --port 5001
```

This will start the application on port 5001. Ensure that the weather data API is running on a different port (e.g., the default Flask port 5000).

4. **Accessing the Application**

Open a web browser and navigate to [http://localhost:5001](http://localhost:5001) to access the frontend application. You should see a form where you can input the query parameters for the weather data you wish to retrieve.

## Usage

Fill in the form fields with the desired location, data type, start date, and end date. Click the "Submit" button to fetch and display the weather data in raw JSON format below the form.

## Customization

To customize the appearance or functionality of the application:

- Modify `templates/index.html` to change the layout or form elements.
- Update `static/styles.css` to alter the visual styling.
- Edit `static/script.js` to adjust or add JavaScript functionality.
