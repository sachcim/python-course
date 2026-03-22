# Blok 8 - Rozwiązania referencyjne

## B8-C1

```python
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
```

## B8-C2

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True
```

## B8-C3

```python
products = [
    Product("Klawiatura", 199.99, True),
    Product("Monitor", 899.00, False),
    Product("Mysz", 89.50, True),
]

available_products = [product for product in products if product.in_stock]
print(available_products)
```

## B8-P1

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

    def formatted_price(self) -> str:
        return f"{self.price:.2f} PLN"
```

## B8-S1

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    active: bool


users_data = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 17, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]

users = [User(**user_data) for user_data in users_data]
active_adults = [user for user in users if user.active and user.age >= 18]

print(active_adults)
```
