from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            image_alt, image_link = image
            sections = text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image_alt,
                    TextType.IMAGE,
                    image_link,
                )
            )
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            link_text, link_url = link
            sections = text.split(f"[{link_text}]({link_url})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    link_text,
                    TextType.LINK,
                    link_url,
                )
            )
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
