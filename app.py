from ast import If
from crypt import methods
import email
import pwd
from re import S
import sqlite3
from this import s
from xml.etree.ElementInclude import include
from passlib.hash import sha256_crypt
from flask import Flask, flash,render_template,request,session,redirect,url_for
app=Flask(__name__)#variabile globale di py stiamo passando al flask il main del programma
import os.path
app.config['SECRET_KEY']='diahjdfsglsg'

@app.route('/')
def home():

    connection=sqlite3.connect('database.db')#connessione db
    connection.row_factory=sqlite3.Row #organizzazione in righe
    cur=connection.cursor()
    cur.execute('SELECT * FROM item')
    item=cur.fetchall()#dati vengono messi in una lista
    connection.close()
    return render_template('index.html',item=item)

@app.route('/login', methods=['POST','GET'] )
def login():
    if request.method == "POST" :
        if request.form['email'] and request.form['pwd']:
            connection=sqlite3.connect('database2.db')#connessione db
            email=request.form['email']
            pwd=request.form['pwd']
            cur=connection.cursor()
            cur.execute('SELECT * FROM user')
            user=cur.fetchall()#dati vengono messi in una lista
            connection.close()
            for i in user:
                if(email==i[0] and pwd ==i[1]):#login ok
                    session['email']=email 
                    session['pwd']=pwd
                    return redirect(url_for('profile'))
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

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/logout')
def logout():
    session["email"] = None
    session["pwd"] = None
    return redirect("/")

if __name__ == '__main__' :#per far partire il programma
    app.run(debug=True ,port=8080)


