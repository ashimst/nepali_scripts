import os

def add_prefix_to_dirs(root_dir, prefix):
    # Walk through all directories in reverse order (bottom-up)
    for dirpath, dirnames, _ in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            old_path = os.path.join(dirpath, dirname)
            new_name = prefix + dirname
            new_path = os.path.join(dirpath, new_name)
            os.rename(old_path, new_path)

# Example usage
root_directory = "maithili_cropped"  # Change this
prefix = "maithili_"

add_prefix_to_dirs(root_directory, prefix)
