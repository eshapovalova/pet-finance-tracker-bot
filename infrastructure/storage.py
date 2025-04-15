import sqlite3
from datetime import datetime

DB_NAME = "finance.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS incomes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        amount REAL, 
                        timestamp TEXT
                    )
                    """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL,
                category TEXT,
                timestamp TEXT
            )
        """)
        conn.commit()
        
def add_income(user_id, amount):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO incomes (user_id, amount, timestamp) VALUES (?, ?, ?)",
            (user_id, amount, datetime.now().isoformat())
        )
        conn.commit()

def add_expense(user_id, amount, category):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (user_id, amount, category, timestamp) VALUES (?, ?, ?, ?)",
            (user_id, amount, category, datetime.now().isoformat())
        )
        conn.commit()

def get_summary(user_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM incomes WHERE user_id = ?", (user_id,))
        total_income = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,))
        total_expense = cursor.fetchone()[0] or 0

        return total_income, total_expense, total_income - total_expense