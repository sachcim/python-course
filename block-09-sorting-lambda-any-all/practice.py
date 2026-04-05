if __name__ == "__main__":
    users = [
        {"name": "Michał", "age": 24, "active": True},
        {"name": "Ania", "age": 22, "active": False},
        {"name": "Tomek", "age": 31, "active": True},
    ]

    products = [
        {"name": "Klawiatura", "price": 199.99},
        {"name": "Monitor", "price": 899.00},
        {"name": "Mysz", "price": 89.50},
    ]

    tasks = [
        {"title": "A", "done": True, "priority": 2},
        {"title": "B", "done": False, "priority": 1},
        {"title": "C", "done": False, "priority": 3},
    ]

    users_sorted_by_age_asc = sorted(users, key=lambda user: user["age"])
    products_sorted_by_price_desc = sorted(products, key=lambda product: product["price"], reverse=True)

    print(all(user["age"] >= 18 for user in users ))
    print(any(user["active"] for user in users))

    sorted_tasks = sorted(tasks, key=lambda task: task["priority"])

    print(users_sorted_by_age_asc[0])
    print(users_sorted_by_age_asc[-1])
    print(all(user["age"] >= 18 for user in users))
    print(any(not user["active"] for user in users))