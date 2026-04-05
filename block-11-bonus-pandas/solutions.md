# Bonus - Rozwiązania referencyjne

## BP-C1

```python
from pathlib import Path

import pandas as pd

df = pd.read_csv(Path("data/orders.csv"))

print(list(df.columns))
print(df.head(3))
print(len(df))
```

## BP-C2

```python
df["total"] = df["price"] * df["quantity"]

average_total = df["total"].mean()
paid_orders = df[df["status"] == "paid"]

print(average_total)
print(paid_orders)
```

## BP-C3

```python
sorted_orders = df.sort_values("total", ascending=False)

print(sorted_orders[["customer", "category", "total"]].head(3))
```

## BP-P1

```python
revenue_by_category = df.groupby("category")["total"].sum()
print(revenue_by_category)
```

## BP-S1

```python
import json
from pathlib import Path

import pandas as pd

df = pd.read_csv(Path("data/orders.csv"))
df["total"] = df["price"] * df["quantity"]

paid_orders = df[df["status"] == "paid"]
top_orders = (
    df.sort_values("total", ascending=False)[["customer", "category", "total"]]
    .head(3)
    .to_dict(orient="records")
)
revenue_by_category = df.groupby("category")["total"].sum().to_dict()

report = {
    "orders_count": len(df),
    "paid_orders_count": len(paid_orders),
    "average_total": df["total"].mean(),
    "top_orders": top_orders,
    "revenue_by_category": revenue_by_category,
}

output_path = Path("output/pandas_report.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", encoding="utf-8") as file:
    json.dump(report, file, ensure_ascii=False, indent=2)
```
