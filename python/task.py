class Task:
    def __init__(self, title, description, priority, status="Не виконано"):
        self.title = title
        self.description = description
        self.priority = priority  
        self.status = status  

    def __repr__(self):
        return f"Завдання: {self.title}, Опис: {self.description}, Пріоритет: {self.priority}, Статус: {self.status}"


class TaskList:
    def __init__(self):
        self.tasks = {}
        self.task_id = 0

    def add_task(self, title, description, priority):
        self.task_id += 1
        new_task = Task(title, description, priority)
        self.tasks[self.task_id] = new_task
        print(f"Завдання '{title}' додано з ID: {self.task_id}")

    def update_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            print(f"Статус завдання з ID: {task_id} змінено на '{status}'.")
        else:
            print(f"Завдання з ID: {task_id} не знайдено.")

    def filter_tasks_by_priority(self, priority):
        filtered_tasks = {task_id: task for task_id, task in self.tasks.items() if task.priority == priority}
        return filtered_tasks

    def filter_tasks_by_status(self, status):
        filtered_tasks = {task_id: task for task_id, task in self.tasks.items() if task.status == status}
        return filtered_tasks

    def get_statistics(self):
        completed_tasks = sum(1 for task in self.tasks.values() if task.status == "Виконано")
        incomplete_tasks = sum(1 for task in self.tasks.values() if task.status == "Не виконано")
        return {
            "Виконано": completed_tasks,
            "Не виконано": incomplete_tasks
        }

    def display_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"ID: {task_id}, {task}")


task_list = TaskList()
task_list.add_task("Вивчити Python", "Прочитати документацію", "Високий")
task_list.add_task("Зробити зарядку", "Зробити ранкову зарядку", "Середній")
task_list.add_task("Придбати продукти", "Купити овочі", "Низький")
task_list.add_task("Придбати продукти", "Купити фрукти", "Низький")

task_list.update_status(1, "Виконано")
task_list.update_status(3, "Виконано")


print("Завдання з високим пріоритетом:")
for task_id, task in task_list.filter_tasks_by_priority("Високий").items():
    print(f"ID: {task_id}, {task}")

print("Невиконані завдання:")
for task_id, task in task_list.filter_tasks_by_status("Не виконано").items():
    print(f"ID: {task_id}, {task}")


print("Статистика завдань:")
stats = task_list.get_statistics()
print(stats)


print("Усі завдання:")
task_list.display_tasks()
