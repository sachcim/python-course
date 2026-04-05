from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


TASK_MANAGER_PATH = Path(__file__).resolve().parents[1] / "starter" / "task_manager.py"
spec = spec_from_file_location("task_manager_under_test", TASK_MANAGER_PATH)
assert spec is not None and spec.loader is not None
task_manager_module = module_from_spec(spec)
spec.loader.exec_module(task_manager_module)

Task = task_manager_module.Task
TaskManager = task_manager_module.TaskManager


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

    assert report["total_tasks"] == 3
    assert report["completed_tasks"] == 1
    assert report["incomplete_tasks"] == 2
    assert report["tasks"][0]["title"] == "Task A"
