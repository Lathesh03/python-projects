import random
FILE_NAME = "todo.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, we just start with an empty list
        pass
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
def view_tasks(tasks):
    if not tasks:
        print("Your To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task(tasks):
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' added.")
def mark_complete(tasks):
    view_tasks(tasks)  # Show the list so the user knows which task to complete
    try:
        task_number = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            print(f"Task '{completed_task}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def main_menu():
    print("\nTo-Do List Application")
    print("------------------------")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Complete")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
            save_tasks(tasks)  # Save the list after marking a task complete
        elif choice == '4':
            print("Exiting application. Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

