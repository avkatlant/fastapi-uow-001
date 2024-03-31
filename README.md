# fastapi-uow-001

## Начало работы

Для того чтобы выполнить описанные ниже команды, вам необходимо:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

**ПРИМЕЧАНИЕ**: В проекте используется Python 3.11, поэтому сначала необходимо установить его.

### Вот краткая инструкция о том, как быстро настроить проект для разработки:

1. Установите [`poetry`](https://python-poetry.org/)
2. Установите зависимости:

```bash
poetry install
poetry shell
```

3. Установите pre-commit hooks: `pre-commit install`

4. Запустите контейнер с БД: `make local`

5. Примените миграции:

```bash
alembic -c src/models/alembic.ini upgrade head
```

6. Выполните команду в консоле:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
# or
gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
# or
gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --capture-output --log-level debug --access-logfile '-' --error-logfile '-' --reload
```

7. Документация API:
    - http://localhost:8000/docs
    - http://localhost:8000/redoc


### Другие команды:

Отображение логов контейнеров:  
`make local_logs`

Остановить и удалить контейнеры:  
`make local_down`

Удалите БД для разработки (не забудьте остановить контейнеры!):  
`make local_db_del`


Откройть в терминале запущенный контейнер:

```bash
docker exec -it [id|name container] /bin/bash
# or:
docker exec -it [id|name container] /bin/zsh
```

Создание миграций:

```sh
alembic -c src/models/alembic.ini revision --autogenerate -m "name"
```

Применение миграций:

```sh
alembic -c src/models/alembic.ini upgrade head
# or:
alembic -c src/models/alembic.ini upgrade [revision]
```

Откатить миграцию:

```sh
alembic -c src/models/alembic.ini downgrade -1
```

Проверка mypy:
```sh
mypy --config-file mypy.ini src/main.py
# or
mypy --config-file mypy.ini src/**/*.py
```

Запуск форматирования кода (black):

```sh
black src/
```
