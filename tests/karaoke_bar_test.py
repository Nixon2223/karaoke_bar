import unittest

from src.karaoke_bar import Karaoke_Bar
from src.room import Room
from src.guest import Guest

class TestKaraoke_Bar(unittest.TestCase):

    def setUp(self):
        self.karaoke_bar = Karaoke_Bar("Velvet Palace", 15)
        self.guest1 = Guest(1, 100, "We Are The Champions")
        self.guest2 = Guest(2, 50, "Song 2")
        self.room1 = Room(1, 100)
        self.room2 = Room(2, 75)
        self.karaoke_bar.rooms = [self.room1, self.room2]
    
    def test_get_name(self):
        self.assertEqual("Velvet Palace", self.karaoke_bar.name)
    
    def test_get_entry(self):
        self.assertEqual(15, self.karaoke_bar.entry_fee)
    
    def test_sell_entry(self):
        self.karaoke_bar.sell_entry(self.guest2, self.room1)
        self.assertEqual(35, self.guest2.wallet)
        self.assertEqual(1, self.room1.guest_count())