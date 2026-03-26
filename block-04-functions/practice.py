from typing import List, Optional


def calc_discount(price: float, percent: int) -> float:
    return price * (1 - percent / 100)


def calc_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def get_larger(a: float, b: float) -> float:
    return a if a > b else b

def get_active_users(users: List[dict]) -> List[dict]:
    return [u for u in users if u["active"]]

def find_user_by_name(users: list[dict], name: str) -> Optional[dict]:
    matches = [u for u in users if u["name"] == name]
    return matches[0] if matches else None


if __name__ == "__main__":
    users = [
        {"name": "Michał", "age": 24, "active": True},
        {"name": "Ania", "age": 17, "active": False},
        {"name": "Tomek", "age": 31, "active": True},
    ]

    print(get_active_users(users))
    print(find_user_by_name(users, "Ania"))