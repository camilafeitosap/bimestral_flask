# database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('music.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela de Música
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS musica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        artista TEXT NOT NULL
    )
    ''')

    # Tabela de Playlist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS playlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')

    # Tabela de relação Playlist-Música (muitos-para-muitos)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS playlist_musica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        playlist_id INTEGER NOT NULL,
        musica_id INTEGER NOT NULL,
        FOREIGN KEY (playlist_id) REFERENCES playlist(id),
        FOREIGN KEY (musica_id) REFERENCES musica(id)
    )
    ''')

    conn.commit()
    conn.close()

# Executa a função para criar as tabelas
create_tables()
