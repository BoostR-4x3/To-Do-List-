from datetime import datetime
tasks = []

def add_tasks():
    task = input("Enter the task you want to add: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    print("Set priority: [1] High 🔺  [2] Medium 🔸  [3] Low 🔹")
    priority_choice = input("Enter choice (1/2/3): ")

    if priority_choice == "1":
        priority = "🔺 High"
    elif priority_choice == "2":
        priority = "🔸 Medium"
    elif priority_choice == "3":
        priority = "🔹 Low"
    else:
        priority = "🔹 Low"  # default fallback

    tasks.append({
        "task": task,
        "done": False,
        "due": due_date,
        "priority": priority
    })

    print(f'"{task}" has been added with due date {due_date} and priority {priority}.')

def view_tasks():
    if not tasks:
        print("Your To Do list is empty.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task["done"] else "❌"
            due = task.get("due", "No due date")
            days_left_msg = ""

            try:
                due_date = datetime.strptime(due, "%Y-%m-%d").date()
                today = datetime.today().date()
                days_left = (due_date - today).days

                if days_left < 0:
                    days_left_msg = "🔴 Overdue!"
                elif days_left == 0:
                    days_left_msg = "🟡 Due today!"
                elif days_left == 1:
                    days_left_msg = "🟡 Due tomorrow!"
                else:
                    days_left_msg = f"({days_left} days left)"
            except ValueError:
                days_left_msg = "❌ Invalid date format"

            priority = task.get("priority", "🔹 Low")
            print(f"{i}. [{status}] {task['task']} (Due: {due}) {days_left_msg} | Priority: {priority}")

def save_tasks():
    pass  # (Optional for now)

def mark_done():
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("Which task do you want to mark as done?")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['task']}")

    try:
        choice = int(input("Enter the task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print(f'Task "{tasks[choice - 1]["task"]}" marked as done ✅')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_tasks():
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("Which task do you want to remove?")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']}")

    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f'"{removed["task"]}" has been removed from your list.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    pending = total - completed

    today = datetime.today().date()
    overdue = sum(
        1 for t in tasks
        if not t["done"] and t.get("due") and is_overdue(t.get("due"), today)
    )

    high_priority = sum(1 for t in tasks if t.get("priority") == "🔺 High")

    print("\n📊 --- TASK STATS ---")
    print(f"📋 Total Tasks      : {total}")
    print(f"❌ Pending Tasks    : {pending}")
    print(f"✔️ Completed Tasks  : {completed}")
    print(f"🔴 Overdue Tasks    : {overdue}")
    print(f"🔺 High Priority    : {high_priority}")

def is_overdue(due_str, today):
    try:
        due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
        return due_date < today
    except:
        return False


# ✅ Menu Loop for the user
while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add task")
    print("2. View Tasks")
    print("3. Mark as completed")
    print("4. Remove task")
    print("5. View Stats")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_tasks()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_tasks()
    elif choice == '5':
        show_stats()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break





