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
                                        id integer,
                                        name text,
                                        cellnumber integer,
                                        phoneid integer
                                    ); """

    # create tables
    if conn is not None:
        # create patrols table
        create_table(conn, sql_create_patrols_table)
    else:
        print("Error! cannot create the database connection.")
    return


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
    return

    
def add_patrol(id, name, phonenumber, phoneid):
    data = (id, name, phonenumber, phoneid)
    conn = connect_db("test.db")
    """
    Create a new patrol in the database
    """
    sql = ''' INSERT INTO patrols(id,name,cellnumber,phoneid)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return

def edit_patrol(id, newname, newnumber, newphone):
    conn = connect_db("test.db")
    data = (newname, newnumber, newphone, id)
    """
    update existing patrol data by id
    """
    sql = ''' UPDATE patrols
              SET name = ? ,
                  cellnumber = ? ,
                  phoneid = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return



def delete_patrol(id):
    conn = connect_db("test.db")
    """
    Delete a patrol by task id
    """
    sql = 'DELETE FROM patrols WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def delete_all_patrols():
    """
    Delete all patrol data from the database
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()