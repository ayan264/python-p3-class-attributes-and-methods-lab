class Song:
    # Class-level variables to track overall stats
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance variables
        self.name = name
        self.artist = artist
        self.genre = genre

        # 1. Increment total song count
        Song.count += 1

        # 2. Add to unique sets of genres and artists
        Song.genres.add(genre)
        Song.artists.add(artist)

        # 3. Update the genre count dictionary
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # 4. Update the artist count dictionary
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            
pass