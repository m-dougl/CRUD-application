import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv


class CRUD:
    def __init__(self):
        load_dotenv()

    def create(self):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            cursor = connection.cursor()
            query = """
                    CREATE TABLE IF NOT EXISTS foodsrequests(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(20) NOT NULL,
                        last_name VARCHAR(20) NOT NULL,
                        address TEXT NOT NULL,
                        date DATE NOT NULL,
                        requests TEXT
                    )
            """
            cursor.execute(query)

    def insert(self, request):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            cursor = connection.cursor()
            query = """
                    INSERT INTO foodsrequests
                        (first_name, last_name, address, date, requests)
                    VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(
                query,
                (
                    request.first_name,
                    request.last_name,
                    request.address,
                    request.date,
                    request.requests,
                ),
            )

    def read(self):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            query = """
                    SELECT * FROM foodsrequests
            """
            table = pd.read_sql_query(query, connection)
            return table

    def update(self, new_values, first_name, last_name):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            cursor = connection.cursor()
            query = """
                    UPDATE foodsrequests
                    SET requests = %s
                    WHERE first_name = %s AND last_name = %s
                """
            cursor.execute(query, (new_values, first_name, last_name))

    def delete(self, first_name, last_name):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            cursor = connection.cursor()
            query = """
                    DELETE FROM foodsrequests
                    WHERE first_name=%s AND last_name=%s
            """
            cursor.execute(query, (first_name, last_name))

    def check_existence(self, first_name, last_name):
        with psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        ) as connection:
            cursor = connection.cursor()
            query = """
                    SELECT first_name, last_name FROM foodsrequests
                    WHERE first_name=%s AND last_name=%s
            """
            cursor.execute(query, (first_name, last_name))
            if cursor.fetchone():
                return True
            else:
                return False


if __name__ == "__main__":
    print(CRUD().check_existence("douglas", "maia"))
