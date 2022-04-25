import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("select * from 'users' where 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))