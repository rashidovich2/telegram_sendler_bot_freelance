import sqlite3


class MainDatabase:
    def __init__(self, file_connect):
        self.conn = sqlite3.connect(file_connect)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        with self.conn:
            list_user = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(list_user))

    def add_user(self, user_id):
        with self.conn:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)",
                                       (user_id,))

    def get_user(self, user):
        with self.conn:
            return self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user,)).fetchone()
