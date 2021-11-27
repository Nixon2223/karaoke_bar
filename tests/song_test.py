import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("We Are The Champions", "Queen")
    
    def test_get_name(self):
        self.assertEqual("We Are The Champions", self.song.name)

    def test_get_artist(self):
        self.assertEqual("Queen", self.song.artist)