# Aircraft Tracker

Проект получает информацию о самолетах, находящихся в воздушном пространстве различных стран, используя публичные API OpenStreetMap (Nominatim) и OpenSky Network, а затем сохраняет полученные данные в базу данных PostgreSQL.

## Возможности

- Получение координат выбранной страны через Nominatim API.
- Получение информации о самолетах через OpenSky API.
- Автоматическое создание базы данных PostgreSQL.
- Создание таблиц `country` и `airplane`.
- Заполнение базы данных актуальной информацией.
- Выполнение SQL-запросов через класс `DBManager`.

## Используемые технологии

- Python 3
- PostgreSQL
- psycopg2
- requests
- python-dotenv

## Установка

1. Клонируйте репозиторий:

```bash
git clone <repository_url>
```

2. Перейдите в папку проекта:

```bash
cd db_aircraft_tracker
```

3. Установите зависимости:

```bash
poetry install
```

4. Создайте файл `.env` и заполните его:

```
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

5. Запустите проект:

```bash
python main.py
```

## Методы класса DBManager

- `get_countries_and_aeroplanes_count()` — список стран и количество самолетов.
- `get_all_aeroplanes()` — список всех самолетов.
- `get_avg_speed()` — средняя скорость самолетов.
- `get_aeroplanes_with_higher_speed()` — самолеты со скоростью выше средней.
- `get_aeroplanes_with_keyword(keyword)` — поиск самолетов по части позывного.

## Используемые API

- OpenSky Network API
- OpenStreetMap Nominatim API