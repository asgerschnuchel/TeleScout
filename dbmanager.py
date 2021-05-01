import sqlite3

def connect_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_db(filename):
    #create database with the right content
    conn = connect_db(filename)
    
    #Create DB connection
    
    sql_create_patrols_table = """ CREATE TABLE IF NOT EXISTS patrols (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        cellnumber integer,
                                        phone ID integer
                                    ); """

    # create tables
    if conn is not None:
        # create patrols table
        create_table(conn, sql_create_patrols_table)
    else:
        print("Error! cannot create the database connection.")


def create_table(conn, create_table_sql):
    #creates table from sql statement in function call
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

    
def add_patrol(name,id,phonenumber):
    return

create_db("test.db")