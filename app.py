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
from datetime import timedelta

app=Flask(__name__)#variabile globale di py stiamo passando al flask il main del programma
import os.path
app.config['SECRET_KEY']='diahjdfsglsg'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=24)

@app.route('/' ,methods=['POST','GET'] )
def home():
    connection=sqlite3.connect('cart.db')#connessione db
    connection.row_factory=sqlite3.Row #organizzazione in righe
    cur=connection.cursor()
    cur.execute('SELECT * FROM item')
    item=cur.fetchall()#dati vengono messi in una lista
    connection.close()


    if request.method == "POST" :
        if session['email']!= None :
            connection=sqlite3.connect('cart.db')#connessione db
            title=request.form.get('title')
            email=session['email']
            cur=connection.cursor()
            cur.execute('SELECT title,email,quantity FROM cart WHERE email=? AND title=? ',(email,title,))
            item2=cur.fetchall()#dati vengono messi in una lista
            if item2 :
                if item2[0][2] >= 1:
                    connection.execute("UPDATE cart SET quantity=quantity+1 WHERE email=? AND title=?",(email,title))#dati vengono messi in una lista
                    connection.commit()
                    connection.close()

                else:
                    connection.execute("INSERT INTO cart (title,email,quantity) VALUES( ? , ?, ?)",(title,email,'1'))#dati vengono messi in una lista
                    connection.commit()
                    connection.close()  
            else:
                connection.execute("INSERT INTO cart (title,email,quantity) VALUES( ? , ?, ?)",(title,email,'1'))#dati vengono messi in una lista
                connection.commit()
                connection.close()  
        else:
            return redirect("/authenticate")
    return render_template('index.html',item=item)

@app.route('/cart', methods=['GET','POST'])
def cart():
    connection=sqlite3.connect('cart.db')#connessione db
    connection.row_factory=sqlite3.Row #organizzazione in righe
    cur=connection.cursor()
    cur.execute('SELECT * FROM cart NATURAL JOIN item WHERE email= ?',(session['email'],))
    item=cur.fetchall()#dati vengono messi in una lista
    connection.close()
    if request.method == "POST" :
        connection=sqlite3.connect('cart.db')#connessione db
        cur=connection.cursor()
        title=request.form.get('title')
        email=session['email']
        print(title,email)
        cur.execute('DELETE FROM cart WHERE title=? AND email=?',(title,email))
        connection.commit()
        connection.close()
        return redirect(url_for('cart'))
    return render_template('cart.html',item=item)


@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

@app.route('/login', methods=['POST','GET'] )
def login():
    if request.method == "POST" :
        if request.form['email'] and request.form['pwd']:
            connection=sqlite3.connect('cart.db')#connessione db
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
            connection=sqlite3.connect('cart.db')#connessione db
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


