import sqlite3
connection=sqlite3.connect('cart.db')
with open('cart.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()