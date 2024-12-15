import pickle
import os

class TodoApp:
    def __init__(self, filename="todolist.pkl"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from a file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def save_todos(self):
        """Save todos to a file"""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.todos, f)

    def display_todos(self):
        """Display all todos"""
        if not self.todos:
            print("Your to-do list is empty!")
        else:
            for idx, task in enumerate(self.todos, start=1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        """Add a new task"""
        self.todos.append(task)
        self.save_todos()
        print(f"Task added: {task}")

    def remove_task(self, task_number):
        """Remove a task by its index"""
        if 0 < task_number <= len(self.todos):
            removed_task = self.todos.pop(task_number - 1)
            self.save_todos()
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")

    def update_task(self, task_number, new_task):
        """Update an existing task"""
        if 0 < task_number <= len(self.todos):
            old_task = self.todos[task_number - 1]
            self.todos[task_number - 1] = new_task
            self.save_todos()
            print(f"Task updated from: {old_task} to: {new_task}")
        else:
            print("Invalid task number.")

def main():
    app = TodoApp()

    while True:
        print("\n===== To-Do List =====")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Update a task")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            app.display_todos()
        elif choice == "2":
            task = input("Enter the task to add: ")
            app.add_task(task)
        elif choice == "3":
            app.display_todos()
            try:
                task_number = int(input("Enter the task number to remove: "))
                app.remove_task(task_number)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == "4":
            app.display_todos()
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                app.update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
