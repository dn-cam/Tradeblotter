from Database import SQLite3
import pandas as pd
import numpy as np

class Blotter():
    
    def __init__(self):
        self.sqlite = SQLite3("klscp.sqlite")
        self.conn = self.sqlite.conn
        
    def insertOrder(self, trader, date, ticker, side, contract, position):
        """
        inserts one order at at time to the database, to the ORDER table
        """
        with self.conn:
            # create a new project
            order = (trader, date, ticker, side, contract, position);
            sql = ''' INSERT INTO orders(trader, date, ticker, side, contract, position)
                  VALUES(?,?,?,?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, order)
            conn.commit()
            
            
    def getPosition(self):
        """
        if orders table is empty:
            return summary of portfolio table
        else:
            read all records from orders table
            update portfolio table
            delete records from orders table
            return summary of portfolio table
        """
        
        with self.conn:
            conn = self.conn
            orders = pd.read_sql_query("SELECT * FROM ORDERS", self.conn)
            if len(orders) > 0:
                for row in orders:
                    # get the row['contracts'] and row['positions'] from the portfolio table matching row['ticker']
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM portfolio WHERE ticker=?", (row['ticker']))
                    row = cur.fetchall()
                    oldPosition = int(row['position'])
                    buyOrSell = int(row['side'])
                    print(type(oldPosition))
                    if row['contracts'] is not None:
                        val = int(row['contracts'])
                        if buyOrSell == 1:#buy
                            oldPosition += val
                        else: #sell
                            if val <= oldPosition:
                                oldPosition -= val
                    else:
                        perc = int(row['positions'])
                        val = 0.01*oldPosition*perc
                        if buyOrSell == 1:#buy
                            oldPosition += val
                        else: #sell
                            if val <= oldPosition:
                                oldPosition -= val
                    
                    # update portfolio table
                    sql = ''' UPDATE portfolio
                              SET position = ?
                              WHERE ticker = ?'''
                    curs = conn.cursor()
                    curs.execute(sql, (oldPosition, row['ticker']))
                    conn.commit()
                #delete from orders table
                sql1 = 'DELETE FROM orders'
                cur1 = conn.cursor()
                cur1.execute(sql1)
                conn.commit()
            
        return self.readPortfolio()
                
    def readPortfolio(self):
        #helper function to read portfolio table 
        portfolio = pd.read_sql_query("SELECT * FROM PORTFOLIO", self.conn)
        return portfolio
    