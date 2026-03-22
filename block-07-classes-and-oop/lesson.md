# Blok 7 - Klasy i OOP praktycznie

## Cel

Po tym bloku masz rozumieć, czym jest klasa, czym jest obiekt i kiedy klasa porządkuje kod lepiej niż luźne funkcje i słowniki.

## Minimum teorii

- Klasa to przepis na obiekty.
- Obiekt to konkretna instancja klasy.
- `self` oznacza "ten konkretny obiekt".
- `__init__` ustawia stan początkowy obiektu.
- Metoda to funkcja przypisana do obiektu.

## Demo

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Cześć, mam na imię {self.name}"


user = User("Michał", 24)
print(user.introduce())
```

## Jak o tym myśleć

- Jeśli kilka danych i zachowań stale chodzi razem, klasa ma sens.
- Jeśli problem to tylko prosty rekord danych, czasem wystarczy słownik albo później `dataclass`.
- `self` nie jest magią. To po prostu obiekt, na którym właśnie pracujesz.

## Typowe błędy

- Zapominanie o `self` w definicji metody.
- Próba używania pól bez `self.` wewnątrz klasy.
- Robienie klasy do czegoś, co jest tylko jedną krótką funkcją.

## Co wyszukać

- `python class __init__ self`
- `python methods examples`
- `python object oriented basics`

## Jak pytać AI

- `wyjaśnij self bez akademickiego bełkotu`
- `porównaj funkcję i klasę na przykładzie task managera`

## Checkpoint

Powinieneś umieć:

- utworzyć obiekt
- wywołać metodę
- powiedzieć, czemu klasa ma sens w danym przypadku

## Jak sprawdzić, czy umiesz

- Umiesz napisać klasę z 2 polami i 1 metodą.
- Umiesz wyjaśnić, skąd bierze się `self.name`.
- Umiesz wskazać przypadek, gdzie klasa upraszcza model danych i zachowań.
