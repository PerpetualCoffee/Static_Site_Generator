# import everything!
from splitnode import split_nodes_delimiter
from textnode import TextType, TextNode, text_node_to_html_node
from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode

# 8 helper functionns to convert markdown to HTML nodes
# 1 dispatcher (looks at the block type and calls the appropriate function)
# one function for each block type (paragraph, codeblock, list, etc.)
# one shared inline helper (text_to_children) that takes a string of text and returns a list of HTMLNodes (think TextNode -> HTMLNode)

def block_to_html_node(block: str) -> ParentNode:
    # takes a block and returns an HTMLNode
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_htmlnode(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    raise ValueError("invalid block type")

def paragraph_to_html_node(block):
    # takes a paragraph block and returns an HTMLNode
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode("p", children)

def heading_to_html_node(block):
    # takes a heading block and returns an HTMLNode
    level = 0
    for ch in block:
        if ch == "#":
            level += 1
        else:
            break
    text = block.lstrip("#").strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    # this one may be special then the rest (see instructions)
    text = block[3:-3].lstrip("\n")
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    # takes a quote block and returns an HTMLNode
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    joined = " ".join(new_lines)
    children = text_to_children(joined)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    # takes an unoordered list and returns an HTMLNode
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        new_lines.append(ParentNode("li", children))
    return ParentNode("ul", new_lines)
    

def olist_to_html_node(block):
    # takes an ordered list and returns an HTMLNode
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        parts = line.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        new_lines.append(ParentNode("li", children))
    return ParentNode("ol", new_lines)
    

def text_to_children(text):
    # takes a string of text and returns a list of HTMLNodes (think TextNode -> HTMLNode)
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def markdown_to_html_node(markdown):
    split = markdown_to_blocks(markdown)
    html_nodes = []
    for s in split:
        html_nodes.append(block_to_html_node(s))
    return ParentNode("div", html_nodes)
