import os
import unittest
from shutil import copyfile
from library import Song, Playlist


class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song(title="Odin", 
                         artist="Manowar", 
                         album="The Sons of Odin", 
                         length="3:44")
        self.second_song = Song(title="Odin", 
                                artist="Manowar", 
                                album="The Sons of Odin", 
                                length="3:44")
        self.better_song = Song(title="Habibi", 
                                artist="Azis", 
                                album="Napipai gooo", 
                                length="5:16")

    def test__str__(self):
        self.assertEqual(str(self.song), 
                         "Manowar - Odin from The Sons of Odin - 3:44")

    def test__eq__(self):
        self.assertTrue(self.song==self.second_song)
        self.assertFalse(self.song==self.better_song)

    def test__hash__(self):
        self.assertTrue(self.song.__hash__() == self.second_song.__hash__())
        self.assertFalse(self.song.__hash__() == self.better_song.__hash__())

    def test_length(self):
        self.assertEqual(self.song.length(seconds=True), '224')
        self.assertEqual(self.song.length(minutes=True), '3.73')
        self.assertEqual(self.song.length(hours=True), '0.06')
        self.assertEqual(self.song.length(), self.song._length)


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist(name="Code", repeat=True, shuffle=True)
        # Song instances:
        self.song = Song(title="Odin", 
                         artist="Manowar", 
                         album="The Sons of Odin", 
                         length="3:44")
        self.second_song = Song(title="Thor", 
                                artist="Manowar", 
                                album="The Sons of Odin", 
                                length="4:32")
        self.better_song = Song(title="Habibi", 
                                artist="Azis", 
                                album="Napipai gooo", 
                                length="5:16")
        
    def test_add_song(self):
        self.assertEqual(len(self.playlist.song_list), 0)
        self.playlist.add_song(self.song)
        self.assertEqual(len(self.playlist.song_list), 1)

    def test_remove_song(self):
        self.playlist.song_list = [self.song, 
                                   self.second_song, 
                                   self.better_song]
        self.assertEqual(len(self.playlist.song_list), 3)
        self.assertTrue(self.playlist.remove_song(self.song))    
        self.assertEqual(len(self.playlist.song_list), 2)
        self.assertFalse(self.playlist.remove_song(self.song))
        self.assertTrue(self.playlist.remove_song(self.second_song))
        self.assertTrue(self.playlist.remove_song(self.better_song))    
        self.assertEqual(len(self.playlist.song_list), 0)
        
    def test_add_songs(self):
        self.assertEqual(len(self.playlist.song_list), 0)
        self.playlist.add_songs([self.song, 
                                 self.second_song, 
                                 self.better_song])
        self.assertEqual(len(self.playlist.song_list), 3)

    def test_total_length(self):
        self.playlist.add_songs([self.song, 
                                 self.second_song, 
                                 self.better_song])
        self.assertEqual(self.playlist.total_length(), '13:32')

    def test_artists(self):
        self.assertFalse(self.playlist.artists())
        self.playlist.add_songs([self.song, 
                                 self.second_song, 
                                 self.better_song])
        self.assertEqual(self.playlist.artists(), 
                         {'Manowar': 2, 'Azis': 1})

    def test_next_song(self):
        self.assertEqual(self.playlist.next_song(), False)
        self.playlist.add_songs([self.song, 
                                 self.second_song, 
                                 self.better_song])
        self.playlist.repeat = False
        self.playlist.shuffle = False
        self.playlist.next_song()
        self.assertEqual(len(self.playlist.song_list), 2)
        self.assertEqual(len(self.playlist.played_songs), 1)
        self.playlist.next_song()
        self.playlist.next_song()
        self.assertEqual(len(self.playlist.song_list), 0)
        self.assertEqual(len(self.playlist.played_songs), 3)
        self.assertFalse(self.playlist.next_song())
        self.playlist.repeat = True
        self.playlist.next_song()
        self.assertEqual(len(self.playlist.song_list), 2)
        self.assertEqual(len(self.playlist.played_songs), 1)
        self.playlist.shuffle = True # TODO: implement randomness
        self.playlist.next_song()
        self.assertEqual(len(self.playlist.song_list), 1)
        self.assertEqual(len(self.playlist.played_songs), 2)
        self.playlist.next_song()
        self.assertEqual(len(self.playlist.song_list), 0)
        self.assertEqual(len(self.playlist.played_songs), 3)
        self.playlist.repeat = False
        self.assertFalse(self.playlist.next_song())
        
    def test_pprint_playlist(self):
        self.assertFalse(self.playlist.pprint_playlist())
        self.playlist.add_songs([self.song, 
                                 self.second_song])
        self.assertEqual(self.playlist.pprint_playlist(),
                         ['| Artist  | Song | Length |',
                          '| ------- | ---- | ------ |',
                          '| Manowar | Odin | 3:44   |',
                          '| Manowar | Thor | 4:32   |'])

    def test_save(self):
        self.playlist.name = ' '
        self.playlist.save()
        self.assertEqual(self.playlist.name, '-')
        os.remove('-.json')
        self.playlist.name = "TestCode"
        self.assertTrue(self.playlist.save())
        self.assertTrue(os.path.isfile('TestCode.json'))
        os.remove('TestCode.json')
        

    def test_load(self):
        self.assertFalse(Playlist.load('wrong.json'))
        copyfile('Code.json', 'test_code.json')
        new = Playlist.load('test_code.json')
        self.assertEqual(len(new.song_list), 3)
        os.remove('test_code.json')


if __name__ == '__main__':
    unittest.main()
