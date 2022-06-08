from app import app
from flask import render_template

@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():

    return render_template("index.html")

@app.route("/form/", methods=["POST","GET"])
def form():
    return render_template("uwiForm.html")
