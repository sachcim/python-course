# Blok 10 - Podpowiedzi

## B10-C1

- `hint_1`: Najpierw policz wartości prostymi funkcjami albo zmiennymi pomocniczymi.
- `hint_2`: Liczbę ukończonych policz przez `sum(task["done"] for task in tasks)`, a sortowanie zrób przez `sorted(tasks, key=lambda task: task["priority"])`.

## B10-C2

- `hint_1`: Raport to zwykły słownik, więc możesz go łatwo zapisać do JSON.
- `hint_2`: Użyj `json.dump(report, file, ensure_ascii=False, indent=2)`.

## B10-C3

- `hint_1`: Najpierw stwórz `Task` jako `@dataclass`, potem zamień słowniki na obiekty.
- `hint_2`: Przy sortowaniu i filtrowaniu przejdź z `task["done"]` na `task.done`.

## B10-P1

- `hint_1`: `TaskManager` powinien zarządzać taskami, ale nie musi znać całego świata.
- `hint_2`: Zacznij od `self.tasks = tasks or []`, potem dodaj małe metody `add_task`, `mark_done`, `generate_report`.

## B10-S1

- `hint_1`: Test ma sprawdzić zachowanie, nie implementację.
- `hint_2`: Dla `mark_done` sprawdź zmianę `done` z `False` na `True`. Dla `generate_report` sprawdź liczniki i kolejność priorytetów.
