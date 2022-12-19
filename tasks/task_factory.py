from tasks.task_four import TaskFour
from tasks.task_one import TaskOne
from tasks.task_three import TaskThree
from tasks.task_two import TaskTwo


class TaskFactory():
    def __init__(self):
        pass

    def generate_task(self, alg_name: str):
        if alg_name == 'Task1':
            return TaskOne()
        elif alg_name == 'Task2':
            return TaskTwo()
        elif alg_name == 'Task3':
            return TaskThree()
        elif alg_name == 'Task4':
            return TaskFour()
        else:
            pass
