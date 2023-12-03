def show_menu():
    print("****/Todo List/****")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark task as complete")
    print("4. Quit")

def add_task(todo_list, task):
    '''
    Add task function take a todo list which is used to store all it todo inside it
    Task is a new todo which will be added to the todo_list
    Append function of the list is used to add a new element of the end of the list
    '''
    todo_list.append(task)
    print(f"Task{task} added to the todo list")

def view_tasks(todo_list):
    '''
    view_task function takes a todo_list and shows all of the todos present inside it
    First, we are checking if the todo_list doesn't contain anything and if it doesn't contain anything, then it
    if it contain anything, then use a for loop to itrate in the todo_list and getting the index
    and the task and printing it using Fstring
    enumerate function is used to put some condition like here, we are putting that the index should
    start with 1
    '''

    if not todo_list:
        print("Todo list to empty")
    else:
        print("/n Current Task")

        for index, task in enumerate(todo_list, start=1):
            print(f"{index}, {task}")

def mark_completed(todo_list, task_index):
    '''
    mark_complete index takes todo list and the index of the task which you want to delete from the list
    Checking if the task index is present in todo_list or not, it it's present removing the task from 
    the list using pop function and pop function
    take the index of the list element which we need to delete
    '''

    if 1<= task_index <= len(todo_list):
        Completed_task=todo_list. pop(task_index -1)
        print(f"Task {Completed_task} marked as completed")
    else:
        print("Invalid task index")

def todo_list_app():
    todo_list = []
    while True:
        # While true is an infinite looop which will ask for the user choice again and again and if you want to stop the while loop then you need 
        # a break statement so we all using break statement on 'choice = 4'
        show_menu()
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            task= input("Enter the task: ")
            add_task(todo_list, task)

        elif choice == '2':
            view_tasks(todo_list)

        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(todo_list, task_index)

        elif choice == '4':
            print("Quitting todo list app! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

todo_list_app()