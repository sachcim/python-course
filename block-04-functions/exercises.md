# Blok 4 - Ćwiczenia

Przy tych zadaniach celowo trzymaj funkcje małe. Jeśli jedna funkcja robi się nieczytelna, rozbij ją.

## Core

### B4-C1 - Większa z dwóch liczb

Napisz funkcję:

```python
def get_larger_number(a: float, b: float) -> float:
    ...
```

Ma zwracać większą z dwóch liczb.

### B4-C2 - Średnia

Napisz funkcję:

```python
def calculate_average(numbers: list[float]) -> float:
    ...
```

która zwraca średnią z listy liczb.

### B4-C3 - Aktywni użytkownicy

Napisz funkcję `get_active_users(users)`, która z listy słowników zwraca tylko aktywnych użytkowników.

## Plus

### B4-P1 - Wyszukiwanie po imieniu

Napisz funkcję:

```python
def find_user_by_name(users: list[dict], name: str) -> dict | None:
    ...
```

Jeśli użytkownik istnieje, zwróć słownik użytkownika. W przeciwnym razie zwróć `None`.

## Stretch

### B4-S1 - Pierwsze testy

Dodaj 2 testy `pytest`:

- dla `calculate_average`
- dla `get_larger_number`

Nie chodzi o rozbudowany zestaw testów. Chodzi o zrozumienie, jak sprawdzić funkcję automatycznie.

## Git/GitHub checkpoint

### Artefakt dnia

- małe funkcje z typami
- pierwsze testy `pytest`
- wejście w pracę z `venv`

### Aktualizacja README

- zaznacz dzień 4 w tabeli `Postęp 10 dni`
- dopisz jedno zdanie o tym, czemu `.venv/` nie powinno trafić do repo

### Sugerowany commit

Przed commitem sprawdź, czy `.gitignore` chroni `.venv/` i cache.

```bash
git status
git diff
git add .
git commit -m "day-04: functions and first tests"
git push
```
