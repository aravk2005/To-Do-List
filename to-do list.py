import os

# Function to display the menu options
def display_menu():
    print("\n==== To-Do List Menu ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to view tasks
def view_tasks(tasks):
    print("\n==== To-Do List ====")
    if tasks:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in the list.")

# Function to add a task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to mark a task as done
def mark_task_done(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index] += " - Done"
        save_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()