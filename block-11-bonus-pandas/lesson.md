# Bonus - Pandas

## Cel

Po tym bonusie masz rozumieć, kiedy `pandas` daje przewagę nad ręcznym `csv.DictReader` i jak zrobić prostą analizę tabeli bez przepisywania wszystkiego pętlami.

## Minimum teorii

- `pandas` pracuje głównie na `DataFrame`, czyli tabeli danych.
- `pd.read_csv(...)` wczytuje CSV do `DataFrame`.
- Możesz brać pojedyncze kolumny, filtrować wiersze i tworzyć nowe kolumny.
- `sort_values(...)` sortuje tabelę po wybranej kolumnie.
- `groupby(...)` grupuje dane i pozwala liczyć podsumowania.

## Demo

```python
from pathlib import Path

import pandas as pd

path = Path("data/orders.csv")
df = pd.read_csv(path)

df["total"] = df["price"] * df["quantity"]

paid_orders = df[df["status"] == "paid"]
sorted_orders = df.sort_values("total", ascending=False)

print(df[["customer", "total"]])
print(paid_orders[["customer", "total"]])
print(sorted_orders[["customer", "total"]].head(3))
print(df["total"].mean())
```

## Jak o tym myśleć

- `csv.DictReader` uczy Cię podstaw i daje pełną kontrolę.
- `pandas` ma sens, gdy dane stają się bardziej tabelaryczne i chcesz szybciej filtrować, grupować i liczyć podsumowania.
- Nie porzucasz podstaw. Po prostu dostajesz wygodniejsze narzędzie do konkretnego typu problemów.

## Typowe błędy

- Wchodzenie w `pandas` bez rozumienia, skąd biorą się kolumny i typy danych.
- Zgadywanie nazw kolumn zamiast sprawdzić `df.columns`.
- Mieszanie `list` i `DataFrame` bez świadomości, na czym aktualnie pracujesz.
- Tworzenie bonusu `pandas`, gdy jeszcze nie rozumiesz `csv.DictReader`.

## Co wyszukać

- `pandas read_csv`
- `pandas filter rows`
- `pandas sort_values`
- `pandas groupby sum`
- `pandas to_dict orient records`

## Jak pytać AI

- `porównaj to samo zadanie w csv.DictReader i pandas`
- `wyjaśnij mi dataframe prostymi słowami`
- `daj mi 3 małe zadania na pandas bez rozwiązań`

## Checkpoint

Powinieneś umieć:

- wczytać CSV do `DataFrame`
- dodać kolumnę wyliczaną
- odfiltrować tylko wybrane wiersze
- posortować dane po jednej kolumnie
- zrobić prosty raport do JSON

## Jak sprawdzić, czy umiesz

- Umiesz powiedzieć, kiedy lepiej użyć `csv.DictReader`, a kiedy `pandas`.
- Umiesz policzyć prostą statystykę bez ręcznej pętli po każdym wierszu.
- Umiesz zamienić fragment `DataFrame` na dane do JSON przez `to_dict(...)`.
