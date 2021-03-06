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
    if not 'id' in session:
        session['id'] = 0
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
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
            session['first_name'] = user[0]['first_name']
            session['id'] = user[0]['id']
            return redirect('/wall')
        else:
            flash("Invalid Password!")
            return redirect('/')
    else:
        flash("Invalid Email Address!")
        return redirect('/')

@app.route('/wall')
def wall():
    # Query for all message posts
    query = "SELECT messages.message, DATE_FORMAT(messages.created_at, '%M, %D') AS date, DATE_FORMAT(messages.created_at, '%Y') AS year, CONCAT(users.first_name, ' ', users.last_name) AS full_name, messages.id, messages.user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    message_posts = mysql.query_db(query)
    
    #Query for Comments on specific posts
    query = "SELECT comments.comment, DATE_FORMAT(comments.created_at, '%M, %D') AS date, DATE_FORMAT(comments.created_at, '%Y') AS year, CONCAT(users.first_name, ' ', users.last_name) AS full_name, comments.id, comments.message_id, comments.user_id FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON messages.user_id = users.id"
    comment_posts = mysql.query_db(query)
    return render_template('wall.html', all_posts = message_posts,all_comments = comment_posts)

@app.route('/message', methods = ['POST'])
def message():
    message_post = request.form['message']
    query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message_post, NOW(), NOW(), :id)"
    data = {
            'message_post': request.form['message'],
            'id': session['id']
            }
    session['message_id'] = mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<message_id>', methods = ['POST'])
def comment(message_id):
    comment_post = request.form['comment']
    query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment_post, NOW(), NOW(), :id, :message_id)"
    data = {
            'comment_post': request.form['comment'],
            'id': session['id'],
            'message_id': message_id
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
