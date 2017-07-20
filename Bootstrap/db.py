import sqlite3
conn=sqlite3.connect('mywebsite')
c=conn.cursor()
conn.execute("SELECT * FROM CONTACTINFO ")
c.fetchall();

conn.close()