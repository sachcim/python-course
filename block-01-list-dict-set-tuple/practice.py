# imiona = [ "Michał", "Kajetan", "Marcin", "Andrzej", "Ola"]
#
# print(imiona)
#
# print(imiona[0])
# print(imiona[-1])
# print(len(imiona))

# user = {
#     "name": "Michał",
#     "age": 21,
#     "city": "Katowice",
# }
#
# print(f"Imię {user['name']} Miasto {user['city']}")

# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# uniqueNum = set(numbers)
# print(f"Unikalne Elementy: {uniqueNum}, Ilość elementów: {len(uniqueNum)}")

# point = (120, 350)
# x,y=point
# print(x, y)

names = ["Michał", "Kajetan", "Marcin", "Andrzej", "Ola"]

user = {
    "Michał":"Bielsko-Biała",
    "Kajetan":"Bielsko-Biała",
    "Alina":"Ruda Śląska"
}


cities = {"Warszawa", "Katowice", "Gdańsk", "Szczecin", "Pszczyna", "Warszawa", "Katowice"}

userTuple = ("Michał", "Bielsko-Biała")
# Kazda z tych struktur ma swoje zastosowanie ze wzgledu na ich unikalne właściwości. Names daje nam szybki dostep do imion,
# user pokazuje gdzie kazda osoba mieszka za pomoca klucza (imienia), miasta są jako set bo istnieje tylko jedno miasto
# o danej nazwie w przeciwienstwie do imion ktore powtórzyć się mogą a tuple jest krótkie dlatego nadaje się do opisania jednej osoby i jej miasta.

print(names)
names.append("Kasia")
print(len(names))

print(f'Kajetan: {user["Kajetan"]}')
user["Kajetan"] = "Warszawa"
print(f'Kajetan: {user["Kajetan"]}')

user["Zosia"] = "Kraków"
print(f'Zosia: {user["Zosia"]}')
print(cities)
cities.remove("Szczecin")
print(cities)
cities.add("Warszawa")
print(cities)

variable1 = userTuple[0]
variable2 = userTuple[1]
print(f'{variable1} mieszka w {variable2}')