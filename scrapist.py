from scrapists import *
import pickle
from configparser import ConfigParser

creds = ConfigParser()
creds.read('creds.cfg')

artists = pickle.load(open('artists/artists_all.bin', 'rb'))
data = []
songs_per_artist = {}

i = 0
for artist in artists:
    print(f'\rGENIUS - {i:>3}/{len(artists)} - {artist}', end='')
    got_songs = False
    attempts = 3
    while attempts:
        try:
            for artist_, title, lyrics in genius.get_artist_lyrics(artist, True, creds['GENIUS']['client_access_token']):
                data.append({'artist': artist_, 'title': title, 'lyrics': lyrics})
                songs_per_artist.setdefault(artist_, set()).add(title)
                got_songs = True
            if not got_songs:
                print(f'\rGENIUS - NO SONGS FOR {artist}')
            break
        except:
            attempts -= 1
    else:
        print(f'\rGENIUS - ERROR FOR {artist}')
    i += 1


with open('genius.bin', 'wb') as f, open('genius_songs_per_artist.bin', 'wb') as f2:
    pickle.dump(data, f)
    pickle.dump(songs_per_artist, f2)


data = []
songs_per_artist = {}
i = 0
for artist in artists:
    print(f'\rSASS - {i:>3}/{len(artists)} - {artist}', end='')
    got_songs = False
    for artist_, title, lyrics in sasslantis.get_artist_lyrics(artist, True):
        data.append({'artist': artist_, 'title': title, 'lyrics': lyrics})
        songs_per_artist.setdefault(artist_, set()).add(title)
        got_songs = True
    if not got_songs:
        print(f'\rSASS - NO SONGS FOR {artist}')
    i += 1

with open('sass.bin', 'wb') as f, open('sass_songs_per_artist.bin', 'wb') as f2:
    pickle.dump(data, f)
    pickle.dump(songs_per_artist, f2)