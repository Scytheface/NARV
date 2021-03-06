import bs4
import requests


def get_artist_lyrics(artist, featuring=False):
    resp = requests.get("https://sasslantis.ee/search.php", params={'q': artist})
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    for result in soup.find('div', class_='col-md-12').find_all('div', class_='row'):
        song_artist = result.find('h4').a.text.split('-')[0].strip().lower()
        if not featuring and artist.lower() != song_artist:
            continue
        lyrics_page = requests.get(f"https://sasslantis.ee/{result.find('a')['href']}")
        container = bs4.BeautifulSoup(lyrics_page.text, 'lxml').find('div', class_='col-md-8')

        song_title = container.find('a').next.next
        song_lyrics = '\n'.join(s.strip() for s in container.find("h1").find_next_siblings(text=True))

        song_artist = song_artist.strip().lower()
        song_title = song_title.replace('-', '').strip().lower()
        yield song_artist, song_title, song_lyrics


if __name__ == '__main__':
    print(*get_artist_lyrics('nublu'), sep='\n\n\n')