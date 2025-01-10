tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks to show.")

def delete_task(index):
    if 0 < index <= len(tasks):
        tasks.pop(index - 1)
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        task_num = int(input("Enter task number to delete: "))
        delete_task(task_num)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
