class Task:
    """Task class. Foundation building block """

    def __init__(self, name, text):
        self.name = name 
        self.text = text
        self._child_tasks = []

    def add_child_task(self, task):
        self._child_tasks.append(task)

    def get_child_tasks(self):
        return self._child_tasks
    
    def remove_child_task(self, position):
        length = len(self._child_tasks) - 1
        if position >= 0 and length >= position:
            self._child_tasks.pop(position)

