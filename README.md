# QRKOT

Приложение для Благотворительного фонда поддержки котиков QRKot. 
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологический стек

- Python 3.9
- **Веб-фреймворк:** FastApi
- SQLAlchemy
- Alembic
- Uvicorn

## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ibonish/cat_charity_fund.git
```

```
cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корневой директории создать файл .env и наполнить его:

```
app_title = 'Сервис для поддержки котиков!'
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET = 'ваш секретный ключ'
```

Запустить проект командой:

```
uvicorn app.main:app --reload
```

## Автор:

- [Скрябина Ольга](https://github.com/ibonish)