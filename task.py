#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task: #класс Task, который позволяет управлять задачами (делами).
    def __init__(self):  #  экземпляр класса Task.
        self.tasks = [] # список задач.

    def add_task(self, description, deadline): # функция добавления задачи.
        self.tasks.append({'description': description, 'deadline': deadline, 'status': 'не выполнено'}) # добавляем задачу в список задач.
        print(f'Задача "{description}" добавлена.') # выводим сообщение о добавлении задачи.

    def mark_task_as_completed(self, description): # функция отметки выполненных задач.
        for task in self.tasks: # перебираем список задач.
            if task['description'] == description: # если задача найдена.
                task['status'] = 'выполнено' # изменяем статус задачи.
                print(f'Задача "{description}" выполнена.') # выводим сообщение о выполнении задачи.
                return # выходим из функции.
        print(f'Задача "{description}" Выполнена.')

    def print_tasks(self): # функция вывода списка текущих задач.
        print('Текущие задачи:')  # выводим сообщение о текущих задачах.
        for task in self.tasks: # перебираем список задач.
            if task['status'] == 'не выполнено': # если задача не выполнена.
                print(f'Описание: {task["description"]}, Срок: {task["deadline"]}') # выводим задачу.

task_men = Task()
task_men.add_task("Попить воды", "18.10.2024")
task_men.add_task("Погулять", "18.10.2024")
task_men.mark_task_as_completed("Почитать книгу")
task_men.print_tasks()

