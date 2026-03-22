# Blok 10 - Rozwiązania referencyjne

## B10-C1

```python
tasks = [
    {"title": "Nauka Pythona", "done": True, "priority": 2},
    {"title": "Przygotować CV", "done": False, "priority": 1},
    {"title": "Przeczytać o GCP", "done": False, "priority": 3},
]

completed_count = sum(task["done"] for task in tasks)
report = {
    "total": len(tasks),
    "completed": completed_count,
    "pending": len(tasks) - completed_count,
    "sorted_by_priority": sorted(tasks, key=lambda task: task["priority"]),
}

print(report)
```

## B10-C2

```python
import json
from pathlib import Path

output_path = Path("output/report.json")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=2)
```

## B10-C3 i B10-P1

```python
from dataclasses import asdict, dataclass


@dataclass
class Task:
    title: str
    done: bool
    priority: int


class TaskManager:
    def __init__(self, tasks: list[Task] | None = None):
        self.tasks = tasks or []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def mark_done(self, title: str) -> bool:
        for task in self.tasks:
            if task.title == title:
                task.done = True
                return True
        return False

    def generate_report(self) -> dict:
        completed_count = sum(task.done for task in self.tasks)
        sorted_tasks = sorted(self.tasks, key=lambda task: task.priority)

        return {
            "total": len(self.tasks),
            "completed": completed_count,
            "pending": len(self.tasks) - completed_count,
            "sorted_by_priority": [asdict(task) for task in sorted_tasks],
        }
```

## B10-S1

```python
def test_mark_done():
    manager = TaskManager([Task("Napisać kod", False, 2)])

    result = manager.mark_done("Napisać kod")

    assert result is True
    assert manager.tasks[0].done is True


def test_generate_report():
    manager = TaskManager([
        Task("B", False, 2),
        Task("A", True, 1),
    ])

    report = manager.generate_report()

    assert report["total"] == 2
    assert report["completed"] == 1
    assert report["pending"] == 1
    assert report["sorted_by_priority"][0]["title"] == "A"
```
