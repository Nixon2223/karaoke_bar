import unittest

from src.karaoke_bar import Karaoke_Bar

class TestKaraoke_Bar(unittest.TestCase):

    def setUp(self):
        self.karaoke_bar = Karaoke_Bar("Velvet Palace", 15)
    
    def test_get_name(self):
        self.assertEqual("Velvet Palace", self.karaoke_bar.name)
    
    def test_get_entry(self):
        self.assertEqual(15, self.karaoke_bar.entry_fee)