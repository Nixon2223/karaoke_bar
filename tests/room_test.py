import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 100)
        self.guest1 = Guest(1, 100, "We Are The Champions")
        self.guest2 = Guest(2, 50, "Song 2")
        self.song1 = Song("We Are The Champions", "Queen")
        self.room.guests = [self.guest1]
    
    def test_get__number(self):
        self.assertEqual(1, self.room.number)
    
    def test_get_capacity(self):
        self.assertEqual(100, self.room.capacity)
    
    def test_check_guest_count(self):
        self.assertEqual(1, self.room.guest_count())
    
    def test_add_guest(self):
        self.room.add_guest(self.guest2)
        self.assertEqual(2, self.room.guest_count())
    
    def test_remove_guest(self):
        self.room.remove_guest(1)
        self.assertEqual(0, self.room.guest_count())
    
    def test_add_song(self):
        self.room.add_song(self.song1)
        self.assertEqual(1, len(self.room.songs))