from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def print_form():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print name, location, language, comment
    return render_template('/survey.html', name = name, location = location, language = language, comment = comment)
app.run(debug=True)
copy