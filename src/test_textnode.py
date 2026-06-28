import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_noteq(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		node2 = TextNode("This is not a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_noteq_url(self):
		node = TextNode("this is a url", TextType.BOLD, None)
		node2 = TextNode("this is a url", TextType.BOLD, "https://www.google.com")
		self.assertNotEqual(node, node2)

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
	
	def test_bold(self):
		node = TextNode("This is bold", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is bold")

	def test_italic(self):
		node = TextNode("This is italic", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is italic")

	def test_code(self):
		node = TextNode("print('hello')", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "print('hello')")

	def test_link(self):
		node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "Boot.dev")
		self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

	def test_image(self):
		node = TextNode("A cute bear", TextType.IMAGE, "https://www.boot.dev/bear.png")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(
			html_node.props,
			{"src": "https://www.boot.dev/bear.png", "alt": "A cute bear"},
		)


if __name__ == "__main__":
    unittest.main()
