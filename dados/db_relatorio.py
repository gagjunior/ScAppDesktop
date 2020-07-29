import os
import sqlite3

diretorio = os.path.dirname(__file__)

class DbRelatorios():
    conn = sqlite3.connect('relatorios.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (userid TEXT PRIMARY KEY, nome TEXT, email TEXT, senha TEXT)''')

    conn.commit()

    conn.close()







