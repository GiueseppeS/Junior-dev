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

""""Create a list"""



def clear_screen():
    """Clearing screen funtion"""
    os.system("cls")

def display_selection_menu():
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





#USER_LIST : User = [] 
TASK_LIST : Task = []

logged_user : str = ""




LOGGED_IN = False
while not LOGGED_IN:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    logged_user_instance = User()
    LOGGED_IN = logged_user_instance.authenticate(curr_user, curr_pass)

#USER_LIST.append(logged_user_instance)
logged_user = logged_user_instance.username
clear_screen()
print("Logged in as " + logged_user)

#Creating an instance of the Task class in order to retrieve the tasks from the tasks.txt file
tasks_getter = Task()
TASK_LIST = tasks_getter.get_tasks_from_file()

time.sleep(1)

del tasks_getter

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = display_selection_menu()

    if menu == 'r':
        new_user_instance = User()
        new_user_instance.reg_user()

    elif menu == 'a':
        task_instance = Task()
        TASK_IS_CORRECT = task_instance.add_task()
        #Adding the new user to the users list
        if TASK_IS_CORRECT:
            TASK_LIST.append(task_instance)

    elif menu == 'va':
        #Visualise all the tasks with the user assigned, the date, 
        #the due date and the task description

        task_instance = Task()
        TASK_LIST = task_instance.get_tasks_from_file()

        clear_screen()
        if len(TASK_LIST) > 0:
            for task in TASK_LIST:
                print(task)
        else:
            print("No tasks to show")


    elif menu == 'vm':
        pass
    #     '''Reads the task from task.txt file and prints to the console in the 
    #        format of Output 2 presented in the task pdf (i.e. includes spacing
    #        and labelling)
    #     '''a
    #     for t in task_list:
    #         if t['username'] == curr_user:
    #             disp_str = f"Task: \t\t {t['title']}\n"
    #             disp_str += f"Assigned to: \t {t['username']}\n"
    #             disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    #             disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    #             disp_str += f"Task Description: \n {t['description']}\n"
    #             print(disp_str)
                
    
    # elif menu == 'ds' and curr_user == 'admin': 
    #     '''If the user is an admin they can display statistics about number of users
    #         and tasks.'''
    #     num_users = len(username_password.keys())
    #     num_tasks = len(task_list)

    #     print("-----------------------------------")
    #     print(f"Number of users: \t\t {num_users}")
    #     print(f"Number of tasks: \t\t {num_tasks}")
    #     print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")