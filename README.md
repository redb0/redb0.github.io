# Личный сайт

Личный сайт [Владимира Воронова](https://redb0.github.io/) на [Pelican](https://getpelican.com/).

Прод-URL задаётся в `publishconf.py`: `SITEURL = "https://redb0.github.io"` (без завершающего слэша).

## Сборка

```bash
uv sync
make devserver                 # pelican -lr, http://localhost:8000
# или
uv run invoke livereload
```

Прод-сборка локально (без выкладки): `make publish` или `uv run invoke preview`.

Зависимости пинятся в `uv.lock`. `requirements.txt` для pip генерируется из lock:

```bash
make requirements
```

JS не минифицируется (`rjsmin` в зависимостях нет). CSS — `cssmin` через webassets.

## Деплой

Только GitHub Actions при пуше в `main` (`.github/workflows/pelican.yml`, конфиг `publishconf.py`). Локальный `gh-pages` / rsync не используется.

## Опечатки

```bash
pre-commit install   # хук typos
# или разово:
uvx typos
```
