import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """

    print('a')
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            print('closed')
            conn.close()


if '__name__' == '__main__':
    db_file= r'/Users/roopeshbharatwajkr/Documents/sqlite/db/sqlite_python01.db'
    create_connection(db_file)

