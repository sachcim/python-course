from pathlib import Path
import sys


STARTER_PATH = Path(__file__).resolve().parents[1] / "starter"
sys.path.append(str(STARTER_PATH))

from task_manager import Task, TaskManager


def test_add_task_increases_count():
    manager = TaskManager()

    manager.add_task(Task("Napisać test", False, 2))

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Napisać test"


def test_mark_done_updates_task_status():
    manager = TaskManager([
        Task("Ukończyć blok 10", False, 1),
    ])

    result = manager.mark_done("Ukończyć blok 10")

    assert result is True
    assert manager.tasks[0].done is True


def test_generate_report_counts_and_sorts():
    manager = TaskManager([
        Task("Task B", False, 3),
        Task("Task A", True, 1),
        Task("Task C", False, 2),
    ])

    report = manager.generate_report()

    assert report["total"] == 3
    assert report["completed"] == 1
    assert report["pending"] == 2
    assert report["sorted_by_priority"][0]["title"] == "Task A"
