import os, shutil

def copy_files_recursive(source_dir, dest_dir):
    """
    Recursively copies files from source_dir to dest_dir.
    """

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)
        print(f"Copying {source_item} to {dest_item}...")
        if os.path.isfile(source_item):
            shutil.copy(source_item, dest_item)
        elif os.path.isdir(source_item):
            copy_files_recursive(source_item, dest_item)


