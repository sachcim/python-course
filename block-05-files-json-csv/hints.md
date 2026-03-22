# Blok 5 - Podpowiedzi

## B5-C1

- `hint_1`: Najpierw wczytaj cały plik do jednej zmiennej.
- `hint_2`: Użyj `json.load(file)` i potem przejdź pętlą po liście użytkowników.

## B5-C2

- `hint_1`: Po wczytaniu JSON dostaniesz zwykłą listę słowników.
- `hint_2`: Użyj `users.append({...})`, a potem `json.dump(...)` z `indent=2`.

## B5-C3

- `hint_1`: `DictReader` zwraca stringi, nawet jeśli wyglądają jak liczby.
- `hint_2`: Dodawaj `int(row["score"])` do listy wyników, a średnią policz na końcu.

## B5-P1

- `hint_1`: To jest filtrowanie po warunku.
- `hint_2`: Sprawdź `if int(row["score"]) > 80:`.

## B5-S1

- `hint_1`: Nie mieszaj wszystkiego w jednej pętli. Najpierw wczytaj źródła.
- `hint_2`: Zbuduj słownik raportu i zapisz go przez `json.dump(...)`.
