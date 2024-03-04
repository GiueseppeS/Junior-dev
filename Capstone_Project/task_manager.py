# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
import time
from datetime import datetime, date
from User_management.user import User
from task import Task

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def clear_screen():
    """Clearing screen funtion"""
    os.system("cls")


def display_selection_menu():
    """Display the selection menu"""
    print()
    _menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()
    return _menu


def display_statistics():
    '''If the user is an admin they can display statistics about number of users
            and tasks.'''
    num_user = len(USER_LIST)
    num_task = len(TASK_LIST)
    clear_screen()
    print("-----------------------------------")
    print(f"Number of users: \t\t {num_user}")
    print(f"Number of tasks: \t\t {num_task}")
    print("-----------------------------------")
    time.sleep(1)

#Creating list of users from the user.txt file
USER_LIST : User = User().get_register_user_from_file()

#Creating a list of tasks from the task.txt
TASK_LIST = Task().get_tasks_from_file()

#Keeping track of the logged user
logged_user : str = ""


user = User().authenticate()

#USER_LIST.append(logged_user_instance)
logged_user = user.username
clear_screen()
print("Logged in as " + logged_user)

#retrieve the tasks from the tasks.txt file
TASK_LIST = Task().get_tasks_from_file()

time.sleep(1)




while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = display_selection_menu()

    if menu == 'r':
        #new_user_instance = User()
        User().reg_user()

    elif menu == 'a':
        new_task = Task()
        TASK_IS_CORRECT = new_task.add_task()
        #Adding the new user to the users list
        if TASK_IS_CORRECT:
            TASK_LIST.append(new_task)

    elif menu == 'va':
        #Visualise all the tasks with the user assigned, the date, 
        #the due date and the task description
        clear_screen()
        if len(TASK_LIST) > 0:
            for task in TASK_LIST:
                print(task)
        else:
            print("No tasks to show")


    elif menu == 'vm':
    #     '''Reads the task from task.txt file and prints to the console in the 
    #        format of Output 2 presented in the task pdf (i.e. includes spacing
    #        and labelling)
    #     '''a
        user_selection : int
        while True:
            if len(TASK_LIST) <= 0:
                print("No task assigned yet")
                break
            else:
                for task_num, task in enumerate(TASK_LIST):
                    if task.task_username == logged_user:
                        disp_str =  f"\nTask number: \t {task_num}"
                        disp_str += f"\nTask: \t\t {task.task_title}\n"
                        disp_str += f"Assigned to: \t {task.task_username}\n"
                        disp_str += f"Date Assigned: \t {task.assigned_date}\n"
                        disp_str += f"Due Date: \t {task.task_due_date}\n"
                        disp_str += f"Task Description: \n {task.task_description}\n"
                        print(disp_str)
                user_selection = int(input("Select a task or -1 to exit"))
                if user_selection == -1:
                    break
                elif user_selection >= 0 and user_selection <= len(TASK_LIST) -1:
                    clear_screen()
                    selected_task = TASK_LIST[user_selection]
                    print(f"You selected the task {selected_task.task_title}")
                    selection = input("Do you want to: \n 1: Mark the task as complete\n 2: Edit the task")
                else:
                    print("Wrong selection")

                
    
    elif menu == 'ds' and logged_user == 'admin': 
        display_statistics()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")