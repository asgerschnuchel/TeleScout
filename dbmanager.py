import sqlite3

def create_db(filename):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()