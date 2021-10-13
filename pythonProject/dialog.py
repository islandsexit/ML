from flask import Flask, request, make_response, jsonify
import requests
import json
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


def results():
    global feels_like
    req = request.get_json(force=True)

    action = req.get('queryResult').get('action')

    result = req.get("queryResult")
    parameters = result.get("parameters")

    if parameters.get('location').get('city'):
        geolocator = Nominatim(user_agent='weather-bot')
        location = geolocator.geocode(parameters.get('location').get('city'))
        lat = location.latitude
        long = location.longitude
        weather_req = requests.get(
            'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(lat, long, API_KEY))
        current_weather = json.loads(weather_req.text)['current']
        temp = round(current_weather['temp'] - 273.15)
        feels_like = round(current_weather['feels_like'] - 273.15)
        clouds = current_weather['clouds']
        wind_speed = current_weather['wind_speed']

    return {
        'fulfillmentText': 'Сейчас температура воздуха - {} градусов, ощущается как {} градусов, облачность - {}%, скорость ветра - {}м/с'.format(
            str(temp), str(feels_like), str(clouds), str(wind_speed))}


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))
