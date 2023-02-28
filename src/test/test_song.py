from artist import Artist
from record import Record
from song import Song


def test_song_init_title_runtime_genre():
    """
    Should be able to initialize a new song object
    with a title, runtime, and genre
    """
    song = Song('You Oughta Know', 120, 'rock')
    assert song.title == 'You Oughta Know'
    assert song.runtime == 120
    assert song.genre == 'rock'

def test_song_get_title():
    """
    get_title() should return the title of the song
    in title-case
    """
    song = Song('you oughta know', 120, 'rock')
    assert song.get_title() == 'You Oughta Know'

def test_song_get_runtime():
    """
    get_runtime() should return the runtime of
    the song
    """
    # Changed from "You Oughta Know" to 120
    # because it is trying to test for runtime
    # rather than Title
    song = Song('You Oughta Know', 120, 'rock')
    assert song.get_runtime() == 120

    # Corrected from get_gengre() to get_genre()
def test_song_get_genre():
    """
    get_genre() should return the genre of the song
    """
    song = Song('You Oughta Know', 120, 'rock')
    assert song.get_genre() == 'rock'

def test_song_get_record():
    """
    get_record() should return the record object
    associated with the song
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    song = Song('You Oughta Know', 120, 'rock')
    song.record = record
    assert song.get_record() == record

def test_song_get_artist():
    """
    get_artist() should return the artist object
    associated with the song's record object
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    song = Song('You Oughta Know', 120, 'rock')
    song.artist = alanis
    assert song.get_artist() == alanis
