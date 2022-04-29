# This python script demonstrates storing a new token in the database.

import time

from MongoDatabaseConnection import MongoDatabaseConnection

db_connection = MongoDatabaseConnection()
db_connection.open()

# Token information
uuid = '35t'
email = None
token = 'sdfgtj'
create_timestamp = time.time()
expire_timestamp = create_timestamp + 60 * 60

# Store token in database
db_connection.add_token(uuid, email, token, create_timestamp, expire_timestamp)

db_connection.close()
