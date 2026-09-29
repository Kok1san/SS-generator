import unittest
from textnode import TextNode, TextType
# Заміни 'your_module_name' на назву файлу, де лежить твоя функція split_nodes_delimiter
from split_nodes import split_nodes_delimiter
from inline_markdown import split_nodes_image, split_nodes_link


class TestInlineMarkdown(unittest.TestCase):

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_missing_closing(self):
        node = TextNode("This is a *broken italic text", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_non_text_node_ignored(self):
        node = TextNode("Already a link", TextType.LINK, url="https://boot.dev")
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual([node], new_nodes)

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
                    TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ],
                new_nodes,
            )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://youtube.com"),
            ],
            new_nodes,
        )
