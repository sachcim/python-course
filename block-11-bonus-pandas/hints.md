# Bonus - Podpowiedzi

## BP-C1

- `hint_1`: Zacznij od `pd.read_csv(...)`.
- `hint_2`: Kolumny sprawdzisz przez `df.columns`, pierwsze wiersze przez `df.head(3)`, liczbę rekordów przez `len(df)`.

## BP-C2

- `hint_1`: W `pandas` da się policzyć nową kolumnę bez pętli.
- `hint_2`: Użyj `df["total"] = df["price"] * df["quantity"]`, a filtrowanie zrób przez `df[df["status"] == "paid"]`.

## BP-C3

- `hint_1`: Do sortowania służy `sort_values(...)`.
- `hint_2`: Sprawdź `df.sort_values("total", ascending=False)` i potem wybierz tylko potrzebne kolumny.

## BP-P1

- `hint_1`: Najpierw zbuduj kolumnę `total`, dopiero potem grupuj.
- `hint_2`: Sprawdź `df.groupby("category")["total"].sum()`.

## BP-S1

- `hint_1`: Nie zapisuj całego `DataFrame` bezmyślnie. Najpierw zbuduj zwykły słownik raportu.
- `hint_2`: `top_orders` możesz zamienić na listę słowników przez `to_dict(orient="records")`, a wynik grupowania na słownik przez `.to_dict()`.
