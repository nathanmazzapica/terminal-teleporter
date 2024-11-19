import sys
import os
import argparse


MARKERS_DIR = os.path.join(os.environ["HOME"], "term-tp")
MARKERS_FILE = os.path.join(MARKERS_DIR, "markers.txt")

def ensure_markers_dir_exists():
    os.makedirs(MARKERS_DIR, exist_ok=True)


def load_markers() -> dict[str, str]:
    if not os.path.exists(MARKERS_FILE):
        return {}
    with open(MARKERS_FILE, 'r') as file:
        return {k:v for k, v in (line.split(":") for line in file.read().split(";") if line)}

def save_markers(markers: dict[str, str]):
    ensure_markers_dir_exists()
    with open(MARKERS_FILE, 'w') as file:
        file.write(";".join(f"{k}:{v}" for k, v in markers.items()))


def main():
    parser = argparse.ArgumentParser(description="Move quickly between directories.")
    parser.add_argument('-a', '--add', help='Adds a new marker by the provided name', action='store_true')
    parser.add_argument('-l', '--list', help='Lists all existing markers', action='store_true')
    parser.add_argument('-d', '--delete', help='Deletes target marker', action='store_true')
    parser.add_argument("name", nargs='?', help='The name of the marker to jump or modify')
    args = parser.parse_args()

    markers = load_markers()

    if args.delete:
        target = args.name
        print(f"Deleting: {target}")
        if target not in markers:
            print(f"Marker '{args.name}' does not exist!")
            sys.exit(1)
        del markers[args.name]
        save_markers(markers)
        print(f"Marker '{args.name}' removed!")

    elif args.add:
        if args.name in markers:
            print(f"Marker '{args.name}' already exists!")
            sys.exit(1)

        if args.name is None:
            print(f"Marker name cannot be blank!")
            sys.exit(1)

        elif ":" in args.name or ";" in args.name:
            print(f"{args.name} contains illegal characters!")
            sys.exit(1)

        markers[args.name] = os.getcwd()
        save_markers(markers)
        print(f"Marker '{args.name}' added at {os.getcwd()}!")

    elif args.list:
        print(f"\n{'MARKER':20}:\tDESTINATION")
        for marker in markers:
            print(f"{marker:20}:\t{markers[marker]}")
        print("\n")

    else:
        if args.name in markers:
            print(markers[args.name])
        else:
            if len(markers) == 0:
                print(f"You have no created any markers! Use -a or --add to create a marker!")
            print(f"Marker: {args.name} does not exist!")
            sys.exit(1)

if __name__ == '__main__':
    main()


