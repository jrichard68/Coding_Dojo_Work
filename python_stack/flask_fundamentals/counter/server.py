from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecreet'
# our index route will handle rendering our form

@app.route('/')
def index():
  session['counter'] = session['counter'] + 1
  return render_template("index.html")

@app.route('/bytwo')
def level_1():
    session['counter'] = session['counter'] + 2
    return render_template('index.html')

@app.route('/reset')
def level_2():
  session['counter'] = 1
  return render_template('index.html')
   
app.run(debug=True) # run our server