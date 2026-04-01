# PythonCourse

Warsztatowy kurs Pythona rozpisany na 10 dni i 10 bloków. Materiał jest napisany po polsku dla osoby, która zna już absolutne podstawy i chce przejść do sensownej praktyki, a przy okazji budować sensowny ślad pracy na GitHubie.

## Jak korzystać z kursu

1. Otwórz `lesson.md` w wybranym bloku i przerób teorię oraz demo.
2. Rozwiąż zadania z `exercises.md` bez zaglądania do rozwiązań.
3. Jeśli utkniesz, użyj `hints.md`:
   - `hint_1` daje kierunek
   - `hint_2` daje konkretniejszą wskazówkę
4. Na końcu porównaj swoje podejście z `solutions.md`.
5. Zaktualizuj sekcję `Postęp 10 dni` oraz dodaj krótki wpis do `Dzienny update`.
6. Zakończ dzień jednym sensownym commitem i zrób `push`.

## Jak pracować z repo

Ten kurs zakłada jedno repo kursowe i pracę głównie na `main`. Celem nie jest spam commitami, tylko regularny, czytelny ślad postępu.

Start wykonujesz raz:

```bash
git init
git branch -M main
git add .
git commit -m "day-00: initialize python course repo"
```

Potem utwórz puste repo na GitHubie i podepnij je jako zdalne:

```bash
git remote add origin <url-z-githuba>
git push -u origin main
```

Podstawowy rytm dnia:

```bash
git status
git diff
git add .
git commit -m "day-XX: <krótki temat>"
git push
```

Pełny skrót komend i zasady jakości commitów znajdziesz w `git-github-playbook.md`.

## Struktura kursu

- `block-01-list-dict-set-tuple`
- `block-02-list-operations-pythonic`
- `block-03-filtering-and-processing`
- `block-04-functions`
- `block-05-files-json-csv`
- `block-06-errors-and-try-except`
- `block-07-classes-and-oop`
- `block-08-dataclass`
- `block-09-sorting-lambda-any-all`
- `block-10-mini-project`

Każdy blok ma stały układ:

- `lesson.md` - minimum teorii, przykład demo i sens użycia
- `exercises.md` - zadania `core`, `plus`, `stretch` oraz dzienny checkpoint Git/GitHub
- `hints.md` - warstwowe podpowiedzi bez wpychania gotowca
- `solutions.md` - rozwiązania referencyjne poza główną ścieżką

## Plan 10-dniowy

1. Dzień 1: listy, słowniki, sety, tuple
2. Dzień 2: operacje na listach i pythoniczne podstawy
3. Dzień 3: filtrowanie i przetwarzanie danych
4. Dzień 4: funkcje, typowanie i lekki wstęp do narzędzi
5. Dzień 5: pliki, JSON, CSV
6. Dzień 6: błędy i `try/except`
7. Dzień 7: klasy i OOP praktycznie
8. Dzień 8: `dataclass`
9. Dzień 9: sortowanie, `lambda`, `any`, `all`
10. Dzień 10: mini projekt `Task Report Generator`

## Postęp 10 dni

| Dzień | Blok | Status | Artefakt dnia | Commit dnia |
| --- | --- |-----| --- | --- |
| 1 | Listy, słowniki, sety, tuple | ✓   | Pierwsze skrypty z kolekcjami i porównaniem struktur | `day-01: collections basics` |
| 2 | Operacje na listach i pythoniczne podstawy | ✓   | Zadania z slicingiem, `enumerate` i `zip` | `day-02: list operations and slicing` |
| 3 | Filtrowanie i przetwarzanie danych | ✓   | Filtrowanie użytkowników i mały raport tekstowy | `day-03: filtering and list comprehensions` |
| 4 | Funkcje, typowanie i narzędzia | ✓   | Małe funkcje, pierwsze testy i `venv` | `day-04: functions and first tests` |
| 5 | Pliki, JSON, CSV | ✓   | Skrypty do odczytu, zapisu i prostych raportów | `day-05: files json and csv` |
| 6 | Błędy i `try/except` | ✓   | Obsługa wyjątków i odporne funkcje pomocnicze | `day-06: error handling and try except` |
| 7 | Klasy i OOP praktycznie | ✓    | Klasy `Book`, `Task`, `BankAccount` i proste użycie | `day-07: practical classes and oop` |
| 8 | `dataclass` | ✓   | Refaktor modeli danych do `dataclass` | `day-08: dataclass refactor` |
| 9 | Sortowanie, `lambda`, `any`, `all` | ⬜   | Sortowanie i logiczne sprawdzenia warunków | `day-09: sorting lambda any all` |
| 10 | Mini projekt `Task Report Generator` | ⬜   | Działający mini projekt z opisem uruchomienia | `day-10: finish task report generator` |

## Dzienny update

Po każdym dniu dopisz 2-4 zdania. Nie chodzi o pamiętnik, tylko o krótki ślad nauki.

Szablon:

```md
### Dzień XX - <temat>
Dziś zrobiłem ...
Najtrudniejsze było ...
Po tym dniu lepiej rozumiem ...
Jutro chcę domknąć ...
```

## Finał portfolio

W dniu 10 uzupełnij publiczny opis mini projektu w tym README. Wystarczą 3 krótkie elementy:

- co projekt robi
- jak go uruchomić
- czego nauczył Cię ten etap kursu

Możesz użyć takiego szkicu:

```md
## Mini projekt - Task Report Generator

Projekt wczytuje taski, liczy statystyki, sortuje dane po priorytecie i zapisuje raport.

Uruchomienie:
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `python3 -m pip install -r requirements-dev.txt`
4. `pytest block-10-mini-project/tests`

Na tym etapie nauczyłem się ...
```

## Lekki moduł narzędziowy

Po bloku 4 możesz pracować we własnym środowisku:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
```

`pytest` jest używany lekko i głównie w mini projekcie z bloku 10.

## Zasady pracy

- Najpierw własna próba, potem podpowiedź.
- Czytelność kodu jest ważniejsza niż sztuczki.
- Jeden sensowny commit dziennie jest obowiązkowy. Więcej tylko wtedy, gdy zmiany są logicznie rozdzielone.
- Nie commituj środowiska `.venv`, cache ani wygenerowanych plików wynikowych.
- Jeśli nie umiesz czegoś wytłumaczyć prostymi słowami, wróć do krótszego przykładu.
- Po każdym bloku odpowiedz sobie: co robi ten kod, czemu działa, czy umiem zrobić podobny bez patrzenia.
