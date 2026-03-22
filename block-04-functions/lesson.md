# Blok 4 - Funkcje na sensownym poziomie

## Cel

Po tym bloku masz pisać małe funkcje, które jasno mówią:

- co przyjmują
- co zwracają
- za co odpowiadają

## Minimum teorii

- Parametry to dane wejściowe funkcji.
- `return` oddaje wynik na zewnątrz.
- Wartości domyślne upraszczają wywołanie.
- Type hints pomagają zrozumieć kod i ułatwiają pracę w edytorze.
- Dobra funkcja robi jedną rzecz.

## Demo

```python
def calculate_discount(price: float, percent: int) -> float:
    return price * (1 - percent / 100)


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


print(calculate_discount(200, 15))
print(average([3, 4, 5]))
```

## Jak o tym myśleć

- Jeśli nazwa funkcji wymaga długiego tłumaczenia, możliwe, że robi za dużo.
- Jeśli funkcja coś liczy, zwykle powinna zwrócić wynik, a nie tylko go wypisać.
- Type hints nie uruchamiają magii, ale pomagają szybciej zobaczyć intencję.

## Lekki moduł narzędziowy

Po tym bloku warto zacząć pracować w `venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
```

Uruchamianie skryptu:

```bash
python3 practice.py
```

Pierwszy lekki kontakt z `pytest`:

```python
def test_average():
    assert average([2, 4, 6]) == 4
```

## Typowe błędy

- Funkcja liczy, wypisuje, zapisuje plik i jeszcze pyta użytkownika o dane.
- Brak `return`, gdy wynik ma być używany dalej.
- Zbyt ogólne nazwy typu `do_stuff`.
- Brak obsługi pustej listy tam, gdzie to ma znaczenie.

## Co wyszukać

- `python function arguments`
- `python type hints`
- `python return values`

## Jak pytać AI

- `oceń moje funkcje: czy są za długie?`
- `jak rozbić tę funkcję na mniejsze?`

## Checkpoint

Powinieneś umieć odpowiedzieć:

- co funkcja przyjmuje
- co zwraca
- czy robi jedną rzecz

## Jak sprawdzić, czy umiesz

- Umiesz napisać funkcję bez `print`, która oddaje gotowy wynik.
- Umiesz dodać podstawowe typy wejścia i wyjścia.
- Umiesz powiedzieć, czy funkcja jest za szeroka odpowiedzialnościowo.
