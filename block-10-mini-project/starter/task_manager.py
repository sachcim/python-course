from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool
    priority: int


class TaskManager:
    def __init__(self, tasks: list[Task] | None = None):
        self.tasks = tasks or []

    def add_task(self, task: Task) -> None:
        raise NotImplementedError("Uzupełnij metodę add_task")

    def mark_done(self, title: str) -> bool:
        raise NotImplementedError("Uzupełnij metodę mark_done")

    def generate_report(self) -> dict:
        raise NotImplementedError("Uzupełnij metodę generate_report")
