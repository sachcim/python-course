# numbers = [10, 20, 30, 40, 50]
#
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:4])
# print(numbers[::-1])
#
# fruits = ["apple", "banana", "orange"]
# for index, fruit in enumerate(fruits, start=-5):
#     print(index, fruit)
#
# names = ["Michał", "Ania"]
# scores = [90, 75]
# for name, score in zip(names, scores):
#     print(f"{name} -> {score}")

# Task 1
# names = ["Ania", "Bartek", "Celina", "Dawid"]
# scores = [88, 73, 91, 65]
#
# for index, (name, score) in enumerate(zip(names, scores), start=1):
#     print(f'{index} -> {name} i {score}')

# Task 2
# products = ["chleb", "mleko", "jajka", "ryz", "masło", "ser"]
# prices = [5.5, 3.2, 9.9, 7.0, 8.4, 6.1]
# for product, price in zip(products[::2], prices[::2]):
#     print(f'{product} -> {price}')

# Task 3
# letters = ["a", "b", "c", "d", "e"]
#
# for i, letter in enumerate(letters[::-1], start=1):
#     print(f"{i} -> {letter}")

# Task 4
# names = ["Ola", "Jan", "Marek", "Ewa", "Iza"]
# cities = ["Krakow", "Gdańsk", "Poznan", "Wrocław", "Łódź"]
# ages = [23, 31, 27, 29, 35]
#
# for i, (name, city, age) in enumerate(zip(names[1:4], cities[1:4], ages[1:4]), start = 1):
#     print(f"{i}. {name}, {city}, {age}")

# Task 5
# players = ["Ala", "Bob", "Cezary", "Dorota", "Eryk", "Filip", "Kajetan", "Michał"]
# points = [10, 15, 12, 20, 18, 14, 2, 100]
#
# records = list(zip(players, points))[::-1][:3]
#
# for i, (player, point) in enumerate(records, start=1):
#     print(f'#{i} {player}: {point} pkt')

# fruits = ["apple", "banana", "orange", "kiwi"]
# B2 C1
# print(f'{fruits[0]} {fruits[-1]}  {fruits[:2]} {fruits[::-1]}')
# B2 C2
# for i, fruit in enumerate(fruits, start=1):
#     print(f'{i}. {fruit}')
# B2 C3
# names = ["Michał", "Ania", "Tomek"]
# scores = [90, 75, 88]
# for name, score in zip(names, scores):
#     print(f'{name} -> {score}')

# B2 P1
# numbers = [10, 20, 30, 40, 50, 60]
# print(f'{numbers[::2]}, {numbers[-3:]}, {numbers[1:-1]}')
# B2 S1
# players = ["Michał", "Ania", "Tomek", "Ola"]
# points = [12, 8, 15, 11]
#
# for i, (player, point) in enumerate(zip(players, points), start=1):
#     print(f'{i}. {player} - {point} pkt')
# print(points[::-1])