import sqlite3

DB_PATH = "users.db"


def get_user(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def create_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password),
    )
    conn.commit()


def delete_user(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()