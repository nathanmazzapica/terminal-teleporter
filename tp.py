import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Move quickly between directories.")

parser.add_argument('-a', '--add', help='Adds a new marker by the provided name', action='store_true')
parser.add_argument("name", help='The name of the marker to jump or modify')

args = parser.parse_args()

destinations_dir = os.path.join(os.environ["HOME"], "term-tp")

def load_dict() -> dict[str, str]:
    destinations: dict[str, str] = {}
    try:
        dest_file = open(f'{destinations_dir}/testfail.txt', 'r')
        pairs = dest_file.read()
        for pair in pairs.split(";"):
            if len(pair) == 0:
                continue

            target = pair.split(":")
            marker = target[0]
            target_dir = target[1]
            destinations[marker] = target_dir

    except FileNotFoundError:
        if not args.add:
            print("You have not created any markers!")
            print("Please use this command with the -a/--add flag to create one!")
        return {}

    return destinations

def add_to_dict(marker_name: str, path: str):
    try:
        dest_file = open(f'{destinations_dir}/testfail.txt', 'a')
        dest_file.write(f'{marker_name}:{path};')
        print(f"Marker {marker_name} placed at {os.getcwd()}!")
    except FileNotFoundError:
        os.makedirs(os.path.join(os.environ["HOME"], "term-tp"))
        add_to_dict(marker_name, path)

# Read and initialize destinations
dest_file = None
def main():
    destinations = load_dict()
    if args.add:
        cwd = os.getcwd()
        marker_name = args.name
        add_to_dict(marker_name, cwd)
    else:
        if args.name in destinations:
            print(destinations[args.name])
        else:
            print(f"Marker: {args.name} does not exist!")
            sys.exit(1)

if __name__ == '__main__':
    main()


