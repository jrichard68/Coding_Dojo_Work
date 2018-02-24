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
    pass_word = request.form['pass_word']
    hashed_pw = md5.new(pass_word + salt).hexdigest()
    if len(request.form['first_name']) < 2:
        flash("First Name cannot be blank!")
        return redirect('/')
    elif not str.isalpha(str(request.form['first_name'])):
        flash("First Name can only contain letters.")
        return redirect('/')
    elif len(request.form['last_name']) < 2:
        flash("Last Name cannot be blank!")
        return redirect('/')
    elif not str.isalpha(str(request.form['last_name'])):
        flash("Last Name cannot contain any numbers.")
        return redirect('/')
    elif len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['pass_word']) < 1:
        flash("Password cannot be blank!")
        return redirect('/')
    elif len(request.form['pass_word']) < 8:
        flash("Password must be more than 8 characters!")
        return redirect('/')
    elif len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!")
        return redirect('/')
    elif str(request.form['pass_word']) != str(request.form['confirm_password']):
        flash("Password and Password Confirmation must match.")
        return redirect('/')
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
