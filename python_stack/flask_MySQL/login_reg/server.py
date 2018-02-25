from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii
salt = binascii.b2a_hex(os.urandom(15))

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'login_regdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
    errors = []
    pass_word = request.form['pass_word']
    hashed_pw = md5.new(pass_word + salt).hexdigest()
    if len(request.form['first_name']) < 2:
        error.append("First Name cannot be blank!")
    if not str.isalpha(request.form['first_name']):
        error.append("First Name can only contain letters.")
    if len(request.form['last_name']) < 2:
        error.append("Last Name cannot be blank!")
    if not str.isalpha(request.form['last_name']):
        error.append("Last Name cannot contain any numbers.")
    if len(request.form['email']) < 1:
        error.append("Email cannot be blank!")
    if not EMAIL_REGEX.match(request.form['email']):
        error.append("Invalid Email Address!")
    if len(request.form['pass_word']) < 1:
        error.append("Password cannot be blank!")
    if len(request.form['pass_word']) < 8:
        error.append("Password must be more than 8 characters!")
    if len(request.form['confirm_password']) < 1:
        error.append("Confirm Password cannot be blank!")
    if request.form['pass_word'] != request.form['confirm_password']:
        error.append("Password and Password Confirmation must match.")
    if len(errors) > 0:
      for error in errors:
        flash(error)
    else:
        query = "INSERT INTO users (first_name, last_name, email, pass_word, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, :salt, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'hashed_pw': hashed_pw,
            'salt': salt
            }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    pass_word = request.form['pass_word']
    query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data = {'email': email}
    user = mysql.query_db(query, data)
    if len(user) != 0:
        encrypted_password = md5.new(pass_word + user[0]['salt']).hexdigest()
        if user[0]['pass_word'] == encrypted_password:
            return redirect('/success')
        else:
            flash("Invalid Password!")
            return redirect('/')
    else:
        flash("Invalid Email Address!")
        return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
