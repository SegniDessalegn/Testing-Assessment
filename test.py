import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(to_upper('test text'), 'TEST TEXT')
        self.assertEqual(to_upper('TEST TEXT'), 'TEST TEXT')

class TestToLower(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(to_lower('TEST TEXT'), 'test text')
        self.assertEqual(to_lower('Test text'), 'test text')

class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        self.assertEqual(capitalize('test text'), 'Test text')
        self.assertEqual(capitalize('Test text'), 'Test text')
        self.assertEqual(capitalize('Test Text'), 'Test text')


if __name__ == '__main__':
    unittest.main()
