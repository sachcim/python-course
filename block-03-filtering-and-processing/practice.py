from os.path import join

users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 17, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]
#
# names = []
# for user in users:
#     names.append(user["name"])
#
# active_users = [user for user in users if user["active"]]
#
# print(names)
# print(active_users)

# B3 C1
# names = [u["name"] for u in users]
# print(names)

# B3 C2
# activeUsers= [u for u in users if u["active"]]
# print(activeUsers)

# B3 C3
# matureUsers = []
# counter = 0
# for u in users:
#     if u["age"] >= 18:
#         matureUsers.append(u)
#     if u["active"]:
#         counter += 1
# print(matureUsers)
# print(counter)

# Zostawiam wersję z pełną pętlą for poniewaz jest ona najbardziej czytelna
# Korzystanie tutaj z list comprehension aby pozostalo czytelne wymaga
# stworzenia listy dla counter a pozniej jej zsumowania, co powoduje
# 2 iteracje po liscie i niepotrzebnie obniza wydajnosc
# Równiez pominalem punkt B3 P1 bo od razu robilem to na list comprehension :)

# B3 S1
activeCount = 0
usersCount = len(users)
matureCount = 0
activeUsersName = []
for u in users:
    if u["age"] >= 18:
        matureCount += 1
    if u["active"]:
        activeCount += 1
        activeUsersName.append(u["name"])

print(f'Wszyscy użytkownicy: {usersCount}\n'
      f'Aktywni: {activeCount}\n'
      f'Pełnoletni: {matureCount}\n'
      f'Imiona aktywnych: {", ".join(activeUsersName)}')