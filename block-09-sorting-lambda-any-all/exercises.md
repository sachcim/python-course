# Blok 9 - Ćwiczenia

## Core

### B9-C1 - Sortowanie użytkowników

Posortuj użytkowników po wieku rosnąco.

```python
users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 22, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]
```

### B9-C2 - Produkty malejąco

Posortuj produkty po cenie malejąco.

```python
products = [
    {"name": "Klawiatura", "price": 199.99},
    {"name": "Monitor", "price": 899.00},
    {"name": "Mysz", "price": 89.50},
]
```

### B9-C3 - Any i all

Sprawdź, czy:

- wszyscy użytkownicy są pełnoletni
- chociaż jeden użytkownik jest aktywny

## Plus

### B9-P1 - Sortowanie tasków

Masz listę tasków:

```python
tasks = [
    {"title": "A", "done": True, "priority": 2},
    {"title": "B", "done": False, "priority": 1},
    {"title": "C", "done": False, "priority": 3},
]
```

Posortuj taski po `priority` rosnąco.

## Stretch

### B9-S1 - Mały raport logiczny

Na podstawie listy użytkowników wypisz:

- najmłodszą osobę
- najstarszą osobę
- czy wszyscy są pełnoletni
- czy ktoś jest nieaktywny

## Git/GitHub checkpoint

### Artefakt dnia

- rozwiązania z `sorted`, `lambda`, `any` i `all`
- uporządkowana historia commitów przed finałem projektu

### Aktualizacja README

- zaznacz dzień 9 w tabeli `Postęp 10 dni`
- dopisz, kiedy użyłeś `any`, a kiedy `all`

### Sugerowany commit

Po commicie sprawdź historię przez `git log --oneline -9` i oceń, czy ostatnie wpisy wyglądają jak czytelna ścieżka nauki, a nie przypadkowy zrzut zmian.

```bash
git status
git diff
git add .
git commit -m "day-09: sorting lambda any all"
git log --oneline -9
git push
```
