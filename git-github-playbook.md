# Git i GitHub Playbook

To jest minimalny workflow do tego kursu. Ma pomagać budować nawyk pracy z repo i sensowną historię na GitHubie, a nie robić z kursu osobny bootcamp z Gita.

## Cel tego toru

- jedno repo kursowe
- praca głównie na `main`
- jeden sensowny commit na koniec każdego dnia
- regularny `push` na GitHub
- czytelna historia, bez sztucznego nabijania aktywności

## Setup na start

Jeśli katalog nie jest jeszcze repozytorium:

```bash
git init
git branch -M main
git add .
git commit -m "day-00: initialize python course repo"
```

Potem utwórz repo na GitHubie i podepnij zdalne:

```bash
git remote add origin <url-z-githuba>
git push -u origin main
```

Publiczne repo jest preferowane, jeśli chcesz, żeby ten kurs realnie budował profil.

## Dzienny workflow

Na koniec każdego dnia:

```bash
git status
git diff
git add .
git commit -m "day-XX: <krótki temat>"
git push
```

Jeśli chcesz szybko zobaczyć historię:

```bash
git log --oneline -5
```

## Co robi każda komenda

- `git status` pokazuje, co się zmieniło i co jest gotowe do commita.
- `git diff` pokazuje treść zmian przed dodaniem lub commitem.
- `git add .` zbiera aktualną porcję pracy do commita.
- `git commit -m "..."` zapisuje logiczny etap pracy.
- `git log --oneline` pozwala ocenić, czy historia wygląda czytelnie.
- `git push` wysyła aktualny stan na GitHub.

## Zasady dobrych commitów

- Jeden commit ma odpowiadać jednej logicznej porcji pracy.
- Commit ma opisywać efekt, nie wysiłek.
- `day-04: functions and first tests` jest dobre.
- `update`, `fix`, `stuff`, `kolejne zmiany` są za słabe.
- Jeśli w danym dniu zrobiłeś dwie naprawdę osobne rzeczy, drugi commit jest OK, ale nie jest obowiązkowy.

## Czego nie commitować

Do repo nie wrzucaj:

- `.venv/`
- `__pycache__/`
- `.pytest_cache/`
- wygenerowanych plików wynikowych jak `users_updated.json`, `report.json` albo katalogów `output/`
- plików tymczasowych z edytora albo systemu

Jeśli coś wygląda na wygenerowany wynik ćwiczenia, a nie materiał źródłowy kursu, zwykle nie powinno trafić do commita.

## Rytm Git w tym kursie

- Dzień 0: inicjalizacja repo i pierwszy push.
- Dzień 1: pierwszy pełny commit po kolekcjach.
- Dzień 2: zacznij używać `git diff` i `git log --oneline`.
- Dzień 4: sprawdź `.gitignore` po wejściu w `venv`.
- Dzień 6: przed commitem zawsze rzuć okiem na `git diff`.
- Dzień 8: potraktuj przejście na `dataclass` jako refaktor i nazwij commit właśnie tak.
- Dzień 10: dopracuj README, zrób finalny push, opcjonalnie dodaj tag:

```bash
git tag day-10-complete
git push origin day-10-complete
```

## Szybka checklista przed push

- Zadania `core` na dany dzień są skończone.
- `README.md` ma uzupełniony status dnia i krótki wpis postępu.
- `git status` nie pokazuje przypadkowych śmieci.
- Commit ma konkretną nazwę.
- Wiesz, co dokładnie wrzucasz na GitHub.
