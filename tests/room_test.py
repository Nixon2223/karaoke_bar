import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 100)
        self.guest1 = Guest(100, "We Are The Champions")
    
    def test_get__number(self):
        self.assertEqual(1, self.room.number)
    
    def test_get_capacity(self):
        self.assertEqual(100, self.room.capacity)
    
    def test_check_guest_count(self):
        self.assertEqual(0, self.room.guest_count())
    
    def test_add_guest(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(1, self.room.guest_count())