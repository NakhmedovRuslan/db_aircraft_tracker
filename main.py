from src.db_manager import DBManager
from src.utils_db import create_database, create_tables, fill_database

DB_NAME = "airplanes"

create_database(DB_NAME)
create_tables(DB_NAME)
fill_database(DB_NAME)

db = DBManager(DB_NAME)

print()
print(db.get_countries_and_aeroplanes_count())

print()
print(db.get_all_aeroplanes())

print()
print(db.get_avg_speed())

print()
print(db.get_aeroplanes_with_higher_speed())

print()
print(db.get_aeroplanes_with_keyword("ACA"))

db.close()
