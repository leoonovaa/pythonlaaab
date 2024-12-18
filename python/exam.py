import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt

# Клас команд для додавання витрат
class Command:
    def execute(self):
        print("HHHH")

class AddExpenseCommand(Command):
    def __init__(self, expense, amount, budget):
        self.expense = expense
        self.amount = amount
        self.budget = budget

    def execute(self):
        self.budget.add_expense(self.expense, self.amount)

# Клас бюджету, який містить всі витрати
class Budget:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, expense, amount):
        if expense in self.expenses:
            self.expenses[expense] += amount
        else:
            self.expenses[expense] = amount

    def get_expenses(self):
        return self.expenses

    def save(self, filename='budget.json'):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)

    def load(self, filename='budget.json'):
        try:
            file = open(filename, 'r')
            
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = {}

# Клас контролера для виконання команд
class BudgetController:
    def __init__(self):
        self.history = []

    def execute(self, command):
        self.history.append(command)
        command.execute()

# Функція для відображення графіку витрат
def plot_expenses(budget):
    categories = list(budget.get_expenses().keys())
    amounts = list(budget.get_expenses().values())

    plt.bar(categories, amounts)
    plt.xlabel('Категорії')
    plt.ylabel('Сума витрат')
    plt.title('Графік витрат')
    plt.xticks(rotation=45)
    plt.show()

# Графічний інтерфейс
class BudgetApp:
    def __init__(self, root, budget, controller):
        self.root = root
        self.budget = budget
        self.controller = controller

        self.root.title("Програма управління бюджетом")

        # Ввід категорії витрат
        self.category_label = tk.Label(root, text="Категорія витрат:")
        self.category_label.grid(row=0, column=0)

        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=0, column=1)

        # Ввід суми витрат
        self.amount_label = tk.Label(root, text="Сума витрат:")
        self.amount_label.grid(row=1, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        # Кнопка для додавання витрат
        self.add_button = tk.Button(root, text="Додати витрату", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # Кнопка для збереження бюджету
        self.save_button = tk.Button(root, text="Зберегти бюджет", command=self.save_budget)
        self.save_button.grid(row=3, column=0, columnspan=2)

        # Кнопка для відображення графіка витрат
        self.plot_button = tk.Button(root, text="Показати графік", command=self.show_graph)
        self.plot_button.grid(row=4, column=0, columnspan=2)

        self.load_budget()

    def add_expense(self):
        category = self.category_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if category and amount > 0:
                command = AddExpenseCommand(category, amount, self.budget)
                self.controller.execute(command)
                messagebox.showinfo("Успіх", f"Витрата на категорію '{category}' на суму {amount} додано!")
                self.clear_inputs()  # Очищаємо поля після додавання витрати
            else:
                messagebox.showwarning("Помилка", "Введіть правильні дані!")
        except ValueError:
            messagebox.showwarning("Помилка", "Сума повинна бути числом!")

    def save_budget(self):
        self.budget.save()
        messagebox.showinfo("Успіх", "Бюджет збережено!")

    def load_budget(self):
        self.budget.load()

    def show_graph(self):
        plot_expenses(self.budget)

    def clear_inputs(self):
        """Очищає поля вводу після додавання витрат"""
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

# Головна програма
if __name__ == "__main__":
    budget = Budget()
    controller = BudgetController()
    root = tk.Tk()
    app = BudgetApp(root, budget, controller)
    root.mainloop()