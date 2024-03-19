from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    json_data = None
    if request.method == 'POST':
        # Collect form data
        location = request.form.get('location')
        data_type = request.form.get('data_type')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        # Construct the API request URL
        api_url = f"http://localhost:5000/weather?location={location}&type={data_type}&start_date={start_date}&end_date={end_date}"
        
        # Make a request to the weather API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Process the JSON response if request was successful
            json_data = response.json()

    # Serve the index.html template
    return render_template('index.html', json_data=json_data)

if __name__ == '__main__':
    app.run(port=5001)
