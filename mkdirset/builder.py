import os

def create_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    root = None
    for line in lines:
        line = line.rstrip()
        if not line:
            continue

        indent_level = len(line) - len(line.lstrip('│├└ '))
        name = line.lstrip('│├└─ ')
        if name.endswith('/'):
            name = name[:-1]

        depth = indent_level // 4
        if root is None:
            root = name
            os.makedirs(root, exist_ok=True)
            path_stack = [root]
        else:
            while len(path_stack) > depth:
                path_stack.pop()
            path_stack.append(name)
            current_path = os.path.join(*path_stack)
            if '.' in name:
                os.makedirs(os.path.dirname(current_path), exist_ok=True)
                open(current_path, 'a').close()
            else:
                os.makedirs(current_path, exist_ok=True)

    print(f'cd {root}')
