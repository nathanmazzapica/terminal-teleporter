import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Move quickly between directories.")

parser.add_argument('-a', '--add', help='Adds a new marker by the provided name', action='store_true')
parser.add_argument('-l', '--list', help='Lists all existing markers', action='store_true')
parser.add_argument('-d', '--delete', help='Deletes target marker', action='store_true')
parser.add_argument("name", nargs='?', help='The name of the marker to jump or modify')

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


# I think explicitly typing dicts is good, but I don't like it anywhere else tbh
def delete_from_dict(marker_name: str, destinations: dict [str, str]):
    try:
        dest_file = open(f'{destinations_dir}/testfail.txt', 'w')
        for marker in destinations:
            path = destinations[marker]
            dest_file.write(f'{marker}:{path};')
        print(f"Marker {marker_name} removed!")
    except FileNotFoundError:
        os.makedirs(os.path.join(os.environ["HOME"], "term-tp"))
        delete_from_dict(marker_name, destinations)

# Read and initialize destinations
dest_file = None
def main():
    destinations = load_dict()
    if args.delete:
        target = args.name
        print(f"Deleting: {target}")
        if target in destinations:
            del destinations[target]
            delete_from_dict(target, destinations)
    elif args.list:
        print(f"\n{'MARKER':20}:\tDESTINATION")
        for marker in destinations:
            print(f"{marker:20}:\t{destinations[marker]}")
        print("\n")
    elif args.add:
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


