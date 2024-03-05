import os
from datetime import date

class Overview():
    """Class that generates reports of users and tasks"""

    number_of_generated_tasks = ""
    completed_tasks = ""
    overdue_task = ""
    uncompleted_tasks = ""
    # def generate_reports(self):
    #     """Create two files task_overview and user_overvies with all the informations"""
    #     self.generate_task_report()

    def __str__(self) -> str:
        pass

    def generate_task_report(self, _number_of_tasks, _tasks_list):
        """Generate the report for the tasks"""
        report_to_write = []
        number_of_generated_tasks = _number_of_tasks
        completed_tasks = self.completed_tasks(_tasks_list)
        overdue_task = self.overdue_tasks(_tasks_list)
        uncompleted_tasks = len(_tasks_list) - completed_tasks
        incomplete_percentage, overdue_percentage = self.calculate_percentage(_number_of_tasks, uncompleted_tasks, overdue_task)
        str_attr = [
           str(number_of_generated_tasks),
           str(completed_tasks),
           str(uncompleted_tasks),
           str(overdue_task),
           f"{incomplete_percentage:0.2f}%",
           f"{overdue_percentage:0.2f}%"
         ]
        report_to_write.append(";".join(str_attr))
        self.write_report("task_overview", report_to_write)


    def calculate_percentage(self, _num_task, _uncompled_tasks, _overdue_tasks):
        """Calculate percentage of completed and uncompleted tasks and return"""
        if _num_task > 0:
            incomplete_percentage = (_uncompled_tasks / _num_task) * 100
            overdue_percentage = (_overdue_tasks / _num_task) * 100
            return incomplete_percentage, overdue_percentage

    def completed_tasks(self, _tasks_list):
        """Check the number of completed tasks"""
        completed_tasks = sum(1 if task.completed else 0 for task in _tasks_list)
        return completed_tasks
    
    def overdue_tasks(self, _tasks_list):
        """Check the number of ovedue tasks"""
        overdue_tasks = sum(1 if task.task_due_date < date.today() and not task.completed else 0 for task in _tasks_list)
        return overdue_tasks



    def write_report(self, file_name : str, string_to_write):
        """Write the reports on file"""
        with open(file_name + ".txt", 'w', encoding="utf=8") as file:
            if file_name == "task_overview":
                for string in string_to_write:
                    file.write(string + "\n")
            
            if file_name == "user_overview":
                pass

    
    def task_overview_to_text(self):
        """Write in human readable the overview report"""