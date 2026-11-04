import psycopg2

from config import COUNTRIES, config_db
from src.api import APIAdapter


def create_database(db_name: str):
    """Создает базу данных."""

    conn = psycopg2.connect(dbname="postgres", **config_db())

    conn.autocommit = True

    with conn.cursor() as cursor:
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cursor.execute(f"CREATE DATABASE {db_name}")

    conn.close()


def create_tables(db_name: str):
    """Создает таблицы country и airplane."""

    conn = psycopg2.connect(dbname=db_name, **config_db())

    with conn:
        with conn.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE country
                (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) UNIQUE NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE airplane
                (
                    id SERIAL PRIMARY KEY,
                    callsign VARCHAR(30),
                    country_register VARCHAR(100),
                    velocity FLOAT,
                    altitude FLOAT,
                    country_id INTEGER REFERENCES country(id)
                )
            """)

    conn.close()


def fill_database(db_name: str):
    """Заполняет БД странами и самолетами."""

    api = APIAdapter()

    conn = psycopg2.connect(dbname=db_name, **config_db())

    with conn:
        with conn.cursor() as cursor:

            for country in COUNTRIES:

                cursor.execute(
                    """
                    INSERT INTO country(name)
                    VALUES(%s)
                    RETURNING id
                    """,
                    (country,),
                )

                country_id = cursor.fetchone()[0]

                airplanes = api.get_aeroplanes(country)

                for airplane in airplanes:

                    cursor.execute(
                        """
                        INSERT INTO airplane
                        (
                            callsign,
                            country_register,
                            velocity,
                            altitude,
                            country_id
                        )
                        VALUES(%s,%s,%s,%s,%s)
                        """,
                        (
                            airplane["callsign"],
                            airplane["country_register"],
                            airplane["velocity"],
                            airplane["altitude"],
                            country_id,
                        ),
                    )

    conn.close()
