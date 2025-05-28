# 🔭 Terminal Teleporter

A lightweight command-line tool for setting quick navigation markers in your filesystem.

Jump instantly between important directories using simple commands like:

```bash
tp projects
```

## Features
- Save and name directory "teleporters"
- Instantly jump to saved locations
- Written in Python

## Demo
![Tool Demo](tool-demo.gif)

## Installation

### 1. Clone the Repo
```bash
git clone https://github.com/nathanmazzapica/terminal-teleporter.git
cp terminal-teleporter/tp.py ~/.local/bin/tp.py
chmod +x `/.local/bin/tp.py
```

### 2. Add the Shell Function

Add the following to your `.bashrc` or `.zshrc`:


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

Then reload your shell:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

## Usage

| Command                        | Description                         |
|-------------------------------|-------------------------------------|
| `tp --add <name>` or `-a`     | Adds a marker for the current dir   |
| `tp <name>`                   | Teleports to the saved directory    |
| `tp --list` or `-l`           | Lists all saved markers             |
| `tp --delete <name>` or `-d`  | Deletes the saved marker            |

## Example

```bash
cd ~/github.com/mysuperlongname/my-project-with-a-long-name
tp --add proj

cd ~
tp proj     # instantly jumps back to ~/github.com/mysuperlongname/my-project-with-a-long-name
```


## Important Notes

- Currently **not compatible with Windows** due to shell reliance.
- Requires `python3`.

## Future Plans
- Go rewrite for standalone binary use
- Windows support ***(?)***
- Searching/Fuzzy Match

## Contributions Welcome!

If you have suggestions or would like to help a young man out, feel free to open an issue or PR
