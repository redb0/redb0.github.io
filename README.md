# Личный сайт

Личный сайт [Владимира Воронова](https://redb0.github.io/) на [Pelican](https://getpelican.com/).

Прод-URL задаётся в `publishconf.py`: `SITEURL = "https://redb0.github.io"` (без завершающего слэша).

```bash
uv sync
make devserver
```

Деплой — GitHub Actions при пуше в `main` (`publishconf.py`).
