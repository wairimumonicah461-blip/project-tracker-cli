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


def show_all(users):
    for user in users:
        print(user.name)
        for project in user.projects:
            print("  Project:", project.title)
            for task in project.tasks:
                mark = "x" if task.done else " "
                print("    [" + mark + "]", task.title)


users = storage.load()

while True:
    print()
    print("1. Add user")
    print("2. Add project")
    print("3. Add task")
    print("4. Complete task")
    print("5. Show everything")
    print("6. Quit")
    choice = input("Choose a number: ")

    if choice == "1":
        name = input("User name: ")
        if find_user(users, name):
            print("That user already exists.")
        else:
            users.append(User(name))
            print("Added user", name)

    elif choice == "2":
        user = find_user(users, input("Which user? "))
        if user is None:
            print("User not found.")
        else:
            title = input("Project title: ")
            user.projects.append(Project(title))
            print("Added project", title)

    elif choice == "3":
        project = find_project(users, input("Which project? "))
        if project is None:
            print("Project not found.")
        else:
            title = input("Task title: ")
            project.tasks.append(Task(title))
            print("Added task", title)

    elif choice == "4":
        project = find_project(users, input("Which project? "))
        if project is None:
            print("Project not found.")
        else:
            title = input("Which task? ")
            for task in project.tasks:
                if task.title.lower() == title.lower():
                    task.done = True
                    print("Completed task", task.title)
                    break
            else:
                print("Task not found.")

    elif choice == "5":
        show_all(users)

    elif choice == "6":
        break

    else:
        print("Please type a number from 1 to 6.")

    storage.save(users)

print("Goodbye!")
