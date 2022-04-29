# This python script demonstrates using MongoDatabaseConnection to find all tokens with a particular uuid.

from MongoDatabaseConnection import MongoDatabaseConnection

db_connection = MongoDatabaseConnection()
db_connection.open()

uuid = '35t'

tokens = db_connection.find_tokens_by_uuid(uuid)
print(tokens)

db_connection.close()
