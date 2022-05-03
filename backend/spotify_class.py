'''
Spotify class
'''
from flask import Flask, request, redirect, render_template
import requests
import json, random



class spotify:
    def __init__(self, oauth, token, sentiment):
        self.oauth = oauth
        self.token = token
        #sentiment is passed in range of -1 to 1, but must be converted to range 0 to 1
        self.sentiment = (sentiment + 1)/2
        #self.country, self.username, self.email = self.get_me()
        self.username = self.get_me()

        #these need to be replaced with one function that does everything
        self.playlist_url, self.playlist_id = self.create_empty_playlist()
        self.populate_playlist()

        self.song_list = []
        # self.short_id = self.add_music()
    
    def get_me(self):
        info_url = 'https://api.spotify.com/v1/me'
        userinfo = requests.get(info_url, headers={'Authorization': "Bearer " + self.token})
        response = userinfo.json()
        #print(response)
        #country = response['country']
        name = response['display_name']
        #email= response['email']
        return name
    
    def create_empty_playlist(self):
        playlist_url = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.username)
        playlist_info = {
            'name': 'weather playlist',
            'public': True,
            'collaborative': False,
            'description': 'playlist generated based on the weather :)',
        }
        create = requests.post(playlist_url, json = playlist_info, headers={'Authorization': "Bearer " + self.token})
        playlist = create.json()
        playlist_url = playlist['uri']
        playlist_id = playlist['id']
        return playlist_url, playlist_id

    def populate_playlist(self):
        genres = ['hip-hop', 'pop','country','classical','rock','dance','edm','electronic'] 
        seedGenres = random.sample(genres, k=5)
        seedGenresStr = ""
        for i in seedGenres:
            seedGenresStr += i + ','
        seedGenresStr = seedGenresStr[0:-1]
        #print(seedGenresStr)
        the_url = "https://api.spotify.com/v1/recommendations?seed_genres={}&limit=50&target_valence={}&min_popularity=50&max_popularity=90&target_popularity=90".format(seedGenresStr, self.sentiment)
        # query_info = {
        #     'seed_genres': seedGenresStr,
        #     'limit': 50,
        #     'target_valence': self.sentiment,
        #     'min_popularity': 60,
        #     'max_popularity': 100,
        #     'target_popularity': 90
        # }
        #recs = requests.get(recom_url, data = query_info, headers={'Authorization': "Bearer " + self.token})
        recs = requests.get(the_url, headers={'Authorization': "Bearer " + self.token})
        response = recs.json()
        tracks = response['tracks']
        track_uris = []
        for track in tracks:
            track_uris.append(track["uri"])
        self.song_list = track_uris
        self.add_music()
        return

    # def search_for_songs(self):
    #     url = 'https://api.spotify.com/v1/search'
    #     header = {'q':self.sentiment, 'type':'track', 'Authorization': self.token}
    #     items = requests.get(url, headers = header)
    #     info = json.loads(items.text)
    #     tracks = info['tracks']
    #     song_list = tracks['items']
    #     return song_list

    def add_music(self):
        music_url = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(self.playlist_id)
        songs = {'uris': self.song_list}
        add = requests.post(music_url, json = songs, headers={'Authorization': "Bearer " + self.token})
        response = add.json()
        snapshot_id = response['snapshot_id']
        return snapshot_id
    
    def final_return(self):
        return self.playlist_url, self.playlist_id

test = spotify(1, 
'BQCk-so_iES8GpRC4RchdUGs2aHfiSdoZt7TOs_En1KGIJipboXyZ4wtRIDJHWU3iFFE8pPYUa03RpUVw2KbA6nLNXPoze3LDkN1fxlGcM_zTn--T6b3t77n5aIxNCIv0PMTe_pBoAMklnLXFjinCOy3tLChFekBcn5n60LqImuq3a0D7uzQz2Y7B7IwV3g-1OisIlAdrFpX_6dtPYMQ7IxIajSOQhqjIQSVLgI6Kv08gVHZ5xWcy5rh2TbSf7Jg-vPUN5nlpkJO2ntzmz-Ue8NR37QisBo3ZpsYa_g1-wfXHaF9XuVFQLW9Uo0LXO8OD4jLqM65THikL00Qs_a7DETgO1i3C91O5sHlnu8XJjChiZtxwH'
, -.97)