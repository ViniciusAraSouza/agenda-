import os
import sqlite3
from flask.cli import load_dotenv

load_dotenv()

DB_FILE = os.getenv("DATABASE", "./data/tarefas.sqlite3")

data_dir = os.path.dirname(DB_FILE)
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)


def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                tipo TEXT,
                data_conclusao TEXT,
                status TEXT DEFAULT 'Pendente',
                indicado_por TEXT
            );
        """)
        conn.commit()


class Database:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    def executar(self, query, params=()):
        self.cursor.execute(query, params)

    def buscar_tudo(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()