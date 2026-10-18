class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done


class Project:
    def __init__(self, title, tasks=None):
        self.title = title
        self.tasks = tasks or []


class User:
    def __init__(self, name, projects=None):
        self.name = name
        self.projects = projects or []
