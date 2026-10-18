import argparse
from project_tracker.models import User, Project, Task
from project_tracker import storage


def find_user(users, name):
    for user in users:
        if user.name.lower() == name.lower():
            return user
    return None


def find_project(users, title):
    for user in users:
        for project in user.projects:
            if project.title.lower() == title.lower():
                return project
    return None


parser = argparse.ArgumentParser(description="Simple project management tool")
commands = parser.add_subparsers(dest="command", required=True)

p = commands.add_parser("add-user", help="Create a user")
p.add_argument("--name", required=True)

p = commands.add_parser("add-project", help="Add a project to a user")
p.add_argument("--user", required=True, help="Name of the owner")
p.add_argument("--title", required=True, help="Project title")

p = commands.add_parser("add-task", help="Add a task to a project")
p.add_argument("--project", required=True, help="Project title")
p.add_argument("--title", required=True, help="Task title")

p = commands.add_parser("complete-task", help="Mark a task as done")
p.add_argument("--project", required=True, help="Project title")
p.add_argument("--title", required=True, help="Task title")

p = commands.add_parser("list", help="Show projects and tasks")
p.add_argument("--user", help="Only show this user (optional)")

args = parser.parse_args()

users = storage.load()

if args.command == "add-user":
    if find_user(users, args.name):
        print("That user already exists.")
    else:
        users.append(User(args.name))
        print("Added user", args.name)

elif args.command == "add-project":
    user = find_user(users, args.user)
    if user is None:
        print("User not found.")
    else:
        user.projects.append(Project(args.title))
        print("Added project", args.title)

elif args.command == "add-task":
    project = find_project(users, args.project)
    if project is None:
        print("Project not found.")
    else:
        project.tasks.append(Task(args.title))
        print("Added task", args.title)

elif args.command == "complete-task":
    project = find_project(users, args.project)
    if project is None:
        print("Project not found.")
    else:
        for task in project.tasks:
            if task.title.lower() == args.title.lower():
                task.done = True
                print("Completed task", task.title)
                break
        else:
            print("Task not found.")

elif args.command == "list":
    for user in users:
        if args.user and user.name.lower() != args.user.lower():
            continue
        print(user.name)
        for project in user.projects:
            print("  Project:", project.title)
            for task in project.tasks:
                mark = "x" if task.done else " "
                print("    [" + mark + "]", task.title)

storage.save(users)
