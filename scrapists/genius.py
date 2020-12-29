import lyricsgenius

# mugavus
genius = None


def get_artist_lyrics(artist, featuring=False, token=None):
    global genius
    if not (token or genius):
        raise RuntimeError('pass token at least once')
    if not genius:
        genius = lyricsgenius.Genius(token, verbose=False)
    artist = artist.lower()
    artist_ = genius.search_artist(artist, include_features=featuring, allow_name_change=False, per_page=50)
    if artist_ is None:
        return None
    for song in artist_.songs:
        song_artist = song.artist.lower()
        if not (song_artist == artist or featuring):
            continue
        yield song_artist, song.title.strip().lower(), song.lyrics





