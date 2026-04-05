from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Task:
    title: str
    done: bool
    priority: int


class TaskManager:
    def __init__(self, tasks: Optional[list[Task]] = None):
        self.tasks = tasks or []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        return None

    def mark_done(self, title: str) -> bool:
        for task in self.tasks:
            if task.title == title:
                task.done = True
                return True
        return False

    def generate_report(self) -> dict:
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.done for task in self.tasks)
        incomplete_tasks = sum(not task.done for task in self.tasks)
        sorted_tasks = sorted(self.tasks, key=lambda task: task.priority)

        report = {"total_tasks": total_tasks,
                  "completed_tasks": completed_tasks,
                  "incomplete_tasks": incomplete_tasks,
                  "tasks": [asdict(task) for task in sorted_tasks]}

        return report
