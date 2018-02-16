from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecreet'
# our index route will handle rendering our form

@app.route('/')
def index():
  if 'total_gold' not in session:
    session['total_gold'] = 0
  if 'activityList' not in session:
    session['activityList'] = []
  return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def total_gold():
    import random
    if request.form["building"] == "farm":
      session['found_gold'] = random.randrange(10, 21)
      print session['found_gold']
      session['total_gold'] = session['total_gold'] + session['found_gold']
      activity = "Earned "+ str(session['found_gold']) + " golds from the farm!"
      print activity
      session['activityList'].append(activity)
      print session['activityList']
      return render_template('index.html')
    elif request.form["building"] == "cave":
      session['found_gold'] = random.randrange(5, 11)
      print session['found_gold']
      session['total_gold'] = session['total_gold'] + session['found_gold']
      return render_template('index.html')
    elif request.form["building"] == "house":
      session['found_gold'] = random.randrange(2, 6)
      print session['found_gold']
      session['total_gold'] = session['total_gold'] + session['found_gold']
      return render_template('index.html')
    else:
      num = random.randrange(0, 2)
      if num == 1:
        session['found_gold'] = random.randrange(0, 51)
        print session['found_gold']
        session['total_gold'] = session['total_gold'] + session['found_gold']
      else:
        session['lost_gold'] = random.randrange(0, 51)
        print session['lost_gold']
        session['total_gold'] = session['total_gold'] - session['lost_gold']
      return render_template('index.html')

app.run(debug=True) # run our server