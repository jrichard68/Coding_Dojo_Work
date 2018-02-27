from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'email_validationdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['email'] = request.form['email']
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        # Write query as a string. Notice how we have multiple values we want to insert into our query.
        query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                'email': request.form['email']
            }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # add a user to the database!
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT email, DATE_FORMAT(created_at, '%m %d %y %h %i %p') FROM users"
    users = mysql.query_db(query)   # run query with query_db()
    return render_template('success.html', all_users = users)

@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')

app.run(debug=True)
