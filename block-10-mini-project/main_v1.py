from starter.task_report import load_tasks, save_report

if __name__ == "__main__":
    tasks = load_tasks("tasks.json")

    total_tasks = len(tasks)
    completed_tasks = sum(task["done"] for task in tasks)
    incomplete_tasks = sum(not task["done"] for task in tasks)
    sorted_tasks = sorted(tasks, key=lambda task: task["priority"], reverse=True)

    report = {"total_tasks": total_tasks,
              "completed_tasks": completed_tasks,
              "incomplete_tasks": incomplete_tasks,
              "tasks": sorted_tasks}

    save_report(report, "report.json")