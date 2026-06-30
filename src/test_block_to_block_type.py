import unittest
from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        test_cases = [
            ("This is a paragraph.", BlockType.PARAGRAPH),
            ("# Heading 1", BlockType.HEADING),
            ("## Heading 2", BlockType.HEADING),
            ("### Heading 3", BlockType.HEADING),
            ("#### Heading 4", BlockType.HEADING),
            ("##### Heading 5", BlockType.HEADING),
            ("###### Heading 6", BlockType.HEADING),
            ("> This is a quote.\n> Another line of the quote.", BlockType.QUOTE),
            ("- Item 1\n- Item 2\n- Item 3", BlockType.UNORDERED_LIST),
            ("1. First item\n2. Second item\n3. Third item", BlockType.ORDERED_LIST),
            ("```\nCode block\n```", BlockType.CODE)
        ]

        for block, expected_type in test_cases:
            with self.subTest(block=block):
                self.assertEqual(block_to_block_type(block), expected_type)
    
    def test_no_spaces_after_heading(self):
        block = "#Heading without space"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)
    
    def test_too_many_hashes_for_heading(self):
        block = "####### Too many hashes"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_ordered_list_not_an_ordered_list(self):
        block = "1. First item\n3. third item"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)

    def test_not_a_quote(self):
        block = "> quote line\nNot a quote line"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)
    
    def test_not_an_unordered_list(self):
        block = "- Item 1\n* Item 2"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)
    
    def test_not_a_code_block_without_closing(self):
        block = "```\nCode block without closing"
        expected_type = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected_type)


if __name__ == "__main__":
    unittest.main()