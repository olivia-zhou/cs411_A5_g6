## 7. "As a logged-in user, I want to view a list of previously generated playlists based off of a given destination"

**Happy Path:** Once I've logged in, I want to be able to navigate to a history page (likely through a sidebar). On this page, I'll see a blank panel underneath a text box. I should be able to enter a destination in the text box and search. The panel underneath should then be filled out by a list of playlists which this app has previously generated for that same destination. I should then be able to view the details of any of these individual playlists. This could be done by redirecting the user to Spotify or by giving a more detailed view of the playlist in app.

**Description:** This feature should allow the user to query our database of previously generated playlists for those with some given destination. The results will then be given to the user who can interact with them in a way similar to a newly generated playlist.

**Exceptions:** If no previouly generated playlists are associated with the destination given, the history page should display test clarifying that no playlists were found. A potential alternative to this case is to give playlists associated with the nearest destination to the one entered. In this case, there would be text between the text box and the search results which clarified that there were no playlists for the searched location and that the results were for \[nearby place].

**Edited:** The feature of viewing previously generated playlists was dropped. The logged-in user will be able to view playlists on logged-in Spotify accounts, but not able to view other playlists from the same destination.
