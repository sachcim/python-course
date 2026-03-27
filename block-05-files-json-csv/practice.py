import json, csv
from pathlib import Path

# path = Path("data/users.json")
#
# with path.open("r", encoding="utf-8") as file:
#     users = json.load(file)
#
# users.append({"name": "Tomek", "age": 29})
#
# with Path("data/users_updated.json").open("w", encoding="utf-8") as file:
#     json.dump(users, file, ensure_ascii=False, indent=2)
#
#
def read_json_file(file_path):
    with Path(file_path).open("r", encoding="utf-8") as f:
        return json.load(f)

def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_csv_file(file_path):
    with Path(file_path).open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    users = read_json_file("data/users.json")
    for u in users:
        print(u["name"])
    users.append({"name": "Tomasz", "age": 23})
    write_json_file("data/users_updated.json", users)

    users_score = read_csv_file("data/scores.csv")
    avg = sum([int(u["score"]) for u in users_score]) / len(users_score)
    top_scores = [u["name"] for u in users_score if int(u["score"]) > 80]
    print(top_scores)

    users = read_json_file("data/users.json")
    users_count = len(users)

    report = {
        'user_count': users_count,
        'top_scores': top_scores,
    }
    write_json_file("data/report.json", report)