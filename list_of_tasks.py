# # python M04/04-zadania-YT.py
user_choise = -1

tasks = []
tasks.append("zadanie 1")
tasks.append("zadanie 2")

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + "[" + str(task_index)+ "]" )
        task_index += 1

def add_task():
    task = input("Wpisz zadanie: ")
    tasks.append(task)
    print("-- zadanie zostało dodane --")

def delete_task():
    task_index = int(input("podaj index do usunięcia: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("!!! indeks nie istnieje !!! ")
        return

    tasks.pop(task_index)
    print("Usunięto zadanie")

    # tasks.pop(task_index)
    # print("-- Usunięte zadanie --")

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
    print("1.Pokaż zadanie")
    print("2.Dodaj zadanie")
    print("3.Usuń zadanie")
    print("4.Zapisz zmiany do pliku")
    print("5.Wyjdż")

    user_choise = int(input("Wybierz liczbę: "))
    print()


