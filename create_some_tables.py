import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE Данные_карты(
                Номер_карты int PRIMARY KEY,
                Тип_карты varchar(10),
                Срок_действия date,
                Имя_владельца varchar(40),
                Код_безопасности int);"""
        )
        print("[INFO] Table created successfully")

except Exception as _ex:
    print("[INFO] Error while working with PosgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")