class Book:
    def __init__ (self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self):
        print(f'{self.title} - {self.author}')

class Task:
    def __init__ (self, title: str, done: bool = False):
        self.title = title
        self.done = done

    def mark_done(self):
        self.done = True

    def describe(self):
        print(f'{self.title} - {"" if self.done else "nie"}wykonane')

class BankAccount:
    def __init__ (self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
    def withdraw(self, amount: float):
        tryBalance = self.balance - amount
        if tryBalance < 0:
            print("Not enough money")
        else:
            self.balance -= amount

class TaskList:
    def __init__ (self, tasks: list[Task]):
        self.tasks: list[Task]  = tasks

    def add_task(self, task: Task):
        self.tasks.append(task)
        print("Task added")
    def undone_tasks(self):
        undone_tasks = []
        for index, task in enumerate(self.tasks):
            if not task.done:
                undone_tasks.append(task)
        return undone_tasks

if __name__ == "__main__":
    firstBook = Book("Pan Tadeusz", "Adam Mickiewicz")
    firstBook.describe()
    firstBook.title = "Balladyna"
    firstBook.author = "Juliusz Słowacki"
    firstBook.describe()

    firstTask = Task("Nauczyc się pythona")
    firstTask.describe()
    firstTask.mark_done()
    firstTask.describe()

    firstBankAccount = BankAccount("Michal")
    firstBankAccount.deposit(1000)
    print(firstBankAccount.balance)
    firstBankAccount.withdraw(900)
    print(firstBankAccount.balance)

    task_list = TaskList([firstTask])
    task_list.add_task(Task("Nauczyć się zip"))
    task_list.add_task(Task("Nauczyć się python lambda"))
    task_list.add_task(Task("zrobic mini project"))
    task_list.add_task(Task("nauczyc sie dataclass"))
    task_list.add_task(Task("odpocząć"))
    task_list.add_task(Task("Zrobić zakupy"))
    task_list.add_task(Task("Zrobić ćwiczenia", done=True))

    undone_tasks = task_list.undone_tasks()
    for task in undone_tasks:
        task.describe()