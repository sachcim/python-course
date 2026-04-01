from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    def describe(self):
        return f'{self.title} - {self.author}'

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = False

    def formatted_price(self):
        return f'{self.price:.2f} PLN'

@dataclass
class User:
    name: str
    age: int
    is_active: bool = False

def get_available_products(p: list[Product]) -> list[Product]:
    return [product for product in p if product.in_stock]

def get_active_users(u: list[User]) -> list[User]:
    return [user for user in u if user.is_active]

def get_mature_users(u: list[User]) -> list[User]:
    return [user for user in u if user.age >= 18]

def users_dict_to_obj(users_dict: list[dict]) -> list[User]:
    return [User(**data) for data in users_dict]
