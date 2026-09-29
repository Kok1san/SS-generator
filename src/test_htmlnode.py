import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            "a",
                      "Click me!",
                      None,
                      {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
                   node.props_to_html(),
                   ' href="https://www.google.com" target="_blank"'
               )

    def test_node2(self):
        node2 = HTMLNode("p", "Just text")
        self.assertEqual(
                   node2.props_to_html(),
                   ""
               )

    def test_node3(self):
        node3 = HTMLNode("h1", "Title")
        self.assertEqual(node3.tag, "h1")
        self.assertEqual(node3.value, "Title")

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    node2 = LeafNode("h1", "LOLYCH")
    self.assertEqual(node2.to_html(), "<h1>LOLYCH</h1>")
    node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    self.assertEqual(node3.to_html(), '<a href="https://www.google.com">Click me!</a>')
    node4 = LeafNode("p", None)
    with self.assertRaises(ValueError):
        node4.to_html()
if __name__ == "__main__":
    unittest.main()

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
