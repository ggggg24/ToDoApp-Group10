tasks = []  # Global list to store tasks


def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")


def show_tasks():
    """Displays all tasks in the to-do list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(task_number):
    """Removes a task based on its number."""
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")
print("\n--- TO-DO LIST MENU ---")
print("1. Add Task")
print("2. Show Tasks")
print("3. Remove Task")
print("4. Exit")

Add confirmation for deletion:
confirm = input("Are you sure you want to delete this task? (y/n): ")
if confirm.lower() == "y":
    remove_task(task_number)
else:
    print("Cancelled deletion.")
