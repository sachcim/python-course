# Blok 9 - Rozwiązania referencyjne

## B9-C1

```python
users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 22, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]

sorted_users = sorted(users, key=lambda user: user["age"])
print(sorted_users)
```

## B9-C2

```python
products = [
    {"name": "Klawiatura", "price": 199.99},
    {"name": "Monitor", "price": 899.00},
    {"name": "Mysz", "price": 89.50},
]

sorted_products = sorted(products, key=lambda product: product["price"], reverse=True)
print(sorted_products)
```

## B9-C3

```python
all_adults = all(user["age"] >= 18 for user in users)
any_active = any(user["active"] for user in users)

print(all_adults)
print(any_active)
```

## B9-P1

```python
tasks = [
    {"title": "A", "done": True, "priority": 2},
    {"title": "B", "done": False, "priority": 1},
    {"title": "C", "done": False, "priority": 3},
]

sorted_tasks = sorted(tasks, key=lambda task: task["priority"])
print(sorted_tasks)
```

## B9-S1

```python
youngest_user = min(users, key=lambda user: user["age"])
oldest_user = max(users, key=lambda user: user["age"])
all_adults = all(user["age"] >= 18 for user in users)
any_inactive = any(not user["active"] for user in users)

print(youngest_user["name"])
print(oldest_user["name"])
print(all_adults)
print(any_inactive)
```
