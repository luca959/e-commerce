from ast import If
from crypt import methods
import email
import pwd
import sqlite3
from wtForms import Form
from passlib.hash import sha256_crypt
from flask import Flask,render_template,request,session,redirect,url_for
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

class RegistrationForm(Form):
    email=TextField('email')
    pwd=PasswordField('pwd')

@app.route('/registration', methods=('POST',))
def registration():
    connection=sqlite3.connect('database.db')#connessione db
    connection.row_factory=sqlite3.Row #organizzazione in righe
    cur=connection.cursor()
    form=RegistrationForm(request.form)
    if request.method== "POST" :
        email=form.email.data
        pwd=sha256_crypt.encrypt((str(form.pwd.data)))
        x=cur.execute()
    return render_template('registration.html')
if __name__ == '__main__' :#per far partire il programma
    app.run(debug=True ,port=8080)



if __name__ == '__main__' :#per far partire il programma
    app.run(debug=True ,port=8080)

