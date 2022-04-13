from flask import Flask, request, redirect, render_template
from flask_cors import CORS #comment this on deployment
import requests
from sentiment_processing import get_sentiment

app = Flask(__name__)
CORS(app)

'''
Test Endpoint
'''
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''
API Endpoint to return raw Weather Data based on geolocation
'''
@app.route("/weather", methods=["GET"])
def get_weather():

    lat = request.values.get("lat")
    lon = request.values.get("lon")
    location_request = "https://api.weather.gov/points/"+ lat + "," + lon

    #location_point = requests.get("https://api.weather.gov/gridpoints/LWX/96,70/forecast", headers={"User-Agent": "(test.com, test@test.com)"})
    
    #make initial request to get proper formatted forecast request endpoint
    location_summary = requests.get(location_request, headers={"User-Agent": "(test.com, test@test.com)"})
    #print(location_point.json())
    data = location_summary.json()
    #query for forecast by nws office grid
    location_forecast = requests.get(data["properties"]["forecast"], headers={"User-Agent": "(test.com, test@test.com)"})
    location_data = location_forecast.json()
    #print(location_data["properties"])
    most_recent_forecast = location_data["properties"]["periods"][0]
    return most_recent_forecast

@app.route("/analysis", methods = ["GET", "POST"])
def analysis():
    """sends weather information to Watson for sentiment analysis"""
    new_req_url = request.url.replace("analysis","weather")
    forecast = requests.get(new_req_url).json()["detailedForecast"]
    print(forecast)
    sentiment = get_sentiment(forecast)
    return str(sentiment)