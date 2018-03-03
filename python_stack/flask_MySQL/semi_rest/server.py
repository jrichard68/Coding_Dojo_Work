from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'users')
print "="*100

@app.route("/users")
def users():
    query = "SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_at FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)

@app.route("/users/new")
def new():
    return render_template('add_user.html')

@app.route("/users/<id>/edit")
def edit(id):
    query = "SELECT * FROM users WHERE id = :specific_id"
    data = {'specific_id': id}
    users = mysql.query_db(query, data)
    return render_template ("edit_user.html", one_user = users[0])

@app.route("/users/<id>")
def show(id):
    query = "SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_at FROM users WHERE id = :specific_id"
    data = {'specific_id': id}
    users = mysql.query_db(query, data)
    return render_template ("show_user.html", one_user = users[0])

@app.route("/users/create", methods = ["POST"])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, now(), now())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect("/users")

@app.route("/users/<id>/destroy")
def destroy(id):
    query = "DELETE FROM users WHERE id = :specific_id"
    data = {'specific_id': id}
    mysql.query_db(query, data)
    return redirect("/users")

@app.route("/users/<id>/update", methods = ["POST"])
def update(id):
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = now() WHERE id = :specific_id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'specific_id': id
    }
    users = mysql.query_db(query, data)
    query = "SELECT id, CONCAT(first_name, ' ', last_name) as full_name, email, DATE_FORMAT(created_at, '%M %D, %Y') AS created_at FROM users WHERE id = :specific_id"
    data = {'specific_id': id}
    users = mysql.query_db(query, data)
    return render_template ("show_user.html", one_user = users[0])
    #return redirect("/users/<id>")

app.run(debug=True)