# restaurant_project
### Описание:
Restaurant API - проект получения данных о категориях и блюдах ресторана.

### Технологии:

[![name badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![name badge](https://img.shields.io/badge/Django-3776AB?logo=django&logoColor=white)](https://docs.djangoproject.com/en/4.2/releases/3.2/)
[![name badge](https://img.shields.io/badge/Django_REST_framework-3776AB?logo=djangorestramework&logoColor=white)](https://www.django-rest-framework.org/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Anna9449/restaurant_project.git
```
```
cd restaurant_project
```

Создать файл .env и заполните его своими данными, пример:

```
SECRET_KEY=*** # Секретный ключ Django (без кавычек).
ALLOWED_HOSTS=*** # Список разрешённых хостов (через запятую и без пробелов)
DEBUG=False # Выбрать режим отладки
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Документация к API:

Документация к API проекта доступна по ссылкам:

- http://127.0.0.1:8000/api/schema/swagger-ui/
- http://127.0.0.1:8000/api/schema/redoc/

### Автор
[![name badge](https://img.shields.io/badge/Anna_Pestova-3776AB?logo=github&logoColor=white)](https://github.com/Anna9449)