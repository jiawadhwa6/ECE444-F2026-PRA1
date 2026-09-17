import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.util = utils()

    def test_reversed_string(self):
        self.assertEqual(self.util.reversed("1234"), 4321)

    def test_reversed_float(self):
        self.assertEqual(self.util.reversed(1234.0), 4321)

    def test_reversed_integer(self):
        self.assertEqual(self.util.reversed(1234), 4321)

    def test_formatter_string(self):
        self.assertEqual(self.util.formatter("10"), ("0b1010", "0o12"))

    def test_formatter_float(self):
        self.assertEqual(self.util.formatter(10.0), ("0b1010", "0o12"))

    def test_formatter_integer(self):
        self.assertEqual(self.util.formatter(10), ("0b1010", "0o12"))


if __name__ == "__main__":
    unittest.main()