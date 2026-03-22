# Blok 8 - Ćwiczenia

## Core

### B8-C1 - Book jako dataclass

Przepisz klasę `Book` z poprzedniego bloku na `dataclass`.

### B8-C2 - Product

Zrób `dataclass Product` z polami:

- `name`
- `price`
- `in_stock`

### B8-C3 - Filtrowanie obiektów

Przygotuj listę obiektów `Product` i przefiltruj tylko te, które są dostępne (`in_stock=True`).

## Plus

### B8-P1 - Cena sformatowana

Dodaj do `Product` małą metodę `formatted_price()`, która zwraca np. `19.99 PLN`.

## Stretch

### B8-S1 - Users jako dataclass

Mając listę słowników użytkowników, zamień ją na listę obiektów `User` jako `dataclass`, a potem przefiltruj aktywnych i pełnoletnich.

## Git/GitHub checkpoint

### Artefakt dnia

- modele danych przepisane na `dataclass`
- pierwszy świadomy commit refaktoryzacyjny

### Aktualizacja README

- zaznacz dzień 8 w tabeli `Postęp 10 dni`
- dopisz, co uprościło się po przejściu na `dataclass`

### Sugerowany commit

To jest dobry moment, żeby commit nazwać wprost refaktorem, bo zmienia się forma kodu, a nie jego główny cel.

```bash
git status
git diff
git add .
git commit -m "day-08: dataclass refactor"
git push
```
