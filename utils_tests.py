import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.util = utils()

    # ---------- reversed() ----------

    def test_reversed_integer(self):
        self.assertEqual(self.util.reversed(1234), 4321)

    def test_reversed_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.util.reversed("1234")

    def test_reversed_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.util.reversed(1234.0)

    # ---------- formatter() ----------

    def test_formatter_integer(self):
        self.assertEqual(self.util.formatter(10), ("0b1010", "0o12"))

    def test_formatter_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.util.formatter("10")

    def test_formatter_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.util.formatter(10.0)


if __name__ == "__main__":
    unittest.main()