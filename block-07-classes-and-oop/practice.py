from typing import Optional
class Book:
    def __init__ (self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self):
        return f'{self.title} - {self.author}'

class Task:
    def __init__ (self, title: str, done: bool = False):
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True

    def describe(self):
        return f'{self.title} - {"" if self.done else "nie"}wykonane'

class BankAccount:
    def __init__ (self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            print("Value must be positive")
    def withdraw(self, amount: float):
        if amount < 0:
            print("Value must be positive")
        else:
            tryBalance = self.balance - amount
            if tryBalance < 0:
                print("Not enough money")
            else:
                self.balance -= amount

class TaskList:
    def __init__ (self, tasks : Optional[list[Task]] = None):
        self.tasks = [] if tasks is None else tasks

    def add_task(self, task: Task):
        self.tasks.append(task)
    def undone_tasks(self):
        undone_tasks = []
        for task in self.tasks:
            if not task.done:
                undone_tasks.append(task)
        return undone_tasks

if __name__ == "__main__":
    firstBook = Book("Pan Tadeusz", "Adam Mickiewicz")
    print(firstBook.describe())
    firstBook.title = "Balladyna"
    firstBook.author = "Juliusz Słowacki"
    print(firstBook.describe())

    firstTask = Task("Nauczyc się pythona")
    print(firstTask.describe())
    firstTask.mark_done()
    print(firstTask.describe())

    firstBankAccount = BankAccount("Michal")
    firstBankAccount.deposit(1000)
    print(firstBankAccount.balance)
    firstBankAccount.withdraw(900)
    print(firstBankAccount.balance)

    task_list = TaskList()
    task_list.add_task(Task("Nauczyć się zip"))
    task_list.add_task(Task("Nauczyć się python lambda"))
    task_list.add_task(Task("zrobic mini project"))
    task_list.add_task(Task("nauczyc sie dataclass"))
    task_list.add_task(Task("odpocząć"))
    task_list.add_task(Task("Zrobić zakupy"))
    task_list.add_task(Task("Zrobić ćwiczenia", done=True))

    undone_tasks = task_list.undone_tasks()
    for task in undone_tasks:
        print(task.describe())