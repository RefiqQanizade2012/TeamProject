import sqlite3
from config import DB_NAME, TOP_GAMES_LIMIT

def get_game_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_games_by_genre(genre):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE genre = ?", (genre,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_top_games(limit=TOP_GAMES_LIMIT):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games ORDER BY rating DESC LIMIT ?", (limit,))
    results = cursor.fetchall()
    conn.close()
    return results

def add_game(name, creator, genre, rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO games (name, creator, genre, rating) VALUES (?, ?, ?, ?)",
        (name, creator, genre, rating)
    )
    conn.commit()
    conn.close()
