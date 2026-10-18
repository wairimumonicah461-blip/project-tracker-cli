# Project Tracker CLI

A command-line tool to manage users, projects and tasks. Data is saved in `data.json`.
It uses only the Python standard library, so nothing needs to be installed.

## How to run

Requires Python 3.10+. Use `python3 main.py <command>` (or `python` on Windows).

```
python3 main.py add-user --name "Alex"
python3 main.py add-project --user "Alex" --title "CLI Tool"
python3 main.py add-task --project "CLI Tool" --title "Implement add-task"
python3 main.py complete-task --project "CLI Tool" --title "Implement add-task"
python3 main.py list
python3 main.py list --user "Alex"
python3 main.py list-users
```

Use `python3 main.py --help` to see all commands.

## Files

- `main.py` - the commands (argparse)
- `project_tracker/models.py` - User, Project and Task classes
- `project_tracker/storage.py` - saves and loads `data.json`
- `data.json` - the saved data
