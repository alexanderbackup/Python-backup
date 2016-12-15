from copy import deepcopy
from random import randint
import json
import os.path


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length


    def __str__(self):
        return "{0} - {1} from {2} - {3}".format(self.artist,
                                                 self.title,
                                                 self.album,
                                                 self._length)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(str(self))

    def length(self, seconds=False, minutes=False, hours=False):
        result = 0
        _time = self._length.split(':')
        result += int(_time[-1])
        result += int(_time[-2])*60
        if len(_time) == 3:
            result += int(_time[0])*3600
        if seconds:
            return str(result)
        if minutes:
            return str(round(result/60, 2))
        if hours:
            return str(round(result/3600, 2))
        return self._length


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.song_list = []
        self.played_songs = []

    def add_song(self, song):
        self.song_list.append(song)

    def remove_song(self, song):
        if song in self.song_list:
            self.song_list.remove(song)
            return True
        return False

    def add_songs(self, songs):
        for i in songs:
            self.song_list.append(i)

    def total_length(self):
        seconds = sum(int(song.length(seconds=True)) 
                          for song in self.song_list)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        if h == 0:
            return '{0}:{1}'.format(m ,s)
        return '{0}:{1}:{2}'.format(h, m ,s)

    def artists(self):
        if not self.song_list:
            return False
        result = {}
        for song in self.song_list:
            if song.artist not in result:
                result[song.artist] = 1
            else:
                result[song.artist] += 1
        return result

    def next_song(self):
        if self.song_list == [] and self.played_songs == []:
            return False
        if self.song_list == [] and not self.repeat:
            return False
        if self.song_list == [] and self.repeat:
            self.song_list = deepcopy(self.played_songs)
            self.played_songs = []
        if self.shuffle:
            random_song = self.song_list[randint(0, 
                                                len(self.song_list)-1)]
            self.song_list.remove(random_song)
            self.played_songs.append(random_song)
            return random_song
        next_song = self.song_list[0]
        self.song_list.remove(next_song)
        self.played_songs.append(next_song)
        return next_song

    def pprint_playlist(self):
        pp_playlist = self.played_songs + self.song_list
        if not pp_playlist:
            return False
        artist_col = 0
        song_col = 0
        length_col = 0
        for song in pp_playlist:
            if len(song.artist) > artist_col:
                artist_col = len(song.artist)
            if len(song.title) > song_col:
                song_col = len(song.title)
            if len(song._length) > length_col:
                length_col = len(song._length)
        if length_col < 6:
            length_col = 6
        result = []
        artist_row = '| ' + 'Artist'+(' '*(artist_col-6)) + ' |'
        song_row = ' Song' + (' '*(song_col-3))
        length_row = '| ' + 'Length'+(' '*(length_col-6)) + ' |'
        result.append(artist_row + song_row + length_row)
        second_row = '| ' + '-'*artist_col + ' | ' +'-'*song_col + ' | ' + '-'*length_col + ' |'
        result.append(second_row)
        for song in pp_playlist:
            artist_row = '| ' + song.artist+(' '*(artist_col-len(song.artist))) + ' | '
            song_row = song.title + (' '*(song_col-len(song.title)))
            length_row = ' | ' + song._length+(' '*(length_col-len(song._length))) + ' |'
            result.append(artist_row + song_row + length_row)
        return result


    def save(self):
        if self.name == ' ' or self.name == '':
            self.name = '-'
        fname = self.name + '.json'
        if os.path.isfile(fname):
            print('File with this name already exist!')
            while True:
                answer = input('Do you want to rewrite file?')
                if answer == 'y' or answer == 'yes':
                    break
                elif answer == 'n' or answer == 'no':
                    return False
                else:
                    print('Invalid command!\nTry lowercase')
        with open(fname, 'w') as f:
            json.dump(self, f, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        return True

    @staticmethod
    def load(path):
        if not os.path.isfile(path):
            print('No playlist with this name!')
            return False
        with open(path) as f:
            load_pl = json.load(f) # TODO: check for valid json!
            assert isinstance(load_pl, dict)
        new_pl = Playlist(load_pl['name'], 
                          load_pl['repeat'], 
                          load_pl['shuffle'])
        for s in load_pl['song_list']:
            new_song = Song(s['title'], 
                            s['artist'], 
                            s['album'], 
                            s['_length'])
            new_pl.song_list.append(new_song)
        for s in load_pl['played_songs']:
            new_song = Song(s['title'], 
                            s['artist'], 
                            s['album'], 
                            s['_length'])
            new_pl.played_songs.append(new_song)
        return new_pl

    def generate_playlist(self):
        pass














# from library import *
s1 = Song(title="Odin", 
          artist="Manowar", 
          album="The Sons of Odin", 
          length="3:44")
s2 = Song(title="Thor", 
          artist="Manowar", 
          album="The Sons of Odin", 
          length="1:14:32")
s3 = Song(title="Habibi", 
          artist="Azis", 
          album="Napipai gooo", 
          length="5:16")
pl = Playlist(name="Code", repeat=True, shuffle=True)
pl.add_songs([s1,s2,s3])
#for i in pl.pprint_playlist():
#    print(i)
