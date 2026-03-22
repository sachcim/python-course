# Blok 1 - Rozwiązania referencyjne

## B1-C1

```python
names = ["Michał", "Ania", "Tomek", "Ola", "Kasia"]

print(names[0])
print(names[-1])
print(len(names))
```

## B1-C2

```python
user = {
    "name": "Michał",
    "age": 24,
    "city": "Katowice",
}

print(user["name"])
print(user["city"])
```

## B1-C3

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)
print(len(unique_numbers))
```

## B1-P1

```python
point = (10, 25)
x, y = point

print(x)
print(y)
```

## B1-S1

```python
names = ["Michał", "Ania", "Tomek"]
cities_by_name = {
    "Michał": "Katowice",
    "Ania": "Kraków",
    "Tomek": "Katowice",
}
unique_cities = set(cities_by_name.values())
contact = ("Michał", "Katowice")

print(names)
print(cities_by_name)
print(unique_cities)
print(contact)
```

`list` trzyma kolejność. `dict` daje dostęp po imieniu. `set` usuwa duplikaty miast. `tuple` ma sens dla jednej stałej pary wartości.
