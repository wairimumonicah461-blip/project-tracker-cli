import json
from project_tracker.models import User, Project, Task

FILE = "data.json"


def save(users):
    """Turn the users into plain dictionaries and write them to the JSON file."""
    data = []
    for user in users:
        projects = []
        for project in user.projects:
            tasks = [{"title": t.title, "done": t.done} for t in project.tasks]
            projects.append({"title": project.title, "tasks": tasks})
        data.append({"name": user.name, "projects": projects})
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def load():
    """Read the JSON file and rebuild the users. No file yet means no users."""
    try:
        with open(FILE) as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    users = []
    for u in data:
        projects = []
        for p in u["projects"]:
            tasks = [Task(t["title"], t["done"]) for t in p["tasks"]]
            projects.append(Project(p["title"], tasks))
        users.append(User(u["name"], projects))
    return users
