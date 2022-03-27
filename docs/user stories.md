# 1. "as a user, I want to search for destinations in order to determine the travel time"

Happy Path: The user should be able to access a small Google Maps widget on our web app without logging in. This is the first step to using our web app so it will appear near the top with a small prompt. The widget should work like normal Google Maps, in which the user can input a destination and determine the travel time and directions according to their current or desired starting location. 


Exceptions: A possible issue could occur if the user enters a destination or starting location that do not exist within the Google Maps API. In this case, we will continue using the Google Maps API to display a destination/location error and to prompt the user to try again with a different address. 

Importance/Description: This feature is the backbone of our web app since we will base the length of the playlist on the length of travel and store the playlists depending on the destination. Also, we decided that users do not have to log in to use this feature, or to check the weater, because not everybody always wants to download a playlist. This way, users will still be able to use our web app to determine important information for their travel plans with or without downloading a free playlist, depending on their mood. 

# 2. "as a user, I want to be able to login to Spotify in order to add Spotify playlists to my Spotify account"

Description: The user should press an imbedded Spotify prompt and be directed to a Spotify OAuth window so that they can authenticate. Once they do that, they will return to our main page with the Google Maps widget as mentioned in Story 1. This is necessary so that generated playlists can be added directly into the account of our users. Ideally, this will also allow us to pull and display a history of playlists that the authenticated user has generated with our application.

Exceptions: If a user fails the login, they should be thrown back to the main page from Story 1 and be given a brief error message that login has failed. (This might not be necessary as the Spotify OAuth might catch this and prevent user from being thrown back.)

# 3. "as a logged-in user, I want to view the playlist so I can see what music has been recommended to me"

# 4. "as a logged-in user, I want to be able to log out of spotify to protect my information"

Description: The user should be able to log out any time if they want. The access should be simple, easy to find and works in any situations(include no signal, no internet and etc.). If user has log in an unauthorised device, it should erase everything when user log out(include view history, travel path, playlist and etc). When 
user log in an new device, it should ask user that if they want to authorise current device. If spotify is doing nothing or in background mode for thirty mins, it will automatically log out. 

# 5. "as a user, I want to be able to view the current weather to know what the weather will be like when traveling"
Happy Path: 
After the user successfully enters the destination in Story 1, the user should be able to access the weather on a widget on our web application. The user should be able to view the weather information of the current location, the destination, and the change during traveling. 

Exceptions: 
One possible scenario is that the trip encounters extreme weather conditions, such as a storm or hurricane. We will pop up a window to alert the user of the current situation, but the user can choose to continue or cancel the trip.

Importance/Description: 
The user should be able to view detailed weather information they may experience without logging in. We will include temperature, the chance of rain, humidity, wind, visibility, and air quality press to prepare the user for the trip. The users can also generate playlists regarding current weather in Story 5. 

# 6. "as a logged-in user, I want to press the Generate Playlist button to gerenate a playlist for my destination"

Description: I, an authenticated user, have already searched for a destination as in Story 1 and have authenticated as in Story 2. After checkking the displayed travel length and reviewing the weather (Story 5), I decide to press the Generate Playlist button on the page. Our app then takes the inputted destination and weather and generates a playlist for this specific circumstance and displays it (Story 3) before using embedded Spotify features to add it to their acccount for audio playback on their device of choice.

Exception: If the user clicks this button while not being authenticated or without a destinated selected, they should be given a brief error and told to auth and select a destination.
