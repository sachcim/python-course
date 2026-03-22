# Blok 9 - Sortowanie, lambda, any, all

## Cel

Po tym bloku masz umieć sortować dane po wybranym polu i szybko sprawdzać warunki typu "czy wszyscy..." albo "czy chociaż jeden...".

## Minimum teorii

- `sorted(...)` zwraca nową posortowaną listę.
- `key=` mówi, po czym sortować.
- `lambda` to krótka funkcja używana często właśnie w `key=`.
- `any(...)` sprawdza, czy choć jeden element spełnia warunek.
- `all(...)` sprawdza, czy wszystkie elementy spełniają warunek.

## Demo

```python
users = [
    {"name": "Michał", "age": 24},
    {"name": "Ania", "age": 22},
    {"name": "Tomek", "age": 31},
]

sorted_users = sorted(users, key=lambda user: user["age"])

print(sorted_users)
print(any(user["age"] < 18 for user in users))
print(all(user["age"] >= 18 for user in users))
```

## Jak o tym myśleć

- `key=` mówi Pythonowi, jak ma porównywać elementy.
- `lambda` ma sens, gdy funkcja jest krótka i jednorazowa.
- `any` i `all` zastępują ręczne liczniki w prostych sprawdzeniach.

## Typowe błędy

- Mylenie `sort()` i `sorted()`.
- Pisanie zbyt skomplikowanych `lambda`.
- Ręczne flagi `found = False`, gdy wystarczyłoby `any(...)`.

## Co wyszukać

- `python sorted key lambda`
- `python any all examples`

## Jak pytać AI

- `wyjaśnij lambda na prostych przykładach`
- `daj mi zadania na sorted, any i all`

## Checkpoint

Powinieneś wiedzieć:

- po co jest `key=`
- kiedy `any`, kiedy `all`
- kiedy `lambda` jest czytelna, a kiedy lepiej zrobić zwykłą funkcję

## Jak sprawdzić, czy umiesz

- Umiesz posortować listę słowników po jednym polu.
- Umiesz odwrócić kolejność sortowania.
- Umiesz zastąpić prostą pętlę sprawdzającą warunek przez `any` albo `all`.
