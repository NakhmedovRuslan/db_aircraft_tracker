import psycopg2

from config import config_db


def create_db(db_name):
    conn = psycopg2.connect(
        database="postgres", **config_db())
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cursor.execute(f"CREATE DATABASE {db_name}")
    cursor.close()
    conn.close()

db_name = "airplanes"
create_db(db_name)

# class DBManager:
#     def __init__(self):
#         self.conn = psycopg2.connect(
#             dbname=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             host=DB_HOST,
#             port=DB_PORT,
#         )
#
#         self.cursor = self.conn.cursor()
#
#     def close(self):
#         self.cursor.close()
#         self.conn.close()