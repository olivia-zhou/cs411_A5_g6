# 1. "as a user, I want to search for destinations in order to determine the travel time"

Happy Path: The user should be able to access a small Google Maps widgit on our web app without logging in. This is the first step to using our web app so it will appear near the top with a small prompt. The widgit should work like normal Google Maps, in which the user can input a destination and determine the travel time and directions according to their current or desired starting location. 


Exceptions: A possible issue could occur if the user enters a destination or starting location that do not exist within the Google Maps API. In this case, we will continue using the Google Maps API to display a destination/location error and to prompt the user to try again with a different address. 

Importance/Description: This feature is the backbone of our web app since we will base the length of the playlist pn the length of travel and store the playlists depending on the destination. Also, we decided that users do not have to log in to use this feature, or to check the weater, because not everybody always wants to download a playlist. This way, users will still be able to use our web app to determine important information for their travel plans with or without downloading a free playlist, depending on their mood. 

# 2. "as a user, I want to be able to login to Spotify in order to download playlists and listen to songs"

# 3. "as a logged-in user, I want to view the playlist so I can see what music has been recommended to me"

# 4. "as a logged-in user, I want to be able to log out of spotify to protect my information"

Description: The user should be able to log out any time if they want. The access should be simple, easy to find and works in any situations(include no signal, no internet and etc.). If user has log in an unauthorised device, it should erase everything when user log out(include view history, travel path, playlist and etc). When 
user log in an new device, it should ask user that if they want to authorise current device. If spotify is doing nothing or in background mode for thirty mins, it will automatically log out. 

# 5. "as a user, I want to be able to view the current weather to know what the weather will be like when traveling"
