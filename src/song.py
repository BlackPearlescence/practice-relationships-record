from record import Record
from artist import Artist

class Song(Record):
    def __init__(self,title:str,runtime:int,genre:str):
        self._title = title
        self._runtime = runtime
        self._genre = genre
        self._record = Record("Default","Default Artist",200)
        self._artist = Artist("Default Artist")

    def get_title(self) -> str:
        return self._title.title()
    def set_title(self,title:str):
        self._title = title
    def get_runtime(self) -> int:
        return self._runtime
    def set_runtime(self,runtime:int):
        self._runtime = runtime
    def get_genre(self) -> str:
        return self._genre
    def set_genre(self,genre:str):
        self._genre = genre
    def get_record(self) -> Record:
        return self._record
    def set_record(self,record:Record):
        self._record = record
    def get_artist(self) -> Artist:
        return self._artist

    title = property(get_title,set_title)
    runtime = property(get_runtime,set_runtime)
    genre = property(get_genre,set_genre)
    record = property(get_record,set_record)

artist = Artist("Boosie")
record1 = Record("Boosie's Song 1","Boosie",1999)
record2 = Record("Boosie's Song 2","Booise",1993)
artist.records.append(record1)
artist.records.append(record2)
song = Song('You Oughta Know', 120, 'rock')
song.record = record1
print(record1)
print(song.get_record())