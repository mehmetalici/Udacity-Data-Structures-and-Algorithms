import os
from pathlib import Path

def find_files(suffix: str, path: str) -> list:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        return

    all_files = []
    for dir_item in os.listdir(path):
        files = find_files(suffix, os.path.join(path, dir_item))
        if files is not None:
            all_files += files
    return all_files


if __name__ == "__main__":
    print("\n".join(find_files(".c", ".")))
    try:
        print(find_files(".c", ""))  
    except FileNotFoundError:
        print("Pass")
    try:
        print(find_files(".c", "an_invalid_path")) 
    except FileNotFoundError:
        print("Pass")

