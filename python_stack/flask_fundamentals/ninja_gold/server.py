from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecreet'
# our index route will handle rendering our form

@app.route('/')
def index():
  if not 'total_gold' in session:
    session['total_gold'] = 0
  if not 'activityList' in session:
    session['activityList'] = []
  return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def total_gold():
    import random
    import datetime
    date = datetime.datetime.now()
    if request.form["building"] == "farm":
        session['found_gold'] = random.randrange(10, 21)
        session['total_gold'] = session['total_gold'] + session['found_gold']
        activity = "Earned "+ str(session['found_gold']) + " golds from the farm!"
        session['activityList'].append(activity)
        return render_template('index.html')
    elif request.form["building"] == "cave":
        session['found_gold'] = random.randrange(5, 11)
        session['total_gold'] = session['total_gold'] + session['found_gold']
        activity = "Earned "+ str(session['found_gold']) + " golds from the cave!"
        session['activityList'].append(activity)
        return render_template('index.html')
    elif request.form["building"] == "house":
        session['found_gold'] = random.randrange(2, 6)
        session['total_gold'] = session['total_gold'] + session['found_gold']
        activity = "Earned "+ str(session['found_gold']) + " golds from the house!"
        session['activityList'].append(activity)
        return render_template('index.html')
    else:
      num = random.randrange(0, 2)
      if num == 1:
          session['found_gold'] = random.randrange(0, 51)
          session['total_gold'] = session['total_gold'] + session['found_gold']
          activity = "Earned "+ str(session['found_gold']) + " golds from the casin!"
          session['activityList'].append(activity)
          return render_template('index.html')
      else:
          session['lost_gold'] = random.randrange(0, 51)
          session['total_gold'] = session['total_gold'] - session['lost_gold']
          activity = "Lost "+ str(session['lost_gold']) + " golds from the casino!"
          session['activityList'].append(activity)
          return render_template('index.html')
      
@app.route('/clear')
def clear():
  session.clear()
  return redirect('/')
  '''return render_template('index.html')'''

app.run(debug=True) # run our server