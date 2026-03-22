# Blok 6 - Ćwiczenia

## Core

### B6-C1 - Dzielenie przez input

Napisz program, który:

- pyta użytkownika o liczbę
- dzieli `100` przez tę liczbę
- obsługuje zły input
- obsługuje dzielenie przez zero

### B6-C2 - Bezpieczne czytanie JSON

Napisz funkcję, która czyta plik JSON. Jeśli:

- plik nie istnieje, wypisz sensowny komunikat
- JSON jest niepoprawny, też wypisz sensowny komunikat

### B6-C3 - Bezpieczne pobieranie liczby

Napisz funkcję `read_int(prompt: str) -> int`, która:

- pyta o liczbę
- dopóki użytkownik wpisuje złą wartość, prosi ponownie

## Plus

### B6-P1 - Czyszczenie danych wejściowych

Masz listę:

```python
values = ["10", "abc", "25", "", "7"]
```

Spróbuj zamienić ją na liczby całkowite. Niepoprawne elementy pomiń, ale wypisz, które zostały odrzucone.

## Stretch

### B6-S1 - Odporny loader wyników

Napisz funkcję, która przyjmuje ścieżkę do pliku CSV z wynikami i:

- jeśli plik nie istnieje, zwraca pustą listę
- jeśli wiersz ma zły wynik, pomija go i wypisuje ostrzeżenie
- w poprawnym przypadku zwraca listę słowników z `name` i `score`

## Git/GitHub checkpoint

### Artefakt dnia

- skrypty i funkcje z sensowną obsługą wyjątków
- czytelne komunikaty błędów zamiast ogólnego `except`

### Aktualizacja README

- zaznacz dzień 6 w tabeli `Postęp 10 dni`
- dopisz, jakie wyjątki łapałeś świadomie i dlaczego właśnie te

### Sugerowany commit

Przed commitem obowiązkowo obejrzyj `git diff` i sprawdź, czy commit faktycznie opisuje zmianę związaną z obsługą błędów.

```bash
git status
git diff
git add .
git commit -m "day-06: error handling and try except"
git push
```
