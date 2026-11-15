# Yatube

Учебный блог на Django, начатый в Яндекс Практикуме. Главная страница показывает последние публикации из SQLite. Через Django Admin можно создавать, искать и редактировать записи. Маршрут группы демонстрирует передачу короткого имени (`slug`) из URL.

## Мой вклад

В исходном проекте я настроила структуру Django и маршруты, создала модель `Post` с текстом, датой публикации и связью с автором, подготовила миграцию и настроила админку. Для версии в портфолио лента подключена к базе данных.

## Локальный запуск

Понадобится Python 3.10–3.14. Выполни команды из корня репозитория:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
python yatube/manage.py migrate
python yatube/manage.py createsuperuser
python yatube/manage.py runserver
```

Открой [админку](http://127.0.0.1:8000/admin/), войди под созданным пользователем и добавь публикацию с автором. Запись появится в [ленте](http://127.0.0.1:8000/). Пример маршрута группы доступен по адресу `/group/python/`.
