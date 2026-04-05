from dataclasses import asdict


from starter.task_report import load_tasks, save_report
from starter.task_manager import Task
if __name__ == "__main__":
    tasks = load_tasks("tasks.json")
    tasks = [Task(**task) for task in tasks]

    total_tasks = len(tasks)
    completed_tasks = sum(task.done for task in tasks)
    incomplete_tasks = sum(not task.done for task in tasks)
    sorted_tasks = sorted(tasks, key=lambda task: task.priority, reverse=True)
    report = {"total_tasks": total_tasks,
              "completed_tasks": completed_tasks,
              "incomplete_tasks": incomplete_tasks,
              "tasks": [asdict(task) for task in sorted_tasks]}
    save_report(report, "report.json")