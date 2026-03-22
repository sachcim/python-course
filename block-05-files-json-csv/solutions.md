# Blok 5 - Rozwiązania referencyjne

## B5-C1

```python
import json
from pathlib import Path

with Path("data/users.json").open("r", encoding="utf-8") as file:
    users = json.load(file)

for user in users:
    print(user["name"])
```

## B5-C2

```python
import json
from pathlib import Path

source_path = Path("data/users.json")
target_path = Path("data/users_updated.json")

with source_path.open("r", encoding="utf-8") as file:
    users = json.load(file)

users.append({"name": "Tomek", "age": 29})

with target_path.open("w", encoding="utf-8") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
```

## B5-C3

```python
import csv
from pathlib import Path

scores = []

with Path("data/scores.csv").open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append(int(row["score"]))

average_score = sum(scores) / len(scores)
print(average_score)
```

## B5-P1

```python
import csv
from pathlib import Path

with Path("data/scores.csv").open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["score"]) > 80:
            print(row["name"])
```

## B5-S1

```python
import csv
import json
from pathlib import Path

with Path("data/users.json").open("r", encoding="utf-8") as file:
    users = json.load(file)

top_scores = []
with Path("data/scores.csv").open("r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["score"]) > 80:
            top_scores.append({
                "name": row["name"],
                "score": int(row["score"]),
            })

report = {
    "user_count": len(users),
    "top_scores": top_scores,
}

with Path("data/report.json").open("w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=2)
```
