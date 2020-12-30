import lyricsgenius
from pprint import pp

# mugavus
genius = None


def get_artist_lyrics(artist, featuring=False, token=None):
    global genius
    if not (token or genius):
        raise RuntimeError('pass token at least once')
    if not genius:
        genius = lyricsgenius.Genius(token, verbose=False)
    artist = artist.lower()
    artist_id = None
    search = genius.search_all(artist)
    for item in search['sections']:
        if item['type'] == 'artist':
            for sub_item in item['hits']:
                if sub_item['result']['name'].lower() == artist:
                    artist_id = sub_item['result']['id']
                    break
        if artist_id:
            break
    else:
        return None

    artist_ = genius.search_artist(None, artist_id=artist_id, include_features=featuring,
                                   allow_name_change=False, per_page=50)
    for song in artist_.songs:
        song_artist = song.artist.lower()
        if not (song_artist == artist or featuring):
            continue
        yield song_artist, song.title.strip().lower(), song.lyrics

