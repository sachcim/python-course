# Blok 6 - Błędy i try/except

## Cel

Po tym bloku masz rozumieć, że błędy są normalną częścią pracy i trzeba łapać tylko te wyjątki, których naprawdę się spodziewasz.

## Minimum teorii

- `try` oznacza: tutaj może polecieć wyjątek.
- `except SomeError` oznacza: umiem sensownie obsłużyć konkretny problem.
- Nie łap wszystkiego przez goły `except`.
- Dobrze obsłużony błąd daje użytkownikowi jasny komunikat.

## Demo

```python
try:
    age = int(input("Podaj wiek: "))
except ValueError:
    print("To nie była liczba")
else:
    print(f"Masz {age} lat")
```

## Jak o tym myśleć

- Najpierw zastanów się, jaki błąd realnie może wystąpić.
- Potem zdecyduj, czy chcesz go obsłużyć, czy pozwolić programowi się zatrzymać.
- `try/except` nie ma maskować bałaganu, tylko przewidywane problemy wejścia, plików i parsowania.

## Typowe błędy

- Łapanie wszystkich wyjątków bez wiedzy, co poszło nie tak.
- Zbyt szeroki blok `try`, przez co łapiesz więcej niż trzeba.
- Zjadanie błędu bez komunikatu.

## Co wyszukać

- `python try except ValueError`
- `python FileNotFoundError`
- `python JSONDecodeError`

## Jak pytać AI

- `jakie wyjątki tu realnie mogą wystąpić?`
- `czy ten try/except nie jest zbyt szeroki?`

## Checkpoint

Powinieneś wiedzieć:

- jaki błąd chcesz łapać
- dlaczego właśnie ten
- gdzie kończy się sensowna obsługa błędów

## Jak sprawdzić, czy umiesz

- Umiesz rozpoznać różnicę między złym inputem a błędem pliku.
- Umiesz nazwać wyjątek, którego się spodziewasz.
- Umiesz zawęzić blok `try` do miejsca ryzyka.
