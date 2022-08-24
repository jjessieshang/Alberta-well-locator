from app import app
from flask import render_template
from flask_basicauth import BasicAuth 

app.config['BASIC_AUTH_USERNAME'] = 'BitCan'
app.config['BASIC_AUTH_PASSWORD'] = 'Geosciences'
basic_auth = BasicAuth(app)

@app.route("/")
@app.route("/home/")
@app.route("/index/")
@basic_auth.required
def home():
    return render_template("index.html")

@app.route("/option/")
def option():
    return render_template("uwiOption.html")

@app.route("/form/", methods=["POST","GET"])
def form():
    return render_template("uwiForm.html")

@app.route("/form2/", methods=["POST","GET"])
def form2():
    return render_template("uwiForm2.html")

@app.route('/database/')
def database():
    return render_template('database.html')

