from app import app
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route('/database/')
def read():

    return render_template("database.html")