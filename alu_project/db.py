import sqlite3
from datetime import datetime

DB_FILE = "logs.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                gate TEXT,
                task TEXT,
                status TEXT,
                result TEXT
            )
        ''')
        conn.commit()

def log_action(gate, task, status, result):
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO logs (timestamp, gate, task, status, result)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            gate,
            task,
            status,
            result[:500]
        ))
        conn.commit()
