# Weather Walk
Section A5 group 6 CS411 project

Justin Sayah, Bryce Freeman, Nathan Ho, Yvonne Wu, Olivia Zhou, Zizhuang Guo

Using the weather of a walk's destination to create a Spotify playlist using analysis from IBM's Watson

### Setting up with Git Bash:

*Node.JS has some path issues when installed in venv's on Windows so make sure to do step 6 if you are running Windows*

1) clone repo
2) create a new virtual environment and activate it
3) run bash ./update_reqs.sh in order to get the required packages
4) install Node.JS manually into your virtual environment
5) read the Mongo installation docs under the doc folder and install the necessary MongoDB packages
6) in your virtual environment's folder, go to Lib/script-packages and double check to see that all the packages were 

installed correctly as sometimes this does not happen due to OS or machine-specific issues (required packages are listed in requirements.txt)
7) manually install packages as necessary if any are missing or do not have the correct versions
8) email us for the API keys
9) run bash ./run_backend.sh and bash.run/run_frontend.sh in a GitBash terminal to start the frontend and backend

### Use Flow:

*Burner Spotify account to generate playlists in*

*email: cs411.A5.g6@gmail.com*

*password: computerscience411!*

1) login to Spotify by clicking the green button that says "continue with Spotify"
2) enter your destination
3) click the button that says "Generate Playlist!" in order to generate a playlist based on the weather
4) check your spotify for your new weather playlist!
5) when you are all set, you can either click the logout button in order to log out of spotify

*you will be logged out after 60 minutes automatically, in case you forget to logout manually

### Checking the DB for contents:
*in mongoshell*

use WeatherApp

db.SpotifyAuthTokens.find()
