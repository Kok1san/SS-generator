from markdown_to_blocks import markdown_to_blocks
from text_to_text_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from markdown_blocks import BlockType, block_to_block_type
from htmlnode import ParentNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    nodes_list = []
    for node in text_nodes:
        nodes_list.append(text_node_to_html_node(node))
    return nodes_list

def paragraph_to_html_node(block):
    splited_block = block.split("\n")
    joined_block = " ".join(splited_block)
    children_node = text_to_children(joined_block)
    return ParentNode("p", children_node)

def heading_to_html_node(block):
    count = 0
    for char in block:
        if char == "#":
            count+=1
        else:
            break
    children_node = text_to_children(block[count+1::])
    return ParentNode(f"h{count}", children_node)

def code_to_html_node(block):
    slice = block[4:-4]
    text_node = TextNode(slice, TextType.TEXT)
    child = text_node_to_html_node(text_node)
    parent_node = ParentNode("code", [child])
    return ParentNode("pre", [parent_node])

def quote_to_html_node(block):
    new_string = ""
    split_block = block.split("\n")
    for block in split_block:
        new_block = block.lstrip(">").strip()
        new_string+=new_block+" "
    children_node = text_to_children(new_string)
    return ParentNode("blockquote", children_node)

def ulist_to_html_node(block):
    li_items = []
    split_block = block.split("\n")
    for x in split_block:
        new_block = x[2:]
        children_node = text_to_children(new_block)
        parent_node = ParentNode("li", children_node)
        li_items.append(parent_node)
    return ParentNode("ul", li_items)

def olist_to_html_node(block):
    li_items = []
    split_block = block.split("\n")
    for x in split_block:
        new_block = x.split(". ")
        children_node = text_to_children(new_block[1])
        paent_node = ParentNode("li", children_node)
        li_items.append(paent_node)
    return ParentNode("ol", li_items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
       return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
       return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
       return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
       return ulist_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
       return olist_to_html_node(block)

def markdown_to_html_node(markdown):
    block_list = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_list.append(block_to_html_node(block))
    return ParentNode("div", block_list)
