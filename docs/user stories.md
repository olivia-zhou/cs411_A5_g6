## 1. "as a user, I want to search for destinations in order to determine the travel time"

**Happy Path:** The user should be able to access a small Google Maps widget on our web app without logging in. This is the first step to using our web app so it will appear near the top with a small prompt. The widget should work like normal Google Maps, in which the user can input a destination and determine the travel time and directions according to their current or desired starting location. 


**Exceptions:** A possible issue could occur if the user enters a destination or starting location that do not exist within the Google Maps API. In this case, we will continue using the Google Maps API to display a destination/location error and to prompt the user to try again with a different address. Another potentential issue could occur if the user hsan't granted location access. In this case, we would present a small reminder that the app didn't have location access. This prompt wouldn't disrupt the user, though, since they would still be able to manually enter the 'from' location.

**Importance/Description:** This feature is the backbone of our web app since we will base the length of the playlist on the length of travel and store the playlists depending on the destination. Also, we decided that users do not have to log in to use this feature, or to check the weater, because not everybody always wants to download a playlist. This way, users will still be able to use our web app to determine important information for their travel plans with or without downloading a free playlist, depending on their mood. 

## 2. "as a user, I want to be able to login to Spotify in order to add Spotify playlists to my Spotify account"

**Happy Path:** The user should press an imbedded Spotify prompt and be directed to a Spotify OAuth window so that they can authenticate. Once they do that, they will return to our main page with the Google Maps widget as mentioned in Story 1. 

**Description/Details:** This is necessary so that generated playlists can be added directly into the account of our users and so that we have access to all of the embedded Spotify features that are critical to our app: (Story 3: View Playlist), (Story 6: Generate Playlist). Ideally, this will also allow us to pull and display a history of playlists that the authenticated user has generated with our application if we decide to include this feature.

**Exceptions:** If a user fails the login, they should be thrown back to the main page from Story 1 and be given a brief error message that login has failed. (This might not be necessary as the Spotify OAuth might catch this and prevent user from being thrown back.)

## 3. "as a logged-in user, I want to view the playlist so I can see what music has been recommended to me"

**Happy path:** After clicking generate playlist in Story 6, the app generate a playlist and display it to the user. The user should then be able view all songs in the playlist and listen to the playlist through Spotify.

What the app displays to the user can be some information about each song like its title and artist. The app can also give a short summary of the playlist like the top few artists within the playlist, the most popular genre of music within the playlist, or a title or short phrase for the playlist.

Given that our app is powered by Spotify, which provides music streaming services, it will be convenient for the user if our app enables the user to begin listening to the playlist in just a few clicks. [Spotify allows developers to embed a playlist directly into a website.](https://developer.spotify.com/documentation/widgets/generate/embed/) The app can also give a link that leads directly to a Spotify url for that playlist.

**Exceptions:** If the user is not logged in and they try to follow the playlist, they'll be prompted to log into Spotify first. This would be handled as described in story #2.

## 4. "as a logged-in user, I want to be able to log out of spotify to protect my information"

**Happy path:** There should be a simple log out button which, upon being pressed, prompts the user to confirm that they want to log out. If they confirm, they should be logged out. If they cancel, the prompt should go away and they should be back on the same screen as they were prior to selecting the button.

**Description:** The user should be able to log out any time if they want. The access should be simple, easy to find and works in any situations(include no signal, no internet and etc.). If user has log in an unauthorised device, it should erase everything when user log out(include view history, travel path, playlist and etc). When 
user log in an new device, it should ask user that if they want to authorise current device. If spotify is doing nothing or in background mode for thirty mins, it will automatically log out. 

**Exceptions:** Obviously, if the user isn't logged in, they shouldn't be able to log out. So, we won't provide a way to do so until they've logged in.

## 5. "as a user, I want to be able to view the current weather to know what the weather will be like when traveling"

**Happy Path:** After the user successfully enters the destination in Story 1, the user should be able to access the weather on a widget on our web application. The user should be able to view the weather information of the current location, the destination, and the change during traveling. 

**Exceptions:** One possible scenario is that the trip encounters extreme weather conditions, such as a storm or hurricane. We will pop up a window to alert the user of the current situation, but the user can choose to continue or cancel the trip. If they cancel the trip, the user will return to the main page in Google Maps.

**Description:** The user should be able to view detailed weather information they may experience without logging in. We will include temperature, the chance of rain, humidity, wind, visibility, and air quality press to prepare the user for the trip. The users can also generate playlists regarding current weather in Story 5. 

## 6. "as a logged-in user, I want to press the Generate Playlist button to gerenate a playlist for my destination"

**Happy Path:** I, an authenticated user, have already searched for a destination as in Story 1 and have authenticated as in Story 2. After checkking the displayed travel length and reviewing the weather (Story 5), I decide to press the Generate Playlist button on the page. Our app then takes the inputted destination and weather and generates a playlist for this specific circumstance and displays it (Story 3) before using embedded Spotify features to add it to their acccount for audio playback on their device of choice.

**Description:** As decribed above, this button will generate a playlist for an authed user given a destination. It should also add this playlist into the database which will hold all the playlists generated for a given chosen destination/path.

**Exception:** If the user clicks this button while not being authenticated or without a destinated selected, they should be given a brief error and told to auth and select a destination.

## 7. "As a logged-in user, I want to view a list of previously generated playlists based off of a given destination"

**Happy Path:** Once I've logged in, I want to be able to navigate to a history page (likely through a sidebar). On this page, I should be able to search by destination to get a list of playlists which this app has previously generated for that same destination. I should then be able to view the details of any of these individual playlists.

**Description:** This feature should allow the user to query our database of previously generated playlists for those with some given destination. The results will then be given to the user who can interact with them in a way similar to a newly generated playlist.

**Exceptions:** If no previouly generated playlists are associated with the destination given, the history page should display test clarifying that no playlists were found.
