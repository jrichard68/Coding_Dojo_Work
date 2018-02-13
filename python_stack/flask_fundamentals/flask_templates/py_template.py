from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Jamie")

@app.route('/<template>')
def success():
  return render_template('<template>.html')


app.run(debug=True)