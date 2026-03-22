# Blok 2 - Operacje na listach i pythoniczne podstawy

## Cel

Po tym bloku masz swobodnie używać indeksowania, slicingu, `enumerate` i `zip`.

## Minimum teorii

- `numbers[0]` bierze pierwszy element.
- `numbers[-1]` bierze ostatni element.
- `numbers[1:4]` bierze wycinek od indeksu 1 do 3.
- `numbers[::-1]` zwraca listę od końca.
- `enumerate(...)` daje indeks i wartość.
- `zip(...)` łączy elementy z kilku kolekcji parami.

## Demo

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::-1])

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

names = ["Michał", "Ania"]
scores = [90, 75]
for name, score in zip(names, scores):
    print(f"{name} -> {score}")
```

## Jak o tym myśleć

- Slicing to szybki sposób na wyciągnięcie fragmentu listy.
- `[::-1]` oznacza: przejdź od końca z krokiem `-1`.
- `enumerate` jest czytelniejsze niż ręczny licznik.
- `zip` przydaje się wtedy, gdy dwie listy opisują ten sam zestaw rzeczy.

## Typowe błędy

- Mylenie końca zakresu w slicingu: `1:4` nie zawiera elementu o indeksie `4`.
- Ręczne liczniki tam, gdzie wystarczy `enumerate`.
- Zakładanie, że `zip` połączy listy do długości dłuższej z nich.

## Co wyszukać

- `python slicing`
- `python enumerate`
- `python zip examples`

## Jak pytać AI

- `wyjaśnij mi slicing jak początkującemu, zwłaszcza [::-1]`
- `daj mi 5 ćwiczeń z enumerate i zip`

## Checkpoint

Powinieneś rozumieć:

- czemu `[::-1]` działa
- kiedy `enumerate` jest lepsze niż ręczny licznik
- po co `zip`

## Jak sprawdzić, czy umiesz

- Umiesz bez patrzenia wyjaśnić `lista[start:stop:krok]`.
- Umiesz ponumerować listę bez tworzenia własnego `counter`.
- Umiesz połączyć listę imion i wyników w jedną pętlę.
