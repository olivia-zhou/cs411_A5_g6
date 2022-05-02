

import pymongo

DEFAULT_CONNECTION_URL = 'mongodb://localhost:27017/'
DATABASE_NAME = 'WeatherApp'
COLLECTION_NAME = 'SpotifyUserAuthTokens'

class MongoDatabaseConnection:
        def __init__(self, connection_url = None):
                if connection_url is None:
                        connection_url = DEFAULT_CONNECTION_URL
                
                client = pymongo.MongoClient(connection_url)
                database = client[DATABASE_NAME]
                collection = database[COLLECTION_NAME]
                
                self.client = client
                self.collection = collection
                self.opened = False
                self.closed = False
        
        def open(self):
                if self.closed:
                        raise RuntimeError('Cannot re-open a closed connection.')
                        
                self.opened = True
        
        def close(self):
                if not self.opened:
                        raise RuntimeError('Cannot close a connection that is not opened.')
                        
                self.opened = False
                self.closed = True

        def add_token(self, uuid, email, token, create_timestamp, expire_timestamp):
                '''
                Adds a Spotify user auth token to the database.
                
                If the token already exists, another duplicate of the token will be stored in the database.
                
                Args:
                        uuid: The user's Spotify unique user id.
                        email: The user's email.
                        token: The token string.
                        create_timestamp: The token creation timestamp.
                        expire_timestamp: The token expiration timestamp.
                '''

                if not self.opened:
                        raise RuntimeError('Connection is not open.')
                        
                insert_object = {
                        'email': email,
                        'uuid': uuid,
                        'token': token,
                        'create_timestamp': create_timestamp,
                        'expire_timestamp': expire_timestamp,
                }
                
                self.collection.insert_one(insert_object)

        def find_tokens_by_email(self, email):
                '''
                Returns all Spotify user auth tokens that have matching email fields.
                
                Args:
                        email: The user's Spotify email.
                
                Returns:
                        results: A list of dicts. Each dict represents a token.
                '''

                if not self.opened:
                        raise RuntimeError('Connection is not open.')
                
                find_object = {
                        'email': email,
                }
                
                results = self.collection.find(find_object)
                results = list(results)
                for x in results:
                    del x['_id']
                return results

        def find_tokens_by_uuid(self, uuid):
                '''
                Returns all Spotify user auth tokens that have matching uuid fields.
                
                Args:
                        uuid: The user's Spotify unique user id.
                
                Returns:
                        results: A list of dicts. Each dict represents a token.
                '''
                
                if not self.opened:
                        raise RuntimeError('Connection is not open.')
                        
                find_object = {
                        'uuid': uuid,
                }
                
                results = self.collection.find(find_object)
                results = list(results)
                for x in results:
                    del x['_id']
                return results
