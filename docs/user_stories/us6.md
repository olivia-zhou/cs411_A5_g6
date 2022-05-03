## 6. "as a logged-in user, I want to press the Generate Playlist button to gerenate a playlist for my destination"

**Happy Path:** I, an authenticated user, have already searched for a destination as in Story 1 and have authenticated as in Story 2. After checking the displayed travel length, I decide to press the Generate Playlist button on the page. Our app then takes the inputted destination and weather and generates a playlist for this specific circumstance and displays it (Story 3) before using embedded Spotify features to add it to their acccount for audio playback on their device of choice.

**Description:** As decribed above, this button will generate a playlist for an authed user given a destination. It should also add this playlist into the database which will hold all the playlists generated for a given chosen destination/path.

**Exception:** If the user clicks this button while not being authenticated or without a destinated selected, they should be given a brief error and told to auth and select a destination.
