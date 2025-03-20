# Webscraping Bot

### Описание

Возможности бота:
* Получает файлы Excel от пользователей;
* Сохраняет файлы на сервере;
* Получает из таблицы данные по веб-сайтам для парсера и сохраняет их в БД;
* Выводит данные о сохраненных сайтах пользователю;
* Отправляет сообщение об ошибке в случае, если данные из таблицы не прошли валидацию;
* Выводит меню по команде `/start` или `/menu`.

### Стек технологий:

* Python (3.12)
* Aiogram
* SQLAlchemy
* pandas
* SQLite

### Как развернуть бота:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:NikitaPreis/webscraping-bot
cd webscraping-bot
```

Создать и активировать виртуальное окружение:
```
python -m venv .venv
source venv/Scripts/activate
```

Установить зависимости:
```
pip install -r requirements.txt
```

Установить переменную окружения в файле .env:
```
# Токен бота
BOT_API_TOKEN=<YOUR_BOT_API_TOKEN>
```

Запустить бота:
```
python -m src.main
```
