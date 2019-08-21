import sqlite3
from contextlib import closing

table_name = "bot"


def add_to_database(db_name: str, data: [dict]) -> int:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("SHOW TABLES LIKE {}".format(table_name))
        if cursor.rowcount == 0:
            cursor.execute("CREATE TABLE {} (word1 TEXT, word2 TEXT,\
                                  word3 TEXT, id INTEGER, user TEXT)".format(table_name))

        # insert to table
        insert_sql = "INSERT INTO {} (word1, word2, word3, id, user)\
                                              values (?, ?, ?, ?, ?)".format(table_name)
        params = [(d["word1"], d["word2"], d["word3"], d["id"], d["user"]) for d in data]

        cursor.executemany(insert_sql, params)
        connection.commit()

        cursor.execute("SELECT * FROM {}".format(table_name))
        return cursor.rowcount


def get_latest_tweet(db_name: str) -> int:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()
        max_sql = "SELECT MAX(id) FROM {}".format(table_name)
        cursor.execute(max_sql)
        if cursor.rowcount == 0:
            return 0
        else:
            (m) = cursor.fetchone()
            return m


def get_db_entries(db_name: str) -> [dict]:
    word_blocks = []
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()
        max_sql = "SELECT * FROM {}".format(table_name)
        cursor.execute(max_sql)
        for (w1, w2, w3, i, u) in cursor.fetchall():
            word_blocks.append({
                "word1": w1,
                "word2": w2,
                "word3": w3,
                "id": i,
                "user": u
            })
    return word_blocks
