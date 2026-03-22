# Blok 7 - Ćwiczenia

## Core

### B7-C1 - Book

Zrób klasę `Book` z polami:

- `title`
- `author`

Dodaj metodę `describe()`, która zwraca tekst:

```text
<title> - <author>
```

### B7-C2 - Task

Zrób klasę `Task` z polami:

- `title`
- `done`

Dodaj metodę `mark_done()`, która oznacza task jako wykonany.

### B7-C3 - BankAccount

Zrób klasę `BankAccount` z polami:

- `owner`
- `balance`

Dodaj metody:

- `deposit(amount)`
- `withdraw(amount)`

Przy wypłacie nie pozwalaj zejść poniżej zera.

## Plus

### B7-P1 - Praktyczny obiekt

Utwórz po jednym obiekcie każdej klasy i pokaż krótkim kodem:

- utworzenie obiektu
- zmianę stanu
- wywołanie metody

## Stretch

### B7-S1 - TaskList

Zrób klasę `TaskList`, która:

- przechowuje listę obiektów `Task`
- dodaje nowy task
- zwraca listę tasków niewykonanych

To będzie dobry most do bloku 10.

## Git/GitHub checkpoint

### Artefakt dnia

- klasy `Book`, `Task`, `BankAccount`
- pierwszy kod, w którym zmienia się nie tylko logika, ale też struktura modelu

### Aktualizacja README

- zaznacz dzień 7 w tabeli `Postęp 10 dni`
- dopisz jedno zdanie o tym, kiedy klasa miała sens bardziej niż sama funkcja albo słownik

### Sugerowany commit

Nazwij commit tak, żeby było widać, że dotyczy modelu danych i metod obiektów, a nie przypadkowego "refactoru wszystkiego".

```bash
git status
git diff
git add .
git commit -m "day-07: practical classes and oop"
git push
```
