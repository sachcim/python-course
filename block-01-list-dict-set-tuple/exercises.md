# Blok 1 - Ćwiczenia

Pracuj w jednym pliku `practice.py` albo w kilku małych skryptach. Najpierw zrób część `core`, potem `plus`, na końcu `stretch`.

## Core

### B1-C1 - Lista imion

Utwórz listę 5 imion i wypisz:

- pierwszy element
- ostatni element
- długość listy

### B1-C2 - Słownik użytkownika

Utwórz:

```python
user = {
    "name": "Michał",
    "age": 24,
    "city": "Katowice",
}
```

Wypisz imię i miasto.

### B1-C3 - Unikalne liczby

Dla listy:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

stwórz zbiór unikalnych wartości i wypisz go razem z liczbą unikalnych elementów.

## Plus

### B1-P1 - Współrzędne

Stwórz `tuple` z dwiema współrzędnymi i wypisz każdą wartość osobno.

## Stretch

### B1-S1 - Mały katalog kontaktów

Zrób:

- listę imion
- słownik `name -> city`
- zbiór miast bez duplikatów
- tuple `("Michał", "Katowice")` dla jednego kontaktu

Na końcu wypisz 2-3 zdania, dlaczego każda z tych struktur ma tu sens.

## Git/GitHub checkpoint

### Artefakt dnia

- pierwsze skrypty z zadaniami na `list`, `dict`, `set` i `tuple`
- pierwszy świadomy porządek plików w repo kursowym

### Aktualizacja README

- zaznacz dzień 1 w tabeli `Postęp 10 dni`
- dopisz krótki wpis o tym, kiedy bierzesz `list`, `dict` i `set`

### Sugerowany commit

Jeśli repo nie jest jeszcze zainicjalizowane, najpierw wykonaj setup z `README.md` i `git-github-playbook.md`.

```bash
git status
git add .
git commit -m "day-01: collections basics"
git push
```
