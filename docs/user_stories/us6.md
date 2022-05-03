## 6. "As a developer, I want to view a list of previously generated playlists and tokens for each user"

**Happy Path:** In order to track app useage and to keep track of the tokens for each user, as a developer, I want to be able to view a list of previously generated playlists attached to each user and the tokens associated with that playlist generation. This information should be stored in a database to be easily stored and retrieved. 

**Description:** This feature should allow the developers to query our database of previously generated playlists for those with some user id. The results will then be given to the developer who can view the tokens and their expiration timestamps.

**Exceptions:** If no previouly generated playlists are associated with the destination given, the database should display an empty result, indicating that the user has not logged in and/or generated a playlist yet.
