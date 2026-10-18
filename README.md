# Project Tracker CLI

A command-line tool to manage users, projects and tasks. Data is saved in `data.json`.

## How to run

```
python3 main.py
```

Then type a number from the menu:

1. Add user
2. Add project
3. Add task
4. Complete task
5. Show everything
6. Quit

## Files

- `main.py` - the menu
- `project_tracker/models.py` - User, Project and Task classes
- `project_tracker/storage.py` - saves and loads `data.json`