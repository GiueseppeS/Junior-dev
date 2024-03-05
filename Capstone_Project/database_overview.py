import os
from datetime import date

class Overview():
    """Class that generates reports of users and tasks"""


    def generate_reports(self):
        """Create two files task_overview and user_overvies with all the informations"""
        pass


    def generate_task_report(self, _number_of_tasks, _tasks_list):
        """Generate the report of for the tasks"""
        number_of_generated_tasks = _number_of_tasks
        completed_tasks = sum(task.completed for task in _tasks_list)
        overdue_taks = sum(task.task_due_date < date.today() and not task.completed for task in _tasks_list)
        uncompleted_tasks = len(_tasks_list) - completed_tasks
        incomplete_percentage = (uncompleted_tasks / number_of_generated_tasks) * 100
        overdue_percentage = (overdue_taks * number_of_generated_tasks) * 100
        str_attr = [
           str(number_of_generated_tasks),
           str(completed_tasks),
           str(uncompleted_tasks),
           str(overdue_taks),
           f"{incomplete_percentage:.2f%}",
           f"{overdue_percentage:.2f%})"
         ]



    def write_report(self, file_name : str, string_to_write):
        with open(file_name + "_" + date.today + "_" + ".txt", 'w', encoding="utf=8") as file:
            if file_name == "task_overview":
                pass
            
            if file_name == "user_overview":
                pass

    
    def task_overview_to_text(self):
        """Write in human readable the overview report"""