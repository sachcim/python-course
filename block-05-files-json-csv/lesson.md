# Blok 5 - Pliki, JSON, CSV

## Cel

Po tym bloku masz umieć wczytać plik, zmienić dane i zapisać wynik z powrotem do nowego pliku.

## Minimum teorii

- `open(...)` otwiera plik do czytania albo zapisu.
- `json.load(...)` czyta JSON z pliku.
- `json.dump(...)` zapisuje dane Pythonowe do pliku JSON.
- `csv.DictReader(...)` czyta CSV w postaci słowników.

## Demo

```python
import json
from pathlib import Path

path = Path("data/users.json")

with path.open("r", encoding="utf-8") as file:
    users = json.load(file)

users.append({"name": "Tomek", "age": 29})

with Path("data/users_updated.json").open("w", encoding="utf-8") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
```

## Jak o tym myśleć

- JSON jest wygodny do list, słowników i prostych struktur danych.
- CSV ma sens, gdy dane są tabelaryczne: wiersze i kolumny.
- W praktyce często robisz trzy kroki: wczytaj, zmień, zapisz.

## Typowe błędy

- Mieszanie `json.load` i `json.loads`.
- Zapominanie o konwersji wyniku z CSV do `int` albo `float`.
- Zapis do tego samego pliku bez kopii, gdy chcesz zachować oryginał.

## Co wyszukać

- `python json load dump`
- `python csv reader DictReader`
- `python open file read write`

## Jak pytać AI

- `wyjaśnij różnicę między json.load i json.loads`
- `daj mi mały projekt na JSON i CSV`

## Checkpoint

Powinieneś umieć:

- wczytać JSON
- zmodyfikować dane
- zapisać je z powrotem
- wczytać tabelę CSV i policzyć prostą statystykę

## Jak sprawdzić, czy umiesz

- Umiesz przeczytać listę słowników z pliku JSON.
- Umiesz dodać nowy rekord i zapisać nowy plik.
- Umiesz policzyć średni wynik z pliku CSV.
