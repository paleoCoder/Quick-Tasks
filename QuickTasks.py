#! /usr/bin/env/python
import Task

def print_Tasks(tasks):
    for index, t in enumerate(tasks):
        print "%f - %s" % (index, t.getTaskDetails())

def processCommand(command, tasks):
    if command == "n":
        name = raw_input("task name: ")
        desc = raw_input("task desc: ")
        return createTask(tasks, name, desc)
    elif is_number(command):
        return deleteTask(tasks, command)

def deleteTask(tasks, taskNumber):
    del tasks[float(taskNumber)]
    return tasks

def createTask(tasks, name, desc):
    newTask = Task.Task(name, desc)
    tasks.append(newTask)
    return tasks

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    
    # keeps the input from user
    command = ""

    # array of task objects
    tasks = []

    print "Welcome to the Tasks driver"

    while command != "q":
        print
        print "current tasks"
        print_Tasks(tasks)
        print "--"
        print "what next?"
        command = raw_input("Quit (q) New task (n), or complete (#): ")
        print "you entered: ", command
        tasks = processCommand(command, tasks)


