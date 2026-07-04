import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title\n\nThis is some content."
        expected_title = "This is a title"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_extract_title_with_whitespace(self):
        markdown = "   #   This is a title with whitespace   \n\nThis is some content."
        expected_title = "This is a title with whitespace"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_extract_title_no_title(self):
        markdown = "This is some content without a title."
        self.assertIsNone(extract_title(markdown))


if __name__ == '__main__':
    unittest.main()