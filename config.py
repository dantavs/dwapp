import os
import mysql.connector as mysql


HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

config = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE
}


def iniciar_banco():
    db = mysql.connect(**config)
    print(f'db: {db}')

    cursor = db.cursor()

    return {'db': db, 'cursor': cursor}
