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