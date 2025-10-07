tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def remove_task(task_number):
    try:
        tasks.pop(task_number - 1)
        print("Task removed!")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        ch = input("Enter choice: ")
        
        if ch == "1":
            t = input("Enter task: ").strip()
            if t:
                add_task(t)
            else:
                print("Task cannot be empty.")
        elif ch == "2":
            show_tasks()
        elif ch == "3":
            try:
                n = int(input("Enter task no to remove: "))
                remove_task(n)
            except ValueError:
                print("Please enter a valid number.")
        elif ch == "4":
            print("Exiting app...")
            break
        else:
            print("Invalid choice. Please try again.")

main()

