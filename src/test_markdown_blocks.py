import unittest
from markdown_to_blocks import markdown_to_blocks
from markdown_blocks import BlockType, block_to_block_type

def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
def test_markdown_to_blocks_newlines(self):
        md = """
This is a paragraph



This is another paragraph with extra blank lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph with extra blank lines",
            ],
        )

def test_markdown_to_blocks_whitespace(self):
        md = """


This is a block with leading spaces

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a block with leading spaces",
            ],
        )



class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_block_heading(self):
        md = "# This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_to_block_code(self):
        md = "```\ncode block here\n```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_quote(self):
        md = "> This is a quote\n> Second line of quote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_to_block_paragraph(self):
        md = "Just a normal paragraph with some text."
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
