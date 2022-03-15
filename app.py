from ast import If
from crypt import methods
import email
import pwd
import sqlite3
from passlib.hash import sha256_crypt
from flask import Flask, flash,render_template,request,session,redirect,url_for
app=Flask(__name__)#variabile globale di py stiamo passando al flask il main del programma
import os.path
    
@app.route('/')
def home():

    connection=sqlite3.connect('database.db')#connessione db
    connection.row_factory=sqlite3.Row #organizzazione in righe
    cur=connection.cursor()
    cur.execute('SELECT * FROM item')
    item=cur.fetchall()#dati vengono messi in una lista
    connection.close()
    return render_template('index.html',item=item)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration', methods=['POST','GET'] )
def registration():
    if request.method == "POST" :
        if request.form['email'] and request.form['pwd']:
            connection=sqlite3.connect('database2.db')#connessione db
            email=request.form['email']
            pwd=request.form['pwd']
            connection.execute("INSERT INTO user (email,pwd) VALUES( ? , ?)",(email,pwd))
            connection.commit()
            connection.close()
            return redirect(url_for('login'))

    return render_template('registration.html')
if __name__ == '__main__' :#per far partire il programma
    app.run(debug=True ,port=8080)
