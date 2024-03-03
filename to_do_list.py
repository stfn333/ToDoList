# Global lists to store tasks and marked completed tasks
task_list = []
marked_as_completed = []


def main_menu():
    """Display the main menu options."""
    print("""===== To-Do List Menu =====
    1. Add a new task
    2. Remove a task
    3. Mark a task as completed
    4. View all tasks
    5. Quit
    """)


def enter_choice_prompt():
    """
        Prompt the user to enter their choice.

        Returns:
            int: The user's choice as an integer.
        """
    choice = input("Enter your choice (1-4): ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
        print("Invalid index. Please enter a valid index.")
    else:
        return int(choice)


def add_a_new_task():
    """
       Add a new task to the task list.

       Returns:
           list: The updated task list.
       """
    task = input("Enter a task description: ")
    if task in task_list:
        view_all_tasks()
        yes_or_no = input("Task is already in list. Do you want to add it? [Y]es / [N]o: ")
        if yes_or_no.lower() not in ["y", "n"]:
            print("Please enter a valid answer.")
        else:
            if yes_or_no.lower() == "y":
                task_list.append(task)
                print(f"Task '{task}' added successfully!")
                return task_list
            else:
                print("Task was not added.")
    else:
        task_list.append(task)
        print(f"Task '{task}' added successfully!")
        return task_list


def remove_task():
    """
        Remove a task from the task list.

        Returns:
            None
        """
    if len(task_list) == 0:
        print("No tasks to remove! Please enter a task.")
    else:
        view_all_tasks()
        task_number = input("Enter a task number to remove: ")
        if not task_number.isdigit() or int(task_number) < 1 or int(task_number) > len(task_list):
            print("Invalid index. Please enter a valid index.")
        else:
            index = int(task_number) - 1
            removed = task_list.pop(index)
            if removed in marked_as_completed:
                marked_as_completed.remove(removed)
            print("Task was successfully removed.")


def view_all_tasks():
    """Display all tasks along with their completion status."""
    print("===== Tasks =====")
    for i, task in enumerate(task_list, start=1):
        if i not in marked_as_completed:
            print(f"{i}.[ ] {task}")
        else:
            print(f"{i}.[X] {task}")


def mark_as_completed():
    """
       Mark a task as completed.

       Returns:
           None
       """
    view_all_tasks()
    task_to_mark = input("Enter the index of the task to mark as completed: ")
    if not task_to_mark.isdigit() or int(task_to_mark) < 1 or int(task_to_mark) > len(task_list):
        print("Invalid index. Please enter a valid index.")
    else:
        index = int(task_to_mark) - 1
        if task_list[index] in marked_as_completed:
            print("Task is already completed.")
        else:
            marked_as_completed.append(int(task_to_mark))
            print("Task marked as completed!")


def quit_to_do_list():
    """Quit the to-do list program."""
    raise SystemExit("Exiting the program. Goodbye!")


def to_do_list_program():
    """Run the to-do list program."""
    while True:
        main_menu()
        choice = enter_choice_prompt()
        if choice == 1:
            add_a_new_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            mark_as_completed()
        elif choice == 4:
            view_all_tasks()
        elif choice == 5:
            quit_to_do_list()


# Run the to-do list program
to_do_list_program()










