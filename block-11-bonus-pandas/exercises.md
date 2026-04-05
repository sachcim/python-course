# Bonus - Ćwiczenia

Korzystaj z pliku `data/orders.csv`. Jeśli nie masz jeszcze `pandas`, doinstaluj je przez `requirements-bonus-pandas.txt`.

## Core

### BP-C1 - Wczytaj i obejrzyj dane

Wczytaj `data/orders.csv` do `DataFrame` i wypisz:

- listę kolumn
- pierwsze 3 wiersze
- liczbę wszystkich zamówień

### BP-C2 - Kolumna total i filtrowanie

Dodaj kolumnę:

```python
total = price * quantity
```

Potem:

- policz średnią wartość `total`
- odfiltruj tylko zamówienia o statusie `paid`

### BP-C3 - Sortowanie

Posortuj zamówienia malejąco po `total` i wypisz 3 najwyższe zamówienia w formie:

- `customer`
- `category`
- `total`

## Plus

### BP-P1 - Grupowanie po kategorii

Zgrupuj dane po `category` i policz sumę kolumny `total` dla każdej kategorii.

## Stretch

### BP-S1 - Raport do JSON

Przygotuj raport:

```python
{
    "orders_count": ...,
    "paid_orders_count": ...,
    "average_total": ...,
    "top_orders": [...],
    "revenue_by_category": {...},
}
```

Gdzie:

- `orders_count` to liczba wszystkich zamówień
- `paid_orders_count` to liczba zamówień `paid`
- `average_total` to średnia z kolumny `total`
- `top_orders` to 3 najwyższe zamówienia
- `revenue_by_category` to suma `total` dla każdej kategorii

Zapisz raport do `output/pandas_report.json`.

## Git/GitHub checkpoint

### Artefakt bonusu

- pierwszy kontakt z `pandas`
- `DataFrame`, filtrowanie, sortowanie i prosty raport JSON

### Aktualizacja README

- dopisz w `Dzienny update`, czego `pandas` dał Ci szybciej niż ręczne pętle
- jeśli chcesz, dopisz krótkie zdanie do `Finał portfolio`, że zrobiłeś bonus analityczny po kursie

### Sugerowany commit

Bonus najlepiej zamknąć osobnym, krótkim commitem:

```bash
git status
git diff
git add .
git commit -m "bonus: intro to pandas"
git push
```
