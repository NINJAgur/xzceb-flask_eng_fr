import unittest
from  translator import french_to_english
from  translator import english_to_french

class TestF2E(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Matin'), 'Morning')
    def test_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_none(self):
        self.assertNotEqual(french_to_english('None'),'')

class TestE2F(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Morning'), 'Matin')
    def test_bonjour(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_none(self):
        self.assertNotEqual(english_to_french('None'),'')

unittest.main()