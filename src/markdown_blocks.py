from enum import Enum
import re
from turtle import position
from markdown_to_blocks import markdown_to_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    first_word = markdown.split(" ")[0]

    if len(first_word)<=6 and len(first_word) >= 1 and first_word == "#" * len(first_word):
        position_after_hashes = len(first_word)
        if len(markdown) > position_after_hashes:
            if markdown[position_after_hashes] == " " and len(markdown) - len(first_word) > 1:
                return BlockType.HEADING
    elif markdown.startswith("```"+"\n") and markdown.endswith("```"):
        return BlockType.CODE
    lines = markdown.split("\n")
    quote_list = []
    for line in lines:
        if line.startswith(">"):
            quote_list.append(line)
    if len(quote_list) == len(lines):
        return BlockType.QUOTE
    unordered_list = []
    for line in lines:
        if line.startswith("-"+" "):
            unordered_list.append(line)
    if len(unordered_list) == len(lines):
        return BlockType.UNORDERED_LIST
    ordered_list = []
    for number, line in enumerate(lines, start=1):
        if line.startswith(str(number)+"."+" "):
            ordered_list.append(line)
    if len(ordered_list) == len(lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
