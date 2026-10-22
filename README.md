# Project Tracker CLI

A command-line tool for managing users, projects and tasks. A user can have many projects,
and each project can have many tasks. All data is saved to a JSON file, so it is still there
the next time you run the program.

## Features

- Create users
- Add projects to a user
- Add tasks to a project
- Mark tasks as complete
- Show all users, or one user's projects and tasks
- Data is saved automatically in `data.json`

## Requirements

- Python 3.10 or higher
- No external packages are needed (only the Python standard library)

## How to run

1. Download or clone this repository and open the folder in a terminal.
2. Run a command with `python3 main.py <command>` (use `python` on Windows).
3. To see all commands, run:

```
python3 main.py --help
```

## Commands

| Command | What it does | Example |
|---|---|---|
| `add-user` | Create a user | `python3 main.py add-user --name "Monicah"` |
| `add-project` | Add a project to a user | `python3 main.py add-project --user "Monicah" --title "CLI Tool"` |
| `add-task` | Add a task to a project | `python3 main.py add-task --project "CLI Tool" --title "Write README"` |
| `complete-task` | Mark a task as done | `python3 main.py complete-task --project "CLI Tool" --title "Write README"` |
| `list` | Show projects and tasks (add `--user` for one user) | `python3 main.py list --user "Monicah"` |
| `list-users` | Show all users and how many projects each has | `python3 main.py list-users` |

## Example

```
python3 main.py add-user --name "Monicah"
python3 main.py add-project --user "Monicah" --title "CLI Tool"
python3 main.py add-task --project "CLI Tool" --title "Write README"
python3 main.py complete-task --project "CLI Tool" --title "Write README"
python3 main.py list
```

Output of the last command:

```
Monicah
  Project: CLI Tool
    [x] Write README
```

`[x]` means the task is done, and `[ ]` means it is still pending.

## How the data is saved

The program reads `data.json` when it starts and writes it again after every command.
If the file does not exist, the program starts with no data. If the file is damaged,
the program stops with a message and leaves the file unchanged, so nothing is overwritten.

## Project structure

```
main.py                     the commands (argparse)
project_tracker/
    models.py               User, Project and Task classes
    storage.py              saves and loads data.json
data.json                   the saved data
requirements.txt            dependencies (none needed)
```

## How it works

- `User` has a name and a list of projects.
- `Project` has a title and a list of tasks.
- `Task` has a title and a done status.
- `main.py` reads the command, finds the right user or project, makes the change,
  and saves everything.