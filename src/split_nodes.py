from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splited_node = node.text.split(delimiter)
            if len(splited_node) % 2 == 0:
                raise Exception("there is no closing element")
            for i, text_part in enumerate(splited_node):
                if len(text_part) == 0:
                    continue
                if i % 2 == 0:
                    new_node = TextNode(text_part, TextType.TEXT)
                    new_nodes.append(new_node)
                else:
                    new_node = TextNode(text_part, text_type)
                    new_nodes.append(new_node)
    return new_nodes
