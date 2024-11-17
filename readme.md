# Terminal Teleporter

A simple command line tool to add convenient markers to jump around directories

## Demo
![Tool Demo](tool-demo.gif)

## Installation

The following function must be added to your bash configuration (.bashrc / .zshrc)

~/.local/bin/tp.py can be changed to wherever you wish to keep the script.

```bash
function tp() {
    case "$1" in
        -d|--delete|-a|--add|-l|--list)
            python3 ~/.local/bin/tp.py "$@"
            ;;
        *)
            dir=$(python3 ~/.local/bin/tp.py "$1")
            if [ -d "$dir" ]; then
                cd "$dir"
            else
                echo "Error: $dir"
            fi
            ;;
    esac
}
```

## Usage

To add a new marker run the `tp` command with the `-a` or `--add` flag and then the name of the marker to create

To jump to a marker simply use `tp marker_name`

To list all current markers use `tp -l` or `tp --list`

To delete a marker use `tp -d marker_name` or `tp --delete marker_name`


## Important Notes

Currently does **not** work on windows

There is currently no way to delete or edit markers other than directly editing `~/term-tp/testfail.txt`
*(yes, i need to rename the file)*
