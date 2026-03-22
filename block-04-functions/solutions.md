# Blok 4 - Rozwiązania referencyjne

## B4-C1

```python
def get_larger_number(a: float, b: float) -> float:
    if a > b:
        return a
    return b
```

## B4-C2

```python
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Lista liczb nie może być pusta")
    return sum(numbers) / len(numbers)
```

## B4-C3

```python
def get_active_users(users: list[dict]) -> list[dict]:
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users
```

## B4-P1

```python
def find_user_by_name(users: list[dict], name: str) -> dict | None:
    for user in users:
        if user["name"] == name:
            return user
    return None
```

## B4-S1

```python
from practice import calculate_average, get_larger_number


def test_calculate_average():
    assert calculate_average([2, 4, 6]) == 4


def test_get_larger_number():
    assert get_larger_number(10, 7) == 10
```
