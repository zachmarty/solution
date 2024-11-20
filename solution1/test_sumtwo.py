import unittest
from solution import sum_two

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_two(1, 2), 3)
    
    def test2(self):
        self.assertRaises(TypeError, sum_two, 1, 2.4)