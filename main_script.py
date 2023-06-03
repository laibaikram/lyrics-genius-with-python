import lyricsgenius

def fetch_lyrics(artist, title):
    # Specify your Genius API access token here
    access_token = "YOUR_ACCESS_TOKEN"
    
    genius = lyricsgenius.Genius(access_token)
    song = genius.search_song(title, artist)
    
    if song is not None:
        lyrics = song.lyrics
        return lyrics
    else:
        return None

def main():
    artist = input("Enter the artist name: ")
    title = input("Enter the song title: ")
    
    lyrics = fetch_lyrics(artist, title)
    
    if lyrics:
        print(f"\nLyrics for '{title}' by {artist}:\n")
        print(lyrics)
    else:
        print(f"\nFailed to fetch lyrics for '{title}' by {artist}.")

if __name__ == '__main__':
    main()
