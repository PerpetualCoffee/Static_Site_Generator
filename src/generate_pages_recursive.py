import os
from generate_page import generate_page

def generate_pages_recursively(source_dir, template_path, dest_dir, base_path):
    # inside you'll use os.listdir, os.path.isdir and recursive calls
    
    os.makedirs(dest_dir, exist_ok=True)
    
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)
        if os.path.isfile(source_item) and source_item.endswith(".md"):
            dest_html = dest_item.replace(".md", ".html")
            generate_page(source_item, template_path, dest_html, base_path)
        elif os.path.isdir(source_item):
            generate_pages_recursively(source_item, template_path, dest_item, base_path)

