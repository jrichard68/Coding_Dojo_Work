from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('ninja_turtles.html')

@app.route('/ninja/<color>')
def show_ninja(color):
    if color == 'orange':
        return render_template("orange.html")
    elif color == 'blue':
        return render_template("blue.html")
    elif color == 'purple':
        return render_template("purple.html")
    elif color == 'red':
        return render_template("red.html")
    else:
        return render_template("notapril.html")

app.run(debug=True)