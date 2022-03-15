import sqlite3
connection=sqlite3.connect('database.db')
with open('items.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()