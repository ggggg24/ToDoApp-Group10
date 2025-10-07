# toDoApp.py

tasks = []

def addTask(task):
    tasks.append(task)
    print("Task added!")

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def removeTask(taskNumber):
    if 0 < taskNumber <= len(tasks):
        tasks.pop(taskNumber - 1)
        print("Task removed!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter task: ")
            addTask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("Enter task number to remove: "))
            removeTask(n)
        elif ch == "4":
            print("Exiting program...")
            break
        else:
            print("Wrong choice!")

if __name__ == "__main__":
    main()
