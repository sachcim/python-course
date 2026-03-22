# Blok 10 - Mini projekt: Task Report Generator

## Cel

Masz złożyć wcześniejsze bloki w jeden mały, pełny projekt:

- analiza danych
- sortowanie
- zapis raportu
- refaktor do `dataclass`
- zamknięcie logiki w klasie `TaskManager`

## Minimum teorii

- Mini projekt ma łączyć wcześniejsze tematy, nie wprowadzać nową magię.
- Najpierw ogarnij dane i logikę na prostych strukturach, potem refaktoruj.
- `dataclass` upraszcza model danych, a klasa `TaskManager` porządkuje zachowanie.
- Testy mają sprawdzać zachowanie projektu, a nie jego dokładną implementację.

## Demo

```python
tasks = [
    {"title": "Nauka Pythona", "done": True, "priority": 2},
    {"title": "Przygotować CV", "done": False, "priority": 1},
    {"title": "Przeczytać o GCP", "done": False, "priority": 3},
]

completed_count = sum(task["done"] for task in tasks)
sorted_tasks = sorted(tasks, key=lambda task: task["priority"])

print(completed_count)
print(sorted_tasks)
```

## Dane startowe

Masz plik `data/tasks.json` oraz starter w katalogu `starter/`.

Przykładowe taski:

```python
tasks = [
    {"title": "Nauka Pythona", "done": True, "priority": 2},
    {"title": "Przygotować CV", "done": False, "priority": 1},
    {"title": "Przeczytać o GCP", "done": False, "priority": 3},
]
```

## Etapy projektu

### Wersja 1 - Słowniki

Najpierw pracujesz na taskach jako liście słowników i generujesz prosty raport.

### Wersja 2 - Dataclass

Potem zamieniasz taski na `Task` jako `dataclass`, żeby model danych był czytelniejszy.

### Wersja 3 - TaskManager

Na końcu przenosisz logikę do klasy `TaskManager`, która:

- przechowuje taski
- dodaje task
- oznacza task jako wykonany
- generuje raport

## Raport

Raport powinien zawierać co najmniej:

- liczbę wszystkich tasków
- liczbę ukończonych
- liczbę nieukończonych
- taski posortowane po priorytecie

Możesz zapisać wynik jako JSON albo TXT. W kursie rekomendowany jest JSON.

## Lekki moduł narzędziowy

Jeśli pracujesz w `venv`, możesz uruchomić testy do wersji z `TaskManager`:

```bash
pytest block-10-mini-project/tests
```

## Typowe błędy

- Mieszanie odpowiedzialności: jedna funkcja robi wszystko.
- Sortowanie oryginalnej listy, gdy chcesz tylko raport.
- Rozbudowana klasa `TaskManager`, która robi także I/O, parsowanie i logikę prezentacji naraz.

## Co wyszukać

- `python dataclass`
- `python sorted key lambda`
- `python json dump file`
- `pytest basics`

## Jak pytać AI

- `sprawdź mój TaskManager pod czytelność`
- `czy generate_report robi za dużo`
- `daj jedną podpowiedź do testów pytest bez pełnego rozwiązania`

## Checkpoint

Powinieneś umieć:

- przejść od listy słowników do obiektów
- wydzielić logikę do klasy
- napisać 2-3 podstawowe testy

## Jak sprawdzić, czy umiesz

- Umiesz wytłumaczyć, po co był etap ze słownikami, zanim przeszedłeś do klas.
- Umiesz pokazać jedną metodę, która ma jasną odpowiedzialność.
- Umiesz uruchomić test i zrozumieć, co dokładnie sprawdza.
