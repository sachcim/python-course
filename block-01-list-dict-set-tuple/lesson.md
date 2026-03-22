# Blok 1 - Listy, słowniki, sety, tuple

## Cel

Po tym bloku masz wiedzieć, kiedy brać `list`, kiedy `dict`, kiedy `set`, a kiedy zwykły `tuple`.

## Minimum teorii

- `list` przechowuje elementy po kolei i odczytujesz je po indeksie.
- `dict` przechowuje pary `klucz -> wartość`.
- `set` trzyma tylko unikalne wartości.
- `tuple` to uporządkowany zestaw wartości, którego zwykle nie zmieniasz.

## Demo

```python
names = ["Michał", "Ania", "Tomek"]
user = {"name": "Michał", "age": 24, "city": "Katowice"}
numbers = [1, 2, 2, 3]
unique_numbers = set(numbers)
point = (10, 25)

print(names[0])              # Michał
print(user["city"])          # Katowice
print(unique_numbers)        # {1, 2, 3}
print(point[0], point[1])    # 10 25
```

## Jak o tym myśleć

- Jeśli liczy się kolejność i dostęp po pozycji, najpierw myśl o `list`.
- Jeśli chcesz szybko dobrać się do danych po nazwie pola, myśl o `dict`.
- Jeśli problem brzmi "usuń duplikaty" albo "sprawdź, czy coś już było", myśl o `set`.
- Jeśli masz mały, stały zestaw wartości, np. współrzędne, myśl o `tuple`.

## Typowe błędy

- Mylenie indeksu z kluczem: `user[0]` nie zadziała dla słownika.
- Zapominanie, że indeksy list zaczynają się od `0`.
- Oczekiwanie, że `set` zachowa kolejność.
- Traktowanie `tuple` jak listy i próba zmiany elementu.

## Co wyszukać

- `python list methods`
- `python dict basics`
- `python set unique values`
- `python tuple unpacking`

## Jak pytać AI

- `wyjaśnij różnicę między list, dict i set na prostych przykładach`
- `daj mi 3 krótkie zadania na listy i słowniki bez rozwiązań`

## Checkpoint

Powinieneś umieć odpowiedzieć:

- kiedy biorę listę
- kiedy dict
- kiedy set
- kiedy tuple ma sens zamiast listy

## Jak sprawdzić, czy umiesz

- Umiesz w 2 minuty wymyślić przykład dla każdej z 4 struktur.
- Umiesz odczytać i zmienić dane w liście oraz słowniku.
- Umiesz powiedzieć, czemu `set(numbers)` usuwa duplikaty.
