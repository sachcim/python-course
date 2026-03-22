# Blok 10 - Ćwiczenia

Korzystaj z `data/tasks.json` i startera z katalogu `starter/`.

## Core

### B10-C1 - Policz i posortuj

Na podstawie listy tasków:

- policz wszystkie taski
- policz ukończone
- policz nieukończone
- zwróć taski posortowane po priorytecie

Na tym etapie pracuj jeszcze na słownikach.

### B10-C2 - Zapisz raport

Zapisz raport do pliku JSON albo TXT. Rekomendacja: `output/report.json`.

### B10-C3 - Refaktor do dataclass

Przepisz taski na `Task` jako `dataclass` i zachowaj działające generowanie raportu.

## Plus

### B10-P1 - TaskManager

Dodaj klasę `TaskManager`, która:

- przechowuje taski
- dodaje task
- oznacza task jako wykonany
- generuje raport

## Stretch

### B10-S1 - Testy

Dodaj podstawowe testy `pytest` dla:

- `mark_done`
- `generate_report`

Skorzystaj z pliku `tests/test_task_manager.py` jako punktu startowego albo napisz własne.

## Git/GitHub checkpoint

### Artefakt dnia

- działający `Task Report Generator`
- opis uruchomienia projektu
- końcowy publiczny ślad pracy w `README`

### Aktualizacja README

- zaznacz dzień 10 w tabeli `Postęp 10 dni`
- uzupełnij sekcję `Finał portfolio` o opis projektu, uruchomienie i krótki wniosek z kursu

### Sugerowany commit

To ma być commit, który da się pokazać na GitHubie bez tłumaczenia, co autor miał na myśli. Jeśli chcesz domknąć kurs wyraźnym punktem, możesz dodać opcjonalny tag `day-10-complete`.

```bash
git status
git diff
git add .
git commit -m "day-10: finish task report generator"
git push
```

Opcjonalnie:

```bash
git tag day-10-complete
git push origin day-10-complete
```
