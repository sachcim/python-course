import json
from pathlib import Path

DIR = Path(__file__).parent.parent
DATA_DIR = DIR / "data"
REPORTS_DIR = DIR / "reports"


def load_tasks(filename: str) -> list[dict]:
    file_path = DATA_DIR / filename
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_report(report: dict, filename: str) -> None:
    file_path = REPORTS_DIR / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)
