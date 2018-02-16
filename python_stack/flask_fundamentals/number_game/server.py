from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecreet'
# our index route will handle rendering our form

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess_number():
    session['num_guess'] = int(request.form['num_guess'])
    import random
    session['num'] = random.randrange(0, 101)
    print session['num']
    if session['num'] == session['num_guess']:
      return render_template('user.html', response = "You guessed correctly!")
    elif session['num'] > session['num_guess']:
      return render_template('user.html', response = "Your guess is too low. Guess again.")
    else:
      return render_template('user.html', response = "Your guess is too high. Guess again.")
      
@app.route('/more_guesses', methods=['POST'])
def more_guesses():
    session.pop('num_guess')
    session['num_guess'] = int(request.form['num_guess'])
    print session['num_guess']
    if session['num'] == session['num_guess']:
      return render_template('user.html', response = "You guessed correctly!")
    elif session['num'] > session['num_guess']:
      return render_template('user.html', response = "Your guess is too low. Take another guess.")
    else:
      return render_template('user.html', response = "Your guess is too high. Take another guess.")
   
app.run(debug=True) # run our server