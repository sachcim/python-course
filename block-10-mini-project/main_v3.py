from starter.task_report import load_tasks, save_report
from starter.task_manager import Task, TaskManager

if __name__ == "__main__":
    tasks = load_tasks("tasks.json")
    tasks = [Task(**task) for task in tasks]
    task_manager = TaskManager(tasks)

    task_manager.add_task(Task(title="Buy groceries", done=False, priority=1))
    task_manager.mark_done("Przygotować CV")
    save_report(task_manager.generate_report(), "report.json")