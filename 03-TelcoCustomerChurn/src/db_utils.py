# Importing the sqlite3 library to work with SQLite databases
import sqlite3

def get_connection(db_path="data/telco_customer_churn.db"):
    return sqlite3.connect(db_path)
