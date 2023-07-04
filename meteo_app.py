import requests
from pprint import pprint
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_Key = 'bda149bd945c8543506697042541995d'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    ville = request.form['ville']

    url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={ville}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Impossible de récupérer les données météo.'})

if __name__ == '__main__':
    app.run(debug=True)
