# Blok 6 - Rozwiązania referencyjne

## B6-C1

```python
try:
    number = int(input("Podaj liczbę: "))
    result = 100 / number
except ValueError:
    print("To nie była poprawna liczba.")
except ZeroDivisionError:
    print("Nie można dzielić przez zero.")
else:
    print(result)
```

## B6-C2

```python
import json
from pathlib import Path


def load_json_file(path: str) -> list | dict | None:
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Plik nie istnieje.")
    except json.JSONDecodeError:
        print("Plik nie zawiera poprawnego JSON.")
    return None
```

## B6-C3

```python
def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("To nie była liczba. Spróbuj ponownie.")
```

## B6-P1

```python
values = ["10", "abc", "25", "", "7"]
numbers = []

for value in values:
    try:
        numbers.append(int(value))
    except ValueError:
        print(f"Odrzucono wartość: {value!r}")

print(numbers)
```

## B6-S1

```python
import csv
from pathlib import Path


def load_scores(path: str) -> list[dict]:
    scores = []

    try:
        with Path(path).open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    scores.append({
                        "name": row["name"],
                        "score": int(row["score"]),
                    })
                except ValueError:
                    print(f"Pominięto błędny wynik dla: {row['name']}")
    except FileNotFoundError:
        return []

    return scores
```
