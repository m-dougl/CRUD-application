import psycopg2
from dotenv import load_dotenv
import os

class CRUD:
    def create(self):
        with psycopg2.connect(host=os.getenv("DB_HOST"),
                              port=os.getenv("DB_PORT"),
                              dbname=os.getenv("DB_NAME"),
                              user=os.getenv("DB_USER"),
                              password=os.getenv("DB_PASSWORD")) as connection:
            cursor = connection.cursor()
            query = """
                    CREATE TABLE IF NOT EXISTS foodsrequests(
                        id INTEGER PRIMARY KEY,
                        first_name VARCHAR(20) NOT NULL,
                        last_name VARCHAR(20) NOT NULL,
                        addresss TEXT NOT NULL,
                        date DATE NOT NULL,
                        requests TEXT NOT NULL
                    )
            """
            cursor.execute(query)
        
    def add(self, 
            first_name,
            last_name,
            address,
            date,
            burguer_choice, 
            burguer_quantity, 
            soup_choice, 
            soup_quantity):
        with psycopg2.connect(host=os.getenv("DB_HOST"),
                              port=os.getenv("DB_PORT"),
                              dbname=os.getenv("DB_NAME"),
                              user=os.getenv("DB_USER"),
                              password=os.getenv("DB_PASSWORD")) as connection:
            cursor = connection.cursor()
            query = """
                    INSERT INTO foodsrequests
                        (first_name, last_name, address, date, requests)
                    VALUES ?, ?, ?, ?, ?
            """
                
                
if __name__ == "__main__":
    CRUD().create()