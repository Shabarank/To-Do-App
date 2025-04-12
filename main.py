tasks = []

def show_menu():
  print("\n--- To-Do List Menu ---")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task as Complete")
  print("4. Delete Task")
  print("5. Exit")
def add_task():
  task = input("Enter the task: ")
  tasks.append({"task": task, "completed": False})
  print(f"Task '{task}' added.")
def add_task():
  task = input("Enter the task: ")
  tasks.append({"task": task, "completed": False})
  print(f"Task '{task}' added.")
def view_tasks():
  if not tasks:
      print("No tasks yet.")
      return
  print("\nYour Tasks:")
  for i, task in enumerate(tasks, start=1):
      status = "✓" if task["completed"] else "✗"
      print(f"{i}. [{status}] {task['task']}")
def complete_task():
  view_tasks()
  try:
      task_num = int(input("Enter task number to mark complete: "))
      tasks[task_num - 1]["completed"] = True
      print("Task marked as complete.")
  except (IndexError, ValueError):
      print("Invalid task number.")
def delete_task():
  view_tasks()
  try:
      task_num = int(input("Enter task number to delete: "))
      removed = tasks.pop(task_num - 1)
      print(f"Deleted task: {removed['task']}")
  except (IndexError, ValueError):
      print("Invalid task number.")
while True:
  show_menu()
  choice = input("Choose an option (1-5): ")

  if choice == "1":
      add_task()
  elif choice == "2":
      view_tasks()
  elif choice == "3":
      complete_task()
  elif choice == "4":
      delete_task()
  elif choice == "5":
      print("Goodbye!")
      break
  else:
      print("Invalid choice. Try again.")
