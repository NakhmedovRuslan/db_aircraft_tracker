from src.db_manager import DBManager

db = DBManager()

print("Подключение к базе данных успешно!")

db.close()