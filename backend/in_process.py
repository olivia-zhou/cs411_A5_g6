from flask import Flask, request, redirect, render_template
from flask_cors import CORS #comment this on deployment
import requests
import json
#import sentiment_processing

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



'''
SPOTIFY API AUTHORIZATION PIPELINE
'''

#Spotify information
SPOTIFY_ENDPOINT = 'https://api.spotify.com/v1/'
CLIENT_SECRET = 'b9e9785a1066492e972efe867d5190df'
CLIENT_ID = '409b58756fd146ec81debb62c51eb887'
CLIENT_URL = 'http://127.0.0.1'
PORT = '5000'
REDIRECT_URL = '{}:{}/callback'.format(CLIENT_URL, PORT)
HOME = '{}:{}/'.format(CLIENT_URL, PORT)
SCOPE = 'ugc-image-upload user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private'


@app.route('/login', methods = ["GET"])
def login():
    print (REDIRECT_URL)
    parameters = 'response_type=code&client_id=' + CLIENT_ID + '&redirect_uri=' + REDIRECT_URL + '&scope=' + SCOPE
    authorize_url = 'https://accounts.spotify.com/en/authorize?' + parameters
    return redirect(authorize_url)

@app.route('/callback')
def callback():
    if request.args.get('error'):
        return render_template('index.html', error = 'Spotify error')
    else:
        code = request.args.get('code')
        token = get_token(code)
        if token != None:
            response = json.loads(token.text)
            access_token = response["access_token"]
            token_type = response['token_type']
            scope = response['scope']
            expires_in = response["expires_in"]
            refresh_token = response["refresh_token"]
        else:
            return render_template('index.html', error = 'Token failure')
    #country, name, email = get_user_info(access_token)
    info = get_user_info(access_token)
    print (info)
    return redirect(HOME)


def get_token(code):
    token_url = 'https://accounts.spotify.com/api/token' 
    token_info = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URL,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    response = requests.post(token_url, data = token_info)
    return response

def refresh_token(refresh_token):
    token_url = 'https://accounts.spotify.com/api/token' 
    token_info = {
            'grant_type': 'refresh_token',
            'code': refresh_token,
            'redirect_uri': REDIRECT_URL,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    response = requests.post(token_url, data = token_info, headers = {'Authorization': 'Basic', 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'})
    return response

def get_user_info(access_token):
    authorization_header = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(access_token)}
    me_url = "{}/me".format(SPOTIFY_ENDPOINT)
    profile_data = requests.get(me_url, headers=authorization_header)
    info = json.loads(profile_data.text)
    #country = info['country']
    #display_name = info['display_name']
    #email = info['email']
    return info #country, display_name, email