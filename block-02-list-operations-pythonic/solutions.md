# Blok 2 - Rozwiązania referencyjne

## B2-C1

```python
fruits = ["apple", "banana", "orange", "kiwi"]

print(fruits[0])
print(fruits[-1])
print(fruits[:2])
print(fruits[::-1])
```

## B2-C2

```python
fruits = ["apple", "banana", "orange", "kiwi"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

## B2-C3

```python
names = ["Michał", "Ania", "Tomek"]
scores = [90, 75, 88]

for name, score in zip(names, scores):
    print(f"{name} -> {score}")
```

## B2-P1

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])
print(numbers[-3:])
print(numbers[1:-1])
```

## B2-S1

```python
players = ["Michał", "Ania", "Tomek", "Ola"]
points = [12, 8, 15, 11]

for position, (player, score) in enumerate(zip(players, points), start=1):
    print(f"{position}. {player} - {score} pkt")

print(points[::-1])
```
