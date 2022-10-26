from pathlib import Path


def get_directories_names(root_path):
    for path in Path(root_path).iterdir():
        if path.is_dir():
            print(path)
            get_directories_names(path)


root_dir = r"D:\steam"

get_directories_names(root_dir)


