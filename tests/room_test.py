import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 100)
    
    def test_get__number(self):
        self.assertEqual(1, self.room.number)
    
    def test_get_capacity(self):
        self.assertEqual(100, self.room.capacity)