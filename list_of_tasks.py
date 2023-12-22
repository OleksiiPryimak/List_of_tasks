# # python M04/List_of_tasks.py
user_choise = -1

tasks = []
tasks.append("Task 1")
tasks.append("Task 2")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index)+ "]" )
        task_index += 1

def add_task():
    task = input("Write your Task: ")
    tasks.append(task)
    print("-- Task has been added --")

def delete_task():
    task_index = int(input("enter the index to be removed: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("!!! indeks does not exist !!! ")
        return

    tasks.pop(task_index)
    print("Task was deleted")

    # tasks.pop(task_index)

def save_tasks_to_file():
    try:
        file = open("tasks.txt","w")
        for task in tasks:
            file.write(task+"\n")
        file.close()
    except FileNotFoundError:
        return


def load_tasks_from_file():
    file = open("tasks.txt")

    for line in file.readlines():
        tasks.append(line.strip())
    
    file.close()

load_tasks_from_file()

while user_choise != 5:
    if user_choise == 1:
        # print(tasks)
        show_tasks()
    
    if user_choise == 2:
        add_task()

    if user_choise == 3:
        delete_task()

    if user_choise == 4:
        save_tasks_to_file()

    print()
    print("1.Show Task")
    print("2.Add Task")
    print("3.Delete Task")
    print("4.Save changest to the file")
    print("5.Leave")

    user_choise = int(input("Select a number: "))
    print()


