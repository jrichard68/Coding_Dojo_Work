from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def print_name():
    name = request.form['name']
    print "Your name is", name
    return redirect('/')
app.run(debug=True)
copy