import os

def dump_tree(root='.'):
    def print_tree(current, prefix=""):
        contents = sorted(os.listdir(current))
        for i, name in enumerate(contents):
            path = os.path.join(current, name)
            connector = "├── " if i < len(contents) - 1 else "└── "
            print(prefix + connector + name + ("/" if os.path.isdir(path) else ""))
            if os.path.isdir(path):
                extension = "│   " if i < len(contents) - 1 else "    "
                print_tree(path, prefix + extension)

    print(os.path.basename(os.path.abspath(root)) + "/")
    print_tree(root)
