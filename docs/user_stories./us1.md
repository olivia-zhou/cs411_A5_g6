## 1. "as a user, I want to search for destinations in order to determine the travel time"

**Happy Path:** The user should be able to access a small Google Maps widget on our web app without logging in. This is the first step to using our web app so it will appear near the top with a small prompt. The widget should work like normal Google Maps, in which the user can input a destination and determine the travel time and directions according to their current or desired starting location. 


**Exceptions:** A possible issue could occur if the user enters a destination or starting location that do not exist within the Google Maps API. In this case, we will continue using the Google Maps API to display a destination/location error and to prompt the user to try again with a different address. Another potentential issue could occur if the user hsan't granted location access. In this case, we would present a small reminder that the app didn't have location access. This prompt wouldn't disrupt the user, though, since they would still be able to manually enter the 'from' location.

**Importance/Description:** This feature is the backbone of our web app since we will base the length of the playlist on the length of travel and store the playlists depending on the destination. Also, we decided that users do not have to log in to use this feature, or to check the weater, because not everybody always wants to download a playlist. This way, users will still be able to use our web app to determine important information for their travel plans with or without downloading a free playlist, depending on their mood. 

