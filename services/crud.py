import psycopg2
from dotenv import load_dotenv
import os


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

    def add(self, request):
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
                )
            )
