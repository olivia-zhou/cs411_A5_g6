from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''
Stuff
'''
@app.route("/weather", methods=["GET"])
def get_weather():

    # lat = request.values.get("lat")
    # long = request.values.get("long")
    # location_request = "https://api.weather.gov/points/"+ lat + "," + long
    location_point = requests.get("https://api.weather.gov/gridpoints/LWX/96,70/forecast", headers={"User-Agent": "(test.com, test@test.com)"})
    #print(location_point)
    return location_point