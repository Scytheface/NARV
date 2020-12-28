from configparser import ConfigParser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pp
from collections import deque, Counter
from statistics import stdev
import pickle

creds = ConfigParser()
creds.read("creds.cfg")
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=creds["SPOTIFY"]["client_id"],
                                                                client_secret=creds["SPOTIFY"]["client_secret"]))

all_artists = set()
ids = set()
playlists = deque(("2T6QOAFqbQslxu5xFw3wvT", "6XdW7adQLpt3o3gIJqE9XW", "3Ze6mOt54Tt05N7KSx5U3e",
                   "4Hl7I993RZcZnCxbbB9PCU", "3bNPCk6BqPpa10at5kl2OT", "6eiae5jkrKi5Qtx06UfBuU",
                   "44aQtJKhU4Sv3YYKN3uAFz", "0RmMfOHyNeFsx1fupSakRU", "36dWQuqEmzfaxw1CIaUHSw",
                   "7mFoQ7GTjaSxQlvWxqpzTw"))

while playlists:
    playlist = spotify.playlist(playlists.popleft())['tracks']
    while playlist:
        artists = [artist for item in playlist['items'] for artist in item['track']['artists'] if artist['name']]
        ids.update(artist['id'] for artist in artists)
        all_artists.update(artist['name'] for artist in artists)
        playlist = spotify.next(playlist)
        break

related_artists = set()
for _ in range(5):
    related = Counter()
    for artist_id in ids:
        try:
            for related_artist in spotify.artist_related_artists(artist_id)['artists']:
                related[(related_artist['name'], related_artist['id'])] += 1
        except AttributeError:
            pass    # arusaamatu teegisisene viga
    limit = sum(related.values())/len(related) + stdev(related.values())
    related = [artist for artist in related
               if related[artist] > limit and artist[0] not in all_artists]
    related_artists.update(artist[0] for artist in related)
    ids = set(artist[1] for artist in related)

print(all_artists)
print(related_artists)
print(len(all_artists))
print(len(related_artists))
with open('artists/artists.bin', 'wb') as af, open('artists/related.bin', 'wb') as rf:
    pickle.dump(all_artists, af)
    pickle.dump(related_artists, rf)