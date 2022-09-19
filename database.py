import sqlite3


def create_table():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()
    query_create = """CREATE TABLE IF NOT EXISTS account(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        api_id INTEGER NOT NULL,
        api_hash TEXT NOT NULL,
        name_acc TEXT NOT NULL,
        flag INTEGER NOT NULL
    )"""
    cursor.execute(query_create)
    conn.commit()
    cursor.close()
    conn.close()


def insert_data_account(api_id, api_hash, name_acc, flag):
    conn = sqlite3.connect('account.db', 10)
    cursor = conn.cursor()
    query_insert = """INSERT INTO account(api_id, api_hash, name_acc, flag) VALUES(?, ?, ?, ?);"""
    cursor.execute(query_insert, (api_id, api_hash, name_acc, flag))
    conn.commit()
    cursor.close()
    conn.close()


def drop_table():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()
    query_drop = """DROP TABLE account"""
    cursor.execute(query_drop)
    conn.commit()
    cursor.close()
    conn.close()


def select_all_acc():
    conn = sqlite3.connect('account.db', 10)
    cursor = conn.cursor()
    query_select = """SELECT * FROM account"""
    cursor.execute(query_select)
    info_user = cursor.fetchall()
    cursor.close()
    conn.close()
    return info_user


def select_flag_acc():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()
    query_select = """SELECT api_id, flag FROM account"""
    cursor.execute(query_select)
    flag_acc = cursor.fetchall()
    cursor.close()
    conn.close()
    return flag_acc

