# Blok 7 - Rozwiązania referencyjne

## B7-C1

```python
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self) -> str:
        return f"{self.title} - {self.author}"
```

## B7-C2

```python
class Task:
    def __init__(self, title: str, done: bool = False):
        self.title = title
        self.done = done

    def mark_done(self) -> None:
        self.done = True
```

## B7-C3

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

## B7-P1

```python
book = Book("Python od zera", "Jan Kowalski")
print(book.describe())

task = Task("Napisać ćwiczenia")
task.mark_done()
print(task.done)

account = BankAccount("Michał", 100)
account.deposit(50)
print(account.withdraw(70))
print(account.balance)
```

## B7-S1

```python
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.done]
```
