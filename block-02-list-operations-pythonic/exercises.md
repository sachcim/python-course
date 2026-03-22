# Blok 2 - Ćwiczenia

## Core

### B2-C1 - Odczyt i slicing

Dla listy:

```python
fruits = ["apple", "banana", "orange", "kiwi"]
```

wypisz:

- pierwszy element
- ostatni element
- dwa pierwsze elementy
- listę od końca

### B2-C2 - Enumerate

Użyj `enumerate`, żeby wypisać:

```text
1. apple
2. banana
3. orange
4. kiwi
```

### B2-C3 - Zip

Połącz:

```python
names = ["Michał", "Ania", "Tomek"]
scores = [90, 75, 88]
```

i wypisz:

```text
Michał -> 90
Ania -> 75
Tomek -> 88
```

## Plus

### B2-P1 - Różne wycinki

Dla listy `numbers = [10, 20, 30, 40, 50, 60]` wypisz:

- co drugi element
- trzy ostatnie elementy
- wszystko oprócz pierwszego i ostatniego

## Stretch

### B2-S1 - Ranking zawodników

Masz:

```python
players = ["Michał", "Ania", "Tomek", "Ola"]
points = [12, 8, 15, 11]
```

Połącz dane przez `zip`, ponumeruj przez `enumerate(start=1)` i wypisz ranking w formacie:

```text
1. Michał - 12 pkt
```

Na końcu wypisz też listę punktów od końca.

## Git/GitHub checkpoint

### Artefakt dnia

- rozwiązania z `slicing`, `enumerate` i `zip`
- pierwszy czytelny commit po pełnym dniu pracy

### Aktualizacja README

- zaznacz dzień 2 w tabeli `Postęp 10 dni`
- dopisz 2-4 zdania, w tym jedno o tym, czemu `[::-1]` działa

### Sugerowany commit

Przed commitem zobacz różnicę i krótką historię:

```bash
git status
git diff
git add .
git commit -m "day-02: list operations and slicing"
git log --oneline -5
git push
```
