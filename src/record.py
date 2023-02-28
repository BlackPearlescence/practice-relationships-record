from artist import Artist
from functools import reduce

class Record(Artist):
    def __init__(self,title:str,artist:Artist,year:int):
        self._title = title
        self._artist = artist
        self._year = year
        self._songs = []
    
    def get_title(self) -> str:
        return self._title.title()
    def set_title(self,title:str):
        self._title = title
    def get_artist(self) -> Artist:
        return self._artist
    def set_artist(self,artist:Artist):
        self._artist = artist
    def get_year(self) -> int:
        return self._year
    def set_year(self,year:int):
        self._year = year
    def get_songs(self) -> list:
        return self._songs
    def set_songs(self,songs:list):
        self._songs = songs
    def total_runtime(self) -> int:
        total = reduce(lambda a,b:a+b,[song.runtime for song in self._songs])
        return total
    def has_song(self,song) -> bool:
        if(self._songs.count(song) == 0):
            return False
        else:
            return True
    def get_longest_song(self):
        return max(self._songs,key=lambda song:song.runtime)

    title = property(get_title,set_title)
    artist = property(get_artist,set_artist)
    year = property(get_year,set_year)
    songs = property(get_songs,set_songs)

