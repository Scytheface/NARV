import bs4
import requests


def search(artist):
    resp = requests.get("https://sasslantis.ee/search.php", params={'q': artist})
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    for result in soup.find('div', class_='col-md-12').find_all('div', class_='row'):
        lyrics_page = requests.get(f"https://sasslantis.ee/{result.find('a')['href']}")
        container = bs4.BeautifulSoup(lyrics_page.text, 'lxml').find('div', class_='col-md-8')
        song_artist = container.find('a').next
        song_title = song_artist.next
        song_lyrics = '\n'.join(s.strip() for s in container.find("h1").find_next_siblings(text=True))

        song_artist = song_artist.strip().lower()
        song_title = song_title.replace('-', '').strip().lower()
        yield song_artist, song_title, song_lyrics


if __name__ == '__main__':
    print(*search('nublu'), sep='\n\n\n')