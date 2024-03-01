from User_management.user import User
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"



class Task:
    """Class that allow to create/list/eliminates tasks"""

    def __init__(self) -> None:
        self.task_username = ""
        self.task_title = ""
        self.task_description = ""
        self.task_due_date = ""
        self.assigned_date = ""
        self.completed : bool = False



    def add_task(self) -> bool:
        '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''

        users_list = User().get_register_user()
        _task_username = input("Name of person assigned to task: ")
        if _task_username not in users_list:
            print("User does not exist. Please enter a valid username")
            return False
        self.task_username = _task_username
        self.task_title = input("Title of Task: ")
        self.task_description = input("Description of Task: ")
        while True:
            try:
                _task_due_date = input("Due date of task (YYYY-MM-DD): ")
                self.task_due_date = datetime.strptime(_task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")
         # Then get the current date.
        self.assigned_date = date.today()
        return True