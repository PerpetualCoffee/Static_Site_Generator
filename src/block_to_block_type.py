from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
        
    counter = 0
    for ch in block:
        if ch == "#":
            counter += 1
        else:
            break
    if counter > 0 and counter <= 6 and counter < len(block) and block[counter] == " ":
        return BlockType.HEADING

    lines = block.split("\n")

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    expected_number = 1
    is_ordered_list = True
    for line in lines:
        if not line.startswith(f"{expected_number}. "):
            is_ordered_list = False
            break
        expected_number += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

            
    
