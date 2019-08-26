import sqlite3
from contextlib import closing
from typing import List, Dict, Union

table_name = "bot"

DBEntry = Dict[str, Union[str, int]]


def add_to_database(db_name: str, data: List[DBEntry]) -> int:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS {} \
        (word1 TEXT, word2 TEXT, word3 TEXT, id INTEGER, user TEXT);".format(table_name))

        # insert to table
        insert_sql = "INSERT INTO {} (word1, word2, word3, id, user)\
                                              VALUES (?, ?, ?, ?, ?);".format(table_name)
        params = [(d["word1"], d["word2"], d["word3"], d["id"], d["user"]) for d in data]

        cursor.executemany(insert_sql, params)
        connection.commit()

        cursor.execute("SELECT * FROM {}".format(table_name))
        return len(cursor.fetchall())


def get_latest_tweet(db_name: str) -> int:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS {} \
        (word1 TEXT, word2 TEXT, word3 TEXT, id INTEGER, user TEXT);".format(table_name))

        max_sql = "SELECT MAX(id) FROM {};".format(table_name)
        cursor.execute(max_sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return 0

        m = result[0][0]
        if m is None:
            return 0
        else:
            return m


def get_db_entries(db_name: str) -> List[DBEntry]:
    word_blocks = []
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS {} \
                (word1 TEXT, word2 TEXT, word3 TEXT, id INTEGER, user TEXT);".format(table_name))

        max_sql = "SELECT * FROM {};".format(table_name)
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


def delete_db_entries_by_id(db_name: str, tweet: int) -> bool:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS {} \
                (word1 TEXT, word2 TEXT, word3 TEXT, id INTEGER, user TEXT);".format(table_name))

        delete_sql = "DELETE FROM {} WHERE (id) = (?);".format(table_name)
        cursor.execute(delete_sql, (str(tweet), ))
        connection.commit()

        check_sql = "SELECT * FROM {} WHERE (id) = (?);".format(table_name)
        cursor.execute(check_sql, (str(tweet), ))
        return len(cursor.fetchall()) == 0


def clear_db(db_name: str) -> bool:
    connection = sqlite3.connect(db_name)
    with closing(connection):
        cursor = connection.cursor()

        # create table
        cursor.execute("CREATE TABLE IF NOT EXISTS {} \
                (word1 TEXT, word2 TEXT, word3 TEXT, id INTEGER, user TEXT);".format(table_name))

        delete_sql = "DELETE FROM {};".format(table_name)
        cursor.execute(delete_sql)
        connection.commit()

        check_sql = "SELECT * FROM {}".format(table_name)
        cursor.execute(check_sql)
        return len(cursor.fetchall()) == 0
