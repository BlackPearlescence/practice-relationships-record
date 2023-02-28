from artist import Artist
from record import Record
from song import Song


def test_record_init_with_title_artist_year():
    """
    Should be able to initialize a record object
    with a title, artist, and year
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('Jagged Little Pill', alanis, 1995)
    assert record.title == 'Jagged Little Pill'
    assert record.artist == alanis
    assert record.year == 1995

def test_record_get_title():
    """
    get_title() should return the record's title
    in title-case
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    assert record.get_title() == 'Jagged Little Pill'

def test_record_get_artist():
    """
    get_artist() should return the artist object
    associated with the record
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    assert record.get_artist() == alanis

def test_record_get_year():
    """
    get_year() should return the record's year
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    assert record.get_year() == 1995

def test_record_get_songs():
    """
    get_songs() should return the list of Song objects
    associated with the record
    """
    s1 = Song('You Oughta Know', 120, 'rock')
    s2 = Song('Hand in My Pocket', 115, 'rock')
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    record.songs = [s1, s2]
    assert record.get_songs() == [s1, s2]

def test_record_total_runtime():
    """
    total_runtime() should return the total runtime
    of all songs on the record
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    s1 = Song('You Oughta Know', 120, 'rock')
    s2 = Song('Hand in My Pocket', 115, 'rock')
    record.songs = [s1, s2]
    assert record.total_runtime() == 120+115

def test_record_has_song():
    """
    has_song(song) should return True if the song
    object exists in the record, False otherwise
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    s1 = Song('You Oughta Know', 120, 'rock')
    s2 = Song('Hand in My Pocket', 115, 'rock')
    record.songs = [s1, s2]
    assert record.has_song(s1) == True
    # Did not have enough arguments
    assert record.has_song(Song('Blah Blah',220,'Complicated')) == False

def test_record_get_longest_song():
    """
    get_longest_song() should return the song object
    with the longest runtime
    """
    alanis = Artist('Alanis Morrisette')
    record = Record('jagged little pill', alanis, 1995)
    s1 = Song('You Oughta Know', 120, 'rock')
    s2 = Song('Hand in My Pocket', 115, 'rock')
    record.songs = [s1, s2]
    assert record.get_longest_song() == s1
