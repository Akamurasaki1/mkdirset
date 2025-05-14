import sys
from mkdirset.builder import create_from_file
from mkdirset.dumper import dump_tree

def main():
    if len(sys.argv) < 2:
        print("Usage: mkdirset from <file> | mkdirset dump [dir]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "from":
        if len(sys.argv) != 3:
            print("Usage: mkdirset from <file>")
            sys.exit(1)
        create_from_file(sys.argv[2])
    elif command == "dump":
        dir_to_dump = sys.argv[2] if len(sys.argv) > 2 else "."
        dump_tree(dir_to_dump)
    else:
        print("Unknown command:", command)
