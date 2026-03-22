# Blok 3 - Filtrowanie i przetwarzanie danych

## Cel

Po tym bloku masz umieć przejść po liście danych, wyciągnąć z niej to, co potrzebne, i przepisać prosty kod na `list comprehension`.

## Minimum teorii

- Pętla `for` pozwala przejść po każdym elemencie kolekcji.
- Nową listę możesz budować przez `append`.
- Filtrowanie to zwykle `if` wewnątrz pętli albo wewnątrz comprehension.
- `list comprehension` jest dobra do prostych i czytelnych transformacji.

## Demo

```python
users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 17, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]

names = []
for user in users:
    names.append(user["name"])

active_users = [user for user in users if user["active"]]

print(names)
print(active_users)
```

## Jak o tym myśleć

- Najpierw napisz zwykłą pętlę, jeśli problem nie jest jeszcze jasny.
- Dopiero potem sprawdź, czy comprehension nadal jest czytelna.
- Czytelność wygrywa ze sztuczkami.

## Typowe błędy

- Robienie zbyt skomplikowanego comprehension.
- Zapominanie, że `if` w comprehension filtruje elementy.
- Niewłaściwe nazwy zmiennych, przez co nie wiadomo, co reprezentuje dany element.

## Co wyszukać

- `python list comprehension`
- `python filter list of dicts`

## Jak pytać AI

- `pokaż mi zwykłą pętlę i list comprehension dla tego samego zadania`
- `kiedy comprehension jest czytelne, a kiedy już przesadzone?`

## Checkpoint

Powinieneś umieć:

- napisać zwykłą pętlę
- przepisać prostą pętlę na comprehension
- świadomie wybrać bardziej czytelną wersję

## Jak sprawdzić, czy umiesz

- Umiesz wyciągnąć z listy słowników tylko potrzebne pola.
- Umiesz zbudować nową listę na podstawie warunku.
- Umiesz powiedzieć, kiedy zostajesz przy pętli zamiast na siłę robić comprehension.
