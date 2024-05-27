import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv
from models.foods import RequestModel
from datetime import datetime


class CRUD:
    def __init__(self):
        load_dotenv()
        self.database_parameters = {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
        }

    def _get_conection(self):
        return psycopg2.connect(**self.database_parameters)

    def create(self):
        try:
            with self._get_conection() as connection:
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
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert(self, request_model):
        try:
            with self._get_conection() as connection:
                cursor = connection.cursor()
                query = """
                        INSERT INTO foodsrequests
                            (first_name, last_name, address, date, requests)
                        VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(
                    query,
                    (
                        request_model.first_name,
                        request_model.last_name,
                        request_model.address,
                        request_model.date,
                        request_model.requests,
                    ),
                )
        except Exception as e:
            print(f"An error occurred: {e}")

    def read(self):
        try:
            with self._get_conection() as connection:
                query = """
                        SELECT * FROM foodsrequests
                """
                table = pd.read_sql_query(query, connection)
                return table
        except Exception as e:
            print(f"An error occurred: {e}")

    def update(self, request_model):
        try:
            with self._get_conection() as connection:
                cursor = connection.cursor()
                query = """
                        UPDATE foodsrequests
                        SET requests = CONCAT(requests, %s)
                        WHERE first_name = %s AND last_name = %s
                    """
                cursor.execute(
                    query,
                    (
                        request_model.requests,
                        request_model.first_name,
                        request_model.last_name,
                    ),
                )
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete(self, first_name, last_name):
        try:
            with self._get_conection() as connection:
                cursor = connection.cursor()
                query = """
                        DELETE FROM foodsrequests
                        WHERE first_name=%s AND last_name=%s
                """
                cursor.execute(query, (first_name, last_name))
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_existence(self, first_name, last_name):
        try:
            with self._get_conection() as connection:
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
        except Exception as e:
            print(f"An error occurred: {e}")
