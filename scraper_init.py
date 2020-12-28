from configparser import ConfigParser
import lyricsgenius

creds = ConfigParser()
creds.read('creds.cfg')

genius = lyricsgenius.Genius(creds['GENIUS']['client_access_token'])

artists = [
    "Sipelga 14",
    "Nublu",
    "Arop",
    "Suur Papa",
    "Jung Abso",
    "POI$T€KOOR",
    "Angaar",
    "Reket",
    "Mick Moon",
    "Beebilõust",
    "bad art",
    "tigran",
    "5miinust",
    "Hoax [EST]",
    "lil till",
    "EUTANAA$IA",
    "Väike PD",
    "YUNG $EMPER",
    "Clicherik & Mäx",
    "Clicherik",
    "Marp$",
    "ROM [EST]",
    "HVNS [EE]",
    "KUNERIK",
    "KiROT",
    "Leis",
    "GODJAKO",
    "Noormeek",
    "Kriipsu-Uku",
    "Raha.pesu.karud",
    "Säm x Kaw",
    "Maleva",
    "Nuuskmõmmik",
    "AR€NG",
    "MänguPoi$$ Käru",
    "Pluuto",
    "@villemdrillem",
    "Utoopia",
    "Seaduskuulekus",
    "Thot Patrol",
    "Väike Kelder",
    "MÕMMI",
    "CKELETOV",
    "Sammalhabe",
    "Tussuvagun",
    "Niiduk",
    "Denu$ion",
    "OkeiOkei",
    "Heleza",
    "Pitsa",
    "VakstuLelle",
    "GAMEBOY TETRIS",
    "Genka",
    "12EEK MONKEY",
    "Hanf Kung",
    "AZMA",
    "PIIR",
    "Lepa$te",
    "Robert Lõvi",
    "Kozinak",
    "Manipulated Mindz",
    "EiK",
    "Küberünnak & Karmo",
    "Maian",
    "Öed (Tuuli Rand ja Kristel Aaslaid)",
    "Maxtract",
    "Jaanus Saks",
    "NOORYUKI",
    "LilEedik",
    "Makaagid",
    "372Kaspar",
    "97thghts",
    "VK (Estonia)",
    "DVPH",
    "5loops",
    "Metsakutsu"
]

lyrics = []
song_counter = 0

for artist in artists:
    artist = genius.search_artist(artist, include_features=True)
    print("=================================")
    print(artist.name)
    print()
    for song in artist.songs:
        song_counter += 1
        try:
            name = str(song).split("\', \'")[0][1:].split("\" by")[0]  # TODO: fix later
            lyrics.append({"artist": artist.name, "name": name, "lyrics": song.lyrics})
        except:
            continue

# for lyric in lyrics:
#	print()
#	print(lyric)
#	print()

print()
print(song_counter)

with open("tulemus.py", "w", encoding="UTF8") as f:
    f.write("sisu = " + str(lyrics))
