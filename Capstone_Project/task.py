"""Task related class"""
import os


from datetime import datetime, date
from User_management.user import User

DATETIME_STRING_FORMAT = "%Y-%m-%d"



class Task:
    """Class that allow to create/list/eliminates tasks"""

    def __init__(self, _username = "", _title = "", _description = "", \
                 _due_date = "", _assigned_date = "", _completed = "") -> None:
        self.task_username = _username
        self.task_title = _title
        self.task_description = _description
        self.task_due_date = _due_date
        self.assigned_date = _assigned_date
        self.completed = _completed



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
        self.completed = False
        self._register_task()
        return True


    def _register_task(self):
        """Write the task in the tast.txt, storing it in the memory"""
        curr_date = date.today()


        with open("tasks.txt", "a", encoding="utf-8") as task_file:
            str_attrs = [
                self.task_username,
                self.task_title,
                self.task_description,
                self.task_due_date.strftime(DATETIME_STRING_FORMAT),
                curr_date.strftime(DATETIME_STRING_FORMAT),
                "Yes" if self.completed else "No"
               ]
            task_list_to_write = []
            task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n" + task_list_to_write)
            print("Task successfully added.")


    def get_tasks_from_file(self):
        """Retrieving the tasks from the tasks.txt file, if missing it will be created"""
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w", encoding="utf-8") as default_file:
                default_file.write("")

        with open("tasks.txt", 'r', encoding="utf=8") as tasks_file:
            task_data = tasks_file.read().split("\n")
            for task in task_data:
                if task:
                    task_info = task.split(';')
                    new_task = Task(*task_info)
            return new_task


