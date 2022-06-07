from app import app
from flask import render_template, request

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")