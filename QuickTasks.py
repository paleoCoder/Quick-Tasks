#! /usr/bin/env/python
import Task

def print_task(task):
    print "%s: %s" % (task.name, task.text)
    for index, t in enumerate(task.get_child_tasks()):
        print "  %f - %s: %s" % (index, t.name, t.text)

def process_command(command, task):
    if command == "n":
        name = raw_input("task name: ")
        text = raw_input("task text: ")
        return add_task(task, name, text)
    elif is_number(command):
        return delete_task(task, command)

def delete_task(task, taskNumber):
    task.remove_child_task(int(taskNumber))
    return task

def add_task(task, name, text):
    newTask = Task.Task(name, text)
    task.add_child_task(newTask)
    return task

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    
    # keeps the input from user
    command = ""

    # array of task objects
    parentTask = Task.Task("Parent Task", "things to do")

    print "Welcome to the Tasks driver"

    while command != "q":
        print
        print "current tasks"
        print_task(parentTask)
        print "--"
        print "what next?"
        command = raw_input("Quit (q) New task (n), or complete (#): ")
        print "you entered: ", command
        task = process_command(command, parentTask)


