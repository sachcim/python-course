# Blok 6 - Podpowiedzi

## B6-C1

- `hint_1`: Tu są dwa przewidywalne błędy i każdy ma swój typ.
- `hint_2`: Użyj `except ValueError:` i `except ZeroDivisionError:`.

## B6-C2

- `hint_1`: Przy pracy z JSON mogą pojawić się problemy zarówno z plikiem, jak i z treścią.
- `hint_2`: Sprawdź `FileNotFoundError` i `json.JSONDecodeError`.

## B6-C3

- `hint_1`: To jest dobre zadanie na pętlę `while True`.
- `hint_2`: W `try` spróbuj zrobić `return int(input(prompt))`, a w `except` wypisz komunikat i pętla ruszy od nowa.

## B6-P1

- `hint_1`: Jedne dane chcesz zachować, inne odrzucić z komunikatem.
- `hint_2`: Dla każdego elementu z listy spróbuj `int(value)` i złap `ValueError`.

## B6-S1

- `hint_1`: Tu będziesz łapał wyjątki na dwóch poziomach: plik i pojedynczy wiersz.
- `hint_2`: Wczytaj plik przez `csv.DictReader`, a konwersję `score` do `int` opakuj w osobny `try`.
