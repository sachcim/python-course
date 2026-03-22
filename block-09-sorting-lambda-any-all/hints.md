# Blok 9 - Podpowiedzi

## B9-C1

- `hint_1`: Potrzebujesz wskazać pole, po którym ma iść sortowanie.
- `hint_2`: Użyj `sorted(users, key=lambda user: user["age"])`.

## B9-C2

- `hint_1`: Tu też `key=`, ale chcesz odwrotny kierunek.
- `hint_2`: Dodaj `reverse=True`.

## B9-C3

- `hint_1`: Jedno pytanie dotyczy wszystkich elementów, drugie tylko jednego.
- `hint_2`: Użyj `all(user["age"] >= 18 for user in users)` i `any(user["active"] for user in users)`.

## B9-P1

- `hint_1`: Task to zwykły słownik, więc sortujesz jak użytkowników.
- `hint_2`: Klucz sortowania to `task["priority"]`.

## B9-S1

- `hint_1`: Najmłodszą i najstarszą osobę możesz znaleźć przez sortowanie albo `min` i `max`.
- `hint_2`: Sprawdzenie nieaktywnego użytkownika zrobisz przez `any(not user["active"] for user in users)`.
