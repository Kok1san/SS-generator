from markdown_to_html_node import markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    for string in markdown.split('\n'):
        if string.startswith("# "):
            new_string = string[1:]
            striped_string = new_string.strip()
            return striped_string
    raise Exception("No h1 in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, "r")
    markdown_content = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()
    html_node = markdown_to_html_node(markdown_content)
    html_string = html_node.to_html()
    new_title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", new_title)
    template_content = template_content.replace("{{ Content }}", html_string)
    get_name = os.path.dirname(dest_path)
    os.makedirs(get_name, exist_ok=True)
    open_file = open(dest_path, "w")
    open_file.write(template_content)
    open_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_files = os.listdir(dir_path_content)
    for file in list_files:
        path_to_file = os.path.join(dir_path_content, file)
        new_dest = Path(os.path.join(dest_dir_path, file))
        if os.path.isfile(path_to_file) == True:
            new_dest = new_dest.with_suffix(".html")
            generate_page(path_to_file, template_path, new_dest)
        else:
            generate_pages_recursive(path_to_file, template_path, new_dest)
