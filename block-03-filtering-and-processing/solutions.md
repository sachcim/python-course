# Blok 3 - Rozwiązania referencyjne

## B3-C1

```python
users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 17, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]

names = []
for user in users:
    names.append(user["name"])

print(names)
```

## B3-C2

```python
active_users = []
for user in users:
    if user["active"]:
        active_users.append(user)

print(active_users)
```

## B3-C3

```python
adult_users = []
active_count = 0

for user in users:
    if user["age"] >= 18:
        adult_users.append(user)
    if user["active"]:
        active_count += 1

print(adult_users)
print(active_count)
```

## B3-P1

```python
names = [user["name"] for user in users]
active_users = [user for user in users if user["active"]]
adult_users = [user for user in users if user["age"] >= 18]
```

## B3-S1

```python
active_users = [user for user in users if user["active"]]
adult_users = [user for user in users if user["age"] >= 18]
active_names = [user["name"] for user in active_users]

report = (
    f"Wszyscy użytkownicy: {len(users)}\n"
    f"Aktywni: {len(active_users)}\n"
    f"Pełnoletni: {len(adult_users)}\n"
    f"Imiona aktywnych: {', '.join(active_names)}"
)

print(report)
```
