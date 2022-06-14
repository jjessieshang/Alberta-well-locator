from app import app
from flask import render_template

@app.route("/")
@app.route("/home/")
@app.route("/index/")
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
