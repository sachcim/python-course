# Blok 3 - Podpowiedzi

## B3-C1

- `hint_1`: Potrzebujesz przejść po wszystkich użytkownikach i zabrać jedno pole.
- `hint_2`: W zwykłej pętli użyj `names.append(user["name"])`.

## B3-C2

- `hint_1`: To jest klasyczne filtrowanie po warunku.
- `hint_2`: Sprawdź `if user["active"]:` wewnątrz pętli.

## B3-C3

- `hint_1`: Lista pełnoletnich i licznik aktywnych to dwie osobne rzeczy.
- `hint_2`: Pełnoletniość sprawdzisz przez `user["age"] >= 18`. Licznik możesz zwiększać ręcznie albo użyć `sum`.

## B3-P1

- `hint_1`: Comprehension ma składnię: co dodajesz, skąd bierzesz, jaki warunek.
- `hint_2`: Schemat: `[user for user in users if user["active"]]`.

## B3-S1

- `hint_1`: Najpierw policz i przygotuj listy, dopiero potem buduj tekst.
- `hint_2`: Aktywne imiona możesz złączyć przez `", ".join(...)`.
