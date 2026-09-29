from textnode import TextNode, TextType
from copystatic import clear_public, copy_static
from gencontent import generate_pages_recursive
import sys

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    clear_public("docs")
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
