from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecreet'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def print_form():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty! Click the Return Button and try again.")
    if len(request.form['comment']) < 1:
        flash("Comment feild cannot be empty! Click the Return Button and try again.")
    if len(request.form['comment']) > 120:
        flash("Comment feild cannot longer than 120 characters! Sorry, click the Return Button and try again.")
        comment = "Your comment is too long."
    return render_template('/survey.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True)
