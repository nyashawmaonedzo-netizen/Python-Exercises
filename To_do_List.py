def add_task(tasks, task):    tasks.append(task)
def remove_task(tasks, task):    tasks.remove(task)


def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def main():
    tasks = []

    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter a task to add: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter a task to remove: ")
            if task in tasks:
                remove_task(tasks, task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
