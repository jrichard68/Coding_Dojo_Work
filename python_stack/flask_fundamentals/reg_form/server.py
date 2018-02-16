from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!")
    elif not str.isalpha(str(request.form['first_name'])):
        flash("First Name cannot contain any numbers.")
    elif not str.isalpha(str(request.form['last_name'])):
        flash("Last Name cannot contain any numbers.")
    elif len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!")
    elif len(request.form['password']) < 1:
        flash("Password cannot be blank!")
    elif len(request.form['password']) < 9:
        flash("Password must be more than 8 characters!")
    elif len(request.form['confirm_password']) < 1:
        flash("Confirm Password cannot be blank!")
    elif str(request.form['password']) != str(request.form['confirm_password']):
        flash("Password and Password Confirmation must match.")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)