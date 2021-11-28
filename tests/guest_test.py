import unittest
from src.guest import Guest
class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest(1, 100, "We Are The Champions")
    
    def test_get_wallet(self):
        self.assertEqual(100, self.guest.wallet)
    
    def test_decrease_wallet(self):
        self.guest.decrease_wallet(15)
        self.assertEqual(85, self.guest.wallet)
