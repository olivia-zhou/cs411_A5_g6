## 2. "as a user, I want to be able to login to Spotify in order to add Spotify playlists to my Spotify account"

**Happy Path:** The user should press an imbedded Spotify prompt and be directed to a Spotify OAuth window so that they can authenticate. Once they do that, they will return to our main page with the Google Maps widget as mentioned in Story 1. 

**Description/Details:** This is necessary so that generated playlists can be added directly into the account of our users and so that we have access to all of the embedded Spotify features that are critical to our app: (Story 3: View Playlist), (Story 6: Generate Playlist). Ideally, this will also allow us to pull and display a history of playlists that the authenticated user has generated with our application if we decide to include this feature.

**Exceptions:** If a user fails the login, they should be thrown back to the main page from Story 1 and be given a brief error message that login has failed. (This might not be necessary as the Spotify OAuth might catch this and prevent user from being thrown back.)
