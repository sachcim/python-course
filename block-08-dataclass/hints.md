# Blok 8 - Podpowiedzi

## B8-C1

- `hint_1`: Część kodu z `__init__` przestanie być potrzebna.
- `hint_2`: Dodaj `@dataclass` nad klasą i wypisz pola jako adnotacje typów.

## B8-C2

- `hint_1`: W `dataclass` pola definiujesz w ciele klasy.
- `hint_2`: Schemat: `name: str`, `price: float`, `in_stock: bool = True`.

## B8-C3

- `hint_1`: To dalej zwykłe filtrowanie, tylko na obiektach zamiast słownikach.
- `hint_2`: Sprawdzasz `product.in_stock`, a nie `product["in_stock"]`.

## B8-P1

- `hint_1`: `dataclass` może mieć też metody.
- `hint_2`: Zwróć `f"{self.price:.2f} PLN"`.

## B8-S1

- `hint_1`: Najpierw utwórz obiekty z danych wejściowych.
- `hint_2`: Użyj comprehension do konwersji: `User(**user_data)`.
