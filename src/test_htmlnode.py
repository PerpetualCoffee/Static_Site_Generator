import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNODE(unittest.TestCase):
        def test_props_to_html(self):
                node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
                self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        def test_constructor(self):
                node = HTMLNode(tag="a", value="This is a HTMLNode", props={"href": "https://www.google.com", "target": "_blank"})
                self.assertEqual(node.tag, "a")
                self.assertEqual(node.value, "This is a HTMLNode")
                self.assertEqual(node.children, None)
                self.assertEqual(node.props, {"href": "https://www.google.com", "target":"_blank"})

        def test___repr__(self):
                node = HTMLNode(tag="a", value="This is a HTMLNode", props={"href": "https://www.google.com", "target": "_blank"})
                self.assertEqual((repr(node)), "HTMLNode(a, This is a HTMLNode, None, {'href': 'https://www.google.com', 'target': '_blank'})")

        def test_leaf_to_html_p(self):
                node = LeafNode("p", "Hello, world!")
                self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
        def test_leaf_to_html_no_tag(self):
                node = LeafNode(None, "Hello, world!")
                self.assertEqual(node.to_html(), "Hello, world!")
        
        def test_leaf_to_html_no_value(self):
                node = LeafNode("p", None)
                with self.assertRaises(ValueError):
                        node.to_html()

        def test_to_html_with_children(self):
                child_node = LeafNode("span", "child")
                parent_node = ParentNode("div", [child_node])
                self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        def test_to_html_with_grandchildren(self):
                grandchild_node = LeafNode("b", "grandchild")
                child_node = ParentNode("span", [grandchild_node])
                parent_node = ParentNode("div", [child_node])
                self.assertEqual(
                        parent_node.to_html(),
                        "<div><span><b>grandchild</b></span></div>",
                )
        
        def test_to_html_with_great_grandchildren(self):
                great_grandchild_node = LeafNode("i", "great-grandchild")
                grandchild_node = ParentNode("b", [great_grandchild_node])
                child_node = ParentNode("span", [grandchild_node])
                parent_node = ParentNode("div", [child_node])
                self.assertEqual(
                        parent_node.to_html(),
                        "<div><span><b><i>great-grandchild</i></b></span></div>",
                )

        def test_to_html_raises_on_missing_tag(self):
                child = LeafNode("span", "child")
                node = ParentNode(None, [child])
                with self.assertRaises(ValueError):
                        node.to_html()

        def test_to_html_raises_on_missing_children(self):
                node = ParentNode("div", None)
                with self.assertRaises(ValueError):
                        node.to_html()

        def test_to_html_raises_on_empty_children(self):
                none = ParentNode("div", [])
                with self.assertRaises(ValueError):
                        none.to_html()

        def test_to_html_with_props(self):
                node = ParentNode("a", [LeafNode(None, "link")], props={"href": "https://www.google.com"})
                self.assertEqual(node.to_html(), '<a href="https://www.google.com">link</a>')


if __name__ == "__main__":
    unittest.main()
