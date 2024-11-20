import unittest
import pathlib
from solution import get_answer

class TestCase(unittest.TestCase):
    def test1(self):
        get_answer()
        if not pathlib.Path("./beasts.csv").resolve().is_file():
            raise AssertionError