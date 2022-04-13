from flask import Flask, request, redirect, render_template
from flask_cors import CORS #comment this on deployment
import requests
import sentiment_processing

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
    print(request.url)
    # forecast = requests.get("localhost/weather")
    pass

@app.route('/login', methods = ["GET"])
def login():
    client_secret = 'b9e9785a1066492e972efe867d5190df'
    client_id = '409b58756fd146ec81debb62c51eb887'
    redirect_url = 'http://localhost:8888/callback'
    #state = gen_state_key();       for if we want a state key
    scope = 'ugc-image-upload user-read-email user-top-read playlist-modify-public playlist-modify-private playlist-read-private'
    parameters = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_url + '&scope=' + scope #+ '&state=' + state
    authorize_url = 'https://accounts.spotify.com/en/authorize?' + parameters
    response = requests.get(authorize_url)
    return response

@app.route('/callback', methods = ["GET"])
def callback():
    #if request.args.get('state') != session['state_key']:
	#	return render_template('index.html', error='State mismatch')
	if request.args.get('error'):
		return render_template('index.html', error='Spotify error.')
	else:
        current_user = getUserInformation(session)
        session['user_id'] = current_user['id']
        logging.info('new user:' + session['user_id'])
        code = request.args.get('code')
		payload = get_token(code)
		if payload != None:
			#get token info here
            token = payload
        else:
			return render_template('index.html', error='Failed to access token.')
        
	    return redirect(session['previous_url'])

@app.route('/get_token()', mehtods = ["POST"])
def get_token():
    token_url = 'https://accounts.spotify.com/api/token' 
    body = {'code': code, 'redirect_uri': redirect_uri, 'grant_type': 'authorization_code'}
    response = request.post(token_url, headers = {'Authorization': 'Basic', 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'})
    pass

@app.route('/get_new_token')
def get_new_token():
    pass


@app.route("/get_music", methods = ["GET", "POST"])
def get_music():
    """
    uses sentiment analysis from Watson to get spotify playlist
    get current user id: https://api.spotify.com/v1/me
    create playlist: https://api.spotify.com/v1/users/{user_id}/playlists
    add to playlist: https://api.spotify.com/v1/playlists/{playlist_id}/tracks

    """
    #our team's client id and secret - i registered us with spotify so we can access user data
    
    login_request = "https://api.spotify.com/v1/me"
    get_user_info = requests.get(login_request, headers={"User"})
    user_info = get_user_info.json()

    pass