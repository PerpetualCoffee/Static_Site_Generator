import unittest
from markdown_to_html_node import markdown_to_html_node, block_to_html_node, paragraph_to_html_node, code_to_html_node, heading_to_html_node, quote_to_html_node, ulist_to_html_node, olist_to_html_node
from text_to_textnodes import text_to_textnodes
from htmlnode import HTMLNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_headings(self):
        md = """
# this is heading 1.

## this is heading 2.

### this is heading 3.

#### this is heading 4.

##### this is heading 5.

###### this is heading 6.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is heading 1.</h1><h2>this is heading 2.</h2><h3>this is heading 3.</h3><h4>this is heading 4.</h4><h5>this is heading 5.</h5><h6>this is heading 6.</h6></div>",
        )

    def test_multiple_items_unordered_list(self):
        md = """
- item 1
- item 2
- item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>item 1</li><li>item 2</li><li>item 3</li></ul></div>",
        ) 

    def test_multiple_items_ordered_list(self):
        md = """
1. item 1
2. item 2
3. item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>item 1</li><li>item 2</li><li>item 3</li></ol></div>",
        )    

    def test_lists_longer_than_9_items_ordered_list(self):
        md = """
1. item 1
2. item 2
3. item 3
4. item 4
5. item 5
6. item 6
7. item 7
8. item 8
9. item 9
10. item 10
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>item 1</li><li>item 2</li><li>item 3</li><li>item 4</li><li>item 5</li><li>item 6</li><li>item 7</li><li>item 8</li><li>item 9</li><li>item 10</li></ol></div>",
        )

    def test_quote(self):
        md = """
> This is a quote block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block</blockquote></div>",
        )
    
    def test_mixed_content(self):
        md = """
# Heading 1

```
This is a code block
```

> This is a quote block

- Item 1
- Item 2
- Item 3

1. Item 1
2. Item 2
3. Item 3

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><pre><code>This is a code block</code></pre><blockquote>This is a quote block</blockquote><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
        )
    
    def test_empty_markdown(self):
        with self.assertRaises(ValueError):
            node = markdown_to_html_node("")
            html = node.to_html()


if __name__ == "__main__":
    unittest.main() 
        