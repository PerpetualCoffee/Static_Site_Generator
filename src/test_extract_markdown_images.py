import unittest, re
from extract_markdown_images import extract_markdown_images, extract_markdown_links

class test_extract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)


    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![cat](https://cat.com/cat.png) and ![dog](https://dog.com/dog.png)"
        )
        self.assertListEqual(
            [("cat", "https://cat.com/cat.png"), ("dog", "https://dog.com/dog.png")],
            matches,
        )

    def test_extract_markdown_images_none(self):
        matches = extract_markdown_images("No images here at all")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_ignores_images(self):
        matches = extract_markdown_links(
            "![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_links_mixed_content(self):
        matches = extract_markdown_links(
            "Here is a [link](https://boot.dev) and an ![image](https://img.com/a.png)"
        )
        self.assertListEqual([("link", "https://boot.dev")], matches)    

if __name__ == "__main__":
    unittest.main()