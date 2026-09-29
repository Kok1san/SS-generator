from textnode import TextNode, TextType
from copystatic import clear_public, copy_static
from gencontent import generate_pages_recursive

def main():

    node = TextNode("some text", TextType.BOLD, url=None)
    print(node)
    clear_public("public")
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()
