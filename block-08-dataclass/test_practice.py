import practice

book = practice.Book("The Great Gatsby", "F. Scott Fitzgerald")

products = [practice.Product(name='first', price=5.00, in_stock=True),
                practice.Product(name='second', price=15.00),
                practice.Product(name='third', price=25.00),
                practice.Product(name='fourth', price=2.00, in_stock=True)]
users_dict = [
        {"name": "Michał","age": 17, "is_active": True},
        {"name": "Ania","age": 21, "is_active": False}
    ]
def test_book_describe():
    assert book.describe() == "The Great Gatsby - F. Scott Fitzgerald"

def test_product_formatted_price():
    assert products[0].formatted_price() == '5.00 PLN'

def test_get_available_products():
    assert practice.get_available_products(products) == [practice.Product(name='first', price=5.00, in_stock=True), practice.Product(name='fourth', price=2.00, in_stock=True)]

def test_users_dict_to_obj():
    assert practice.users_dict_to_obj(users_dict) == [practice.User(name='Michał', age=17, is_active=True), practice.User(name='Ania', age=21, is_active=False)]

def test_get_active_users():
    assert practice.get_active_users(practice.users_dict_to_obj(users_dict)) == [practice.User(name='Michał', age=17, is_active=True)]

def test_get_mature_users():
    assert practice.get_mature_users(practice.users_dict_to_obj(users_dict)) == [practice.User(name='Ania', age=21, is_active=False)]