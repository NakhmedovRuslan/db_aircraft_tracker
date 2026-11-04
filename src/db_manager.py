import psycopg2

from config import config_db


class DBManager:
    """Класс для работы с БД."""

    def __init__(self, db_name: str):
        self.conn = psycopg2.connect(dbname=db_name, **config_db())

    def get_countries_and_aeroplanes_count(self):
        """
        Возвращает список стран и количество самолетов
        в воздушном пространстве каждой страны.
        """

        with self.conn.cursor() as cursor:

            cursor.execute("""
                SELECT
                    country.name,
                    COUNT(airplane.id)
                FROM country
                LEFT JOIN airplane
                    ON country.id = airplane.country_id
                GROUP BY country.name
                ORDER BY country.name
            """)

            return cursor.fetchall()

    def get_all_aeroplanes(self):
        """
        Возвращает список всех самолетов.
        """

        with self.conn.cursor() as cursor:

            cursor.execute("""
                SELECT
                    callsign,
                    country_register,
                    velocity,
                    altitude
                FROM airplane
                ORDER BY callsign
            """)

            return cursor.fetchall()

    def get_avg_speed(self):
        """
        Возвращает среднюю скорость самолетов.
        """

        with self.conn.cursor() as cursor:

            cursor.execute("""
                SELECT AVG(velocity)
                FROM airplane
            """)

            return cursor.fetchone()[0]

    def get_aeroplanes_with_higher_speed(self):
        """
        Самолеты, скорость которых выше средней.
        """

        with self.conn.cursor() as cursor:

            cursor.execute("""
                SELECT
                    callsign,
                    velocity
                FROM airplane
                WHERE velocity >
                (
                    SELECT AVG(velocity)
                    FROM airplane
                )
                ORDER BY velocity DESC
            """)

            return cursor.fetchall()

    def get_aeroplanes_with_keyword(self, keyword):
        """
        Поиск самолета по части позывного.
        """

        with self.conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT
                    callsign,
                    country_register,
                    velocity,
                    altitude
                FROM airplane
                WHERE callsign ILIKE %s
                ORDER BY callsign
            """,
                (f"%{keyword}%",),
            )

            return cursor.fetchall()

    def close(self):
        self.conn.close()
