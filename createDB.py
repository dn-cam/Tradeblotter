import sqlite3
from sqlite3 import Error

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

sql_create_portfolio_table = """ CREATE TABLE IF NOT EXISTS portfolio (
                                        ticker integer NOT NULL,
                                        position integer NOT NULL
                                    ); """

#Trader Date Ticker Side '# of contract' '% of position'

sql_create_orders_table = """CREATE TABLE IF NOT EXISTS orders (
                                    trader integer NOT NULL,
                                    date text NOT NULL,
                                    ticker text NOT NULL,
                                    side integer NOT NULL,
                                    contracts integer,
                                    positions integer
                                );"""



conn = None
db_file = "klscp1.sqlite"

try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except Error as e:
    print(e)
    
if conn is not None:
    # create projects table
    create_table(conn, sql_create_portfolio_table)

    # create tasks table
    create_table(conn, sql_create_orders_table)
    print('created')
    if conn:
        conn.close()
else:
    print('Error! cannot create the database connection.')