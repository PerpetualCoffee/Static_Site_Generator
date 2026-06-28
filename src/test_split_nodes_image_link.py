import unittest
from split_nodes_image import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class test_split_nodes_image_link(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_multiple_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This is text with no images or links", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_no_links(self):
        node = TextNode(
            "This is text with no images or links", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_non_text_node(self):
        node = TextNode("This is a code block", TextType.CODE)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_image_without_text_before(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and only text after", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and only text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_without_text_after(self):
        node = TextNode(
            "This is some text before ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is some text before ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_link_without_text_before(self):
        node = TextNode(
            "[link](https://www.google.com) this is text after", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" this is text after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_without_text_after(self):
        node = TextNode(
            "This is text before [link](https://www.google.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text before ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                            ],
            new_nodes,
        )    

if __name__ == "__main__":
    unittest.main() 