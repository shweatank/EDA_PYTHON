# db.py
import sqlite3
import os

DATABASE = "gates_db.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gates_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            file_path TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def store(file_name):
    vcd_path = f"/home/abhishek/day_6/{file_name}"

    if not os.path.exists(vcd_path):
        return
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gates_files (file_name, file_path) VALUES (?, ?)", 
                  (file_name[:file_name.index(".")], vcd_path))
    conn.commit()
    conn.close()