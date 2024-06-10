import os

# Define the file path for storing tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

# Function to remove an existing task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: ").strip())
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
