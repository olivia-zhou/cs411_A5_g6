from audioop import cross
from flask import Flask, request, redirect, render_template, make_response
from flask_cors import CORS, cross_origin #comment this on deployment
import requests
from sentiment_processing import get_sentiment
import json
from spotify_class import spotify
import base64


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

'''
Test Endpoint
'''
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

global_lat = 0
global_long = 0

'''
API Endpoint to return raw Weather Data based on geolocation
'''
@app.route("/weather", methods=["GET"])
def get_weather():

    #lat = request.values.get("lat")
    #lon = request.values.get("lon")
    #print(lat, lon)
    location_request = "https://api.weather.gov/points/" + global_lat + "," + global_long

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
API Endpoint to return raw Weather Data based on geolocation
'''
@app.route("/update_coordinates", methods=["GET"])
def update_coords():
    global_lat = request.values.get("lat")
    global_long = request.values.get("lon")
    return 'success'

@app.route("/analysis", methods = ["GET", "POST"])
def analysis():
    """sends weather information to Watson for sentiment analysis"""
    new_req_url = request.url.replace("analysis","weather")
    forecast = requests.get(new_req_url).json()["detailedForecast"]
    print(forecast)
    sentiment = get_sentiment(forecast)
    return str(sentiment)


'''
SPOTIFY API AUTHORIZATION PIPELINE
'''
f = open('spotify_key.json')
key = json.load(f)

#Spotify information
SPOTIFY_ENDPOINT = 'https://api.spotify.com/v1/'
CLIENT_ID = f'409b58756fd146ec81debb62c51eb887'
CLIENT_URL = 'http://127.0.0.1'
CLIENT_SECRET = key['client_secret']
PORT = '5000'
REDIRECT_URL = '{}:{}/callback'.format(CLIENT_URL, PORT)
HOME = '{}:{}/'.format(CLIENT_URL, PORT)
SCOPE = 'ugc-image-upload user-read-email user-read-private user-top-read playlist-modify-public playlist-modify-private playlist-read-private'


@app.route('/login', methods = ["GET"])
def login():
    print (REDIRECT_URL)
    parameters = 'response_type=code&client_id=' + CLIENT_ID + '&redirect_uri=' + REDIRECT_URL + '&scope=' + SCOPE
    authorize_url = 'https://accounts.spotify.com/en/authorize?' + parameters
    response = make_response(redirect(authorize_url))
    response.set_cookie('cross-site-cookie', 'bar', samesite='None', secure=True)
    response.headers.add('Set-Cookie','cross-site-cookie=bar; SameSite=None; Secure')
    return response

@app.route('/callback')
def callback():
    if request.args.get('error'):
        return render_template('index.html', error = 'Spotify error')
    else:
        code = request.args.get('code')
        token = get_token(code)
        sentiment = 0.7
        #spotifyinfo = spotify(CLIENT_ID, token, sentiment)
    return make_response(token)


def get_token(code):
    token_url = 'https://accounts.spotify.com/api/token' 
    token_info = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URL,
            'client_id': CLIENT_ID
        }
    encoded_id = base64.b64encode(str.encode(CLIENT_ID)).decode()
    encoded_secret = base64.b64decode(str.encode(CLIENT_SECRET)).decode()
    header = {
        'Authorization': 'Basic <{}:{}>'.format(encoded_id, encoded_secret),
        'Content-Type':'application/x-www-form-urlencoded'
        }
    token = requests.post(token_url, data = token_info, headers=header)
    if token != None:
        response = json.loads(token.text)
        access_token = response["access_token"]
        token_type = response['token_type']
        scope = response['scope']
        expires_in = response["expires_in"]
        refresh_token = response["refresh_token"]
    else:
        return render_template('index.html', error = 'Token failure')
    return access_token

def refresh_token(refresh_token):
    token_url = 'https://accounts.spotify.com/api/token' 
    token_info = {
            'grant_type': 'refresh_token',
            'code': refresh_token,
            'redirect_uri': REDIRECT_URL,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    token = requests.post(token_url, data = token_info, headers = {'Authorization': 'Basic', 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'})
    if token != None:
        response = json.loads(token.text)
        access_token = response["access_token"]
        token_type = response['token_type']
        scope = response['scope']
        expires_in = response["expires_in"]
    return access_token

@app.route('/generate_playlist')
def generate_playlist():
    token = request.args.get('access_token')
    token_type = request.args.get('token_type')
    expires_in = request.args.get('expires_in')
    if token != None:
        #sentiment = redirect('http://127.0.0.1:5000/analysis')
        sentiment = .5
        # print(sentiment)
        # print('checkcheckcheck')
        spotifyplaylist = spotify(CLIENT_ID, token, sentiment)
        #print (spotifyplaylist.final_return())
        return make_response('check')
    else:
        print('fail')
        return "hi"
    return make_response('bug check - delete later')


@app.route('/logout')
def logout():
    url = 'https://accounts.spotify.com/en/logout'
    return redirect(url)

    #TEST: http://127.0.0.1:5000/weather?lat=40.730610&lon=-73.935242