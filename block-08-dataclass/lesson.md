# Blok 8 - Dataclass

## Cel

Po tym bloku masz rozumieć, kiedy zwykła klasa jest zbyt ciężka i kiedy `dataclass` daje prostszy model danych.

## Minimum teorii

- `@dataclass` automatycznie generuje m.in. `__init__` i czytelny `repr`.
- Dobrze pasuje do modeli danych: rekordów, produktów, użytkowników, tasków.
- Jeśli klasa ma głównie przechowywać dane, `dataclass` jest często lepsza niż ręczne pisanie klasy.

## Demo

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    active: bool = True


user = User("Michał", 24)
print(user)
```

## Jak o tym myśleć

- `dataclass` jest świetna, gdy dane są ważniejsze niż rozbudowana logika.
- Zwykła klasa dalej ma sens, gdy klasa ma dużo zachowania, walidacji albo steruje stanem.
- To nie jest "lepsza klasa do wszystkiego". To po prostu wygodniejsze narzędzie do konkretnego typu problemu.

## Typowe błędy

- Używanie `dataclass` do obiektu, który ma skomplikowany cykl życia i dużo metod.
- Przepisywanie na `dataclass` tylko dlatego, że "tak nowocześniej".
- Brak zrozumienia, że `dataclass` nadal jest zwykłą klasą, tylko z pomocą dekoratora.

## Co wyszukać

- `python dataclass`
- `dataclass vs normal class`

## Jak pytać AI

- `kiedy dataclass ma sens, a kiedy lepiej zwykła klasa?`
- `przepisz moją klasę na dataclass i wyjaśnij różnice`

## Checkpoint

Powinieneś rozumieć:

- `dataclass` do danych
- zwykła klasa do większej logiki

## Jak sprawdzić, czy umiesz

- Umiesz przepisać prostą klasę z polami na `dataclass`.
- Umiesz wskazać, co zyskałeś po usunięciu ręcznego `__init__`.
- Umiesz nie przesadzić i zostawić zwykłą klasę tam, gdzie ma to sens.
