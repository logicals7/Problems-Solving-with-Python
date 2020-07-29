def tracklist(**tracks):
    for artist, album_and_song in tracks.items():
        print(artist)
        for album, track in album_and_song.items():
            print("ALBUM:", album, "TRACK:", track)
