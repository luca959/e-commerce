import sqlite3
connection=sqlite3.connect('database.db')
with open('items.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()
connection=sqlite3.connect('database2.db')
with open('user.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()