import practice

users = [
        {"name": "Michał", "age": 24, "active": True},
        {"name": "Ania", "age": 17, "active": False},
        {"name": "Tomek", "age": 31, "active": True},
    ]

def test_calc_average():
    assert practice.calc_average([2, 4, 6]) == 4

def test_calc_discount():
    assert practice.calc_discount(200, 15) == 170

def test_get_larger():
    assert practice.get_larger(5, 10) == 10

def test_get_active_users():
    assert practice.get_active_users(users) == [
        {"name": "Michał", "age": 24, "active": True},
        {"name": "Tomek", "age": 31, "active": True},
    ]
def test_find_user_by_name():
    assert practice.find_user_by_name(users, "Ania") == {
        "name": "Ania",
        "age": 17,
        "active": False
    }