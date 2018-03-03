from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'twitter_demo')
print "="*100
print mysql.query_db("SELECT * FROM users")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods = ["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    query = "INSERT INTO users (username, password, created_at, updated_at) VALUES (:username, :password, now(), now())"
    data = {
        "username" : request.form["username"],
        "password" : request.form["password"]
    }
    mysql.query_db(query, data)
    flash("successfully registered")
    return redirect ("/")

@app.route("/login", methods = ["POST"])
def login():
    query = "SELECT * FROM users WHERE username = :user_name"
    data = {
        "user_name": request.form['username']
    }
    users = mysql.query_db(query, data)
    if len(users) > 0:
        user = users[0]
        if user["password"] == request.form["password"]:
            session["logged_id"] = user["id"]
            return redirect ("/dashboard")
        else:
            flash("password doesn't match")
            return redirect("/")
    else:
        flash("no username found")
        return redirect("/")

@app.route("/dashboard")
def dashboard():
    return "logged in"
app.run(debug=True)