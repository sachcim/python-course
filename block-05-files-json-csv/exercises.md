# Blok 5 - Ćwiczenia

Korzystaj z plików w katalogu `data/`.

## Core

### B5-C1 - Wczytaj JSON

Wczytaj `data/users.json` i wypisz wszystkie imiona.

### B5-C2 - Zmień i zapisz

Dodaj nowego użytkownika do danych z `users.json` i zapisz wynik do pliku `data/users_updated.json`.

### B5-C3 - Wczytaj CSV i policz średnią

Wczytaj `data/scores.csv`, policz średni wynik i wypisz go jako liczbę.

## Plus

### B5-P1 - Wyniki powyżej 80

Wypisz osoby z `scores.csv`, których wynik jest większy niż `80`.

## Stretch

### B5-S1 - Raport z dwóch źródeł

Przygotuj słownik:

```python
{
    "user_count": ...,
    "top_scores": [...],
}
```

gdzie:

- `user_count` to liczba użytkowników z JSON
- `top_scores` to lista słowników z osobami, które mają wynik powyżej `80`

Zapisz raport do `data/report.json`.

## Git/GitHub checkpoint

### Artefakt dnia

- skrypty do odczytu JSON i CSV
- obliczanie średniej i prostego raportu
- zrozumienie różnicy między danymi źródłowymi a wygenerowanym wynikiem

### Aktualizacja README

- zaznacz dzień 5 w tabeli `Postęp 10 dni`
- dopisz, które pliki są materiałem wejściowym kursu, a które są tylko wynikiem ćwiczenia

### Sugerowany commit

Do commita wrzuć kod źródłowy i materiały wejściowe. Wygenerowane pliki typu `users_updated.json` albo `report.json` zostaw poza historią, jeśli są tylko wynikiem ćwiczenia.

```bash
git status
git diff
git add .
git commit -m "day-05: files json and csv"
git push
```
