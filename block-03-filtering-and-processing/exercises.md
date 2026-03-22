# Blok 3 - Ćwiczenia

Pracuj na danych:

```python
users = [
    {"name": "Michał", "age": 24, "active": True},
    {"name": "Ania", "age": 17, "active": False},
    {"name": "Tomek", "age": 31, "active": True},
]
```

## Core

### B3-C1 - Lista imion

Zrób listę samych imion.

### B3-C2 - Aktywni użytkownicy

Zrób listę tylko aktywnych użytkowników.

### B3-C3 - Pełnoletni i liczenie

Zrób listę użytkowników pełnoletnich i policz, ilu użytkowników jest aktywnych.

## Plus

### B3-P1 - To samo przez comprehension

Przepisz zadania `B3-C1`, `B3-C2` i listę pełnoletnich z `B3-C3` na `list comprehension`.

## Stretch

### B3-S1 - Mały raport tekstowy

Na podstawie `users` przygotuj tekst:

```text
Wszyscy użytkownicy: 3
Aktywni: 2
Pełnoletni: 2
Imiona aktywnych: Michał, Tomek
```

Nie musisz robić jednej funkcji. Zadbaj o czytelność.

## Git/GitHub checkpoint

### Artefakt dnia

- filtrowanie użytkowników zwykłą pętlą
- wersje z `list comprehension`
- krótki raport tekstowy

### Aktualizacja README

- zaznacz dzień 3 w tabeli `Postęp 10 dni`
- dopisz, kiedy comprehension była czytelna, a kiedy wolałeś zwykłą pętlę

### Sugerowany commit

Trzymaj się zasady: jedna logiczna porcja zmian = jeden commit. Jeśli naprawdę rozdzielasz pracę na dwie osobne części, drugi commit jest opcjonalny.

```bash
git status
git diff
git add .
git commit -m "day-03: filtering and list comprehensions"
git push
```
