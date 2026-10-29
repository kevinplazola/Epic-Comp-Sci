class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_total_duration(self):
        total_seconds = sum(song.duration for song in self.songs)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"{minutes}:{seconds:02d}")
        return f"{minutes}:{seconds:02d}"

    def find_by_artist(self, artist_name):
        found_songs = [song for song in self.songs if song.artist == artist_name]
        if found_songs:
            for song in found_songs:
                print(f"{song.title} by {song.artist}")
        else:
            print(f"No songs found by {artist_name}")

    def print_playlist(self):
        for song in self.songs:
            print(f"{song.title} by {song.artist}")

    def load_songs(self, filename):
        self.filename = filename
        with open(self.filename, "r") as f:
            for line in f:
                title, artist, duration = line.strip().split(',')
                self.add_song(Song(title, artist, int(duration)))

def main():
    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")

if __name__ == '__main__':
    main()