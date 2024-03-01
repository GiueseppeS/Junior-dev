# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
from User_management.user import User
from task import Task

DATETIME_STRING_FORMAT = "%Y-%m-%d"

""""Create a list"""
#USER_LIST : User = [] 
TASK_LIST : Task = []


""" def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''

    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        #continue
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()

    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


 """


# # Create tasks.txt if it doesn't exist
# if not os.path.exists("tasks.txt"):
#     with open("tasks.txt", "w") as default_file:
#         pass

# with open("tasks.txt", 'r') as task_file:
#     task_data = task_file.read().split("\n")
#     task_data = [t for t in task_data if t != ""]


# task_list = []
# for t_str in task_data:
#     curr_t = {}

#     # Split by semicolon and manually add each component
#     task_components = t_str.split(";")
#     curr_t['username'] = task_components[0]
#     curr_t['title'] = task_components[1]
#     curr_t['description'] = task_components[2]
#     curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
#     curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
#     curr_t['completed'] = True if task_components[5] == "Yes" else False

#     task_list.append(curr_t)




LOGGED_IN = False
while not LOGGED_IN:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    logged_user_instance = User()
    LOGGED_IN = logged_user_instance.authenticate(curr_user, curr_pass)

#USER_LIST.append(logged_user_instance)

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()

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
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        # for t in task_list:
        #     disp_str = f"Task: \t\t {t['title']}\n"
        #     disp_str += f"Assigned to: \t {t['username']}\n"
        #     disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #     disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #     disp_str += f"Task Description: \n {t['description']}\n"
        #     print(disp_str)
        pass


    elif menu == 'vm':
        pass
    #     '''Reads the task from task.txt file and prints to the console in the 
    #        format of Output 2 presented in the task pdf (i.e. includes spacing
    #        and labelling)
    #     '''
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