import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_with_only_whitespace(self):
        md = "   \n\n  \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_with_leading_and_trailing_whitespace(self):
        md = "   \n\nThis is a paragraph with leading and trailing whitespace\n\n  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph with leading and trailing whitespace"])

    def test_markdown_to_blocks_with_multiple_consecutive_blank_lines(self):
        md = "This is a paragraph\n\n\n\nThis is another paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph", "This is another paragraph"])

    def test_markdown_to_blocks_with_only_blank_lines(self):
        md = "\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

     
if __name__ == "__main__":
    unittest.main()