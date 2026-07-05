import shutil, os, sys

from copystatic import copy_files_recursive
from generate_pages_recursive import generate_pages_recursively

dir_path_static = "./static"
dir_path_docs = "./docs"

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
        
    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    generate_pages_recursively("content", "template.html", "docs", "base_path")
	


main()

