import unittest
from gencontent import extract_title

class TestExample(unittest.TestCase):
    def test_something(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("текст без заголовка")

if __name__ == "__main__":
    unittest.main()
