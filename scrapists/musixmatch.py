import requests

print(requests.get('https://www.musixmatch.com/search/nublu/artists', headers={'user-agent': 'real browser i promise'}).content)

