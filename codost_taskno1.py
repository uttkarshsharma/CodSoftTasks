import os

#Adding_Task

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully")

#Viewing_task

def view_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do List is empty")

#Completing_Task

def complete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks.pop(task_index - 1)
        print("Task marked as completed")
    else:
        print("Invalid task index")

#Deleting_Task

def delete_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        tasks.pop(task_index - 1)
        print("Task deleted successfully")
    else:
        print("Invalid task index")

#Saving_task

def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved successfully")

#Loading_Task

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice:- ")

        if choice == "1":
            task = input("Enter the task:- ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            idx = int(input("Enter the task index to mark as completed:- "))
            complete_task(tasks, idx)
        elif choice == "4":
            idx = int(input("Enter the task index to delete:- "))
            delete_task(tasks, idx)
        elif choice == "5":
            save_tasks(tasks, filename)
        elif choice == "6":
            print("Exiting!!!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
