from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii
salt = binascii.b2a_hex(os.urandom(15))

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'the_wall')

@app.route('/')
def index():
    if not 'first_name' in session:
        session['first_name'] = 0
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    print session['first_name']
    errors = False
    password = request.form['password']
    hashed_pw = md5.new(password + salt).hexdigest()
    if len(request.form['first_name']) < 2:
        flash("First Name must be at least 2 letters!")
        errors = True
    if not str.isalpha(str(request.form['first_name'])):
        flash("First Name can only contain letters.")
        errors = True
    if len(request.form['last_name']) < 2:
        flash("Last Name must be at least 2 letters!")
        errors = True
    if not str.isalpha(str(request.form['last_name'])):
        flash("Last Name cannot contain any numbers.")
        errors = True
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
        errors = True
    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters!")
        errors = True
    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!")
        errors = True
    if request.form['password'] != request.form['confirm_password']:
        flash("Password and Password Confirmation must match.")
        errors = True
    print errors
    if errors:
        return redirect("/")
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'hashed_pw': hashed_pw,
            'salt': salt
            }
        mysql.query_db(query, data)
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data = {'email': email}
    user = mysql.query_db(query, data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            query = "SELECT first_name FROM users WHERE users.email = email LIMIT 1"
            first_name = mysql.query_db(query)[0]['first_name']
            session['first_name'] = first_name
            print session['first_name']
            return redirect('/wall')
        else:
            flash("Invalid Password!")
            return redirect('/')
    else:
        flash("Invalid Email Address!")
        return redirect('/')

@app.route('/wall')
def wall():
    return render_template('wall.html')#, name = session['first_name'])

@app.route('/message')
def message():
    return render_template('wall.html')

@app.route('/clear')
def clear():
    session.clear()
    print session
    return redirect('/')

app.run(debug=True)
