import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'database.db')

def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(os.path.dirname(DATABASE_PATH)):
        os.makedirs(os.path.dirname(DATABASE_PATH))
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS button_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            button_number INTEGER,
            is_on BOOLEAN,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users(username),
            UNIQUE(username, button_number)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()